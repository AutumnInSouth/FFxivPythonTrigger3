from ..combos import ComboBase
from FFxivPythonTrigger import plugins


rdm_prepares = {1234, 1235}
speed_swing = {167, 1249, 1238}


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
        if speed_swing.intersection(effects) and lv >= 4:
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
        if lv < 18 or speed_swing.intersection(me.effects.get_set()): return 7509
        gauge = plugins.XivMemory.gauge
        return 16525 if gauge.white_mana <= gauge.black_mana and lv >= 22 else 16524


class Sword(ComboBase):
    action_id = 7516
    combo_id = "rdm/sword"
    title = "魔六连"

    @staticmethod
    def combo(me):
        lv = me.level
        gauge = plugins.XivMemory.gauge
        if gauge.mana_stacks >= 3:
            if lv < 70: return 7525
            prepare = rdm_prepares.intersection(me.effects.get_set())
            if len(prepare) == 1:
                return 7526 if next(iter(prepare)) == 1234 else 7525
            else:
                return 7526 if gauge.white_mana < gauge.black_mana else 7525

        match plugins.XivMemory.combo_state.action_id:
            case 7504 if lv > 35:
                return 7512
            case 7512 if lv >= 50:
                return 7516
            case 7525 | 7526 if lv >= 80:
                return 16530
            case 16530 if lv >= 90:
                return 25858
            case _:
                return 7504


combos = [Single, Multi, Sword]
