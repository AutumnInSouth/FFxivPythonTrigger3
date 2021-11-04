from ..combos import ComboBase
from FFxivPythonTrigger import plugins

"""
15989：瀑泻（1）
15990：喷泉（2）
15991：逆瀑泻（20）
15992：坠喷泉（40）
15993：风车（15）
15994：落刃雨（25）
15995：升风车（35）
15996：落血雨（45）
16007：扇舞·序（30）
16008：扇舞·破（50）
16009：扇舞·急（66）
15997：标准舞步（15）
15998：技巧舞步（70）
15999: 
16005：剑舞（76）
"""
"""
1814,逆瀑泻预备
1815,坠喷泉预备
1816,升风车预备
1817,落血雨预备
1818,标准舞步
1819,技巧舞步
1820,扇舞·急预备
1821,标准舞步结束
1822,技巧舞步结束
"""
# index 0  is a fallback for special cases
dnc_standard_step_skill_mapping = [15999, 15999, 16000, 16001, 16002]

class Single(ComboBase):
    action_id = 15989
    combo_id = "dnc/single"
    title = "瀑布-单体连"

    @staticmethod
    def combo(me):
        effects = me.effects.get_set()
        # note that we give skill 15992 priority because it's of higher damage for now
        # TODO: better check remain time of according effect to avoid wasting
        if 1815 in effects: return 15992
        if 1814 in effects: return 15991
        return 15990 if plugins.XivMemory.combat_data.combo_state.action_id == 15989 and me.level >= 2 else 15989 


class Multi(ComboBase):
    action_id = 15993
    combo_id = "dnc/multi"
    title = "风车-群体连"

    @staticmethod
    def combo(me):
        effects = me.effects.get_set()
        # note that we give skill 15996 priority because it's of higher damage for now
        # TODO: better check remain time of according effect to avoid wasting
        if 1817 in effects: return 15996
        if 1816 in effects: return 15995
        return 15994 if plugins.XivMemory.combat_data.combo_state.action_id == 15993 and me.level >= 25 else 15993


class Standard(ComboBase):
    action_id = 15997
    combo_id = "dnc/standard"
    title = "标准舞步"

    @staticmethod
    def combo(me):
        gauge = plugins.XivMemory.player_info.gauge
        
        # check whether in standard dance and dance isn't finish
        if 1818 in me.effects.get_set() and gauge.current_step < 2:
            # mapping to next demanding spell
            return dnc_standard_step_skill_mapping[gauge.step[gauge.current_step].raw_value]
        # start/finsh dance
        return 15997


class Skill(ComboBase):
    action_id = 15998
    combo_id = "dnc/skill"
    title = "技巧舞步"

    @staticmethod
    def combo(me):
        gauge = plugins.XivMemory.player_info.gauge
        
        # check whether in standard dance and dance isn't finish
        if 1819 in me.effects.get_set() and gauge.current_step < 4:
            # mapping to next demanding spell
            return dnc_standard_step_skill_mapping[gauge.step[gauge.current_step].raw_value]
        # start/finsh dance
        return 15998


combos = [Single, Multi, Standard, Skill]
