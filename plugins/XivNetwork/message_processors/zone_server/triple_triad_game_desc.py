from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerTripleTriadGameDesc(OffsetStruct({
    'event_id': (c_ushort, 0x0),
    'category': (c_ushort, 0x2),  # 0x23
    'rules': (c_ubyte * 4, 0xc),
}, 40)):
    event_id: int
    category: int
    rules: list[int]


class ServerTripleTriadGameDescEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'triple_triad_game_desc'
    struct_message: ServerTripleTriadGameDesc

    def __str__(self):
        return f"game rules of {self.struct_message.event_id}: {list(self.struct_message.rules)}"


class TripleTriadGameDesc(BaseProcessors):
    opcode = 'TripleTriadGameDesc'
    struct = ServerTripleTriadGameDesc
    event = ServerTripleTriadGameDescEvent
