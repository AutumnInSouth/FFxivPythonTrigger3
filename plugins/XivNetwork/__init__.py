from ctypes import *
from pathlib import Path
from typing import Iterable

from FFxivPythonTrigger import PluginBase, AddressManager
from FFxivPythonTrigger.memory import read_memory
from FFxivPythonTrigger.memory.struct_factory import PointerStruct
from .base_struct import BundleHeader, MessageHeader
from .decoder import unpacked_messages
from .hook import RecvHook, SendHook
from .ping import Ping

send_sig = "48 83 EC ? 48 8B 49 ? 45 33 C9 FF 15 ? ? ? ? 85 C0"
recv_sig = "48 83 EC ? 48 8B 49 ? 45 33 C9 FF 15 ? ? ? ? 83 F8 ?"
zone_socket_ptr_sig = ("48 8D 0D * * * * E8 ? ? ? ? BA ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? "
                       "BA ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? 48 8D 0D ? ? ? ?")
socket_type_name = ["lobby", "zone", "chat"]


class XivNetwork(PluginBase):
    name = "XivNetwork"

    def __init__(self):
        super().__init__()

        am = AddressManager(self.name, self.logger)
        socket_ptr_base = am.scan_point('packet_ptr', zone_socket_ptr_sig)
        self.zone_pointer = read_memory(PointerStruct(c_longlong, 0x3c8, 0x8, 0, 0x28, 0x10), socket_ptr_base)
        self.chat_pointer = read_memory(PointerStruct(c_longlong, 0x3c8, 0x8, 0x80, 0xa8, 0x10), socket_ptr_base)
        self.recv_hook = RecvHook(self, am.scan_address('recv', recv_sig))
        self.send_hook = SendHook(self, am.scan_address('send', send_sig))
        self.pings = dict()

    def socket_type(self, socket: int) -> int:
        if socket == self.zone_pointer.value:
            return 1
        elif socket == self.chat_pointer.value:
            return 2
        else:
            return 0

    def process_message(self, bundle_header: BundleHeader, message: bytearray, is_send: bool, socket: int):
        if len(message) < MessageHeader.struct_size:
            self.pings.setdefault(socket, Ping()).set(is_send)
            return message
        else:
            # self.logger("\t", MessageHeader.from_buffer(message), message[MessageHeader.struct_size:].hex(' '))
            return message

    def process_messages(self, bundle_header: BundleHeader, messages: Iterable[bytearray], is_send: bool, socket: int) -> unpacked_messages:
        # self.logger(("send" if is_send else "recv"), hex(socket), socket_type_name[self.socket_type(socket)], bundle_header)
        return bundle_header, [self.process_message(bundle_header, message, is_send, socket) for message in messages]
