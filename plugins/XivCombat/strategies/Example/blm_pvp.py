from time import time
from FFxivPythonTrigger.decorator import event
from XivCombat.strategies import *
from XivCombat import define, api
from XivCombat.multi_enemy_selector import FarCircle

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent
    from XivNetwork.extra_messages.actor_add_remove_effect import ActorRemoveEffectEvent


class ThunderRecord:
    def __init__(self, max_damage: float, dot_damage: float, initial_damage: float):
        self.last_time = time()
        self.taken_damage = initial_damage
        self.max_damage = max_damage
        self.dot_damage = dot_damage

    def remain(self):
        dot_time = time() - self.last_time
        if dot_time > 15: return 1e+99
        dot_damage = dot_time // 3 * self.dot_damage
        return self.max_damage - self.taken_damage - dot_damage


def thunder_remain(target_id):
    try:
        return thunder_records[target_id].remain()
    except KeyError:
        return 1e+99


thunder_actions = {8861: (400, 8000, 400), 8860: (2400, 8000, 400), 18935: (200, 4000, 200), 18936: (1200, 4000, 200)}
thunder_records = {}


@event('network/zone/server/action_effect')
def blm_pvp_record_thunder(evt: 'ActionEffectEvent'):
    if evt.action_type != 'action' or evt.source_id != api.get_me_actor().id: return
    if evt.action_id in thunder_actions:
        base_dmg, max_dmg, dot_dmg = thunder_actions[evt.action_id]
    else:
        base_dmg, max_dmg, dot_dmg = 0, 0, 0
    for target_id, effects in evt.targets.items():
        new_buff = 0
        dmg = 0
        for effect in effects:
            if 'buff' in effect.tags and (effect.param == 2075 or effect.param == 1324):
                new_buff = effect.param
            elif 'ability' in effects:
                dmg += effect.param
        if new_buff:
            adjust = dmg / base_dmg
            thunder_records[target_id] = ThunderRecord(max_dmg, int(dot_dmg * adjust), dmg)


@event('network/zone/server/effect_remove')
def blm_pvp_effect_remove(evt: 'ActorRemoveEffectEvent'):
    if evt.effect_id != 2075 and evt.effect_id != 1324 or evt.source_id != api.get_me_actor().id:
        return
    try:
        del thunder_records[evt.actor_id]
    except KeyError:
        pass
