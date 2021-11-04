from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneClientEvent, BaseProcessors, NetworkZoneServerEvent


class ClientMarketBoardPurchaseHandler(OffsetStruct({
    'retainer_id': c_ulonglong,
    'listing_id': c_ulonglong,
    'item_id': c_uint,
    'total_item_count': c_uint,
    'price_per_unit': c_uint,
    'total_tax': c_uint,
    'unk0': c_ushort,  # item.unk0
    'unk1': c_ubyte,
    'retainer_city_id': c_ubyte,
    'unk2': c_uint,  # ?
})):
    retainer_id: int
    listing_id: int
    item_id: int
    quantity: int
    price_per_unit: int
    total_tax: int
    unk0: int
    unk1: int
    retainer_city_id: int
    unk2: int


class ServerMarketBoardPurchaseHandlerEvnet(NetworkZoneClientEvent):
    id = NetworkZoneServerEvent.id + 'market_board_purchase_handler'


class MarketBoardPurchaseHandler(BaseProcessors):
    opcode = "MarketBoardPurchaseHandler"
    struct = ClientMarketBoardPurchaseHandler
    event = ServerMarketBoardPurchaseHandlerEvnet
