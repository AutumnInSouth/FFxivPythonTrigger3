from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.saint_coinach import item_sheet,item_names
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerMarketBoardItemListCount(OffsetStruct({
    'item_id': c_uint,
    'item_count': (c_ubyte, 0xb),
}, 0x10)):
    item_id: int
    item_count: int


class MarketBoardItemListCountEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'market_board_item_listing_count'
    struct_message: ServerMarketBoardItemListCount

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerMarketBoardItemListCount):
        super(MarketBoardItemListCountEvent, self).__init__(bundle_header, message_header, raw_message, struct_message)
        if self.struct_message.item_id in item_names:
            self.item_name = item_names[self.struct_message.item_id]
            self.item = item_sheet[self.struct_message.item_id]
        else:
            self.item_name = 'Unknown'
            self.item = None

    def __str__(self):
        return f"{self.item_name} x{self.struct_message.item_count}"


class MarketBoardItemListCount(BaseProcessors):
    opcode = "MarketBoardItemListingCount"
    event = MarketBoardItemListCountEvent
    struct = ServerMarketBoardItemListCount
