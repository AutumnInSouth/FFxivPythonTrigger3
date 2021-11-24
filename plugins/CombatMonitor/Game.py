from typing import TYPE_CHECKING, List, Dict, Tuple

from FFxivPythonTrigger import plugins

if TYPE_CHECKING:
    from XivMemory.struct.actor import Actor as ActorStruct


class EffectType:
    damage = 1
    heal = 2
    dot = 3
    hot = 4
    sim_dot = 5
    sim_hot = 6
    action = 11
    status = 12


class Record:
    def __init__(self, occur_time: float, effect_type: int, effect_amt: int):
        self.occur_time = occur_time
        self.effect_type = effect_type
        self.effect_amt = effect_amt


class Actor:
    _actor: 'ActorStruct|None'
    ability_record: List[Record]
    taken_ability_record: List[Record]
    total_damage_by_ability: Dict[Tuple[int, int], int]
    total_heal_by_ability: Dict[Tuple[int, int], int]

    def __init__(self, aid: int):
        self.aid = aid
        self._actor = None

        self.total_damage = 0
        self.total_damage_by_ability = {}
        self.damage_in_minute = 0
        self.total_heal = 0
        self.heal_in_minute = 0
        self.total_heal_by_ability = {}
        self.ability_record = []

        self.critical_count = 0
        self.direct_count = 0
        self.total_heal_ability = 0
        self.total_damage_ability = 0

        self.total_taken_damage = 0
        self.taken_damage_in_minute = 0
        self.total_taken_heal = 0
        self.taken_heal_in_minute = 0
        self.taken_ability_record = []

        self.critical_extra = 0
        self.base_damage = 1
        self.base_heal = 1

        self.dot_hot = {}

    @property
    def actor(self) -> 'ActorStruct|None':
        if self._actor is None or self._actor.id != self.aid:
            self._actor = plugins.XivMemory.actor_table.get_actor_by_id(self.aid)
        return self._actor


class Combat:
    def __init__(self):
        self.actors = {}

    def get_actor(self, aid: int) -> Actor | None:
        if not aid or aid == 0xE0000000: return
        if aid not in self.actors:
            self.actors[aid] = Actor(aid)
        return self.actors[aid]

    def add_dmg(self, occur_time: float, source_actor: Actor | None,
                   target_actor: Actor | None, effect_type: int,
                   effect_id: int, effect_amt: int, is_critical=False, is_direct=False):
        match effect_type:
            case EffectType.damage | EffectType.heal:
                k = EffectType.action, effect_id
            case _:
                k = EffectType.status, effect_id

        match effect_type:
            case EffectType.damage | EffectType.dot | EffectType.sim_dot:
                record = Record(occur_time, EffectType.damage, effect_amt)
                if source_actor:
                    source_actor.total_damage += effect_amt
                    source_actor.damage_in_minute += effect_amt
                    source_actor.total_damage_by_ability.setdefault(k, 0)
                    source_actor.total_damage_by_ability[k] += effect_amt
                    source_actor.ability_record.append(record)
                    if effect_type == EffectType.damage:
                        if is_critical: source_actor.critical_count += 1
                        if is_direct: source_actor.direct_count += 1
                        source_actor.total_damage_ability += 1
                if effect_type != EffectType.sim_dot:
                    target_actor.total_taken_damage += effect_amt
                    target_actor.taken_damage_in_minute += effect_amt
                    target_actor.taken_ability_record.append(record)
            case _:
                record = Record(occur_time, EffectType.heal, effect_amt)
                if source_actor:
                    source_actor.total_heal += effect_amt
                    source_actor.heal_in_minute += effect_amt
                    source_actor.total_heal_by_ability.setdefault(k, 0)
                    source_actor.total_heal_by_ability[k] += effect_amt
                    source_actor.ability_record.append(record)
                    if effect_type == EffectType.heal:
                        if is_critical: source_actor.critical_count += 1
                        source_actor.total_heal_ability += 1
                if effect_type != EffectType.sim_hot:
                    target_actor.total_taken_heal += effect_amt
                    target_actor.taken_heal_in_minute += effect_amt
                    target_actor.taken_ability_record.append(record)

    def process_outdated(self, current: float):
        base = current - 60
        for actor in list(self.actors.values()):
            while actor.ability_record and actor.ability_record[0].occur_time < base:
                ability_record = actor.ability_record.pop(0)
                if ability_record.effect_type == EffectType.damage:
                    actor.damage_in_minute = max(0, actor.damage_in_minute - ability_record.effect_amt)
                else:
                    actor.heal_in_minute = max(0, actor.heal_in_minute - ability_record.effect_amt)
            while actor.taken_ability_record and actor.taken_ability_record[0].occur_time < base:
                ability_record = actor.taken_ability_record.pop(0)
                if ability_record.effect_type == EffectType.damage:
                    actor.taken_damage_in_minute = max(0, actor.taken_damage_in_minute - ability_record.effect_amt)
                else:
                    actor.taken_heal_in_minute = max(0, actor.taken_heal_in_minute - ability_record.effect_amt)



    def add_status(self):
        pass