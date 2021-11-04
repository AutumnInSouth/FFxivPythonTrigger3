from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneClientEvent, BaseProcessors, NetworkZoneServerEvent


class ClientMarketBoardQueryItemCount(OffsetStruct({
    'item_id': c_uint,
    'unk1': c_uint,  # 0x902
}, 0x8)):
    item_id: int
    unk1: int


class ClientMarketBoardQueryItemCountEvent(NetworkZoneClientEvent):
    id = NetworkZoneServerEvent.id + 'market_board_query_item_count'

class MarketBoardQueryItemCount(BaseProcessors):
    opcode="MarketBoardQueryItemCount"
    struct = ClientMarketBoardQueryItemCount
    event = ClientMarketBoardQueryItemCountEvent
