from ..combos import ComboBase
from FFxivPythonTrigger import plugins

"""
3624,伤残,1
3617,重斩,1
3623,吸收斩,2
3632,噬魂斩,26
7392,血溅
7391,寂灭,64
7390,血乱,68
3621,释放,6
3641,吸血深渊
3643,精雕怒斩
16468,刚魂,72
16466,暗黑波动
16467,暗黑锋
3625,嗜血
"""
"""
1972,血乱
"""

class Single(ComboBase):
    action_id = 3617
    combo_id = "dk/single"
    title = "重斩"

    @staticmethod
    def combo(me):
        lv = me.level
        combo_id = plugins.XivMemory.combat_data.combo_state.action_id
        # single combat loop: 3617, 3623, 3632
        if combo_id == 3617:
            return 3623 if lv >= 2 else 3617
        elif combo_id == 3623:
            return 3632 if lv >= 26 else 3617
        else:
            return 3617


class Multi(ComboBase):
    action_id = 3621
    combo_id = "dk/multi"
    title = "释放"

    @staticmethod
    def combo(me):
        combo_id = plugins.XivMemory.combat_data.combo_state.action_id
        return 16468 if combo_id == 3621 and me.level >= 72 else 3621


combos = [Single, Multi]