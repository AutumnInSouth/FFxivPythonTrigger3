from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerCraftStatus(OffsetStruct({
    'actor_id': (c_uint, 0),
    'prev_action_id': (c_uint, 0x2c),
    'round': (c_uint, 0x34),
    'current_progress': (c_int, 0x38),
    'add_progress': (c_int, 0x3c),
    'current_quality': (c_int, 0x40),
    'add_quality': (c_int, 0x44),
    'current_durability': (c_int, 0x4c),
    'add_durability': (c_int, 0x50),
    'status_id': (c_ushort, 0x54),
    'prev_action_flag': (c_ushort, 0x5c),
}, 160)):
    actor_id: int
    prev_action_id: int
    round: int
    current_progress: int
    add_progress: int
    current_quality: int
    add_quality: int
    current_durability: int
    add_durability: int
    status_id: int
    prev_action_flag: int

    @property
    def prev_action_success(self):
        return bool(self.prev_action_flag & 0x10)


class ServerCraftStatusEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'craft_status'
    struct_message: ServerCraftStatus

    def __str__(self):
        msg = self.struct_message
        return f"round:{msg.round}({msg.current_progress}/{msg.current_quality}/{msg.current_durability})status:{msg.status_id}"


class CraftStatus(BaseProcessors):
    opcode = "CraftStatus"
    struct = ServerCraftStatus
    event = ServerCraftStatusEvent
