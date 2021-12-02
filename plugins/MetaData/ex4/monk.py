from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Bootshine(ActionBase):
        """
        Delivers an attack with a potency of 200. (source.job==20?(source.level>=50?Leaden Fist Potency: 370 :):)Opo-opo Form Bonus: Critical damage if dealt from a target's rear Additional Effect: Changes form to raptor Duration: 15s
        """
        id = 53
        name = {"Bootshine", "连击"}

    class TrueStrike(ActionBase):
        """
        Delivers an attack with a potency of 270. 300 when executed from a target's rear. Can only be executed when in raptor form. Additional Effect: Changes form to coeurl Duration: 15s
        """
        id = 54
        name = {"True Strike", "正拳"}

    class SnapPunch(ActionBase):
        """
        Delivers an attack with a potency of 270. 300 when executed from a target's flank. Can only be executed when in coeurl form. Additional Effect: Changes form to opo-opo Duration: 15s
        """
        id = 56
        name = {"Snap Punch", "崩拳"}

    class FistsOfEarth(ActionBase):
        """
        Reduces damage taken by 10%. Cannot be used with Fists of Fire or Fists of Wind, and shares a recast timer with both. Effect ends upon reuse.
        104, Fists of Earth, Fists of Earth, Damage taken is reduced.
        2006, Fists of Earth, Fists of Earth, Damage taken is reduced.
        """
        id = 60
        name = {"Fists of Earth", "金刚体势"}

    class TwinSnakes(ActionBase):
        """
        Delivers an attack with a potency of 230. 260 when executed from a target's flank. Can only be executed when in raptor form. Additional Effect: Increases damage by 10% Duration: 15s Additional Effect: Changes form to coeurl Duration: 15s
        101, Twin Snakes, Twin Snakes, Damage dealt is increased.
        """
        id = 61
        name = {"Twin Snakes", "双掌打"}

    class ArmOfTheDestroyer(ActionBase):
        """
        Delivers an attack with a potency of 110 to all nearby targets. Opo-opo Form Potency: 140 Additional Effect: Changes form to raptor Duration: 15s
        """
        id = 62
        name = {"Arm of the Destroyer", "破坏神冲"}

    class FistsOfFire(ActionBase):
        """
        Increases damage dealt by (source.job==20?(source.level>=72?10:5):5)%. Cannot be used with Fists of Earth or Fists of Wind, and shares a recast timer with both. Effect ends upon reuse.
        103, Fists of Fire, Fists of Fire, Damage dealt is increased.
        2005, Fists of Fire, Fists of Fire, Damage dealt is increased.
        """
        id = 63
        name = {"Fists of Fire", "红莲体势"}

    class Mantra(ActionBase):
        """
        Increases HP recovery via healing actions by 10% for self and nearby party members. Duration: 15s
        102, Mantra, Mantra, HP recovery via healing actions is increased.
        """
        id = 65
        name = {"Mantra", "真言"}

    class Demolish(ActionBase):
        """
        Delivers an attack with a potency of 80. 110 when executed from a target's rear. Can only be executed when in coeurl form. Additional Effect: Damage over time Potency: 80 Duration: 18s Additional Effect: Changes form to opo-opo Duration: 15s
        246, Demolish, Demolish, Internal bleeding is causing damage over time.
        1309, Demolish, Demolish, Sustaining damage over time, as well as increased damage from target who executed Demolish.
        """
        id = 66
        name = {"Demolish", "破碎拳"}

    class PerfectBalance(ActionBase):
        """
        Grants 6 stacks of Perfect Balance, each stack allowing the execution of a weaponskill that requires a certain form, without being in that form. Duration: 15s
        110, Perfect Balance, Perfect Balance, Employing all three pugilistic fighting stances─opo-opo, raptor, and coeurl.
        """
        id = 69
        name = {"Perfect Balance", "震脚"}

    class Rockbreaker(ActionBase):
        """
        Delivers an attack with a potency of 150 to all nearby enemies. Can only be executed when in coeurl form. Additional Effect: Changes form to opo-opo Duration: 15s
        """
        id = 70
        name = {"Rockbreaker", "地烈劲"}

    class ShoulderTackle(ActionBase):
        """
        Rushes target and delivers an attack with a potency of 100. (source.job==20?(source.level>=66?Maximum Charges: 2 :):)Cannot be executed while bound.
        """
        id = 71
        name = {"Shoulder Tackle", "罗刹冲"}

    class FistsOfWind(ActionBase):
        """
        Increases movement speed. Cannot be used with Fists of Earth or Fists of Fire, and shares a recast timer with both. Effect ends upon reuse.
        105, Fists of Wind, Fists of Wind, Movement speed is increased.
        2007, Fists of Wind, Fists of Wind, Weaponskill recast time is reduced.
        """
        id = 73
        name = {"Fists of Wind", "疾风体势"}

    class DragonKick(ActionBase):
        """
        Delivers an attack with a potency of 230. 260 when executed from a target's flank. Opo-opo Form Bonus: Grants Leaden Fist Duration: 30s Additional Effect: Changes form to raptor Duration: 15s
        98, Dragon Kick, Dragon Kick, Blunt resistance is reduced.
        """
        id = 74
        name = {"Dragon Kick", "双龙脚"}

    class TornadoKick(ActionBase):
        """
        Delivers an attack with a potency of 400.
        """
        id = 3543
        name = {"Tornado Kick", "斗魂旋风脚"}

    class ElixirField(ActionBase):
        """
        Delivers an attack with a potency of 250 to all nearby enemies.
        """
        id = 3545
        name = {"Elixir Field", "苍气炮"}

    class Meditation(ActionBase):
        """
        Opens a chakra. Up to five chakra can be opened at once. Opens all five chakra when used outside of combat. Shares a recast timer with all other weaponskills.
        1865, Meditation, Meditation, Deep in contemplation.
        2176, Meditation, Meditation, Deep in contemplation.
        """
        id = 3546
        name = {"Meditation", "斗气"}

    class TheForbiddenChakra(ActionBase):
        """
        Delivers an attack with a potency of 340. Can only be executed while in combat and under the effect of the Fifth Chakra. The five chakra close upon execution. Shares a recast timer with Enlightenment. ※This action cannot be assigned to a hotbar.
        """
        id = 3547
        name = {"the Forbidden Chakra", "阴阳斗气斩"}

    class FormShift(ActionBase):
        """
        Grants Formless Fist to self, allowing the execution of a weaponskill that requires a certain form, without being in that form. Duration: 15s Any additional effects associated with the executed action will also be applied.
        """
        id = 4262
        name = {"Form Shift", "演武"}

    class RiddleOfEarth(ActionBase):
        """
        Grants 3 stacks of Riddle of Earth, each stack reducing damage taken by 10% and nullifying all action direction requirements. Duration: 10s Maximum Charges: 3 Effect ends when time expires or upon execution of three weaponskills.
        1179, Riddle of Earth, Riddle of Earth, Contemplating the riddle of earth. Damage taken is reduced and all action direction requirements are nullified.
        1310, Riddle of Earth, Riddle of Earth, Contemplating the riddle of earth. Taking a certain amount of damage triggers <UIForeground(506)><UIGlow(507)>Earth's Reply</UIGlow></UIForeground>.
        2008, Riddle of Earth, Riddle of Earth, A barrier created through profound comprehension of the earth is nullifying damage.
        """
        id = 7394
        name = {"Riddle of Earth", "金刚极意"}

    class RiddleOfFire(ActionBase):
        """
        Increases damage dealt by 25%. Duration: 20s
        1181, Riddle of Fire, Riddle of Fire, Damage dealt is increased.
        1413, Riddle of Fire, Riddle of Fire, Next weaponskill will deal increased damage.
        """
        id = 7395
        name = {"Riddle of Fire", "红莲极意"}

    class Brotherhood(ActionBase):
        """
        Grants Brotherhood and Meditative Brotherhood to all nearby party members. Brotherhood Effect: Increases damage dealt by 5% Meditative Brotherhood Effect: 20% chance you open a chakra when party members under this effect execute a weaponskill or cast a spell Duration: 15s
        1185, Brotherhood, Brotherhood, Damage dealt is increased.
        2174, Brotherhood, Brotherhood, Damage dealt is increased.
        """
        id = 7396
        name = {"Brotherhood", "义结金兰"}

    class FourPointFury(ActionBase):
        """
        Delivers an attack with a potency of 140 to all nearby enemies. Can only be executed when in raptor form. Additional Effect: Extends Twin Snakes duration by 10s to a maximum of 15s Additional Effect: Changes form to coeurl Duration: 15s
        """
        id = 16473
        name = {"Four-point Fury", "四面脚"}

    class Enlightenment(ActionBase):
        """
        Delivers an attack with a potency of 220 to all enemies in a straight line before you. Can only be executed while in combat and under the effect of the Fifth Chakra. The five chakra close upon execution. Shares a recast timer with the Forbidden Chakra.
        """
        id = 16474
        name = {"Enlightenment", "万象斗气圈"}

    class Anatman(ActionBase):
        """
        Extends the duration of Twin Snakes and your present form to maximum and halts their expiration. Duration: 30s Cancels auto-attack upon execution. Effect ends upon using another action or moving (including facing a different direction). Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.
        1862, Anatman, Anatman, Form and <UIForeground(506)><UIGlow(507)>Twin Snakes</UIGlow></UIForeground> timers are suspended due to a transcendent inner calm.
        """
        id = 16475
        name = {"Anatman", "无我"}

    class SixSidedStar(ActionBase):
        """
        Delivers an attack with a potency of 540. Additional Effect: Increases movement speed Duration: 5s This weaponskill does not share a recast timer with any other actions. Upon execution, the recast timer for this action will be applied to all other weaponskills and magic actions.
        2514, Six-sided Star, Six-sided Star, Movement speed is increased.
        """
        id = 16476
        name = {"Six-sided Star", "六合星导脚"}
