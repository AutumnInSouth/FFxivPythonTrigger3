from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerTripleTriadGameData(OffsetStruct({
    'event_id': (c_ushort, 0x0),
    'category': (c_ushort, 0x2),
    'rules': (c_ubyte * 4, 0xc),
    '_force_hand_id': (c_ubyte, 0x12),
    'blue_first': (c_bool, 0x13),
    '_cards': (c_ushort * 10, 0x18),
}, 72)):
    event_id: int
    category: int
    rules: list[int]
    blue_first: bool

    @property
    def force_hand_id(self):
        return self._force_hand_id if self._force_hand_id < 5 else None

    @property
    def blue_card(self):
        return [self._cards[1], self._cards[0], self._cards[3], self._cards[2], self._cards[5]]

    @property
    def red_card(self):
        return [self._cards[4], self._cards[7], self._cards[6], self._cards[9], self._cards[8]]


class ServerTripleTriadGameDataEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'triple_triad_game_data'
    struct_message: ServerTripleTriadGameData

    def __str__(self):
        msg = self.struct_message
        return (f"game data of {msg.event_id}: {'blue' if msg.blue_first else 'red'} first, "
                f"rules: {list(msg.rules)}, blue_card:{msg.blue_card}, red_card:{msg.red_card}")


class TripleTriadGameData(BaseProcessors):
    opcode = 'TripleTriadGameData'
    struct = ServerTripleTriadGameData
    event = ServerTripleTriadGameDataEvent
