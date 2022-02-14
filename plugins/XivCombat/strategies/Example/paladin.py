from XivCombat.strategies import *
from XivCombat import define, api, utils
from XivCombat.multi_enemy_selector import NearCircle, select

"""
28,钢铁信念,10
9,先锋剑,1
15,暴乱剑,4
3538,沥血剑,54
21,战女神之怒,26（3539,王权剑,60）
16460,赎罪剑,76
7381,全蚀斩,6
16457,日珥斩,40
23,厄运流转,50
29,深奥之灵,30
7383,安魂祈祷,68
7384,圣灵,64
16458,圣环,72
16459,悔罪,80
24,投盾,15
16461,调停,74
16,盾牌猛击,10
7382,干预,62
3542,盾阵,35
17,预警,38
3540,圣光幕帘,56
7385,武装戍卫,70
30,神圣领域,50
3541,深仁厚泽,58
27,保护,45
20,战逃反应,2
"""
"""
1902,忠义之剑,可以发动赎罪剑
725,沥血剑,体力逐渐减少,
1368,安魂祈祷
76,"战逃反应"
"""

aoe = NearCircle(5)


class PaladinLogic(Strategy):
    name = "paladin_logic"
    job = "Paladin"

    def global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        if data.target_distance <= 4 and data.target_action_check(9, data.target):
            single_target = data.target
        else:
            single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(9))
            if not single_target: return
        _, cnt = utils.cnt_enemy(data, aoe)
        if data.me.level >= 40 and data.combo_id == 7381: return UseAbility(16457)

        if cnt > 1 and data.me.level >= 6:
            if 1368 in data.effects and data.me.level >= 72 and (not data.is_moving or data.me.level >= 78):
                if (data.effects[1368].timer > 3 and data.me.current_mp >= 4000) or data.me.level < 80:
                    return UseAbility(16458)
                else:
                    return UseAbility(16459)
            else:
                return UseAbility(7381)
        if 1902 in data.effects and (utils.res_lv(data) or data.effects[1902].timer < 2.5 * data.effects[1902].param):
            return UseAbility(16460, single_target.id)
        if data.combo_id == 9 and data.me.level >= 4:
            return UseAbility(15, single_target.id)
        if data.combo_id == 15 and data.me.level >= 26:
            if data.me.level >= 54:
                t_effect = single_target.effects.get_dict(source=data.me.id)
                if (725 not in t_effect or t_effect[725].timer < 5) and data.time_to_kill_target >= 10:
                    return UseAbility(3538, single_target.id)
            if 1902 in data.effects:
                return UseAbility(16460, single_target.id)
            return UseAbility(21, single_target.id)
        if 1368 in data.effects and (not data.is_moving or data.me.level >= 78):
            if (data.effects[1368].timer > 3 and data.me.current_mp >= 4000) or data.me.level < 80:
                return UseAbility(7384, single_target.id)
            else:
                return UseAbility(16459, single_target.id)
        else:
            return UseAbility(9)

    def non_global_cool_down_ability(self, data: 'LogicData') -> AnyUse:
        if utils.res_lv(data):
            if data.target_distance <= 4 and data.target_action_check(9, data.target):
                single_target = data.target
            else:
                single_target = data.get_target(define.DISTANCE_NEAREST, data.enemy_can_attack_by(9))
                if not single_target: return
            if not data[20] and 1368 not in data.effects: return UseAbility(20)
            if not data[7383] and \
                    76 not in data.effects and \
                    data.me.current_mp / data.me.max_mp > 0.8 and \
                    data.combo_id not in {7381, 9, 15} and \
                    1902 not in data.effects:
                return UseAbility(7383, single_target.id)
            if not data[29]: return UseAbility(29, single_target.id)
            if not data[23]: return UseAbility(23, single_target.id)
