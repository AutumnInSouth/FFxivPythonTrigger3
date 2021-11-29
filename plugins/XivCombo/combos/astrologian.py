from ..combos import ComboBase
from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.saint_coinach import action_sheet

redraw_group = action_sheet[3593]['CooldownGroup']

card_map_arc = {
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 2,
    6: 3,
}


class Draw(ComboBase):
    action_id = 3590
    combo_id = "ast/draw"
    title = "抽卡重抽"

    @staticmethod
    def combo(me):
        gauge = plugins.XivMemory.gauge
        if gauge.held_card.raw_value and me.level >= 40 and plugins.XivMemory.cool_down_group[redraw_group].remain < 60:
            return 3593
        return 3590


class Send(ComboBase):
    action_id = 17055
    combo_id = "ast/send"
    title = "发卡奥秘"

    @staticmethod
    def combo(me):
        gauge = plugins.XivMemory.gauge
        held = card_map_arc.get(gauge.held_card.raw_value, 0)
        if held and me.level >= 50:
            for arcanum in gauge.arcanums:
                if arcanum.raw_value == held:
                    return 7443
        return 17055


combos = [Draw, Send]
