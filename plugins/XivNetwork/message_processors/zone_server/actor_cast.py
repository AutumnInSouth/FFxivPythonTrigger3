from ctypes import *
from typing import TYPE_CHECKING

from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.saint_coinach import action_names
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors

if TYPE_CHECKING:
    from XivMemory.struct.actor import Actor


class ServerActorCast(OffsetStruct({
    'action_id': c_ushort,
    'skill_type': c_ubyte,
    'display_delay': c_ubyte,
    'display_action_id': c_uint,
    'cast_time': c_float,
    'target_id': c_uint,
    'rotation': c_float,
    'unk2': c_uint,
    'x': c_ushort,
    'y': c_ushort,
    'z': c_ushort,
    'unk3': c_ushort,
})):
    action_id: int
    skill_type: int
    display_delay: int
    display_action_id: int
    cast_time: float
    target_id: int
    rotation: float
    unk2: int
    x: int
    y: int
    z: int
    unk3: int


class ServerActorCastEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'actor_cast'
    struct_message: ServerActorCast
    target_actor: 'Actor|None'
    source_actor: 'Actor|None'

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.target_id = struct_message.target_id
        self.source_id = message_header.actor_id
        self.action_id = struct_message.action_id
        self.cast_time = struct_message.cast_time
        self.target_name = hex(self.target_id)
        self.source_name = hex(self.source_id)

    def init(self):
        self.target_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.target_id)
        if self.target_actor is not None: self.target_name = self.target_actor.name
        self.source_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.source_id)
        if self.source_actor is not None: self.source_name = self.source_actor.name

    def _text(self):
        return f"{self.source_name} is casting {action_names.get(self.action_id)} on {self.target_name} for {self.cast_time:.2f} seconds"

    def _str_event(self):
        return f"network_cast|{self.action_id}|{action_names.get(self.action_id)}|{self.source_name}|{self.target_name}|{self.cast_time:.2f}"


class ActorCast(BaseProcessors):
    opcode = "ActorCast"
    event = ServerActorCastEvent
    struct = ServerActorCast
