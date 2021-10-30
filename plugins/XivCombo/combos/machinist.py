from ..combos import ComboBase
from FFxivPythonTrigger import plugins


class Single(ComboBase):
    action_id = 2873
    combo_id = "mch/single"
    title = "机工单体连击及热冲击"

    @staticmethod
    def combo(me):
        lv = me.level
        if lv >= 35 and plugins.XivMemory.gauge.overheat_ms:
            return 7410
        match plugins.XivMemory.combo_state.action_id:
            case 2866 if lv > 2:
                return 2868
            case 2868 if lv >= 26:
                return 2873
            case _:
                return 2866


class Multi(ComboBase):
    action_id = 2870
    combo_id = "mch/multi"
    title = "散射自动替换自动弩"

    @staticmethod
    def combo(me):
        return 16497 if plugins.XivMemory.gauge.overheat_ms and me.level >= 52 else 2870


combos = [Single, Multi]
