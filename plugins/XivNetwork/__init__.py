from ctypes import *
from typing import Iterable, Tuple

from FFxivPythonTrigger import PluginBase, AddressManager
from FFxivPythonTrigger.memory import read_memory, BASE_ADDR
from FFxivPythonTrigger.memory.struct_factory import PointerStruct
from .base_struct import BundleHeader, MessageHeader
from .decoder import unpacked_messages
from .hook import RecvHook, SendHook

send_sig = "48 83 EC ? 48 8B 49 ? 45 33 C9 FF 15 ? ? ? ? 85 C0"
recv_sig = "48 83 EC ? 48 8B 49 ? 45 33 C9 FF 15 ? ? ? ? 83 F8 ?"
zone_socket_ptr_sig = ("48 8D 0D * * * * E8 ? ? ? ? BA ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? "
                       "BA ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? 48 8D 0D ? ? ? ?")


class XivNetwork(PluginBase):
    name = "XivNetwork"

    def __init__(self):
        super().__init__()
        am = AddressManager(self.name, self.logger)
        self.zone_pointer = read_memory(
            PointerStruct(c_longlong, 0x368),
            am.scan_point('zone_packet_ptr', zone_socket_ptr_sig)
        )
        self.recv_hook = RecvHook(self, am.scan_address('recv', recv_sig))
        self.send_hook = SendHook(self, am.scan_address('send', send_sig))

    def is_zone_socket(self, socket: int) -> bool:
        return socket == self.zone_pointer.value

    def process_msg(self, bundle_header: BundleHeader, messages: Iterable[bytearray],
                    is_send: bool, socket: int) -> unpacked_messages:
        # self.logger(("send" if is_send else "recv"), ("zone" if self.is_zone_socket(socket) else f"non_zone:{self.zone_pointer.value:x}"), bundle_header)
        # for message in messages:
        #     if len(message) < MessageHeader.struct_size:
        #         self.logger("\t", message.hex(' '))
        #     else:
        #         self.logger("\t", MessageHeader.from_buffer(message),message[MessageHeader.struct_size:].hex(' '))
        return bundle_header, list(messages)


"""
<?xml version="1.0" encoding="utf-8"?>
<CheatTable>
  <CheatEntries>
    <CheatEntry>
      <ID>0</ID>
      <Description>"zone socket"</Description>
      <LastState Value="2627302936" RealAddress="2349BF04070"/>
      <VariableType>4 Bytes</VariableType>
      <Address>"ffxiv_dx11.exe"+01D6B3C8</Address>
      <Offsets>
        <Offset>0</Offset>
        <Offset>368</Offset>
      </Offsets>
    </CheatEntry>
    <CheatEntry>
      <ID>1</ID>
      <Description>"chat result"</Description>
      <LastState Value="2627302936" RealAddress="2349BF04210"/>
      <VariableType>4 Bytes</VariableType>
      <Address>"ffxiv_dx11.exe"+01D6B3C8</Address>
      <Offsets>
        <Offset>0</Offset>
        <Offset>10</Offset>
        <Offset>10</Offset>
        <Offset>8</Offset>
        <Offset>130</Offset>
        <Offset>368</Offset>
      </Offsets>
    </CheatEntry>
  </CheatEntries>
</CheatTable>
"""
