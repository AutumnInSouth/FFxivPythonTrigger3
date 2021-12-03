from ..base import *


class Actions:

    class Snort(ActionBase):
        """
Deals a 20-yalm knockback to all enemies in a cone before you.
        """
        id = 11383
        name = {'鼻息', 'Snort'}

    class FourTonzeWeight(ActionBase):
        """
Drops a 4-tonze weight dealing physical damage at a designated location with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Heavy +40%
Duration: 30s
        """
        id = 11384
        name = {'4-tonze Weight', '4星吨'}

    class WaterCannon(ActionBase):
        """
Deals water damage with a potency of 200.
        """
        id = 11385
        name = {'水炮', 'Water Cannon'}

    class SongOfTorment(ActionBase):
        """
Deals unaspected damage with a potency of 50.
Additional Effect: Unaspected damage over time
Potency: 50
Duration: 30s
        """
        id = 11386
        name = {'Song of Torment', '苦闷之歌'}

    class HighVoltage(ActionBase):
        """
Deals lightning damage to all nearby enemies with a potency of 180 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Paralysis
Duration: 15s
Additional Effect: Potency increased to 220 when target is afflicted with Dropsy
Additional Effect: Duration of Paralysis is increased to 30 seconds when target is afflicted with Dropsy
        """
        id = 11387
        name = {'High Voltage', '高压电流'}

    class BadBreath(ActionBase):
        """
Blow noxious breath on all enemies in a cone before you, inflicting Slow +20%, Heavy +40%, Blind, and Paralysis.
Additional Effect: Poison
Potency: 20
Additional Effect: Damage dealt reduced 10%
Duration: 15s
Additional Effect: Interrupts target
        """
        id = 11388
        name = {'Bad Breath', '臭气'}

    class FlyingFrenzy(ActionBase):
        """
Delivers a jumping physical attack to target and all enemies nearby it with a potency of 150 for the first enemy, and 50% less for all remaining enemies.
Cannot be executed while bound.
        """
        id = 11389
        name = {'狂乱', 'Flying Frenzy'}

    class AquaBreath(ActionBase):
        """
Deals water damage to all enemies in a cone before you with a potency of 140 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Inflicts Dropsy, dealing water damage over time
Potency: 20
Duration: 12s
        """
        id = 11390
        name = {'Aqua Breath', '水流吐息'}

    class Plaincracker(ActionBase):
        """
Deals earth damage to all nearby enemies with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
        """
        id = 11391
        name = {'平原震裂', 'Plaincracker'}

    class AcornBomb(ActionBase):
        """
Puts target and all enemies nearby it to sleep.
Duration: 30s
Cancels auto-attack upon execution.
        """
        id = 11392
        name = {'Acorn Bomb', '橡果炸弹'}

    class Bristle(ActionBase):
        """
Increases the potency of the next spell cast by 50%.
Duration: 30s
Effect cannot be stacked with Harmonized.
        """
        id = 11393
        name = {'怒发冲冠', 'Bristle'}

    class MindBlast(ActionBase):
        """
Deals unaspected damage to all nearby enemies with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Paralysis
Duration: 30s
        """
        id = 11394
        name = {'精神冲击', 'Mind Blast'}

    class BloodDrain(ActionBase):
        """
Deals unaspected damage with a potency of 50.
Additional Effect: Restores MP
        """
        id = 11395
        name = {'吸血', 'Blood Drain'}

    class BombToss(ActionBase):
        """
Deals fire damage at a designated location with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Stun
Duration: 3s
        """
        id = 11396
        name = {'Bomb Toss', '投弹'}

    class ThousandNeedles(ActionBase):
        """
Deals a fixed 1,000 points of physical damage which is shared by all enemies around you.
        """
        id = 11397
        name = {'1000 Needles', '千针刺'}

    class DrillCannons(ActionBase):
        """
Deals physical damage to all enemies in a straight line before you with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Potency is increased to 600 when target is afflicted with Petrification. The Petrification effect is also removed.
        """
        id = 11398
        name = {'Drill Cannons', '钻头炮'}

    class TheLook(ActionBase):
        """
Deals unaspected damage to all enemies in a cone before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Increased enmity
        """
        id = 11399
        name = {'诡异视线', 'the Look'}

    class SharpenedKnife(ActionBase):
        """
Deals physical damage with a potency of 220.
Additional Effect: Potency is increased to 450 when target is stunned
>> 211, Sharpened Knife, Next Lateral Slash is changed to Sharpened Knife, increasing damage dealt.
        """
        id = 11400
        name = {'Sharpened Knife', '锋利菜刀'}

    class Loom(ActionBase):
        """
Move quickly to the specified location.
Cannot be executed while bound.
        """
        id = 11401
        name = {'若隐若现', 'Loom'}

    class FlameThrower(ActionBase):
        """
Deals fire damage to all enemies in a cone before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
        """
        id = 11402
        name = {'Flame Thrower', '火炎放射'}

    class Faze(ActionBase):
        """
Stuns all enemies in a cone before you.
Duration: 6s
        """
        id = 11403
        name = {'拍掌', 'Faze'}

    class Glower(ActionBase):
        """
Deals lightning damage to all enemies in a straight line before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Paralysis
Duration: 6s
        """
        id = 11404
        name = {'Glower', '怒视'}

    class Missile(ActionBase):
        """
Deals damage equal to 50% of target's current HP.
Chance of successful attack is low. Has no effect on enemies whose level is higher than your own.
        """
        id = 11405
        name = {'Missile', '导弹'}

    class WhiteWind(ActionBase):
        """
Restores own HP and the HP of all nearby party members by an amount equal to your current HP.
        """
        id = 11406
        name = {'White Wind', '白风'}

    class FinalSting(ActionBase):
        """
Deals physical damage with a potency of 2,000 while incapacitating self.
Additional Effect: Inflicts Brush with Death on self
Duration: 600s
Effect will not be removed upon revival or further incapacitation.
Cannot be executed while under the effect of Brush with Death.
        """
        id = 11407
        name = {'终极针', 'Final Sting'}

    class SelfDestruct(ActionBase):
        """
Deals fire damage with a potency of 1,500 to all nearby enemies while incapacitating self.
Additional Effect: Potency is increased to 1,800 when you are under the effect of Toad Oil
Additional Effect: Inflicts Brush with Death on self
Duration: 600s
Effect will not be removed upon revival or further incapacitation.
Cannot be executed while under the effect of Brush with Death.
        """
        id = 11408
        name = {'自爆', 'Self-destruct'}

    class Transfusion(ActionBase):
        """
Restores all HP and MP of a single party member while incapacitating self.
Additional Effect: Inflicts Brush with Death on self
Duration: 600s
Effect will not be removed upon revival or further incapacitation.
Cannot be executed while under the effect of Brush with Death.
        """
        id = 11409
        name = {'Transfusion', '融合'}

    class ToadOil(ActionBase):
        """
Increases evasion by 20%.
Duration: 180s
>> 1737, Toad Oil, Evasion is enhanced.
        """
        id = 11410
        name = {'Toad Oil', '油性分泌物'}

    class OffGuard(ActionBase):
        """
Increases target's damage taken by 5%.
Duration: 15s
Recast timer cannot be affected by other spells. However, this action shares a recast timer with Peculiar Light.
>> 1717, Off-guard, Damage taken is increased.
        """
        id = 11411
        name = {'Off-guard', '破防'}

    class StickyTongue(ActionBase):
        """
Draws target towards caster.
Additional Effect: Stun
Duration: 4s
Additional Effect: Increased enmity
        """
        id = 11412
        name = {'滑舌', 'Sticky Tongue'}

    class TailScrew(ActionBase):
        """
Reduces target's HP to a single digit.
Chance of successful attack is low. Has no effect on enemies whose level is higher than your own.
        """
        id = 11413
        name = {'Tail Screw', '螺旋尾'}

    class Level5Petrify(ActionBase):
        """
Petrifies all enemies in a cone before you.
Duration: 20s
Chance of successful attack is low.
Enemy level must be a multiple of 5. Has no effect on enemies whose level is higher than your own.
        """
        id = 11414
        name = {'5级石化', 'Level 5 Petrify'}

    class MoonFlute(ActionBase):
        """
Grants the effect of Waxing Nocturne, increasing damage dealt by 50% and movement speed by 30%.
Duration: 15s
When effect ends, the player is afflicted with Waning Nocturne, preventing the use of auto-attack, weaponskills, spells, or abilities.
Duration: 15s
        """
        id = 11415
        name = {'Moon Flute', '月之笛'}

    class Doom(ActionBase):
        """
Inflicts Doom on target.
Duration: 15s
When effect expires, the target will be KO'd.
Chance of successful attack is low. Has no effect on enemies whose level is higher than your own.
>> 1769, Doom, Certain death when counter reaches zero. Effect dissipates once fully healed.
>> 1738, Doom, Certain death when counter reaches zero.
>> 910, Doom, Certain death when counter reaches zero.
>> 1970, Doom, Certain death when counter reaches zero.
>> 210, Doom, Certain death when counter reaches zero.
>> 2516, Doom, Certain death when counter reaches zero.
>> 2519, Doom, Certain death when counter reaches zero.
        """
        id = 11416
        name = {'死亡宣告', 'Doom'}

    class MightyGuard(ActionBase):
        """
Reduces damage taken by 40% while reducing damage dealt by 40%, increasing enmity generation, and preventing casting interruptions via damage taken.
Effect ends upon reuse.
>> 1719, Mighty Guard, Damage taken and dealt are reduced, while enmity is increased.
        """
        id = 11417
        name = {'强力守护', 'Mighty Guard'}

    class IceSpikes(ActionBase):
        """
Counters enemies with ice damage every time you suffer physical damage.
Counter Potency: 40
Duration: 15s
Additional Effect: 50% chance that when you are struck, the striker will be afflicted with Slow +20%
Duration: 15s
>> 2528, Ice Spikes, Elemental spikes are dealing ice damage to and slowing down attackers.
>> 198, Ice Spikes, Elemental spikes are dealing ice damage to and sometimes slowing down attackers.
>> 1720, Ice Spikes, Upon taking physical damage, sharpened spikes deal ice damage to the attacking opponent, potentially slowing them.
>> 1307, Ice Spikes, Upon taking physical damage, sharpened spikes deal ice damage to the attacking opponent, potentially slowing them.
        """
        id = 11418
        name = {'冰棘屏障', 'Ice Spikes'}

    class TheRamsVoice(ActionBase):
        """
Deals ice damage to all nearby enemies with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Deep Freeze
Duration: 12s
        """
        id = 11419
        name = {'寒冰咆哮', "the Ram's Voice"}

    class TheDragonsVoice(ActionBase):
        """
Deals lightning damage to all nearby enemies with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
Enemies within an 8-yalm radius will be unaffected.
Additional Effect: Paralysis
Duration: 9s
Additional Effect: Potency is increased to 400 against most enemies afflicted with Deep Freeze. The Deep Freeze effect is also removed.
        """
        id = 11420
        name = {'雷电咆哮', "the Dragon's Voice"}

    class PeculiarLight(ActionBase):
        """
Increases magic damage taken by all nearby enemies by 5%.
Duration: 15s
Recast timer cannot be affected by other spells. However, this action shares a recast timer with Off-guard.
>> 1721, Peculiar Light, Magic damage taken is increased.
        """
        id = 11421
        name = {'惊奇光', 'Peculiar Light'}

    class InkJet(ActionBase):
        """
Deals unaspected damage to all enemies in a cone before you with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Blind
Duration: 30s
        """
        id = 11422
        name = {'喷墨', 'Ink Jet'}

    class FlyingSardine(ActionBase):
        """
Deals physical damage with a potency of 10.
Additional Effect: Interrupts target
        """
        id = 11423
        name = {'Flying Sardine', '投掷沙丁鱼'}

    class Diamondback(ActionBase):
        """
Reduces damage taken by 90% and nullifies most knockback and draw-in effects.
Unable to move or take action for the duration of this effect.
Duration: 10s
If used when Waxing Nocturne is active, its effect will transition immediately to Waning Nocturne.
The effect of this action cannot be ended manually.
>> 1722, Diamondback, Though unable to move, damage taken is reduced.
        """
        id = 11424
        name = {'Diamondback', '超硬化'}

    class FireAngon(ActionBase):
        """
Deals physical fire damage to target and all enemies nearby it with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
        """
        id = 11425
        name = {'Fire Angon', '火投枪'}

    class FeatherRain(ActionBase):
        """
Deals wind damage with a potency of 220 to all enemies at a designated location.
Additional Effect: Wind damage over time
Potency: 40
Duration: 6s
Shares a recast timer with certain blue magic spells.
        """
        id = 11426
        name = {'Feather Rain', '飞翎雨'}

    class Eruption(ActionBase):
        """
Deals fire damage with a potency of 300 to all enemies at a designated location.
Shares a recast timer with certain blue magic spells.
        """
        id = 11427
        name = {'Eruption', '地火喷发'}

    class MountainBuster(ActionBase):
        """
Deals physical earth damage to all enemies in a cone before you with a potency of 400 for the first enemy, and 50% less for all remaining enemies.
Shares a recast timer with certain blue magic spells.
        """
        id = 11428
        name = {'山崩', 'Mountain Buster'}

    class ShockStrike(ActionBase):
        """
Deals lightning damage to target and all enemies nearby it with a potency of 400 for the first enemy, and 50% less for all remaining enemies.
Shares a recast timer with certain blue magic spells.
        """
        id = 11429
        name = {'Shock Strike', '轰雷'}

    class GlassDance(ActionBase):
        """
Deals ice damage to all enemies in a wide arc to your fore and flanks with a potency of 350 for the first enemy, and 50% less for all remaining enemies.
Shares a recast timer with certain blue magic spells.
        """
        id = 11430
        name = {'Glass Dance', '冰雪乱舞'}

    class VeilOfTheWhorl(ActionBase):
        """
Counters enemies with water damage every time you suffer damage.
Counter Potency: 50
Duration: 30s
Shares a recast timer with certain blue magic spells.
>> 1724, Veil of the Whorl, Dealing water damage to attackers upon taking damage.
>> 478, Veil of the Whorl, Reflecting damage dealt by ranged attacks.
        """
        id = 11431
        name = {'Veil of the Whorl', '水神的面纱'}

    class AlpineDraft(ActionBase):
        """
Deals wind damage to all enemies in a straight line before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
        """
        id = 18295
        name = {'Alpine Draft', '高山气流'}

    class ProteanWave(ActionBase):
        """
Deals water damage to all enemies in a cone before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: 15-yalm knockback
        """
        id = 18296
        name = {'万变水波', 'Protean Wave'}

    class Northerlies(ActionBase):
        """
Deals ice damage to all enemies in a cone before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Enemies affected by Dropsy are frozen. The Dropsy effect is also removed.
Duration: 20s
        """
        id = 18297
        name = {'Northerlies', '狂风暴雪'}

    class Electrogenesis(ActionBase):
        """
Deals lightning damage to target and all enemies nearby it with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
        """
        id = 18298
        name = {'Electrogenesis', '生物电'}

    class Kaltstrahl(ActionBase):
        """
Deals physical damage to all enemies in a cone before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
        """
        id = 18299
        name = {'寒光', 'Kaltstrahl'}

    class AbyssalTransfixion(ActionBase):
        """
Deals physical damage with a potency of 220.
Additional Effect: Paralysis
Duration: 30s
        """
        id = 18300
        name = {'Abyssal Transfixion', '深渊贯穿'}

    class Chirp(ActionBase):
        """
Puts all nearby enemies to sleep.
Duration: 40s
Cancels auto-attack upon execution.
        """
        id = 18301
        name = {'唧唧咋咋', 'Chirp'}

    class EerieSoundwave(ActionBase):
        """
Removes one beneficial effect from all nearby enemies.
        """
        id = 18302
        name = {'Eerie Soundwave', '怪音波'}

    class PomCure(ActionBase):
        """
Restores target's HP.
Cure Potency: 100
Cure potency is increased to 500 when you are under the effect of Aetherial Mimicry: Healer.
        """
        id = 18303
        name = {'绒绒治疗', 'Pom Cure'}

    class Gobskin(ActionBase):
        """
Creates a barrier around self and all nearby party members that absorbs damage equivalent to a heal of 100 potency.
Duration: 30s
Barrier strength is increased to absorb damage equivalent to a heal of 250 potency when you are under the effect of Aetherial Mimicry: Healer.
Effect cannot be stacked with those of scholar's Galvanize or sage's Eukrasian Diagnosis and Eukrasian Prognosis.
>> 2114, Gobskin, Hardened flesh is absorbing damage.
        """
        id = 18304
        name = {'哥布防御', 'Gobskin'}

    class MagicHammer(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 250 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Lowers intelligence and mind attributes by 10%
Duration: 10s
Additional Effect: Restores 10% of maximum MP
This action does not share a recast timer with any other actions.
        """
        id = 18305
        name = {'魔法锤', 'Magic Hammer'}

    class Avail(ActionBase):
        """
Direct damage intended for you to another party member.
Duration: 12s
Can only be executed when member is within 10 yalms. Does not activate with certain attacks.
This action does not share a recast timer with any other actions.
        """
        id = 18306
        name = {'防御指示', 'Avail'}

    class FrogLegs(ActionBase):
        """
Provoke nearby enemies, placing yourself at the top of their enmity list.
        """
        id = 18307
        name = {'Frog Legs', '蛙腿'}

    class SonicBoom(ActionBase):
        """
Deals wind damage with a potency of 210.
        """
        id = 18308
        name = {'Sonic Boom', '音爆'}

    class Whistle(ActionBase):
        """
Increases the potency of the next physical damage spell cast by 80%.
Duration: 30s
Effect cannot be stacked with Boost.
>> 880, Whistle, Synthesis-related effects granted based on stack size.
        """
        id = 18309
        name = {'Whistle', '口笛'}

    class WhiteKnightsTour(ActionBase):
        """
Deals unaspected damage to all enemies in a straight line before you with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Potency is increased to 400 when enemies are bound. The Bind effect is also removed.
Additional Effect: Slow +20%
Duration: 20s
        """
        id = 18310
        name = {"White Knight's Tour", '白骑士之旅'}

    class BlackKnightsTour(ActionBase):
        """
Deals unaspected damage to all enemies in a straight line before you with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Potency is increased to 400 when enemies are under the effect of Slow. The Slow effect is also removed.
Additional Effect: Bind
Duration: 20s
        """
        id = 18311
        name = {'黑骑士之旅', "Black Knight's Tour"}

    class Level5Death(ActionBase):
        """
KOs all nearby enemies.
Chance of successful attack is low.
Enemy level must be a multiple of 5. Has no effect on enemies whose level is higher than your own.
Shares a recast timer with certain blue magic spells.
        """
        id = 18312
        name = {'Level 5 Death', '5级即死'}

    class Launcher(ActionBase):
        """
Delivers an attack to all nearby enemies randomly dealing 50%, 30%, 20%, or 10% of their HP.
Has no effect on enemies whose level is higher than your own.
        """
        id = 18313
        name = {'Launcher', '火箭炮'}

    class PerpetualRay(ActionBase):
        """
Deals unaspected damage with a potency of 220.
Additional Effect: Stun
Duration: 1s
Ignores target's Stun resistance.
        """
        id = 18314
        name = {'永恒射线', 'Perpetual Ray'}

    class Cactguard(ActionBase):
        """
Reduces target party member's damage taken by 5%.
Duration: 6s
Increases damage reduction to 15% when you are under the effect of Aetherial Mimicry: Tank.
>> 2119, Cactguard, Damage taken is reduced.
        """
        id = 18315
        name = {'仙人盾', 'Cactguard'}

    class RevengeBlast(ActionBase):
        """
Deals physical damage with a potency of 50.
Potency is increased to 500 when your HP is below 20%.
        """
        id = 18316
        name = {'复仇冲击', 'Revenge Blast'}

    class AngelWhisper(ActionBase):
        """
Resurrects target to a weakened state.
This action does not share a recast timer with any other actions.
        """
        id = 18317
        name = {'Angel Whisper', '天使低语'}

    class Exuviation(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 50
Additional Effect: Removes one detrimental effect from all nearby party members
Cure potency is increased to 300 when you are under the effect of Aetherial Mimicry: Healer.
        """
        id = 18318
        name = {'蜕皮', 'Exuviation'}

    class Reflux(ActionBase):
        """
Deals lightning damage with a potency of 220.
Additional Effect: Heavy +40%
Duration: 10s
Ignores target's Heavy resistance.
        """
        id = 18319
        name = {'Reflux', '逆流'}

    class Devour(ActionBase):
        """
Deals unaspected damage with a potency of 250.
Additional Effect: Increases maximum HP by 20%
Duration: 15s
Increases duration to 70s when you are under the effect of Aetherial Mimicry: Tank.
Additional Effect: Restores an amount of own HP equal to damage dealt
This action does not share a recast timer with any other actions.
        """
        id = 18320
        name = {'Devour', '捕食'}

    class CondensedLibra(ActionBase):
        """
Afflicts target with Physical Attenuation, Astral Attenuation, or Umbral Attenuation.
Duration: 30s
Physical Attenuation Effect: Increases damage taken from physical attacks by 5%
Astral Attenuation Effect: Increases damage taken from fire-, wind-, and lightning-aspected attacks by 5%
Umbral Attenuation Effect: Increases damage taken from water-, earth-, and ice-aspected attacks by 5%
Only one of these statuses can be applied to a target at a time.
        """
        id = 18321
        name = {'Condensed Libra', '小侦测'}

    class AetherialMimicry(ActionBase):
        """
Mirror the aetherial properties of your target, granting yourself a beneficial effect corresponding with the target's role.
If target is a tank, grants Aetherial Mimicry: Tank, increasing your defense and augmenting certain blue magic spells.
If target is a DPS, grants Aetherial Mimicry: DPS, increasing critical hit rate and direct hit rate by 20%, as well as augmenting certain blue magic spells.
If target is a healer, grants Aetherial Mimicry: Healer, increasing healing magic potency by 20% and augmenting certain blue magic spells.
Cannot be cast on self. Effect ends upon reuse.
        """
        id = 18322
        name = {'以太复制', 'Aetherial Mimicry'}

    class Surpanakha(ActionBase):
        """
Deals earth damage to all enemies in a cone before you with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Grants Surpanakha's Fury, increasing potency of Surpanakha by 50%
Duration: 3s
Can be stacked up to 3 times.
Maximum Charges: 4
Effect is canceled upon execution of any action other than Surpanakha.
        """
        id = 18323
        name = {'穿甲散弹', 'Surpanakha'}

    class Quasar(ActionBase):
        """
Deals unaspected damage to all nearby enemies with a potency of 300 for the first enemy, and 50% less for all remaining enemies.
Shares a recast timer with certain blue magic spells.
        """
        id = 18324
        name = {'类星体', 'Quasar'}

    class JKick(ActionBase):
        """
Delivers a jumping physical attack to target and all enemies nearby it with a potency of 300 for the first enemy, and 50% less for all remaining enemies.
Cannot be executed while bound.
Shares a recast timer with certain blue magic spells.
        """
        id = 18325
        name = {'正义飞踢', 'J Kick'}

    class AetherialMimicry(ActionBase):
        """
Mirror the aetherial properties of your target, granting yourself a beneficial effect corresponding with the target's role.
If target is a tank, grants Aetherial Mimicry: Tank, increasing your defense and augmenting certain blue magic spells.
If target is a DPS, grants Aetherial Mimicry: DPS, increasing critical hit rate and direct hit rate by 20%, as well as augmenting certain blue magic spells.
If target is a healer, grants Aetherial Mimicry: Healer, increasing healing magic potency by 20% and augmenting certain blue magic spells.
Cannot be cast on self. Effect ends upon reuse.
        """
        id = 19238
        name = {'以太复制', 'Aetherial Mimicry'}

    class AetherialMimicry(ActionBase):
        """
Mirror the aetherial properties of your target, granting yourself a beneficial effect corresponding with the target's role.
If target is a tank, grants Aetherial Mimicry: Tank, increasing your defense and augmenting certain blue magic spells.
If target is a DPS, grants Aetherial Mimicry: DPS, increasing critical hit rate and direct hit rate by 20%, as well as augmenting certain blue magic spells.
If target is a healer, grants Aetherial Mimicry: Healer, increasing healing magic potency by 20% and augmenting certain blue magic spells.
Cannot be cast on self. Effect ends upon reuse.
        """
        id = 19239
        name = {'以太复制', 'Aetherial Mimicry'}

    class AetherialMimicry(ActionBase):
        """
Mirror the aetherial properties of your target, granting yourself a beneficial effect corresponding with the target's role.
If target is a tank, grants Aetherial Mimicry: Tank, increasing your defense and augmenting certain blue magic spells.
If target is a DPS, grants Aetherial Mimicry: DPS, increasing critical hit rate and direct hit rate by 20%, as well as augmenting certain blue magic spells.
If target is a healer, grants Aetherial Mimicry: Healer, increasing healing magic potency by 20% and augmenting certain blue magic spells.
Cannot be cast on self. Effect ends upon reuse.
        """
        id = 19240
        name = {'以太复制', 'Aetherial Mimicry'}

    class TripleTrident(ActionBase):
        """
Delivers a threefold attack, each hit with a potency of 150.
This action does not share a recast timer with any other actions.
        """
        id = 23264
        name = {'渔叉三段', 'Triple Trident'}

    class Tingle(ActionBase):
        """
Deals lightning damage to target and all enemies nearby it with a potency of 100 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Increases the potency of the next physical damage spell cast by 100
Duration: 15s
        """
        id = 23265
        name = {'哔哩哔哩', 'Tingle'}

    class TatamiGaeshi(ActionBase):
        """
Deals unaspected damage to all enemies in a straight line before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Stun
Duration: 3s
        """
        id = 23266
        name = {'Tatami-gaeshi', '掀地板之术'}

    class ColdFog(ActionBase):
        """
Grants Cold Fog to self.
Duration: 5s
Effect changes to Touch of Frost if damage is taken.
Touch of Frost Effect: Action changes from Cold Fog to White Death
Duration: 15s
White Death
Deals ice damage with a potency of 400.
Additional Effect: Deep Freeze
Duration: 10s
Can only be executed while under the effect of Touch of Frost.
>> 2493, Cold Fog, Enveloped in a cold fog. Any damage taken will grant the effect of Touch of Frost.
        """
        id = 23267
        name = {'Cold Fog', '彻骨雾寒'}

    class WhiteDeath(ActionBase):
        """
Deals ice damage with a potency of 400.
Additional Effect: Deep Freeze
Duration: 10s
Can only be executed while under the effect of Touch of Frost.
        """
        id = 23268
        name = {'White Death', '冰雾'}

    class Stotram(ActionBase):
        """
Deals unaspected damage with a potency of 140 to all nearby enemies.
Action effect changes, restoring own HP and the HP of all nearby party members when you are under the effect of Aetherial Mimicry: Healer.
Cure Potency: 300
        """
        id = 23269
        name = {'Stotram', '赞歌'}

    class SaintlyBeam(ActionBase):
        """
Deals unaspected damage with a potency of 100 to target and all enemies nearby it.
Potency increases to 500 when used against undead enemies.
        """
        id = 23270
        name = {'Saintly Beam', '圣光射线'}

    class FeculentFlood(ActionBase):
        """
Deals earth damage to all enemies in a straight line before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
        """
        id = 23271
        name = {'污泥泼洒', 'Feculent Flood'}

    class AngelsSnack(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 400
Additional Effect: Grants healing over time effect when you are under the effect of Aetherial Mimicry: Healer
Cure Potency: 200
Duration: 15s
Shares a recast timer with certain blue magic spells.
>> 2495, Angel's Snack, Regenerating HP over time.
        """
        id = 23272
        name = {"Angel's Snack", '天使的点心'}

    class ChelonianGate(ActionBase):
        """
Summons a chelonian gate, reducing damage taken by 20%.
Duration: 10s
Additional Effect: Grants Auspicious Trance after taking damage equal to 30% of maximum HP
Auspicious Trance Effect: Action changes from Chelonian Gate to Divine Cataract
Chelonian Gate effect ends upon using another action or moving (including facing a different direction).
Auspicious Trance ends upon losing the effect of Chelonian Gate.
Shares a recast timer with certain blue magic spells.
Divine Cataract
Deals water damage to all nearby enemies with a potency of 500 for the first enemy, and 50% less for all remaining enemies.
Potency increases to 1,000 when you are under the effect of Aetherial Mimicry: Tank.
Can only be executed when under the effect of Auspicious Trance.
>> 2496, Chelonian Gate, Damage taken is reduced. Taking a certain amount of damage grants the effect of Auspicious Trance.
        """
        id = 23273
        name = {'Chelonian Gate', '玄结界'}

    class DivineCataract(ActionBase):
        """
Deals water damage to all nearby enemies with a potency of 500 for the first enemy, and 50% less for all remaining enemies.
Potency increases to 1,000 when you are under the effect of Aetherial Mimicry: Tank.
Can only be executed when under the effect of Auspicious Trance.
        """
        id = 23274
        name = {'Divine Cataract', '玄天武水壁'}

    class TheRoseOfDestruction(ActionBase):
        """
Deals unaspected damage with a potency of 400.
Additional Effect: 10-yalm knockback
Shares a recast timer with certain blue magic spells.
        """
        id = 23275
        name = {'斗灵弹', 'The Rose of Destruction'}

    class BasicInstinct(ActionBase):
        """
Increases movement speed by 30%, and healing magic potency and damage dealt by 100%. Also ignores the damage penalty inflicted by Mighty Guard.
Can only be used in duties intended for two or more players while playing alone, while no other party members are in the instance, or when all party members are incapacitated. Effect ends when joined by one or more party members.
>> 2498, Basic Instinct, Movement speed, damage dealt, and healing magic potency are increased. Mighty Guard will not reduce damage dealt while Basic Instinct is in effect.
        """
        id = 23276
        name = {'斗争本能', 'Basic Instinct'}

    class Ultravibration(ActionBase):
        """
KOs all nearby enemies afflicted with Deep Freeze or Petrification. Has no effect on enemies whose level is higher than your own, and certain others.
Shares a recast timer with certain blue magic spells.
        """
        id = 23277
        name = {'超振动', 'Ultravibration'}

    class Blaze(ActionBase):
        """
Deals ice damage to target and all enemies nearby it with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
        """
        id = 23278
        name = {'Blaze', '冰焰'}

    class MustardBomb(ActionBase):
        """
Deals fire damage to target and all enemies nearby it with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Enemies affected by Lightheaded suffer damage over time
Potency: 50
Duration: 15s
        """
        id = 23279
        name = {'芥末爆弹', 'Mustard Bomb'}

    class DragonForce(ActionBase):
        """
Reduces damage taken by 20%.
Duration: 15s
Increases damage reduction to 40% when you are under the effect of Aetherial Mimicry: Tank.
Shares a recast timer with certain blue magic spells.
>> 2500, Dragon Force, Damage taken is reduced.
        """
        id = 23280
        name = {'龙之力', 'Dragon Force'}

    class AetherialSpark(ActionBase):
        """
Deals unaspected damage with a potency of 50 to all enemies in a straight line before you.
Additional Effect: Unaspected damage over time
Potency: 50
Duration: 15s
        """
        id = 23281
        name = {'以太火花', 'Aetherial Spark'}

    class HydroPull(ActionBase):
        """
Deals water damage to all nearby enemies with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Draw-in
        """
        id = 23282
        name = {'Hydro Pull', '水力吸引'}

    class MaledictionOfWater(ActionBase):
        """
Deals water damage to all enemies in a straight line before you with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: 10-yalm knockback to all enemies and party members in range
Cannot be used outside of combat or when target is suffering from certain enfeeblements.
        """
        id = 23283
        name = {'水脉诅咒', 'Malediction of Water'}

    class ChocoMeteor(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 200 for the first enemy, and 50% less for all remaining enemies.
Potency increases to 300 when partied with your personal chocobo.
        """
        id = 23284
        name = {'Choco Meteor', '陆行鸟陨石'}

    class MatraMagic(ActionBase):
        """
Deals an unaspected eightfold attack, each hit with a potency of 50.
Potency is increased to 100 when you are under the effect of Aetherial Mimicry: DPS.
Shares a recast timer with certain blue magic spells.
        """
        id = 23285
        name = {'Matra Magic', '马特拉魔术'}

    class PeripheralSynthesis(ActionBase):
        """
Deals physical damage to all enemies in a straight line before you with a potency of 220 for the first enemy, and 50% less for all remaining enemies.
Potency increased to 400 when target becomes afflicted with Lightheaded.
Additional Effect: Inflicts Lightheaded
Duration: 5s
Repeated use of this action in a short period will reduce the additional effect's duration, eventually rendering targets immune to Lightheaded.
        """
        id = 23286
        name = {'Peripheral Synthesis', '生成外设'}

    class BothEnds(ActionBase):
        """
Deals unaspected damage with a potency of 600 to all nearby enemies.
Shares a recast timer with certain blue magic spells.
        """
        id = 23287
        name = {'Both Ends', '如意大旋风'}

    class PhantomFlurry(ActionBase):
        """
Deals unaspected damage over time with a potency of 200 to all enemies in a cone before you.
Duration: 5s
Executing Phantom Flurry again before its effect expires deals unaspected damage to all enemies in a cone before you with a potency of 600 for the first enemy, and 50% less for all remaining enemies.
Effect ends upon using an action other than Phantom Flurry or moving (including facing a different direction).
>> 2502, Phantom Flurry, Executing Phantom Flurry.
        """
        id = 23288
        name = {'Phantom Flurry', '鬼宿脚'}

    class PhantomFlurry(ActionBase):
        """
Deals unaspected damage over time with a potency of 200 to all enemies in a cone before you.
Duration: 5s
Executing Phantom Flurry again before its effect expires deals unaspected damage to all enemies in a cone before you with a potency of 600 for the first enemy, and 50% less for all remaining enemies.
Effect ends upon using an action other than Phantom Flurry or moving (including facing a different direction).
>> 2502, Phantom Flurry, Executing Phantom Flurry.
        """
        id = 23289
        name = {'Phantom Flurry', '鬼宿脚'}

    class Nightbloom(ActionBase):
        """
Deals unaspected damage to all nearby enemies with a potency of 400 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Unaspected damage over time
Potency: 75
Duration: 60s
        """
        id = 23290
        name = {'Nightbloom', '月下彼岸花'}

    class Stotram(ActionBase):
        """
Deals unaspected damage with a potency of 140 to all nearby enemies.
 Action effect changes, restoring own HP and the HP of all nearby party members when you are under the effect of Aetherial Mimicry: Healer.
 Cure Potency: 300
        """
        id = 23416
        name = {'Stotram', '赞歌'}
