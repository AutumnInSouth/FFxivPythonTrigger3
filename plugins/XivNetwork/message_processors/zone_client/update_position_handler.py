from ctypes import *
from math import degrees

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.popular_struct import Vector3
from ..utils import NetworkZoneClientEvent, BaseProcessors


class ClientUpdatePositionHandler(OffsetStruct({
    'r': c_float,
    'unk0': c_ushort,
    'unk1': c_ushort,
    'pos': Vector3,
    'unk2': c_uint
}, 24)):
    r: float
    unk0: int
    unk1: int
    pos: Vector3
    unk2: int


class ClientUpdatePositionHandlerEvent(NetworkZoneClientEvent):
    id = NetworkZoneClientEvent.id + "update_position_handler"
    struct_message: ClientUpdatePositionHandler

    def __str__(self):
        pos = self.struct_message.pos
        return f"move to ({pos.x:.2f},{pos.y:.2f},{pos.z:.2f}) facing {degrees(self.struct_message.r):.2f}°"


class UpdatePositionHandler(BaseProcessors):
    opcode = "UpdatePositionHandler"
    event = ClientUpdatePositionHandlerEvent
    struct = ClientUpdatePositionHandler
