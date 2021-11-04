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
    'price_per_unit': c_uint,
    'total_tax': c_uint,
    'total_item_count': c_uint,
    'item_id': c_uint,
    'last_review_before': c_ushort,
    'container': c_ushort,
    'slot': c_ushort,
    'unk0': c_ushort,
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
    listing_id: int
    retainer_id: int
    retainer_owner_id: int
    artisan_id: int
    price_per_uint: int
    total_tax: int
    total_item_count: int
    item_id: int
    last_review_before: int
    container: int
    slot: int
    unk0: int
    durability: int
    spiritbond: int
    materias: list[int]
    unk1: int
    unk2: int
    _retainer_name: list[int]
    _player_name: list[int]
    is_hq: bool
    materia_count: int
    is_mannequin: bool
    retainer_city_id: int
    stain_id: int
    unk3: int
    unk4: int

    @cached_property
    def retainer_name(self):
        return bytes(self._retainer_name).decode('utf-8').rstrip("\x00")

    @cached_property
    def player_name(self):
        return bytes(self._player_name).decode('utf-8').rstrip("\x00")


class ServerMarketBoardItemList(OffsetStruct({
    'items': MarketBoardItemEntry * 10,
    'list_index_end': c_ubyte,
    'list_index_start': c_ubyte,
    'request_id': c_ubyte,
    'unk1': c_ubyte
}, 1528)):
    items: list[MarketBoardItemEntry]
    list_index_end: int
    list_index_start: int
    request_id: int
    unk1: int


class MarketBoardItemListEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'market_board_item_listing'
    struct_message: ServerMarketBoardItemList

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerMarketBoardItemList):
        super(MarketBoardItemListEvent, self).__init__(bundle_header, message_header, raw_message, struct_message)
        self.item = item_sheet[struct_message.items[0].item_id]
        self.item_count = 0
        for item in struct_message.items:
            if item.item_id:
                self.item_count += 1
            else:
                break

    def __str__(self):
        return f"{self.item['Name']} x{self.item_count} request:{self.struct_message.request_id} {self.struct_message.list_index_start} - {self.struct_message.list_index_end}"


class MarketBoardItemList(BaseProcessors):
    opcode = "MarketBoardItemListing"
    event = MarketBoardItemListEvent
    struct = ServerMarketBoardItemList
