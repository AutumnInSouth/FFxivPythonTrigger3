from ctypes import *
from typing import TYPE_CHECKING

from FFxivPythonTrigger import plugins, game_ext
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors

if TYPE_CHECKING:
    from XivMemory.struct.actor import Actor


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


class EffectResultEntry(OffsetStruct({
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


structs = {}

if game_ext == 3:
    ServerEffectResult = EffectResultEntry
else:
    class ServerEffectResult(OffsetStruct({
        'result_count': c_ubyte,
        'unk0': c_ubyte,
        'unk1': c_ushort,
        'results': EffectResultEntry * 1,
    })):
        pass


class _EffectResult:
    target_actor: 'Actor|None'
    def __init__(self, result: EffectResultEntry):
        self.raw = result
        self.target_id = result.actor_id
        self.effects = result.effects[:min(result.effect_count, 4)]
        self.target_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.target_id)
        if self.target_actor is not None:
            self.target_name = self.target_actor.name
            t_effect = self.target_actor.effects.get_set()
            self.effects_new = [e.effect_id not in t_effect for e in self.effects]
        else:
            self.target_name = hex(self.target_id)
            self.effects_new = [False] * 4

    def __str__(self):
        e_s = ','.join([f'{e.effect_id}({e.source_actor_id}:x):{e.duration:.1f}' for e in self.effects if e.effect_id])
        return (
            f"{self.target_name}({self.raw.current_hp}(+{self.raw.damage_shield}%)/{self.raw.max_hp},"
            f"{self.raw.current_mp}/10000) add status effects [{e_s}]")


class ServerEffectResultsEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'effect_result'
    struct_message: ServerEffectResult
    actor: 'Actor|None'

    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerEffectResult):
        self.actor_id = message_header.actor_id
        self.actor_name = hex(self.actor_id)
        self.actor: 'Actor|None' = None
        if game_ext == 3:
            self.result_count = 1
            self.results = [struct_message]
            super().__init__(bundle_header, message_header, raw_message, struct_message)
        else:
            self.result_count = struct_message.result_count
            if self.result_count != 1:
                if self.result_count not in structs:
                    structs[self.result_count] = type(f'ServerEffectResult{self.result_count}', (OffsetStruct({
                        'result_count': c_ubyte, 'unk0': c_ubyte, 'unk1': c_ushort,
                        'results': EffectResultEntry * self.result_count,
                    }),), {})
                struct_message = structs[self.result_count].from_buffer(raw_message)
            self.results = struct_message.results
            super().__init__(bundle_header, message_header, raw_message, struct_message)

        self.results = [_EffectResult(r) for r in self.results]

    def init(self):
        self.actor = plugins.XivMemory.actor_table.get_actor_by_id(self.actor_id)
        if self.actor is not None:
            self.actor_name = self.actor.name

    def _text(self):
        return f'effect results on {self.actor_name} :' + ';'.join(str(r) for r in self.results)


class ServerEffectResultEvents(NetworkZoneServerEvent):
    def __init__(self, bundle_header, message_header, raw_message, struct_message: ServerEffectResult):
        super().__init__(bundle_header, message_header, raw_message, struct_message)


class EffectResult(BaseProcessors):
    opcode = "EffectResult"
    struct = ServerEffectResult
    event = ServerEffectResultsEvent


class EffectResult2(BaseProcessors):
    opcode = "EffectResult2"
    struct = ServerEffectResult
    event = ServerEffectResultsEvent


class EffectResult3(BaseProcessors):
    opcode = "EffectResult3"
    struct = ServerEffectResult
    event = ServerEffectResultsEvent
