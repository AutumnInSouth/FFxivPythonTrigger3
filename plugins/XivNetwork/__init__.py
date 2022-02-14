from ctypes import *
from functools import cache
from pathlib import Path
from traceback import format_exc
from typing import Callable, List, Dict, Set, Tuple, Union

import time

from FFxivPythonTrigger import PluginBase, AddressManager, BindValue, process_event, Counter
from FFxivPythonTrigger.decorator import unload_callback, re_event
from FFxivPythonTrigger.memory import read_memory
from FFxivPythonTrigger.memory.struct_factory import _OffsetStruct, OffsetStruct
from FFxivPythonTrigger.utils import WaitRecall
from .extra_messages import ExtraNetworkMessage
from .base_struct import BundleHeader, MessageHeader
from .decoder import unpacked_messages, pack_message
from .hook import SendHook, BufferProcessorHook
from .message_processors import opcode_processors, len_processors, key_to_code, code_to_key, _opcode_processors
from .message_processors.utils import _NetworkEvent, BaseProcessors
from .ping import Ping

send_sig = "48 83 EC ? 48 8B 49 ? 45 33 C9 FF 15 ? ? ? ? 85 C0"
chat_recv_buffer_sig = "48 8D 15 * * * * 48 8B CF E8 ? ? ? ? 48 8D 15 ? ? ? ? 48 8B CF E8 ? ? ? ? 45 8D 47 ?"
lobby_recv_buffer_sig = "48 8D 15 * * * * 48 8B CF E8 ? ? ? ? 48 8D 15 ? ? ? ? 48 8B CF E8 ? ? ? ? 44 8D 46 ?"
zone_recv_buffer_sig = "48 8D 15 * * * * 48 8B CE E8 ? ? ? ? 48 8D 15 ? ? ? ? 48 8B CE E8 ? ? ? ? 45 8D 47 ?"
fix_param_sig = "8B 0D * * * * 8B 15 ? ? ? ? 44 8B 05 ? ? ? ?"
scope_name = ["chat", "lobby", "zone"]

packet_fixer_interface = Callable[[BundleHeader, MessageHeader, bytearray, _OffsetStruct | None], bytearray | _OffsetStruct | None]
response_check_interface = Callable[[_NetworkEvent], bool]
send_message_interface = Tuple[int | str, bytearray | bytes | _OffsetStruct | dict]
allow_response_interface = Tuple[int | str, response_check_interface] | int | str

response_check_all_true = lambda e: True


class FixParam(OffsetStruct({
    'a1': (c_uint, 0),
    'a2': (c_uint, 4),
    'a3': (c_uint, 0xc),
})):
    @property
    def value(self):
        return min(self.a1 + self.a3 - self.a2, 0)


@cache
def scope_idx(key: str | int):
    if isinstance(key, int): return key
    try:
        return scope_name.index(key)
    except ValueError:
        raise ValueError(f"{key} is not a valid scope")


@cache
def get_opcode(scope: str | int, is_server: bool, key: str | int):
    if isinstance(key, int): return key
    try:
        return key_to_code[scope_idx(scope) * 2 + is_server][key]
    except KeyError:
        raise KeyError(f"{key} is not a valid opcode")


unknown_type_event = [dict() for _ in range(6)]


class UnknownOpcodeEvent(_NetworkEvent):
    scope_idx: int
    opcode: int
    msg_len: int

    def possible_processors(self) -> List[BaseProcessors]:
        return [
            processor
            for processor in len_processors[self.scope_idx].get(self.msg_len, set())
            if processor.opcode not in key_to_code[self.scope_idx]
        ]

    @classmethod
    def get_event(cls, bundle_header: 'BundleHeader', message_header: 'MessageHeader', raw_message: bytearray, scope: int, _is_server: bool):
        _scope_idx = scope * 2 + _is_server
        if message_header.msg_type not in unknown_type_event[_scope_idx]:
            _scope_name = scope_name[scope]

            class _UnknownOpcodeEvent(cls):
                scope = _scope_name
                is_server = _is_server
                id = f"{_NetworkEvent.id}unknown/{_scope_name}/{'server' if _is_server else 'client'}/{message_header.msg_type}"
                scope_idx = _scope_idx
                opcode = message_header.msg_type
                msg_len = len(raw_message)

            unknown_type_event[_scope_idx][message_header.msg_type] = _UnknownOpcodeEvent
        return unknown_type_event[_scope_idx][message_header.msg_type](bundle_header, message_header, raw_message)


