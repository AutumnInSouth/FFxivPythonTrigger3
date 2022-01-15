from functools import cache
from math import radians

from XivCombat.utils import a, s, cnt_enemy, res_lv
from XivCombat.strategies import *
from XivCombat import define
from XivCombat.multi_enemy_selector import NearCircle

sch_dot = {1895, 189, 179}


def target_has_dots(data, actor, dots):
    effects = actor.effects.get_dict(source=data.me.id)
    for dot in dots:
        if dot in effects:
            return effects[dot].timer
    return 0


class SchLogic(Strategy):
    name = "ny/sch_logic"
    job = 'Scholar'

    def global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        if not data.pet_id: return UseAbility(a('夕月召唤'))

        if data.target and data.target_distance <= 25:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('毁灭（学者）')))
            if not single_target or data.actor_distance_effective(single_target) > 25: return
        for enemy in data.valid_enemies:
            if target_has_dots(data, enemy, sch_dot) < 3:
                return UseAbility(a('毒菌'), single_target.id)
        return UseAbility(a('毁灭（学者）'), single_target.id)

    def non_global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        res = res_lv(data)
        if res and not data[a('以太超流')] and data.me.is_in_combat and not data.gauge.aether_flow_stacks:
            return UseAbility(a('以太超流'))
        if data.me.current_mp < 8000:
            return UseAbility(a('醒梦'), data.me.id)
        if data.target and data.target_distance <= 25:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('毁灭（学者）')))
            if not single_target or data.actor_distance_effective(single_target) > 25: return
        if res and not data[a('连环计')]:
            return UseAbility(a('连环计'), single_target.id)
