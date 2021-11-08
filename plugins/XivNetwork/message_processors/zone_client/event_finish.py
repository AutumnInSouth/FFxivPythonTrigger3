from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneClientEvent, BaseProcessors


class ClientEventFinish(OffsetStruct({
    'event_id': c_ushort,
    'category': c_ushort,
    'param1': c_uint,
    'param2': c_uint,
    'param3': c_uint,
}, 16)):
    event_id: int
    category: int
    param1: int
    param2: int
    param3: int


class ClientEventFinishEvent(NetworkZoneClientEvent):
    id = NetworkZoneClientEvent.id + 'event_finish'
    struct_message: ClientEventFinish

    def __str__(self):
        return (f"{self.struct_message.category:x}|{self.struct_message.event_id:x}|"
                f"{self.struct_message.param1:x}|{self.struct_message.param2:x}|{self.struct_message.param3:x}")


class EventFinish(BaseProcessors):
    opcode = "EventFinish"
    struct = ClientEventFinish
    event = ClientEventFinishEvent
