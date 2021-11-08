from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerEventFinish(OffsetStruct({
    'event_id': c_ushort,
    'category': c_ushort,
}, 0x10)):
    event_id: int
    category: int


class ServerEventFinishEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'event_finish'
    struct_message: ServerEventFinish

    def __str__(self):
        msg = self.struct_message
        return f'event_finish {msg.category:x} - {msg.event_id:x}'


class EventFinish(BaseProcessors):
    opcode = "EventFinish"
    struct = ServerEventFinish
    event = ServerEventFinishEvent
