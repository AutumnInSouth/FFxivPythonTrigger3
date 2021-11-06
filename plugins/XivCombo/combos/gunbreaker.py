from ..combos import ComboBase
from FFxivPythonTrigger import plugins

"""
16143：闪雷弹（15）
16137：利刃斩（1）
16139：残暴弹（4）
16145：迅连斩（26）
16141：恶魔切（10）
16149：恶魔杀（40）
16162：爆发击（30）
16163：命运之环（72）
16153：音速破（54）
16146：烈牙（60）
16147：猛兽爪（60）
16150：凶禽爪（60）
16155：续剑（70）
16144：危险领域（18/80)
16159：弓形冲波(62)
16138：无情(2)
16164：血壤（76）
"""


class Single(ComboBase):
    action_id = 16145
    combo_id = "gnb/single"
    title = "迅连斩"

    @staticmethod
    def combo(me):
        lv = me.level
        combo_id = plugins.XivMemory.combo_state.action_id
        # single combat loop: 16137, 16139, 16145
        if combo_id == 16137 and lv >= 4:
            return 16139
        elif combo_id == 16139 and lv >= 26:
            return 16145
        else:
            return 16137


class Multi(ComboBase):
    action_id = 16149
    combo_id = "gnb/multi"
    title = "恶魔杀"

    @staticmethod
    def combo(me):
        # TODO: consider adding 16163 after checking cartridge,
        #  note that it's not a pre-defined combo so we cannot use combo_state to check
        return 16149 if plugins.XivMemory.combo_state.action_id == 16141 and me.level >= 40 else 16141

cartridge_auras = [1842, 1843, 1844]
cartridge_spells = [16146, 16147, 16150]
class Cartridge(ComboBase):
    action_id = 16150
    combo_id = "gnb/cartridge"
    title = "子弹连"

    @staticmethod
    def combo(me):
        effects = me.effects.get_set()
        # decide whether to use 16155
        if any(aura in effects for aura in cartridge_auras): return 16155
        return cartridge_spells[plugins.XivMemory.gauge.continuation_state]


combos = [Single, Multi, Cartridge]
