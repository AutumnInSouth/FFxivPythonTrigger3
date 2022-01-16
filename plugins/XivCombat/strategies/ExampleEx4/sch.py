from functools import cache
from math import radians

from XivCombat.utils import a, s, cnt_enemy, res_lv
from XivCombat.strategies import *
from XivCombat import define
from XivCombat.multi_enemy_selector import NearCircle

sch_dot = {1895, 189, 179}


def select_res_target_key(actor):
    return actor.job.is_healer, actor.job.is_tank, actor.job.is_dps


def search_swift_res(data: 'LogicData'):
    if data.me.level < 12: return
    k = data.config['swift_res']
    if k == 'party':
        d = data.valid_party
    elif k == 'alliance':
        d = data.valid_alliance
    elif k == 'all':
        d = data.valid_players
    else:
        d = list()
    d = [member for member in d if not member.current_hp and 148 not in member.effects.get_dict() and data.actor_distance_effective(member) < 30]
    if d: return max(d, key=select_res_target_key)


def target_has_dots(data, actor, dots):
    effects = actor.effects.get_dict(source=data.me.id)
    for dot in dots:
        if dot in effects:
            return effects[dot].timer
    return 0


class SchLogic(Strategy):
    name = "ny/sch_logic"
    job = 'Scholar'
    default_data = {
        'swift_res': 'none',
    }

    def global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        if not data[a('即刻咏唱')] or s('即刻咏唱') in data.effects and data.me.current_mp >= 2400:
            res_target = search_swift_res(data)
            if res_target:
                if s('即刻咏唱') in data.effects:
                    return UseAbility(a('复生'), res_target.id)
                else:
                    return UseAbility(
                        a('即刻咏唱'),
                        ability_type=define.AbilityType.oGCD,
                        wait_until=lambda: s('即刻咏唱') in data.refresh_cache('effects')
                    )

        if not data.pet_id: return UseAbility(a('夕月召唤'))

        if data.target and data.target_distance <= 25:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('毁灭（学者）')))
            if not single_target or data.actor_distance_effective(single_target) > 25: return
        for enemy in data.valid_enemies:
            if data.ttk(enemy) > 10 and target_has_dots(data, enemy, sch_dot) < 3:
                return UseAbility(a('毒菌'), single_target.id)
        if data.is_moving:
            return UseAbility(17870, single_target.id)
        else:
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
