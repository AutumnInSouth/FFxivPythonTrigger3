from ..combos import ComboBase
from FFxivPythonTrigger import plugins

dnc_standard_step_skill_mapping = [15999, 15999, 16000, 16001, 16002]


class Single(ComboBase):
    action_id = 15990
    combo_id = "dnc/single"
    title = "单体连"

    @staticmethod
    def combo(me):
        effects = me.effects.get_set()
        if 2694 in effects: return 15992
        if 2693 in effects: return 15991
        return 15990 if plugins.XivMemory.combo_state.action_id == 15989 and me.level >= 2 else 15989


class Multi(ComboBase):
    action_id = 15994
    combo_id = "dnc/multi"
    title = "群体连"

    @staticmethod
    def combo(me):
        effects = me.effects.get_set()
        if 2694 in effects: return 15996
        if 2693 in effects: return 15995
        return 15994 if plugins.XivMemory.combo_state.action_id == 15993 and me.level >= 25 else 15993


class Standard(ComboBase):
    action_id = 15997
    combo_id = "dnc/standard"
    title = "标准舞步"

    @staticmethod
    def combo(me):
        gauge = plugins.XivMemory.gauge

        # check whether in standard dance and dance isn't finish
        if 1818 in me.effects.get_set() and gauge.current_step < 2:
            # mapping to next demanding spell
            return dnc_standard_step_skill_mapping[gauge.step[gauge.current_step].raw_value]
        # start/finish dance
        return 15997


class Skill(ComboBase):
    action_id = 15998
    combo_id = "dnc/skill"
    title = "技巧舞步"

    @staticmethod
    def combo(me):
        gauge = plugins.XivMemory.gauge

        # check whether in standard dance and dance isn't finish
        if 1819 in me.effects.get_set() and gauge.current_step < 4:
            # mapping to next demanding spell
            return dnc_standard_step_skill_mapping[gauge.step[gauge.current_step].raw_value]
        # start/finish dance
        return 15998


class Fan1(ComboBase):
    action_id = 16007
    combo_id = "dnc/fan1"
    title = "扇舞·序"

    @staticmethod
    def combo(me):
        return 16009 if me.effects.has(1820) else 16007


class Fan2(ComboBase):
    action_id = 16008
    combo_id = "dnc/fan2"
    title = "扇舞·破"

    @staticmethod
    def combo(me):
        return 16009 if me.effects.has(1820) else 16008


class Fan4(ComboBase):
    action_id = 25791
    combo_id = "dnc/fan4"
    title = "Fan4/Florish"

    @staticmethod
    def combo(me):
        return 25791 if me.effects.has(2699) else 16013


class StarFall(ComboBase):
    action_id = 25792
    combo_id = "dnc/starfall"
    title = "星落/进攻"

    @staticmethod
    def combo(me):
        return 25792 if me.effects.has(2700) else 16011


combos = [Single, Multi, Standard, Skill, Fan1, Fan2, Fan4, StarFall]
