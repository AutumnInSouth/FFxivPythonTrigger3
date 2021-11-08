from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.saint_coinach import item_names, item_sheet
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerCurrencyCrystalInfo(OffsetStruct({
    'container_sequence': c_uint,
    'container_id': c_ushort,
    'slot': c_ushort,
    'count': c_uint,
    'unk0': c_uint,
    'item_id': c_uint,
    'unk1': c_uint,
    'unk2': c_uint,
    'unk3': c_uint,
}, 32)):
    container_sequence: int
    container_id: int
    slot: int
    count: int
    unk0: int
    item_id: int
    unk1: int
    unk2: int
    unk3: int


class ServerCurrencyCrystalInfoEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'currency_crystal_info'
    struct_message: ServerCurrencyCrystalInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.struct_message.item_id in item_names:
            self.item_name = item_names[self.struct_message.item_id]
            self.item = item_sheet[self.struct_message.item_id]
        else:
            self.item_name = 'Unknown'
            self.item = None

    def __str__(self):
        return f"{self.item_name} x{self.struct_message.count} at container:{self.struct_message.container_id} - slot:{self.struct_message.slot}"


class CurrencyCrystalInfo(BaseProcessors):
    opcode = "CurrencyCrystalInfo"
    event = ServerCurrencyCrystalInfoEvent
    struct = ServerCurrencyCrystalInfo
