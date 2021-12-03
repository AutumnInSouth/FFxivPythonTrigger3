from ..combos import ComboBase
from FFxivPythonTrigger import plugins

"""
7503,摇荡,2
7504,回刺,1
7505,赤闪雷,4
7506,短兵相接,6
7507,赤疾风,10
7509,散碎,15
7510,赤火炎,26
7511,赤飞石,30
7512,交击斩,35
7513,划圆斩,52
7514,赤治疗,54
7515,移转,40
7516,连攻,50
7517,飞刺,45
7518,促进,50
7519,六分反击,56
7520,鼓励,58
7521,倍增,60
7523,赤复活,64
7524,震荡,62
7525,赤核爆,68
7526,赤神圣,70
7527,魔回刺,1
7528,魔交击斩,35
7529,魔连攻,50
7530,魔划圆斩,52
7559,沉稳咏唱,44
7560,昏乱,8
7561,即刻咏唱,18
7562,醒梦,24
"""
"""
1234,赤火炎预备
1235,赤飞石预备
167,即刻咏唱
1249,连续咏唱
"""

rdm_prepares = {1234, 1235}


class Single(ComboBase):
    action_id = 7510
    combo_id = "rdm/single"
    title = "单体平衡"

    @staticmethod
    def combo(me):
        lv = me.level
        gauge = plugins.XivMemory.gauge
        effects = me.effects.get_set()
        prepare = rdm_prepares.intersection(effects)
        if 1249 in effects or 167 in effects and lv >= 4:
            if len(prepare) == 1:
                return 7507 if next(iter(prepare)) == 1234 else 7505
            else:
                return 7507 if gauge.white_mana < gauge.black_mana and lv >= 10 else 7505
        else:
            if len(prepare) == 2:
                return 7511 if gauge.white_mana < gauge.black_mana else 7510
            if 1235 in prepare: return 7511
            if 1234 in prepare: return 7510
            return 7503


class Multi(ComboBase):
    action_id = 7509
    combo_id = "rdm/multi"
    title = "群体平衡"

    @staticmethod
    def combo(me):
        lv = me.level
        effects = me.effects.get_set()
        if 1249 in effects or 167 in effects or lv < 18: return 7509
        gauge = plugins.XivMemory.gauge
        return 16525 if gauge.white_mana <= gauge.black_mana and lv >= 22 else 16524


class Sword(ComboBase):
    action_id = 7516
    combo_id = "rdm/sword"
    title = "魔六连"

    @staticmethod
    def combo(me):
        lv = me.level
        match plugins.XivMemory.combo_state.action_id:
            case 7504 if lv > 35:
                return 7512
            case 7512 if lv >= 50:
                return 7516
            case 7529 if lv >= 68:
                if lv < 70: return 7525
                prepare = rdm_prepares.intersection(me.effects.get_set())
                if len(prepare) == 1:
                    return 7526 if next(iter(prepare)) == 1234 else 7525
                else:
                    gauge = plugins.XivMemory.gauge
                    return 7526 if gauge.white_mana < gauge.black_mana else 7525
            case 7525 | 7526 if lv >= 80:
                return 16530
            case 16530 if lv >= 90:
                return 25858
            case _:
                return 7504


combos = [Single, Multi,Sword]