class ResponseListener(object):
    def __init__(self, response_data, is_block, recall):
        self.response_data = response_data
        self.is_block = is_block
        self.recall = recall

    def check(self, message_event: _NetworkEvent):
        if self.recall is not None:
            if message_event.message_header.msg_type in self.response_data:
                if self.response_data[message_event.message_header.msg_type](message_event):
                    self.recall(message_event)
                    self.recall = None
                    return self.is_block


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
        self._fix_param = read_memory(FixParam, am.scan_point('fix_param', fix_param_sig))

        self.pings = dict()

        self.sockets = {}
        self.response_counter = Counter()
        self.response_waiting = {}
        self.response_listens = [{} for _ in range(3)]
        self._socket_guessing_cache = {}
        self._packet_fixer = [dict() for _ in range(6)]
        self.magic_backup = [BundleHeader() for _ in range(3)]
        self.header_backup = [MessageHeader() for _ in range(3)]

    @property
    def fix_param(self):
        return self._fix_param.value

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
                if header.sec > 1000000000:
                    return 2  # zone
                else:
                    return 0  # chat
        return -1

    def process_message(self, bundle_header: BundleHeader, message: bytearray, is_server: bool, socket: int):
        if len(message) < MessageHeader.struct_size:
            # ping message
            self.pings.setdefault(socket, Ping()).set(is_server)
            return message
        else:
            message_header = MessageHeader.from_buffer(message)
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
                try:
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
                except Exception:
                    self.logger.error("Exception in fixing message\n" + format_exc())

            if processor is not None:
                event = processor.event(bundle_header, message_header, raw_message, struct_message)
            else:
                event = UnknownOpcodeEvent.get_event(bundle_header, message_header, raw_message, socket, is_server)
            self.create_mission(process_event, event)

            if not is_server:
                memmove(pointer(self.header_backup[socket]), pointer(message_header), message_header.struct_size)
            else:
                for listener_id in self.response_listens[socket].get(opcode, set()).copy():
                    if listener_id in self.response_waiting:
                        is_block = self.response_waiting[listener_id].check(event)
                        if is_block is not None:
                            if is_block:
                                return bytearray()
                            else:
                                break

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
                memmove(pointer(self.magic_backup[socket]), pointer(bundle_header), bundle_header.struct_size)
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
                try:
                    struct_msg = possible.struct.from_buffer(evt.raw_message)
                except ValueError:
                    self.logger.error(f"{possible.opcode} require {possible.struct.struct_size} but {len(evt.raw_message)} is given")
                    continue
                possible_evt = possible.event(evt.bundle_header, evt.message_header, evt.raw_message, struct_msg)
                self.client_event('discover', {
                    'opcode': evt.opcode,
                    'guess': f"{evt.scope}/{'server' if evt.is_server else 'client'}/{possible.opcode}",
                    'struct': struct_msg.get_data(),
                    'event': possible_evt.str_event() or str(possible_evt)
                })

    @unload_callback('unregister_packet_fixer')
    def register_packet_fixer(self, scope: int | str, is_server: bool, opcode: int | str, method: packet_fixer_interface):
        scope = scope_idx(scope)
        opcode = get_opcode(scope, is_server, opcode)
        scope = scope * 2 + is_server
        self._packet_fixer[scope].setdefault(opcode, set()).add(method)
        self.logger(self._packet_fixer)

    def unregister_packet_fixer(self, scope: int | str, is_server: bool, opcode: int | str, method: packet_fixer_interface):
        scope = scope_idx(scope)
        opcode = get_opcode(scope, is_server, opcode)
        scope = scope * 2 + is_server
        try:
            self._packet_fixer[scope][opcode].remove(method)
            if not self._packet_fixer[scope][opcode]:
                del self._packet_fixer[scope][opcode]
        except (ValueError, KeyError):
            pass
        self.logger(self._packet_fixer)

    def send_messages(self, scope: int | str, messages: Union[send_message_interface, List[send_message_interface]],
                      response: Union[allow_response_interface, List[allow_response_interface]] = None,
                      block_response=False, response_timeout=5.):
        _scope = scope_idx(scope)
        _messages = []
        _processors = _opcode_processors[_scope * 2]
        current_time = time.time()

        # build messages
        if not isinstance(messages, list): messages = [messages]
        for opcode, message in messages:
            _opcode = get_opcode(scope, False, opcode)
            if isinstance(message, bytearray):
                _message = message
            else:
                if isinstance(message, dict):
                    if opcode in _processors:
                        message = _processors[opcode].struct.from_dict(message)
                    # self.logger(f"{opcode} {_processors[opcode].event(None,None,bytearray(message),message)}")
                    else:
                        raise Exception(f"no record struct found for opcode [{opcode}]")
                _message = bytearray(message)
            new_header = MessageHeader()
            pointer(new_header)[0] = self.header_backup[_scope]
            new_header.msg_length = len(_message) + MessageHeader.struct_size
            new_header.msg_type = _opcode
            new_header.sec = int(current_time)
            _messages.append(bytearray(new_header) + _message)

        # pack the messages
        new_bundle_header = BundleHeader()
        pointer(new_bundle_header)[0] = self.magic_backup[_scope]
        new_bundle_header.epoch = int(current_time * 1000)
        new_bundle_header.encoding = 0
        packed_message = pack_message(new_bundle_header, _messages)
        packed_length = len(packed_message)
        message_to_send = (c_ubyte * packed_length).from_buffer(packed_message)

        # build response data
        response_id = self.response_counter.get()
        response_data = {}
        if response:
            if not isinstance(response, list): response = [response]
            for _r in response:
                if isinstance(_r, tuple):
                    r_opcode, r_check = _r
                else:
                    r_opcode = _r
                    r_check = response_check_all_true
                r_opcode = get_opcode(_scope, True, r_opcode)
                response_data[r_opcode] = r_check
                self.response_listens[_scope].setdefault(r_opcode, set()).add(response_id)

        # send message, if no response require, just return message length
        socket = self.sockets[_scope]
        with self.send_hook.send_locks[socket]:
            success_size = self.send_hook.original(socket, message_to_send, packed_length)
        if success_size < 1: raise Exception(f"send failed, return code [{success_size}]")
        if not response_data: return success_size

        # set listener and wait for response
        wait_recall = WaitRecall()
        listener = ResponseListener(response_data, block_response, wait_recall.recall)
        self.response_waiting[response_id] = listener
        try:
            res = wait_recall.wait(response_timeout)
        finally:
            del self.response_waiting[response_id]
            for r_code in response_data.keys():
                self.response_listens[_scope][r_code].remove(response_id)
        return res
