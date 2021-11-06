from ..combos import ComboBase
from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.saint_coinach import realm

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
725,沥血剑,体力逐渐减少,
"""

action_sheet = realm.game_data.get_sheet('Action')

low_blow_group = action_sheet[7540]['CooldownGroup']


class Single(ComboBase):
    action_id = 3538
    combo_id = "pld/single"
    title = "单体自动"

    @staticmethod
    def combo(me):
        lv = me.level
        combo_id = plugins.XivMemory.combo_state.action_id
        # combat loop: 9, 15, 21/3538
        if combo_id == 9 and lv >= 4:
            return 15
        if combo_id == 15 and lv >= 26:
            target = plugins.XivMemory.targets.current
            # extend dot
            if lv >= 54 and target is not None:
                t_effect = target.effects.get_dict(source=me.id)
                if 725 not in t_effect or t_effect[725].timer < 5:
                    return 3538
            return 21
        return 9


class SingleNormal(ComboBase):
    action_id = 3539
    combo_id = "pld/single_normal"
    title = "单体普通"

    @staticmethod
    def combo(me):
        lv = me.level
        combo_id = plugins.XivMemory.combo_state.action_id
        # normal combat loop: 9, 15, 21
        if combo_id == 9 and lv >= 4:
            return 15
        if combo_id == 15 and lv >= 26:
            return 21
        return 9


class SingleDot(ComboBase):
    action_id = 3538
    combo_id = "pld/single_dot"
    title = "单体dot"

    @staticmethod
    def combo(me):
        lv = me.level
        combo_id = plugins.XivMemory.combo_state.action_id
        # dot combat loop: 9, 15, 3538
        if combo_id == 9 and lv >= 4:
            return 15
        if combo_id == 15 and lv >= 26:
            return 3538
        return 9


class Stun(ComboBase):
    action_id = 16
    combo_id = "pld/stun"
    title = "眩晕"

    @staticmethod
    def combo(me):
        return 16 if plugins.XivMemory.cool_down_group[low_blow_group].remain else 7540


class Multi(ComboBase):
    action_id = 16457
    combo_id = "pld/multi"
    title = "群体连"

    @staticmethod
    def combo(me):
        return 16457 if me.level >= 40 and plugins.XivMemory.combo_state.action_id == 7381 else 7381


combos = [Single, SingleNormal, SingleDot, Stun, Multi]
