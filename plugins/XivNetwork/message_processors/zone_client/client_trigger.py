from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneClientEvent, BaseProcessors


class ClientTriggerStruct(OffsetStruct({
    'param1': c_uint,
    'param2': c_uint,
    'param3': c_uint,
    'param4': c_uint,
    'param5': c_uint,
    'param6': c_uint,
    'param7': c_uint,
    'param8': c_uint,
}, 32)):
    param1: int
    param2: int
    param3: int
    param4: int
    param5: int
    param6: int
    param7: int
    param8: int


class ClientTriggerEvent(NetworkZoneClientEvent):
    id = NetworkZoneClientEvent.id + 'client_trigger'
    struct_message: ClientTriggerStruct

    def __str__(self):
        return (f"{self.struct_message.param1:x}|{self.struct_message.param2:x}|{self.struct_message.param3:x}|"
                f"{self.struct_message.param4:x}|{self.struct_message.param5:x}|{self.struct_message.param6:x}|"
                f"{self.struct_message.param7:x}|{self.struct_message.param8:x}")


class ClientTrigger(BaseProcessors):
    opcode = "ClientTrigger"
    struct = ClientTriggerStruct
    event = ClientTriggerEvent
