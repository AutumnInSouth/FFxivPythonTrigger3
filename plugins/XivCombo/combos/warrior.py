from ..combos import ComboBase
from FFxivPythonTrigger import plugins


class Single(ComboBase):
    action_id = 42
    combo_id = "war/single"
    title = "暴风斩"

    @staticmethod
    def combo(me):
        lv = me.level
        combo_id = plugins.XivMemory.combo_state.action_id
        # whether has aura
        red = me.effects.get_dict().get(90)
        # combat loop: 31, 37, 42/45
        if combo_id == 31 and lv >= 4:
            return 37
        elif combo_id == 37 and lv >= 26:
            # try to extend aura if its remain time less than 30
            return 45 if lv >= 50 and (red is None or red.timer < 30) else 42
        return 31


class Multi(ComboBase):
    action_id = 16462
    combo_id = "war/multi"
    title = "秘银暴风"

    @staticmethod
    def combo(me):
        return 16462 if plugins.XivMemory.combo_state.action_id == 41 and me.level >= 40 else 41


combos = [Single, Multi]
