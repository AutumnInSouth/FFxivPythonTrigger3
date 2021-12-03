from ctypes import *

from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerActorControlTarget(OffsetStruct({
    'category': c_ushort,
    'padding0': c_ushort,
    'param1': c_uint,
    'param2': c_uint,
    'param3': c_uint,
    'param4': c_uint,
    'padding1': c_uint,
    'target_id': c_uint,
    'padding2': c_uint,
})):
    category: int
    padding0: int
    param1: int
    param2: int
    param3: int
    param4: int
    padding1: int
    target_id: int
    padding1: int


class ActorControlTargetEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'actor_control_target/'
    struct_message: ServerActorControlTarget


class UnknownActorControlTargetEvent(ActorControlTargetEvent):
    id = ActorControlTargetEvent.id + 'unk_144'

    def text(self):
        return f'unknown actor control 144 category from {self.message_header.actor_id:x} {self.struct_message.category:x}|{self.struct_message.param1:x}|' \
               f'{self.struct_message.param2:x}|{self.struct_message.param3:x}|{self.struct_message.param4:x}|' \
               f'{self.struct_message.target_id:x}'


class SetTargetEvent(ActorControlTargetEvent):
    id = ActorControlTargetEvent.id + 'set_target'
    target_actor: any

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.actor_id = struct_message.target_id
        self.actor_name = hex(self.actor_id)
        self.target_id = struct_message.param2
        self.target_name = hex(self.target_id)

    def init(self):
        self.target_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.target_id)
        if self.target_actor is not None: self.target_name = self.target_actor.name
        self.actor = plugins.XivMemory.actor_table.get_actor_by_id(self.actor_id)
        if self.actor is not None: self.actor_name = self.actor.name

    def _text(self):
        return f"{self.actor_name} set target on {self.target_name}"

    def _str_event(self):
        return f"network_actor_set_target|{self.actor_name}|{self.target_name}"


class ActorControlTarget(BaseProcessors):
    opcode = "ActorControlTarget"
    struct = ServerActorControlTarget

    @staticmethod
    def event(bundle_header, message_header, raw_message, struct_message: ServerActorControlTarget):
        if struct_message.category == 502:
            evt = SetTargetEvent
        else:
            evt = UnknownActorControlTargetEvent
        return evt(bundle_header, message_header, raw_message, struct_message)
