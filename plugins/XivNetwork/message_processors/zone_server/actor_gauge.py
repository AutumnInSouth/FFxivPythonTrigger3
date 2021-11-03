from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerActorGauge(OffsetStruct({
    'buffer': c_ubyte * 0x10,
}, 0x10)):
    buffer: list[int]


class ActorGaugeEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'actor_gauge'
    struct_message: ServerActorGauge

    def text(self):
        return "gauge is set as " + self.raw_message.hex(' ')

    def str_event(self):
        return "network_actor_gauge|" + self.raw_message.hex(' ')


class ActorGauge(BaseProcessors):
    opcode = "ActorGauge"
    struct = ServerActorGauge
    event = ActorGaugeEvent
