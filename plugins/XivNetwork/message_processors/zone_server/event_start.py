from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerEventStart(OffsetStruct({
    'target_id': c_uint,
    'unk0': c_uint,
    'event_id': c_ushort,
    'category': c_ushort,
}, 0x18)):
    target_id: int
    event_id: int
    category: int


class ServerEventStartEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'event_start'
    struct_message: ServerEventStart

    def __str__(self):
        msg = self.struct_message
        return f'event_start {msg.category:x} - {msg.event_id:x} target:{msg.target_id:x}'


class EventStart(BaseProcessors):
    opcode = "EventStart"
    struct = ServerEventStart
    event = ServerEventStartEvent
