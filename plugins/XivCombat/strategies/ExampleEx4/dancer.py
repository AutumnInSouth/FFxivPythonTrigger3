from math import radians
from time import perf_counter

from XivCombat.utils import a, s, cnt_enemy, res_lv
from XivCombat.strategies import *
from XivCombat import define
from XivCombat.multi_enemy_selector import Rectangle, FarCircle, NearCircle, Sector

aoe = NearCircle(5)
star_fall = Rectangle(25, 2)
fan_3 = FarCircle(25, 5)
fan_4 = Sector(25, radians(90))
dance = NearCircle(15)

dnc_step_skill_mapping = [
    a('蔷薇曲脚步'),
    a('蔷薇曲脚步'),
    a('小鸟交叠跳'),
    a('绿叶小踢腿'),
    a('金冠趾尖转'),
]

dance_status = {s('技巧舞步'), s('标准舞步')}
prepare_status = {s('Flourishing Flow'), s('Flourishing Symmetry'), s('扇舞·急预备')}


def use_feather(data: 'LogicData'):
    if data.target_distance <= 25 and data.target_action_check(a('瀑泻'), data.target):
        single_target = data.target
    else:
        single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('瀑泻')))
        if not single_target: return

    if data.me.level >= 50:
        aoe_target, aoe_count = cnt_enemy(data, aoe)
    else:
        aoe_target, aoe_count = single_target, 0

    if aoe_count >= 2:
        u = UseAbility(a('扇舞·破'), data.me.id)
    else:
        u = UseAbility(a('扇舞·序'), single_target.id)

    old_cnt = data.gauge.feathers
    u.wait_until = lambda: data.refresh_cache('gauge').feathers < old_cnt
    return u


class DncLogic(Strategy):
    name = "ny/dnc_logic"
    job = "Dancer"

    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        max_step = 4 if s('技巧舞步') in data.effects else 2 if s('标准舞步') in data.effects else 0
        if max_step:
            if data.gauge.current_step < max_step:
                return UseAbility(dnc_step_skill_mapping[data.gauge.step[data.gauge.current_step].raw_value], data.me.id)
            else:
                if cnt_enemy(data, dance)[1] > len(data.valid_enemies) // 2:
                    return UseAbility(a('技巧舞步') if max_step == 4 else a('标准舞步'), data.me.id)
                else:
                    return

        if data.target_distance <= 25 and data.target_action_check(a('瀑泻'), data.target):
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(a('瀑泻')))
            if not single_target: return

        if data.me.level >= 15:
            aoe_target, aoe_count = cnt_enemy(data, aoe)
        else:
            aoe_target, aoe_count = single_target, 0
        res = res_lv(data)
        if res:
            if not data[a('标准舞步')] and (data.effect_time(s('标准舞步结束')) < 8 or data[a('技巧舞步')] > 12):
                return UseAbility(a('标准舞步'), data.me.id)

            if not data[a('技巧舞步')]:
                return UseAbility(a('技巧舞步'), data.me.id)

            if data.gauge.esprit >= (50 if data.effect_time(s('技巧舞步结束')) else 85):
                fan_3_target, fan_3_count = cnt_enemy(data, fan_3, single_target)
                if fan_3_count: return UseAbility(a('剑舞'), fan_3_target.id)

        if s('Flourishing Starfall') in data.effects:
            star_fall_target, star_fall_count = cnt_enemy(data, star_fall)
            if star_fall_count: return UseAbility(a('Starfall Dance'), star_fall_target.id)

        if s('Flourishing Finish') in data.effects and cnt_enemy(data, dance)[1] > len(data.valid_enemies) // 2:
            return UseAbility(a('Tillana'), data.me.id)

        if s('Flourishing Flow') in data.effects:
            if aoe_count >= 2 and data.me.level >= 45:
                return UseAbility(a('落血雨'), data.me.id)
            elif aoe_count < 4:
                return UseAbility(a('坠喷泉'), single_target.id)

        if s('Flourishing Symmetry') in data.effects:
            if aoe_count >= 2 and data.me.level >= 35:
                return UseAbility(a('升风车'), data.me.id)
            elif aoe_count < 4:
                return UseAbility(a('逆瀑泻'), single_target.id)

        if data.combo_id == a('瀑泻') and data.me.level >= 2:
            return UseAbility(a('喷泉'), single_target.id)
        elif data.combo_id == a('风车') and data.me.level >= 25:
            return UseAbility(a('落刃雨'), data.me.id)
        elif aoe_count >= 2 and data.me.level >= 15:
            return UseAbility(a('风车'), data.me.id)
        else:
            return UseAbility(a('瀑泻'), single_target.id)

    def non_global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        r = res_lv(data)
        if not r or dance_status.intersection(data.effects_set): return
        res = r > 1 or data.effect_time(s('技巧舞步结束')) or not data.skill_unlocked(a('技巧舞步'))
        if res and not data[a('进攻之探戈')]: return UseAbility(a('进攻之探戈'), data.me.id)

        if s('扇舞·急预备') in data.effects:
            fan_3_target, fan_3_count = cnt_enemy(data, fan_3)
            if fan_3_count: return UseAbility(a('扇舞·急'), fan_3_target.id)

        if data.gauge.feathers > 3: return use_feather(data)

        if (res or data[a('技巧舞步')] > 40) and not data[a('百花争艳')] and not prepare_status.intersection(data.effects_set):
            return UseAbility(a('百花争艳'), data.me.id)

        if s('Fourfold Fan Dance') in data.effects:
            fan_4_target, fan_4_count = cnt_enemy(data, fan_4)
            if fan_4_count: return UseAbility(a('Fan Dance IV'), fan_4_target.id)

        if res and data.gauge.feathers: return use_feather(data)
