from ctypes import *
from math import degrees

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.popular_struct import Vector3
from ..utils import NetworkZoneClientEvent, BaseProcessors


class ClientUpdatePositionInstance(OffsetStruct({
    'old_r': c_float,
    'new_r': c_float,
    'unk0': c_ushort,
    'unk1': c_ushort,
    'old_pos': Vector3,
    'new_pos': Vector3,
    'unk2': c_uint
}, 40)):
    old_r: float
    new_r: float
    unk0: int
    unk1: int
    old_pos: Vector3
    new_pos: Vector3
    unk2: int


class ClientUpdatePositionInstanceEvent(NetworkZoneClientEvent):
    id = NetworkZoneClientEvent.id + "update_position_instance"
    struct_message: ClientUpdatePositionInstance

    def __str__(self):
        new_pos = self.struct_message.new_pos
        old_pos = self.struct_message.old_pos
        return (f"moving to ({new_pos.x:.2f},{new_pos.y:.2f},{new_pos.z:.2f}) facing {degrees(self.struct_message.new_r):.2f}° "
                f"from ({old_pos.x:.2f},{old_pos.y:.2f},{old_pos.z:.2f}) facing {degrees(self.struct_message.old_r):.2f}°")


class UpdatePositionInstance(BaseProcessors):
    opcode = "UpdatePositionInstance"
    event = ClientUpdatePositionInstanceEvent
    struct = ClientUpdatePositionInstance
