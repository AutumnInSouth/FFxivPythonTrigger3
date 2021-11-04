from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.saint_coinach import item_sheet
from ..utils import NetworkZoneServerEvent, BaseProcessors


class MarketBoardHistoryItemEntry(OffsetStruct({
    'selling_price': c_uint,
    'purchase_time': c_uint,
    'item_count': c_uint,
    'is_hq': c_bool,
    'unk1': c_ubyte,
    'is_mannequin': c_bool,
    '_buyer_name': c_ubyte * 33,
    'item_id': c_uint,
})):
    selling_price: int
    purchase_time: int
    item_count: int
    is_hq: bool
    unk1: int
    is_mannequin: bool
    _buyer_name: list[int]
    item_id: int

    @property
    def buyer_name(self):
        return bytes(self._buyer_name).decode('utf-8').rstrip("\x00")


class ServerMarketBoardItemListHistory(OffsetStruct({
    'item_id': c_uint,
    'item_id2': c_uint,
    'histories': MarketBoardHistoryItemEntry * 20,
})):
    item_id: int
    item_id2: int
    histories: list[MarketBoardHistoryItemEntry]


class MarketBoardItemListHistoryEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'market_board_item_listing_history'
    struct_message: ServerMarketBoardItemListHistory

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerMarketBoardItemListHistory):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.item = item_sheet[self.struct_message.item_id]
        self.history_count = 0
        for history in self.struct_message.histories:
            if history.item_id:
                self.history_count += 1
            else:
                break

    def __str__(self):
        return f"histories of {self.item['Name']} x{self.history_count}"


class MarketBoardItemListHistory(BaseProcessors):
    opcode = "MarketBoardItemListingHistory"
    struct = ServerMarketBoardItemListHistory
    event = MarketBoardItemListHistoryEvent
