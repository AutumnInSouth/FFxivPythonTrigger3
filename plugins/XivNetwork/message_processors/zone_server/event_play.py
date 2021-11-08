from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerEventPlay(OffsetStruct({
    'target_id': c_uint,
    'unk0': c_uint,
    'event_id': c_ushort,
    'category': c_ushort,
}, 0x28)):
    target_id: int
    event_id: int
    category: int


class ServerEventPlayEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'event_play'
    struct_message: ServerEventPlay

    def __str__(self):
        msg = self.struct_message
        return f'event_play {msg.category:x} - {msg.event_id:x} target:{msg.target_id:x}'


class EventPlay(BaseProcessors):
    opcode = "EventPlay"
    struct = ServerEventPlay
    event = ServerEventPlayEvent
