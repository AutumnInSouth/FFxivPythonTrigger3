from ctypes import *
from functools import cache
from typing import Iterable, Callable, Tuple, List, Dict, Set

from FFxivPythonTrigger import PluginBase, AddressManager, BindValue
from FFxivPythonTrigger.memory import read_memory
from FFxivPythonTrigger.memory.struct_factory import PointerStruct, _OffsetStruct
from .base_struct import BundleHeader, MessageHeader
from .decoder import unpacked_messages
from .hook import RecvHook, SendHook
from .message_processors import opcode_processors, len_processors, key_to_code, code_to_key
from .ping import Ping

send_sig = "48 83 EC ? 48 8B 49 ? 45 33 C9 FF 15 ? ? ? ? 85 C0"
recv_sig = "48 83 EC ? 48 8B 49 ? 45 33 C9 FF 15 ? ? ? ? 83 F8 ?"
zone_socket_ptr_sig = ("48 8D 0D * * * * E8 ? ? ? ? BA ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? "
                       "BA ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? 48 8D 0D ? ? ? ?")
scope_name = ["chat", "lobby", "zone"]

packet_fixer_interface = Callable[[BundleHeader, MessageHeader, bytearray, _OffsetStruct | None], Tuple[MessageHeader, bytearray | _OffsetStruct]]


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


class XivNetwork(PluginBase):
    name = "XivNetwork"
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
            if message_header.msg_type in opcode_processors[socket * 2 + is_send]:
                pass
            else:
                pass
            # self.logger("\t", MessageHeader.from_buffer(message), message[MessageHeader.struct_size:].hex(' '))
            return message

    def process_messages(self, bundle_header: BundleHeader, messages: Iterable[bytearray], is_send: bool, socket: int) -> unpacked_messages:
        return bundle_header, [self.process_message(bundle_header, message, is_send, socket) for message in messages]
