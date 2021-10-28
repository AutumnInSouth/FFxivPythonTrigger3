from ctypes import *
from functools import cache
from pathlib import Path
from typing import Iterable, Callable, List, Dict, Set

from FFxivPythonTrigger import PluginBase, AddressManager, BindValue, process_event
from FFxivPythonTrigger.decorator import unload_callback, re_event
from FFxivPythonTrigger.memory import read_memory
from FFxivPythonTrigger.memory.struct_factory import PointerStruct, _OffsetStruct, OffsetStructJsonEncoder
from .base_struct import BundleHeader, MessageHeader
from .decoder import unpacked_messages
from .hook import RecvHook, SendHook
from .message_processors import opcode_processors, len_processors, key_to_code, code_to_key,_opcode_processors
from .message_processors.utils import _NetworkEvent, BaseProcessors
from .ping import Ping

send_sig = "48 83 EC ? 48 8B 49 ? 45 33 C9 FF 15 ? ? ? ? 85 C0"
recv_sig = "48 83 EC ? 48 8B 49 ? 45 33 C9 FF 15 ? ? ? ? 83 F8 ?"
zone_socket_ptr_sig = ("48 8D 0D * * * * E8 ? ? ? ? BA ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? "
                       "BA ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? 48 8D 0D ? ? ? ?")
scope_name = ["chat", "lobby", "zone"]

packet_fixer_interface = Callable[[BundleHeader, MessageHeader, bytearray, _OffsetStruct | None], bytearray | _OffsetStruct | None]


@cache
def scope_idx(key: str | int):
    if isinstance(key, int): return key
    try:
        return scope_name.index(key)
    except ValueError:
        raise ValueError(f"{key} is not a valid scope")


@cache
def get_opcode(scope: str | int, is_send: bool, key: str | int):
    if isinstance(key, int): return key
    try:
        return key_to_code[scope_idx(scope) * 2 + is_send][key]
    except KeyError:
        raise KeyError(f"{key} is not a valid opcode")


unknown_type_event = [dict()] * 6


class UnknownOpcodeEvent(_NetworkEvent):
    scope_idx: int
    opcode: int
    msg_len: int

    def possible_processors(self) -> List[BaseProcessors]:
        return [
            processor
            for processor in len_processors[self.scope_idx].get(self.msg_len, set())
            if processor.opcode not in key_to_code
        ]

    @classmethod
    def get_event(cls, bundle_header: 'BundleHeader', message_header: 'MessageHeader', raw_message: bytearray, scope: int, _is_send: bool):
        _scope_idx = scope * 2 + _is_send
        if message_header.msg_type not in unknown_type_event[_scope_idx]:
            _scope_name = scope_name[scope]

            class _UnknownOpcodeEvent(cls):
                scope = _scope_name
                is_send = _is_send
                id = _NetworkEvent.id + '/unknown/' + _scope_name + '/' + ('client' if _is_send else 'server') + message_header.msg_type
                scope_idx = _scope_idx
                opcode = message_header.msg_type
                msg_len = len(raw_message)

            unknown_type_event[_scope_idx][message_header.msg_type] = _UnknownOpcodeEvent
        return unknown_type_event[_scope_idx][message_header.msg_type](bundle_header, message_header, raw_message)


