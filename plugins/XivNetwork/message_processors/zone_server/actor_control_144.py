from ctypes import *

from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerActorControl144(OffsetStruct({
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

class ActorControl144Event(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'actor_control/'
    struct_message: ServerActorControl144
    target_actor: any

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.target_id = message_header.actor_id
        self.target_name = hex(self.target_id)

    def init(self):
        self.target_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.target_id)
        if self.target_actor is not None: self.target_name = self.target_actor.name

class UnknownActorControl143Event(ActorControl144Event):
    id = ActorControl144Event.id + 'unk_144'

    def text(self):
        return f'unknown actor control 144 category from {self.target_name} {self.struct_message.category:x}|{self.struct_message.param1:x}|' \
               f'{self.struct_message.param2:x}|{self.struct_message.param3:x}|{self.struct_message.param4:x}|' \
               f'{self.struct_message.target_id:x}'


class SetTargetEvent(ActorControl144Event):
    id = ActorControl144Event.id + 'set_target'

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerActorControl144):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.param = struct_message.param1 & 255

    def text(self):
        return f"limit break {self.param}/10000*3"

    def str_event(self):
        return f"network_actor_limit_break|{self.param}"
