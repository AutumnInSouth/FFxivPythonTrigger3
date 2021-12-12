from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerMapEffect(OffsetStruct({
    'param1': c_uint,
    'param2': c_uint,
    'param3': c_ushort,
    'param4': c_ushort,
},16)):
    param1: int
    param2: int
    param3: int
    param4: int


class ServerMapEffectEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'map_effect'
    struct_message: ServerMapEffect

    def __str__(self):
        msg = self.struct_message
        return f'map_effect {self.message_header.actor_id:x} - {msg.param1:x}|{msg.param2:x}|{msg.param3:x}|{msg.param4:x}'

    def str_event(self):
        msg = self.struct_message
        return f"network_map_effect|{self.message_header.actor_id:x}|{msg.param1:x}|{msg.param2:x}|{msg.param3:x}|{msg.param4:x}"


class MapEffect(BaseProcessors):
    opcode = "MapEffect"
    struct = ServerMapEffect
    event = ServerMapEffectEvent
