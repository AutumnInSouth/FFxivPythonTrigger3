from ctypes import *
from typing import Union, TYPE_CHECKING
from functools import cached_property

from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.saint_coinach import status_names
from ..utils import NetworkZoneServerEvent, BaseProcessors

if TYPE_CHECKING:
    from XivMemory.struct.actor import Actor


class ServerStatusEffectListEntry(OffsetStruct({
    'effect_id': c_ushort,
    'param': c_ushort,
    'duration': c_float,
    'actor_id': c_uint,
})):
    effect_id: int
    param: int
    duration: float
    actor_id: int


class StatusEffect:
    effect_id: int
    param: int
    actor_id: int

    def __init__(self, effect_id: int, param: int, actor_id: int):
        self.effect_id = effect_id
        self.param = param
        self.actor_id = actor_id

    def __hash__(self):
        return hash((self.effect_id, self.actor_id))

    def __eq__(self, other):
        return (self.effect_id, self.actor_id) == (other.effect_id, other.actor_id)


class ServerStatusEffectList(OffsetStruct({
    'job_id': c_ubyte,
    'level_1': c_ubyte,
    'level_2': c_ubyte,
    'level_3': c_ubyte,
    'current_hp': c_uint,
    'max_hp': c_uint,
    'current_mp': c_ushort,
    'max_mp': c_ushort,
    'unk0': c_ushort,
    'damage_shield': c_ubyte,
    'unk1': c_ubyte,
    'effects': ServerStatusEffectListEntry * 30,
})):
    job_id: int
    level_1: int
    level_2: int
    level_3: int
    current_hp: int
    max_hp: int
    current_mp: int
    max_mp: int
    unk0: int
    damage_shield: int
    unk1: int
    effects: list[ServerStatusEffectListEntry]


class ServerStatusEffectList2(OffsetStruct({
    'unk0': c_uint,
    'job_id': c_ubyte,
    'level_1': c_ubyte,
    'level_2': c_ubyte,
    'level_3': c_ubyte,
    'current_hp': c_uint,
    'max_hp': c_uint,
    'current_mp': c_ushort,
    'max_mp': c_ushort,
    'unk1': c_ushort,
    'damage_shield': c_ubyte,
    'unk2': c_ubyte,
    'effects': ServerStatusEffectListEntry * 30,
})):
    unk0: int
    job_id: int
    level_1: int
    level_2: int
    level_3: int
    current_hp: int
    max_hp: int
    current_mp: int
    max_mp: int
    unk1: int
    damage_shield: int
    unk2: int
    effects: list[ServerStatusEffectListEntry]


class ServerBossStatusEffectList(OffsetStruct({
    'effects_2': ServerStatusEffectListEntry * 30,
    'job_id': c_ubyte,
    'level_1': c_ubyte,
    'level_2': c_ubyte,
    'level_3': c_ubyte,
    'current_hp': c_uint,
    'max_hp': c_uint,
    'current_mp': c_ushort,
    'max_mp': c_ushort,
    'unk0': c_ushort,
    'damage_shield': c_ubyte,
    'unk1': c_ubyte,
    'effects_1': ServerStatusEffectListEntry * 30,
    'unk2': c_uint,
})):
    effects_2: list[ServerStatusEffectListEntry]
    job_id: int
    level_1: int
    level_2: int
    level_3: int
    current_hp: int
    max_hp: int
    current_mp: int
    max_mp: int
    unk0: int
    damage_shield: int
    unk1: int
    effects_1: list[ServerStatusEffectListEntry]
    unk2: int

    @cached_property
    def effects(self):
        return list(self.effects_1) + list(self.effects_2)


class ServerStatusEffectListEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'status_effect_list'
    struct_message: Union[ServerStatusEffectList, ServerStatusEffectList2, ServerBossStatusEffectList]
    target_actor: 'Actor|None'
    add_effects: set[StatusEffect]
    remove_effects: set[StatusEffect]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.levels = (self.struct_message.level_1, self.struct_message.level_2, self.struct_message.level_3)
        self.effects = [effect for effect in self.struct_message.effects if effect.effect_id != 0]
        self.target_id = self.message_header.actor_id
        self.target_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.target_id)
        if self.target_actor is not None:
            self.target_name = self.target_actor.name
            self.new_effects = {StatusEffect(effect.effect_id, effect.param, effect.actor_id) for effect in self.effects}
            self.old_effects = {StatusEffect(effect.buff_id, effect.param, effect.actor_id) for e_id, effect in self.target_actor.effects.get_items()}
            self.add_effects = self.new_effects - self.old_effects
            self.remove_effects = self.old_effects - self.new_effects
        else:
            self.target_name = hex(self.target_id)
            self.new_effects = set()
            self.old_effects = set()
            self.add_effects = set()
            self.remove_effects = set()

    def _text(self):
        e_s = ', '.join([f"{status_names.get(e.effect_id, 'Unknown')}(from {e.actor_id:x}):{e.duration:.1f}s" for e in self.effects])
        msg = self.struct_message
        return f"update {self.target_name}; {msg.current_hp:,}(+{msg.damage_shield}%)/{msg.max_hp:,}; {msg.current_mp:,}/{msg.max_mp:,}; " + e_s


class StatusEffectList(BaseProcessors):
    opcode = "StatusEffectList"
    struct = ServerStatusEffectList
    event = ServerStatusEffectListEvent


class StatusEffectList2(BaseProcessors):
    opcode = "StatusEffectList2"
    struct = ServerStatusEffectList2
    event = ServerStatusEffectListEvent


class BossStatusEffectList(BaseProcessors):
    opcode = "BossStatusEffectList"
    struct = ServerBossStatusEffectList
    event = ServerStatusEffectListEvent
