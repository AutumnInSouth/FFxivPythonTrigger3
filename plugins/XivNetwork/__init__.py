from ctypes import *
from functools import cache
from pathlib import Path
from typing import Callable, List, Dict, Set

from FFxivPythonTrigger import PluginBase, AddressManager, BindValue, process_event
from FFxivPythonTrigger.decorator import unload_callback, re_event
from FFxivPythonTrigger.memory.struct_factory import _OffsetStruct, OffsetStructJsonEncoder
from .base_struct import BundleHeader, MessageHeader
from .decoder import unpacked_messages
from .hook import SendHook, BufferProcessorHook
from .message_processors import opcode_processors, len_processors, key_to_code, code_to_key, _opcode_processors
from .message_processors.utils import _NetworkEvent, BaseProcessors
from .ping import Ping

send_sig = "48 83 EC ? 48 8B 49 ? 45 33 C9 FF 15 ? ? ? ? 85 C0"
chat_recv_buffer_sig = "48 8D 15 * * * * 48 8B CF E8 ? ? ? ? 48 8D 15 ? ? ? ? 48 8B CF E8 ? ? ? ? 45 8D 47 ?"
lobby_recv_buffer_sig = "48 8D 15 * * * * 48 8B CF E8 ? ? ? ? 48 8D 15 ? ? ? ? 48 8B CF E8 ? ? ? ? 44 8D 46 ?"
zone_recv_buffer_sig = "48 8D 15 * * * * 48 8B CE E8 ? ? ? ? 48 8D 15 ? ? ? ? 48 8B CE E8 ? ? ? ? 45 8D 47 ?"
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
                id = f"{_NetworkEvent.id}unknown/{_scope_name}/{'client' if _is_send else 'server'}/{message_header.msg_type}"
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
        self.send_hook = SendHook(self, am.scan_address('send', send_sig))
        self.chat_buffer_hook = BufferProcessorHook(self, am.scan_point('chat_buffer', chat_recv_buffer_sig), 0)
        self.lobby_buffer_hook = BufferProcessorHook(self, am.scan_point('lobby_buffer', lobby_recv_buffer_sig), 1)
        self.zone_buffer_hook = BufferProcessorHook(self, am.scan_point('zone_buffer', zone_recv_buffer_sig), 2)
        self.pings = dict()

        self.sockets = {}
        self._socket_guessing_cache = {}
        self._packet_fixer = [dict()] * 6
        self.magic_backup = {i: BundleHeader() for i in range(3)}
        self.header_backup = {i: MessageHeader() for i in range(3)}

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

    def guess_socket_type(self, bundle_header: BundleHeader, messages: list[bytearray]):
        if not bundle_header.magic0:
            return -1
        for message in messages:
            if len(message) < MessageHeader.struct_size:
                continue
            else:
                header = MessageHeader.from_buffer(message)
                if header.login_user_id > 0x20000000:
                    return 1  # lobby
                if header.unk3:
                    return 2  # zone
                else:
                    return 0  # chat
        return -1

    def process_message(self, bundle_header: BundleHeader, message: bytearray, is_server: bool, socket: int):
        if len(message) < MessageHeader.struct_size:
            self.pings.setdefault(socket, Ping()).set(is_server)
            return message
        else:
            message_header = MessageHeader.from_buffer(message)
            pointer(self.header_backup[socket])[0] = message_header
            raw_message = message[MessageHeader.struct_size:]
            scope = socket * 2 + is_server
            struct_message = None
            processor = None
            opcode = message_header.msg_type
            if opcode in opcode_processors[scope]:
                processor = opcode_processors[scope][opcode]
                if processor.struct.struct_size and len(raw_message) >= processor.struct.struct_size:
                    struct_message = processor.struct.from_buffer(raw_message)
                elif processor.struct.struct_size:
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
                event = processor.event(bundle_header, message_header, raw_message, struct_message)
            else:
                event = UnknownOpcodeEvent.get_event(bundle_header, message_header, raw_message, socket, is_server)
            self.create_mission(process_event, event)
            return bytearray(message_header) + raw_message

    def process_messages(self, bundle_header: BundleHeader, messages: list[bytearray], is_server: bool, socket: int) -> unpacked_messages:
        if not is_server:
            if socket not in self._socket_guessing_cache:
                guess = self.guess_socket_type(bundle_header, messages)
                if guess < 0: return bundle_header, messages
                self._socket_guessing_cache[socket] = guess
                self.sockets[guess] = socket
                socket = guess
            else:
                socket = self._socket_guessing_cache[socket]
        if bundle_header.magic0:
            pointer(self.magic_backup[socket])[0] = bundle_header
        return bundle_header, [self.process_message(bundle_header, message, is_server, socket) for message in messages]

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
                    'event': possible.event(evt.bundle_header, evt.message_header, evt.raw_message, struct_msg).str_event()
                })
