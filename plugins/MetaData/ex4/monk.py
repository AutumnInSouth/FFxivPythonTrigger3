from ..base import *


class Actions:

    class Bootshine(ActionBase):
        """
Delivers an attack with a potency of (source.job==20?(source.level>=84?210:180):180).
(source.job==20?(source.level>=50?Leaden Fist Potency: (source.job==20?(source.level>=84?310:280):280)
:):)Opo-opo Form Bonus: Guarantees a critical hit
Additional Effect: Changes form to raptor
Duration: 30s
        """
        id = 53
        name = {'连击', 'Bootshine'}

    class TrueStrike(ActionBase):
        """
Delivers an attack with a potency of (source.job==20?(source.level>=84?300:270):270).
Can only be executed when in raptor form.
Additional Effect: Changes form to coeurl
Duration: 30s
        """
        id = 54
        name = {'True Strike', '正拳'}

    class SnapPunch(ActionBase):
        """
Delivers an attack with a potency of (source.job==20?(source.level>=84?250:220):220).
(source.job==20?(source.level>=84?310:280):280) when executed from a target's flank.
Can only be executed when in coeurl form.
Additional Effect: Changes form to opo-opo
Duration: 30s
        """
        id = 56
        name = {'崩拳', 'Snap Punch'}

    class Meditation(ActionBase):
        """
Opens a chakra. Up to five chakra can be opened at once.
Opens all five chakra when used outside of combat.
Shares a recast timer with all other weaponskills.
※Action changes to (source.job==20?(source.level>=54?The Forbidden Chakra:Steel Peak):Steel Peak) when all five chakra are open.
>> 2176, Meditation, Deep in contemplation.
>> 1865, Meditation, Deep in contemplation.
        """
        id = 3546
        name = {'Meditation', '斗气'}

    class SteelPeak(ActionBase):
        """
Delivers an attack with a potency of 180.
Can only be executed while in combat and under the effect of the Fifth Chakra. The five chakra close upon execution.
Shares a recast timer with Howling Fist.
※This action cannot be assigned to a hotbar.
        """
        id = 25761
        name = {'Steel Peak'}

    class TwinSnakes(ActionBase):
        """
Delivers an attack with a potency of (source.job==20?(source.level>=84?280:250):250).
Can only be executed when in raptor form.
Additional Effect: Grants Disciplined Fist
Disciplined Fist Effect: Increases damage dealt by (source.job==20?(source.level>=76?15:10):10)%
Duration: 15s
Additional Effect: Changes form to coeurl
Duration: 30s
>> 101, Twin Snakes, Damage dealt is increased.
        """
        id = 61
        name = {'双掌打', 'Twin Snakes'}

    class ArmOfTheDestroyer(ActionBase):
        """
Delivers an attack with a potency of 100 to all nearby targets.
Opo-opo Form Potency: 110
Additional Effect: Changes form to raptor
Duration: 30s
        """
        id = 62
        name = {'破坏神冲', 'Arm of the Destroyer'}

    class Demolish(ActionBase):
        """
Delivers an attack with a potency of (source.job==20?(source.level>=84?70:40):40).
(source.job==20?(source.level>=84?130:100):100) when executed from a target's rear.
Can only be executed when in coeurl form.
Additional Effect: Damage over time
Potency: 70
Duration: 18s
Additional Effect: Changes form to opo-opo
Duration: 30s
>> 1309, Demolish, Sustaining damage over time, as well as increased damage from target who executed Demolish.
>> 246, Demolish, Internal bleeding is causing damage over time.
        """
        id = 66
        name = {'破碎拳', 'Demolish'}

    class Rockbreaker(ActionBase):
        """
Delivers an attack with a potency of 130 to all nearby enemies.
Can only be executed when in coeurl form.
Additional Effect: Changes form to opo-opo
Duration: 30s
        """
        id = 70
        name = {'Rockbreaker', '地烈劲'}

    class Thunderclap(ActionBase):
        """
Rush to a targeted enemy's or party member's location.
Maximum Charges: (source.job==20?(source.level>=84?3:2):2)
Cannot be executed while bound.
>> 515, Thunderclap, Sustaining damage over time. If the effect is not removed, it will continue to stack, increasing the amount of damage inflicted.
        """
        id = 25762
        name = {'Thunderclap'}

    class HowlingFist(ActionBase):
        """
Delivers an attack with a potency of 100 to all enemies in a straight line before you.
Can only be executed while in combat and under the effect of the Fifth Chakra. The five chakra close upon execution.
Shares a recast timer with (source.job==20?(source.level>=54?The Forbidden Chakra:Steel Peak):Steel Peak).
        """
        id = 25763
        name = {'Howling Fist'}

    class Mantra(ActionBase):
        """
Increases HP recovery via healing actions by 10% for self and nearby party members.
Duration: 15s
>> 102, Mantra, HP recovery via healing actions is increased.
        """
        id = 65
        name = {'真言', 'Mantra'}

    class FourPointFury(ActionBase):
        """
Delivers an attack with a potency of 120 to all nearby enemies.
Can only be executed when in raptor form.
Additional Effect: Grants Disciplined Fist
Disciplined Fist Effect: Increases damage dealt by (source.job==20?(source.level>=76?15:10):10)%
Duration: 15s
Additional Effect: Changes form to coeurl
Duration: 30s
        """
        id = 16473
        name = {'四面脚', 'Four-point Fury'}

    class PerfectBalance(ActionBase):
        """
Grants 3 stacks of Perfect Balance, each stack allowing the execution of a weaponskill that requires a certain form, without being in that form.
Duration: 20s
(source.job==20?(source.level>=60?Additional Effect: Grants Opo-opo Chakra, Coeurl Chakra, or Raptor Chakra depending on the form required by actions executed
:):)Maximum Charges: 2
Can only be executed while in combat.
>> 110, Perfect Balance, Employing all three pugilistic fighting stances─opo-opo, raptor, and coeurl.
        """
        id = 69
        name = {'震脚', 'Perfect Balance'}

    class DragonKick(ActionBase):
        """
Delivers an attack with a potency of (source.job==20?(source.level>=84?320:290):290).
Opo-opo Form Bonus: Grants Leaden Fist
Duration: 30s
Additional Effect: Changes form to raptor
Duration: 30s
>> 98, Dragon Kick, Blunt resistance is reduced.
        """
        id = 74
        name = {'双龙脚', 'Dragon Kick'}

    class FormShift(ActionBase):
        """
Grants Formless Fist to self, allowing the execution of a weaponskill that requires a certain form, without being in that form.
Duration: 30s
Any additional effects associated with the executed action will also be applied.
        """
        id = 4262
        name = {'Form Shift', '演武'}

    class TheForbiddenChakra(ActionBase):
        """
Delivers an attack with a potency of (source.job==20?(source.level>=84?340:310):310).
Can only be executed while in combat and under the effect of the Fifth Chakra. The five chakra close upon execution.
Shares a recast timer with (source.job==20?(source.level>=74?Enlightenment:Howling Fist):Howling Fist).
※This action cannot be assigned to a hotbar.
        """
        id = 3547
        name = {'阴阳斗气斩', 'the Forbidden Chakra'}

    class TornadoKick(ActionBase):
        """
Delivers an attack to target and all enemies nearby it with a potency of 850 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Grants Formless Fist, allowing the execution of a weaponskill that requires a certain form, without being in that form
Duration: 30s
Any additional effects associated with the executed action will also be applied.
Can only be executed while under the effect of Lunar Nadi and Solar Nadi, as well as three Beast Chakra.
※This action cannot be assigned to a hotbar.
        """
        id = 3543
        name = {'Tornado Kick', '斗魂旋风脚'}

    class ElixirField(ActionBase):
        """
Delivers an attack to all nearby enemies with a potency of 600 for the first enemy, and 70% less for all remaining enemies.
Additional Effect: Opens the Lunar Nadi
Additional Effect: Grants Formless Fist, allowing the execution of a weaponskill that requires a certain form, without being in that form
Duration: 30s
Any additional effects associated with the executed action will also be applied.
Can only be executed while under the effect of three of the same Beast Chakra.
※This action cannot be assigned to a hotbar.
        """
        id = 3545
        name = {'苍气炮', 'Elixir Field'}

    class MasterfulBlitz(ActionBase):
        """
Strike the enemy with a technique fueled by the power of your Beast Chakra.
The technique used is determined by the number of different types of Beast Chakra opened.
1 Beast Chakra Type: Elixir Field
2 Beast Chakra Types: Celestial Revolution
3 Beast Chakra Types: (source.job==20?(source.level>=86?Rising Phoenix:Flint Strike):Flint Strike)
3 Beast Chakra and Both Nadi: (source.job==20?(source.level>=90?Phantom Rush:Tornado Kick):Tornado Kick)
        """
        id = 25764
        name = {'Masterful Blitz'}

    class CelestialRevolution(ActionBase):
        """
Delivers an attack with a potency of 450.
Additional Effect: Opens the Lunar Nadi
If the Lunar Nadi is already open, opens the Solar Nadi instead.
Additional Effect: Grants Formless Fist, allowing the execution of a weaponskill that requires a certain form, without being in that form
Duration: 30s
Any additional effects associated with the executed action will also be applied.
Can only be executed while under the effect of three Beast Chakra.
※This action cannot be assigned to a hotbar.
        """
        id = 25765
        name = {'Celestial Revolution'}

    class FlintStrike(ActionBase):
        """
Delivers an attack to all nearby enemies with a potency of 600 for the first enemy, and 70% less for all remaining enemies.
Additional Effect: Opens the Solar Nadi
Additional Effect: Grants Formless Fist, allowing the execution of a weaponskill that requires a certain form, without being in that form
Duration: 30s
Any additional effects associated with the executed action will also be applied.
Can only be executed while under the effect of three distinct Beast Chakra.
※This action cannot be assigned to a hotbar.
        """
        id = 25882
        name = {'Flint Strike'}

    class RiddleOfEarth(ActionBase):
        """
Grants 3 stacks of Riddle of Earth, each stack reducing damage taken by 20%.
Duration: 10s
Maximum Charges: 3
Effect ends when time expires or upon execution of three weaponskills.
>> 2008, Riddle of Earth, A barrier created through profound comprehension of the earth is nullifying damage.
>> 1179, Riddle of Earth, Contemplating the riddle of earth. Damage taken is reduced.
>> 1310, Riddle of Earth, Contemplating the riddle of earth. Taking a certain amount of damage triggers Earth's Reply.
        """
        id = 7394
        name = {'金刚极意', 'Riddle of Earth'}

    class RiddleOfFire(ActionBase):
        """
Increases damage dealt by 15%.
Duration: 20s
>> 1181, Riddle of Fire, Damage dealt is increased.
>> 1413, Riddle of Fire, Next weaponskill will deal increased damage.
        """
        id = 7395
        name = {'Riddle of Fire', '红莲极意'}

    class Brotherhood(ActionBase):
        """
Grants Brotherhood and Meditative Brotherhood to self and all nearby party members.
Brotherhood Effect: Increases damage dealt by 5%
Meditative Brotherhood Effect: (source.job==20?(source.level>=88?20% chance you open a chakra when party members under this effect execute a weaponskill or cast a spell
Chance is 100% when you execute a weaponskill or cast a spell while under the effect of Meditative Brotherhood.:20% chance you open a chakra when you or party members under this effect execute a weaponskill or cast a spell):20% chance you open a chakra when you or party members under this effect execute a weaponskill or cast a spell)
Duration: 15s
>> 1185, Brotherhood, Damage dealt is increased.
>> 2174, Brotherhood, Damage dealt is increased.
        """
        id = 7396
        name = {'义结金兰', 'Brotherhood'}

    class RiddleOfWind(ActionBase):
        """
Reduces auto-attack delay by 50%.
Duration: 15s
>> 1244, Riddle of Wind, Able to execute Riddle of Wind.
>> 2687, Riddle of Wind, Auto-attack delay is reduced.
>> 1364, Riddle of Wind, Able to execute Riddle of Wind.
        """
        id = 25766
        name = {'Riddle of Wind'}

    class Enlightenment(ActionBase):
        """
Delivers an attack with a potency of 170 to all enemies in a straight line before you.
Can only be executed while in combat and under the effect of the Fifth Chakra. The five chakra close upon execution.
Shares a recast timer with The Forbidden Chakra.
        """
        id = 16474
        name = {'Enlightenment', '万象斗气圈'}

    class Anatman(ActionBase):
        """
Extends the duration of Disciplined Fist and your present form to maximum and halts their expiration.
Duration: 30s
Cancels auto-attack upon execution. Effect ends upon using another action or moving (including facing a different direction).
Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.
>> 1862, Anatman, Form and Disciplined Fist timers are suspended due to a transcendent inner calm.
        """
        id = 16475
        name = {'无我', 'Anatman'}

    class SixSidedStar(ActionBase):
        """
Delivers an attack with a potency of (source.job==20?(source.level>=84?550:500):500).
Additional Effect: Increases movement speed
Duration: 5s
This weaponskill does not share a recast timer with any other actions. Upon execution, the recast timer for this action will be applied to all other weaponskills and magic actions.
>> 2514, Six-sided Star, Movement speed is increased.
        """
        id = 16476
        name = {'六合星导脚', 'Six-sided Star'}

    class ShadowOfTheDestroyer(ActionBase):
        """
Delivers an attack with a potency of 110 to all nearby enemies.
Opo-opo Form Bonus: Guarantees a critical hit
Additional Effect: Changes form to raptor
Duration: 30s
        """
        id = 25767
        name = {'Shadow of the Destroyer'}

    class RisingPhoenix(ActionBase):
        """
Deals physical fire damage to all nearby enemies with a potency of 700 for the first enemy, and 70% less for all remaining enemies.
Additional Effect: Opens the Solar Nadi
Additional Effect: Grants Formless Fist, allowing the execution of a weaponskill that requires a certain form, without being in that form
Duration: 30s
Any additional effects associated with the executed action will also be applied.
Can only be executed while under the effect of three distinct Beast Chakra.
※This action cannot be assigned to a hotbar.
        """
        id = 25768
        name = {'Rising Phoenix'}

    class PhantomRush(ActionBase):
        """
Delivers an attack to target and all enemies nearby it with a potency of 1,000 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Grants Formless Fist, allowing the execution of a weaponskill that requires a certain form, without being in that form
Duration: 30s
Any additional effects associated with the executed action will also be applied.
Can only be executed while under the effect of Lunar Nadi and Solar Nadi, as well as three Beast Chakra.
※This action cannot be assigned to a hotbar.
        """
        id = 25769
        name = {'Phantom Rush'}
