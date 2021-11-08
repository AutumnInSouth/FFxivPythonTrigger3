from ctypes import *

from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerStatusEffectEntry(OffsetStruct({
    'effect_index': c_ubyte,
    'unk0': c_ubyte,
    'effect_id': c_ushort,
    'unk1': c_ushort,
    'unk2': c_ushort,
    'duration': c_float,
    'source_actor_id': c_uint,
})):
    effect_index: int
    effect_id: int
    duration: float
    source_actor_id: int
    unk0: int
    unk1: int
    unk2: int


class ServerAddStatusEffect(OffsetStruct({
    'related_action_sequence': c_uint,
    'actor_id': c_uint,
    'current_hp': c_uint,
    'max_hp': c_uint,
    'current_mp': c_ushort,
    'unk0': c_ushort,
    'damage_shield': c_ubyte,
    'effect_count': c_ubyte,
    'unk1': c_ushort,
    'effects': ServerStatusEffectEntry * 4,
})):
    related_action_sequence: int
    actor_id: int
    current_hp: int
    max_hp: int
    current_mp: int
    unk0: int
    damage_shield: int
    effect_count: int
    unk1: int
    effects: list[ServerStatusEffectEntry]


class ServerAddStatusEffectEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'add_status_effect'
    struct_message: ServerAddStatusEffect

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerAddStatusEffect):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.target_id = struct_message.actor_id
        self.target_name = hex(self.target_id)
        self.target_actor = None
        self.effects = struct_message.effects[:min(struct_message.effect_count, 4)]

    def init(self):
        self.target_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.target_id)
        if self.target_actor is not None: self.target_name = self.target_actor.name

    def _text(self):
        e_s = ','.join([f'{e.effect_id}({e.source_actor_id}:x):{e.duration:.1f}' for e in self.effects if e.effect_id])
        return (
            f"{self.target_name}({self.struct_message.current_hp}(+{self.struct_message.damage_shield}%)/{self.struct_message.max_hp},"
            f"{self.struct_message.current_mp}/10000) add status effects [{e_s}]")


class AddStatusEffect(BaseProcessors):
    opcode = "AddStatusEffect"
    struct = ServerAddStatusEffect
    event = ServerAddStatusEffectEvent
