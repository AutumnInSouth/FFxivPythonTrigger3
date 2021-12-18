from typing import TYPE_CHECKING, List, Dict

from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.logger import info

from .logic_data import invincible_actor, is_actor_status_can_damage

if TYPE_CHECKING:
    from XivMemory.struct.actor import Actor as ActorStruct
    from XivNetwork.message_processors.zone_server.actor_control import HotEvent, DotEvent, DeathEvent
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent

split_time = 60


class Actor:
    _actor: 'ActorStruct | None'
    effects: List['Effect']

    def __init__(self, aid: int, actor: 'ActorStruct|None' = None):
        self.aid = aid
        self._actor = actor
        self.effects = []
        self.last_combo = 0
        self.damage = 0
        self.damage_in_min = 0
        self.heal = 0
        self.heal_in_min = 0
        self.taken_damage = 0
        self.taken_damage_in_min = 0
        self.death_cnt = 0
        self._owner_id = None

    @property
    def owner_id(self) -> int | None:
        if self._owner_id is None:
            self._owner_id = getattr(self.actor, 'owner_id', None)
        return self._owner_id

    @property
    def actor(self) -> 'ActorStruct|None':
        if self._actor is None or self._actor.id != self.aid:
            self._actor = plugins.XivMemory.actor_table.get_actor_by_id(self.aid)
        return self._actor

    def __str__(self):
        return f'{self.actor.name}({self.aid:x})'


class Effect:
    def __init__(
            self,
            occur_time: float,
            source_actor: 'Actor | None',
            target_actor: 'Actor | None',
            data_id: int,
            is_cure: bool,
            is_status: bool,
            amount: int,
            prev_combo: int = 0,
            is_critical: bool = False,
            is_direct: bool = False,
    ):
        # info('',target_actor,amount)
        self.occur_time = occur_time
        self.source_actor = source_actor
        self.target_actor = target_actor
        self.data_id = data_id
        self.is_cure = is_cure
        self.is_status = is_status
        self.amount = amount
        self.prev_combo = prev_combo
        self.is_critical = is_critical
        self.is_direct = is_direct
        self.amt_remove = True
        if source_actor:
            if is_cure:
                source_actor.heal += amount
                source_actor.heal_in_min += amount
            else:
                source_actor.damage += amount
                source_actor.damage_in_min += amount
            source_actor.effects.append(self)
        if target_actor:
            if not is_cure:
                target_actor.taken_damage += amount
                target_actor.taken_damage_in_min += amount
            target_actor.effects.append(self)

    def out_date(self):
        if self.amt_remove:
            self.amt_remove = False
            if self.source_actor:
                if self.is_cure:
                    self.source_actor.heal_in_min -= self.amount
                else:
                    self.source_actor.damage_in_min -= self.amount
            if self.target_actor and not self.is_cure:
                self.target_actor.taken_damage_in_min -= self.amount


