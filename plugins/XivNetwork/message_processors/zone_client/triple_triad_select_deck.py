from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneClientEvent, BaseProcessors


class ClientTripleTriadSelectDeck(OffsetStruct({
    'event_id': (c_ushort, 0x0),
    'category': (c_ushort, 0x2),  # 0x23
    'unk0': (c_uint, 0x4),  # 0x6000000
    'unk1': (c_uint, 0x8),  # 0x4
    'cards': (c_uint * 5, 0xc),
}, 40)):
    event_id: int
    category: int
    unk0: int
    unk1: int
    cards: list[int]


class ClientTripleTriadSelectDeckEvent(NetworkZoneClientEvent):
    id = NetworkZoneClientEvent.id + 'triple_triad_select_deck'
    struct_message: ClientTripleTriadSelectDeck

    def __str__(self):
        msg = self.struct_message
        return f'select {msg.event_id}: cards:{list(msg.cards)}'


class TripleTriadSelectDeck(BaseProcessors):
    opcode = 'TripleTriadSelectDeck'
    struct = ClientTripleTriadSelectDeck
    event = ClientTripleTriadSelectDeckEvent
