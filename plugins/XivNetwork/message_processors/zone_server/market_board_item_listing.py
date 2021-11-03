from ctypes import *
from functools import cached_property

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.saint_coinach import item_sheet
from ..utils import NetworkZoneServerEvent, BaseProcessors


class MarketBoardItemEntry(OffsetStruct({
    'listing_id': c_uint64,
    'retainer_id': c_uint64,
    'retainer_owner_id': c_uint64,
    'artisan_id': c_uint64,
    'price_per_uint': c_uint,
    'total_tax': c_uint,
    'total_item_count': c_uint,
    'item_id': c_uint,
    'last_review_before': c_ushort,
    'container': c_ushort,
    'slot': c_uint,
    'durability': c_ushort,
    'spiritbond': c_ushort,
    'materias': c_ushort * 5,
    'unk1': c_ushort,
    'unk2': c_uint,
    '_retainer_name': c_ubyte * 32,
    '_player_name': c_ubyte * 32,
    'is_hq': c_bool,
    'materia_count': c_ubyte,
    'is_mannequin': c_bool,
    'retainer_city_id': c_ubyte,
    'stain_id': c_ushort,
    'unk3': c_ushort,
    'unk4': c_uint,
})):
    @cached_property
    def retainer_name(self):
        return bytes(self._retainer_name).decode('utf-8').rstrip("\x00")

    @cached_property
    def player_name(self):
        return bytes(self._player_name).decode('utf-8').rstrip("\x00")



class ServerActorGauge(OffsetStruct({
    'buffer': c_ubyte * 0x10,
}, 0x10)):
    buffer: list[int]


class ActorGaugeEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'actor_gauge'
    struct_message: ServerActorGauge

    def text(self):
        return "gauge is set as " + self.raw_message.hex(' ')

    def str_event(self):
        return "network_actor_gauge|" + self.raw_message.hex(' ')


class ActorGauge(BaseProcessors):
    opcode = "ActorGauge"
    struct = ServerActorGauge
    event = ActorGaugeEvent
