from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneClientEvent, BaseProcessors


class ClientTripleTriadPlaceCardSend(OffsetStruct({
    'event_id': (c_ushort, 0x0),
    'category': (c_ushort, 0x2),  # 0x23
    'unk0': (c_uint, 0x4),  # 0x4000000
    'unk1': (c_uint, 0x8),  # 0x5
    'round': (c_uint, 0xc),
    'hand_id': (c_uint, 0x10),
    'block_id': (c_uint, 0x14),
}, 24)):
    event_id: int
    category: int
    unk0: int
    unk1: int
    round: int
    hand_id: int
    block_id: int


class ClientTripleTriadPlaceCardSendEvent(NetworkZoneClientEvent):
    id = NetworkZoneClientEvent.id + 'triple_triad_place_card_send'
    struct_message: ClientTripleTriadPlaceCardSend

    def __str__(self):
        msg = self.struct_message
        return f'place {msg.event_id}: round:{msg.round} hand:{msg.hand_id} block:{msg.block_id}'


class TripleTriadPlaceCardSend(BaseProcessors):
    opcode = 'TripleTriadPlaceCardSend'
    struct = ClientTripleTriadPlaceCardSend
    event = ClientTripleTriadPlaceCardSendEvent
