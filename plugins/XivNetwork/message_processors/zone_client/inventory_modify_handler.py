from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneClientEvent, BaseProcessors


class ModifyInventoryEntry(OffsetStruct({
    'container': c_ushort,
    'param1': c_ushort,
    'slot': c_ushort,
    'param2': c_ushort,
    'param3': c_ushort,
    'param4': c_ushort,
    'param5': c_ushort,
})):
    container: int
    slot: int
    param1: int
    param2: int
    param3: int


class ClientInventoryModifyHandler(OffsetStruct({
    'sequence': (c_uint, 0x0),
    'action': (c_ushort, 0x4),
    'source': (ModifyInventoryEntry, 0xc),
    'target': (ModifyInventoryEntry, 0x20),
}, 0x30)):
    sequence: int
    action: int
    source: ModifyInventoryEntry
    target: ModifyInventoryEntry


class ClientInventoryModifyHandlerEvent(NetworkZoneClientEvent):
    id = NetworkZoneClientEvent.id + 'inventory_modify_handler'
    struct_message: ClientInventoryModifyHandler

    def __str__(self):
        msg = self.struct_message
        return f"[{msg.sequence}]{msg.action} from {msg.source.container}-{msg.source.slot} to {msg.target.container}-{msg.target.slot}"


class InventoryModifyHandler(BaseProcessors):
    opcode = "InventoryModifyHandler"
    event = ClientInventoryModifyHandlerEvent
    struct = ClientInventoryModifyHandler