class Monitor:
    actors: Dict[int, Actor]
    effects: List['Effect']

    def __init__(self, zone_id: int):
        self.zone_id = zone_id
        self.actors = {}
        self.effects = []
        self.out_date_idx = 0
        self._freeze = False
        self.last_record = 0
        self.first_record = 0

    def update_record_time(self, time: float):
        self.last_record = max(time, self.last_record)
        if self.first_record == 0: self.first_record = time - 1

    def get_belongs_to(self, actor: Actor) -> Actor:
        if not actor: return actor
        owner_id = actor.owner_id
        return actor if not owner_id or owner_id == 0xe0000000 else self.get_actor(owner_id)

    def on_action(self, occur_time: float, action_event: 'ActionEffectEvent'):
        if action_event.action_type != 'action': return True
        time_update = True
        source_actor = self.get_belongs_to(self.get_actor(action_event.source_id))
        prev_combo = getattr(source_actor, 'last_combo', 0)
        for target_id, effects in action_event.targets.items():
            target_actor = self.get_actor(target_id)
            # info('',source_actor,target_actor,','.join(map(str,effects)))
            is_invincible = False
            for effect in effects:
                if ('invincible' in effect.tags or 'ability' in effect.tags and effect.param == 0) and 'to_source' not in effect.tags:
                    is_invincible = True
                if 'ability' in effect.tags or 'healing' in effect.tags:
                    if time_update:
                        self.update_record_time(occur_time)
                        time_update = False
                    is_heal = 'healing' in effect.tags
                    to_source = 'to_source' in effect.tags
                    self.effects.append(Effect(
                        occur_time=occur_time,
                        source_actor=target_actor if to_source and not is_heal else None if 'limit_break' in effect.tags else source_actor,
                        target_actor=source_actor if to_source else target_actor,
                        data_id=action_event.action_id,
                        is_cure=is_heal,
                        is_status=False,
                        prev_combo=prev_combo,
                        amount=effect.param,
                        is_critical='critical' in effect.tags,
                        is_direct='direct' in effect.tags,
                    ))
                elif 'combo' in effect.tags:
                    if source_actor:
                        source_actor.last_combo = effect.param
            if target_actor.actor and target_id > 0x40000000 and is_actor_status_can_damage(
                    target_actor.actor) == is_invincible and action_event.source_id == plugins.XivMemory.player_info.id:
                try:
                    getattr(invincible_actor, 'add' if is_invincible else 'remove')(target_id)
                except KeyError:
                    pass
        self.process_outdated_effects()
        return True

    def on_dot(self, occur_time: float, dot_event: 'DotEvent'):
        self.update_record_time(occur_time)
        source_actor = self.get_belongs_to(self.get_actor(dot_event.source_id)) if dot_event.status_id else None
        target_actor = self.get_actor(dot_event.target_id)
        record_effect = Effect(
            occur_time=occur_time,
            source_actor=source_actor,
            target_actor=target_actor,
            data_id=dot_event.status_id,
            is_cure=False,
            is_status=True,
            amount=dot_event.damage,
        )
        if source_actor:
            source_actor.effects.append(record_effect)
            source_actor.damage += dot_event.damage
        if target_actor:
            target_actor.effects.append(record_effect)
            target_actor.taken_damage += dot_event.damage
        self.process_outdated_effects()
        return True

    def on_hot(self, occur_time: float, hot_event: 'HotEvent'):
        self.update_record_time(occur_time)
        source_actor = self.get_belongs_to(self.get_actor(hot_event.source_id)) if hot_event.status_id else None
        target_actor = self.get_actor(hot_event.target_id)
        record_effect = Effect(
            occur_time=occur_time,
            source_actor=source_actor,
            target_actor=target_actor,
            data_id=hot_event.status_id,
            is_cure=True,
            is_status=True,
            amount=hot_event.damage,
        )
        if source_actor:
            source_actor.effects.append(record_effect)
            source_actor.heal += hot_event.damage
        if target_actor:
            target_actor.effects.append(record_effect)
        self.process_outdated_effects()
        return True

    def on_death(self, occur_time: float, death_event: 'DeathEvent'):
        target_actor = self.get_actor(death_event.target_id)
        target_actor.death_cnt += 1

    def get_actor(self, aid: int) -> Actor | None:
        if not aid or aid == 0xE0000000:
            return
        if aid not in self.actors:
            self.actors[aid] = Actor(aid)
        return self.actors[aid]

    def process_outdated_effects(self):
        while self.out_date_idx < len(self.effects) and self.effects[self.out_date_idx].occur_time < self.last_record - 60:
            self.effects[self.out_date_idx].out_date()
            self.out_date_idx += 1

    def freeze(self):
        pass

    def dps(self, actor_id: int):
        return self.get_actor(actor_id).damage / (self.last_record - self.first_record) if self.first_record else 0

    def dpsm(self, actor_id: int):
        return self.get_actor(actor_id).damage_in_min / min(self.last_record - self.first_record, 60) if self.first_record else 0

    def hps(self, actor_id: int):
        return self.get_actor(actor_id).heal / (self.last_record - self.first_record) if self.first_record else 0

    def hpsm(self, actor_id: int):
        return self.get_actor(actor_id).heal_in_min / min(self.last_record - self.first_record, 60) if self.first_record else 0

    def dtps(self, actor_id: int):
        return self.get_actor(actor_id).taken_damage / (self.last_record - self.first_record) if self.first_record else 0

    def dtpsm(self, actor_id: int):
        a = self.get_actor(actor_id)
        if a.effects:
            first = a.effects[0].occur_time - 0.1
        else:
            first = self.first_record
        return a.taken_damage_in_min / min(self.last_record - first, 60) if first else 0
