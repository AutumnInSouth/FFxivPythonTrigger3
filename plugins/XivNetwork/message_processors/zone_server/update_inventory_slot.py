from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.saint_coinach import item_names, item_sheet
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerUpdateInventorySlot(OffsetStruct({
    'index': c_uint,
    'unk0': c_uint,
    'container_id': c_ushort,
    'slot': c_ushort,
    'count': c_uint,
    'item_id': c_uint,
    'reserved_flag': c_uint,
    'signature_id': c_ulonglong,
    'quality': c_ubyte,
    'attribute2': c_ubyte,
    'condition': c_ushort,
    'spiritbond': c_ushort,
    'stain': c_ushort,
    'glamour_catalog_id': c_ushort,
    'unk6': c_ushort,
    'materia1': c_ushort,
    'materia2': c_ushort,
    'materia3': c_ushort,
    'materia4': c_ushort,
    'materia5': c_ushort,
    'materia1_tier': c_ubyte,
    'materia2_tier': c_ubyte,
    'materia3_tier': c_ubyte,
    'materia4_tier': c_ubyte,
    'materia5_tier': c_ubyte,
    'unk10': c_ubyte,
    'unk11': c_uint,
}, 0x40)):
    index: int
    unk0: int
    container_id: int
    slot: int
    count: int
    item_id: int
    reserved_flag: int
    signature_id: int
    quality: int
    attribute2: int
    condition: int
    spiritbond: int
    stain: int
    glamour_catalog_id: int
    unk6: int
    materia1: int
    materia2: int
    materia3: int
    materia4: int
    materia5: int
    materia1_tier: int
    materia2_tier: int
    materia3_tier: int
    materia4_tier: int
    materia5_tier: int
    unk10: int
    unk11: int


class ServerUpdateInventorySlotEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'update_inventory_slot'
    struct_message: ServerUpdateInventorySlot

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.struct_message.item_id in item_names:
            self.item_name = item_names[self.struct_message.item_id]
            self.item = item_sheet[self.struct_message.item_id]
        else:
            self.item_name = 'Unknown'
            self.item = None

    def __str__(self):
        return f"update {self.item_name} x{self.struct_message.count} at container:{self.struct_message.container_id} - slot:{self.struct_message.slot}"


class UpdateInventorySlot(BaseProcessors):
    opcode = "UpdateInventorySlot"
    struct = ServerUpdateInventorySlot
    event = ServerUpdateInventorySlotEvent
