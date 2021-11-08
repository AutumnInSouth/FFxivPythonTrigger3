from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerTripleTriadPlaceCardRecv(OffsetStruct({
    'event_id': (c_ushort, 0x0),
    'category': (c_ushort, 0x2),  # 0x23
    'block_id': (c_ubyte, 0xc),
    'hand_id': (c_ubyte, 0xd),
    'card_id': (c_ushort, 0xe),
    '_flags': (c_uint, 0x10),
}, 24)):
    event_id: int
    category: int
    block_id: int
    hand_id: int
    card_id: int

    @property
    def force_hand_id(self):
        _force_hand_id = (self._flags >> 28) // 2
        return _force_hand_id if _force_hand_id < 5 else None


class ServerTripleTriadPlaceCardRecvEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'triple_triad_place_card_recv'
    struct_message: ServerTripleTriadPlaceCardRecv

    def __str__(self):
        msg = self.struct_message
        return f'place {msg.event_id}:hand:{msg.hand_id} block:{msg.block_id} card:{msg.card_id}'


class TripleTriadPlaceCardRecv(BaseProcessors):
    opcode = 'TripleTriadPlaceCardRecv'
    struct = ServerTripleTriadPlaceCardRecv
    event = ServerTripleTriadPlaceCardRecvEvent
