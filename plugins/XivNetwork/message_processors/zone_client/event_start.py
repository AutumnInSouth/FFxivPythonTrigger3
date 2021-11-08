from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneClientEvent, BaseProcessors


class ClientEventStart(OffsetStruct({
    'target_id': c_uint,
    'unk0': c_uint,
    'event_id': c_ushort,
    'category': c_ushort,
    'unk3': c_uint,
}, 16)):
    target_id: int
    unk0: int
    event_id: int
    category: int
    unk3: int


class ClientEventStartEvent(NetworkZoneClientEvent):
    id = NetworkZoneClientEvent.id + 'event_start'
    struct_message: ClientEventStart

    def __str__(self):
        return (f"{self.struct_message.target_id:x}|{self.struct_message.category:x}|{self.struct_message.event_id:x}|"
                f"{self.struct_message.unk0:x}|{self.struct_message.unk3:x}")


class EventStart(BaseProcessors):
    opcode = "EventStart"
    struct = ClientEventStart
    event = ClientEventStartEvent
