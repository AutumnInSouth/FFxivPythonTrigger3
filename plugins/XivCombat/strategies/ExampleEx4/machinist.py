import math
from functools import cache

from XivCombat.utils import a, s, cnt_enemy, res_lv
from XivCombat.strategies import *
from XivCombat import define
from XivCombat.multi_enemy_selector import Sector, FarCircle

spread_shot = Sector(12, math.radians(120))
ricochet = FarCircle(25, 5)


@cache
def mch_special_gcd(lv: int, cd_only: bool = True):
    ans = []
    if lv >= 58:
        ans.append(a('钻头'))
        if lv >= 76:
            ans.append(a('空气锚'))
            if lv >= 90:
                ans.append(a('Chain Saw'))
        elif cd_only:
            ans.append(a('热弹'))
    elif lv >= 26 and not cd_only:
        ans.append(a('狙击弹'))
    else:
        ans.append(a('热弹'))
    return ans


def special_gcd(data: 'LogicData', action_id: int, target_id: int):
    if action_id in mch_special_gcd(data.me.level, False) and data[a('整备')] <= 55:
        return UseAbility(
            a('整备'), data.me.id,
            ability_type=define.AbilityType.oGCD,
            wait_until=lambda: s('整备') in data.refresh_cache('effects')
        )
    return UseAbility(action_id, target_id)


class MachinistLogic(Strategy):
    name = 'ny/mch_logic'
    job = 'Machinist'

    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        if data.target_distance <= 25:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('分裂弹')))
            if data.actor_distance_effective(single_target) > 25: return

        if data.me.level >= 18:
            aoe_target, aoe_cnt = cnt_enemy(data, spread_shot)
        else:
            aoe_target, aoe_cnt = single_target, 0

        if res_lv(data):
            if data.gcd >= data[a('钻头')]:
                return special_gcd(data, a('钻头') if aoe_cnt < 3 or data.me.level < 72 else a('毒菌冲击'), single_target.id)
            hot_shot = a('热弹') if data.me.level < 76 else a('空气锚')
            if data.gcd >= data[hot_shot]:
                return special_gcd(data, hot_shot, single_target.id)
            if data.gcd >= data[a('Chain Saw')]:
                return special_gcd(data, a('Chain Saw'), single_target.id)
        if aoe_cnt < 3 or data.me.level < 18:
            if data.gauge.overheat_ms and data.skill_unlocked(a('热冲击')):
                return UseAbility(a('热冲击'), single_target.id)
            if data.combo_id == a('分裂弹') and data.me.level >= 2:
                return UseAbility(a('独头弹'), single_target.id)
            if data.combo_id == a('独头弹') and data.me.level >= 26:
                return special_gcd(data, a('狙击弹'), single_target.id)
            return UseAbility(a('分裂弹'), single_target.id)
        else:
            if data.gauge.overheat_ms and data.skill_unlocked(a('自动弩')):
                return data.use_ability_to_target(a('自动弩'), aoe_target.id)
            else:
                return data.use_ability_to_target(a('散射'), aoe_target.id)

    def non_global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        if data.target_distance <= 25:
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('分裂弹')))
            if data.actor_distance_effective(single_target) > 25: return

        ricochet_cd = data[a('弹射')]
        gauss_round_cd = data[a('虹吸弹')]
        if data.me.level < 74:
            ricochet_cd -= 30
            gauss_round_cd -= 30

        if min(ricochet_cd, gauss_round_cd) < 15:
            if gauss_round_cd <= ricochet_cd:
                return UseAbility(a('虹吸弹'), single_target.id)
            else:
                return UseAbility(a('弹射'), cnt_enemy(data, ricochet)[0].id)

        if data.gauge.battery >= 90:
            return UseAbility(a('车式浮空炮塔'), single_target.id)

        if data.gauge.heat >= 50 and not data[a('超荷')] and (
                not data.skill_unlocked(a('热冲击')) or
                max(data[action] for action in mch_special_gcd(data.me.level, True)) > 8
        ):
            wild_fire_cd = data[a('野火')]
            if not wild_fire_cd and not data.ability_cnt:
                return UseAbility(a('野火'), single_target.id)
            if wild_fire_cd > 8:
                if data.ability_cnt and data.gcd > 1.3:
                    return
                elif data.gcd <= 1.3:
                    return UseAbility(a('超荷'), data.me.id)
        if data.gauge.heat < 50 and not data[a('枪管加热')]:
            return UseAbility(a('枪管加热'), data.me.id)
        if min(ricochet_cd, gauss_round_cd) <= 60:
            if gauss_round_cd <= ricochet_cd:
                return UseAbility(a('虹吸弹'), single_target.id)
            else:
                return UseAbility(a('弹射'), cnt_enemy(data, ricochet)[0].id)
        if data.gauge.battery >= 50:
            return UseAbility(a('车式浮空炮塔'), single_target.id)
