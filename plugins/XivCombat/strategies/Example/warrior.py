from math import radians
from time import perf_counter

from XivCombat.strategies import *
from XivCombat import define
from XivCombat.multi_enemy_selector import NearCircle, Sector, select

"""
7388,摆脱,68
7386,猛攻,62
3552,泰然自若,58
48,守护,10
43,死斗,42
40,战栗,30
44,复仇,38

16464,原初的勇猛,76
3551,原初的直觉,56
7389,原初的解放,70
38,狂暴,6
52,战嚎,50

7387,动乱,64
46,飞斧,15

16465,狂魂,80
3549,裂石飞环,54
49,原初之魂,35

16463,混沌旋风,72
3550,地毁人亡,60
51,钢铁旋风,45

16462,秘银暴风,40
41,超压斧,10

42,暴风斩,26
45,暴风碎,50
37,凶残裂,4
31,重劈,1
"""

"""
86,狂暴,自身攻击必定暴击并且直击
90,暴风碎,攻击所造成的伤害提高
1897,原初的混沌,"地毁人亡变为混沌旋风 习得狂魂后追加效果：裂石飞环变为狂魂"
1177,原初的解放,兽魂不会消耗，自身攻击必定暴击并且直击，不受眩晕、睡眠、止步、加重和除特定攻击之外其他所有击退、吸引的效果影响
2227,原初的勇猛,自身的物理攻击命中时会吸收体力
"""


def res_lv(data: 'LogicData') -> int:
    match data.config['resource']:
        case define.RESOURCE_SQUAND:
            return 2
        case define.RESOURCE_NORMAL:
            return 1
        case define.RESOURCE_STINGY:
            return 0
        case _:
            return 1


def count_enemy(data: 'LogicData', ability):
    target, cnt = select(data, data.valid_enemies, ability)
    if not cnt: return data.target,0
    if data.config['single'] == define.FORCE_SINGLE: return data.target, 1
    if data.config['single'] == define.FORCE_MULTI: return target, 3
    return target, cnt


a1 = NearCircle(5)
a2 = Sector(8, radians(90))


class WarriorLogic(Strategy):
    name = "warrior_logic"
    job = "Warrior"

    def __init__(self):
        self.last_buff = 0

    def process_ability_use(self, data: 'LogicData', action_id: int, target_id: int) -> Tuple[int, int]|None:
        if action_id in {16464, 7540, 7538}:
            mo_target = api.get_mo_target()
            if mo_target: return action_id, mo_target.id

    def global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        need_red = data.me.level >= 50 and (90 not in data.effects or data.effects[90].timer < 10)
        use_green = data.combo_id == 37 and (data.me.level < 50 or 90 in data.effects and data.effects[90].timer > 30)
        s = 7389 if data.me.level >= 70 else 38
        target, cnt = count_enemy(data, a1)
        if 1177 in data.effects or not need_red and res_lv(data) and data.gauge.beast >= 50 and (
                {86, 1177, 2227, 1897}.intersection(data.me.effects.get_set()) or
                data.gauge.beast > (80 if use_green else 90) or data[52] < (60 if data[s] < 10 else 10)
        ):
            if data.me.level < 45:
                return UseAbility(49)
            return UseAbility(51 if cnt > 2 else 49)
        if data.combo_id == 41 and data.me.level >= 40:
            return UseAbility(16462) if cnt else None
        if data.combo_id == 37 and data.me.level >= 26:
            return UseAbility(42 if use_green else 45)
        if not need_red and data.me.level >= 10:
            target, cnt = count_enemy(data, a2)
            if cnt >= 2: return UseAbility(41, target.id)
        if data.combo_id == 31 and data.me.level >= 4:
            return UseAbility(37)
        return UseAbility(31)

    def non_global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        if res_lv(data) and (data.me.level < 50 or 90 in data.effects):
            s = 7389 if data.me.level >= 70 else 38
            if not data[s] and data[52] > 60 and 1897 not in data.effects:
                if data.ability_cnt or data.gcd < 1.5:
                    if data.gcd < 1.5:
                        return UseAbility(s)
                    else:
                        return
            if not data[7387] and data.gauge.beast >= 20 and data[s] > 10:
                return UseAbility(7387)
            if (data[52] < 60 and self.last_buff < perf_counter() - 1 and
                    not {86, 1177, 1897}.intersection(data.me.effects.get_set()) and
                    data.gauge.beast <= 50 and (data[52] < 5 or data[s] < 10)):
                self.last_buff = perf_counter()
                return UseAbility(52)