class XivNetwork(PluginBase):
    name = "XivNetwork"
    layout = str(Path(__file__).parent / 'layout.js')
    discover_mode = BindValue(default=False)
    _packet_fixer: List[Dict[int, Set[packet_fixer_interface]]]

    def __init__(self):
        super().__init__()

        am = AddressManager(self.name, self.logger)
        socket_ptr_base = am.scan_point('packet_ptr', zone_socket_ptr_sig)
        self.zone_pointer = read_memory(PointerStruct(c_longlong, 0x3c8, 0x8, 0, 0x28, 0x10), socket_ptr_base)
        self.chat_pointer = read_memory(PointerStruct(c_longlong, 0x3c8, 0x8, 0x80, 0xa8, 0x10), socket_ptr_base)
        self.recv_hook = RecvHook(self, am.scan_address('recv', recv_sig))
        self.send_hook = SendHook(self, am.scan_address('send', send_sig))
        self.pings = dict()
        self._packet_fixer = [dict()] * 6

    @unload_callback('unregister_packet_fixer')
    def register_packet_fixer(self, scope: int | str, is_send: bool, opcode: int | str, method: packet_fixer_interface):
        scope = scope_idx(scope)
        opcode = get_opcode(scope, is_send, opcode)
        self._packet_fixer[scope].setdefault(opcode, set()).add(method)

    def unregister_packet_fixer(self, scope: int | str, is_send: bool, opcode: int | str, method: packet_fixer_interface):
        scope = scope_idx(scope)
        opcode = get_opcode(scope, is_send, opcode)
        try:
            self._packet_fixer[scope][opcode].remove(method)
            if not self._packet_fixer[scope][opcode]:
                del self._packet_fixer[scope][opcode]
        except (ValueError, KeyError):
            pass

    def socket_type(self, socket: int) -> int:
        if socket == self.zone_pointer.value:
            return 2
        elif socket == self.chat_pointer.value:
            return 0
        else:
            return 1

    def process_message(self, bundle_header: BundleHeader, message: bytearray, is_send: bool, socket: int):
        if len(message) < MessageHeader.struct_size:
            self.pings.setdefault(socket, Ping()).set(is_send)
            return message
        else:
            message_header = MessageHeader.from_buffer(message)
            raw_message = message[MessageHeader.struct_size:]
            scope = socket * 2 + is_send
            struct_message = None
            processor = None
            opcode = message_header.msg_type
            if opcode in opcode_processors[scope]:
                processor = opcode_processors[scope][message_header.msg_type]
                if processor.struct.struct_size and len(raw_message) >= processor.struct.struct_size:
                    struct_message = processor.struct.from_buffer(raw_message)
                else:
                    self.logger.error(f"message size too short for [{processor.opcode}], "
                                      f"require {processor.struct.struct_size} but {len(raw_message)} is given")
            for fixer in self._packet_fixer[scope].get(opcode, set()).copy():
                new_msg_body = fixer(bundle_header, message_header, raw_message, struct_message)
                if not new_msg_body:
                    return bytearray()
                if isinstance(new_msg_body, bytearray):
                    raw_message = new_msg_body
                    if processor is not None:
                        struct_message = processor.struct.from_buffer(new_msg_body)
                else:
                    struct_message = new_msg_body
                    raw_message = bytearray(new_msg_body)
            if processor is not None:
                process_event(processor.Event(bundle_header, message_header, raw_message, struct_message))
            else:
                process_event(UnknownOpcodeEvent.get_event(bundle_header, message_header, raw_message, socket, is_send))
            return bytearray(message_header) + raw_message

    def process_messages(self, bundle_header: BundleHeader, messages: Iterable[bytearray], is_send: bool, socket: int) -> unpacked_messages:
        return bundle_header, [self.process_message(bundle_header, message, is_send, self.socket_type(socket)) for message in messages]

    # layout used
    def get_key_to_code(self):
        return key_to_code

    def is_discover(self):
        return self.discover_mode

    @re_event(r"^network\/unknown", condition='is_discover')
    def discover_event(self, evt: UnknownOpcodeEvent, _):
        for possible in evt.possible_processors():
            if possible.struct.struct_size:
                struct_msg = possible.struct.from_buffer(evt.raw_message)
                self.client_event('discover', {
                    'opcode': evt.opcode,
                    'guess': possible.opcode,
                    'struct': OffsetStructJsonEncoder.default(struct_msg),
                    'event': possible.Event(evt.bundle_header, evt.message_header, evt.raw_message, struct_msg).str_event()
                })
