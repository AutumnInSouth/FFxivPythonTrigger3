from ..base import *


class Actions:

    class HeavySwing(ActionBase):
        """
Delivers an attack with a potency of (source.job==21?(source.level>=84?200:150):150).
        """
        id = 31
        name = {'Heavy Swing', '重劈'}

    class Maim(ActionBase):
        """
Delivers an attack with a potency of (source.job==21?(source.level>=84?130:100):100).
Combo Action: Heavy Swing
Combo Potency: (source.job==21?(source.level>=84?280:250):250)(source.level>=30?(source.job==21?(source.job==21?(source.level>=35?
Combo Bonus: Increases Beast Gauge by 10:):):):)
>> 85, Maim, Damage dealt is increased.
        """
        id = 37
        name = {'Maim', '凶残裂'}
        combo_action = 31

    class Berserk(ActionBase):
        """
Grants 3 stacks of Berserk, each stack guaranteeing weaponskill attacks are critical and direct hits.
Duration: 15s(source.level>=40?(source.job==3?
Additional Effect: Extends Surging Tempest duration by 10s to a maximum of 60s:(source.job==21?
Additional Effect: Extends Surging Tempest duration by 10s to a maximum of 60s:)):)
>> 86, Berserk, All weaponskill attacks are both critical and direct hits.
        """
        id = 38
        name = {'Berserk', '狂暴'}

    class Overpower(ActionBase):
        """
Delivers an attack with a potency of 110 to all enemies in a cone before you.
        """
        id = 41
        name = {'Overpower', '超压斧'}

    class Defiance(ActionBase):
        """
Significantly increases enmity generation.
Effect ends upon reuse.
>> 91, Defiance, Enmity is increased.
>> 1396, Defiance, Damage dealt and taken are reduced.
        """
        id = 48
        name = {'Defiance', '守护'}

    class Tomahawk(ActionBase):
        """
Delivers a ranged attack with a potency of 100.
Additional Effect: Increased enmity
        """
        id = 46
        name = {'Tomahawk', '飞斧'}

    class StormsPath(ActionBase):
        """
Delivers an attack with a potency of (source.job==21?(source.level>=84?120:100):100).
Combo Action: Maim
Combo Potency: (source.job==21?(source.level>=84?400:380):380)
Combo Bonus: Restores own HP
Cure Potency: 250(source.level>=30?(source.job==21?(source.job==21?(source.level>=35?
Combo Bonus: Increases Beast Gauge by 20:):):):)
>> 408, Storm's Path, Damage dealt is reduced.
        """
        id = 42
        name = {'暴风斩', "Storm's Path"}
        combo_action = 37

    class ThrillOfBattle(ActionBase):
        """
Increases maximum HP by 20% and restores the amount increased.
(source.job==21?(source.level>=78?Additional Effect: Increases HP recovery via healing actions on self by 20%
:):)Duration: 10s
>> 87, Thrill of Battle, Maximum HP is increased.
Enhanced Thrill of Battle Effect: HP recovery via healing actions is increased.
        """
        id = 40
        name = {'战栗', 'Thrill of Battle'}

    class InnerBeast(ActionBase):
        """
Delivers an attack with a potency of 330.
Beast Gauge Cost: 50
>> 411, Inner Beast, Damage taken is reduced.
>> 1398, Inner Beast, Damage taken is reduced.
        """
        id = 49
        name = {'原初之魂', 'Inner Beast'}

    class Vengeance(ActionBase):
        """
Reduces damage taken by 30% and delivers an attack with a potency of 55 every time you suffer physical damage.
Duration: 15s
>> 89, Vengeance, Inflicting a portion of sustained damage back to its source.
        """
        id = 44
        name = {'复仇', 'Vengeance'}

    class MythrilTempest(ActionBase):
        """
Delivers an attack with a potency of 100 to all nearby enemies.
Combo Action: Overpower
Combo Potency: 150
Combo Bonus: Grants Surging Tempest, increasing damage dealt by 10%
Duration: 30s
Extends Surging Tempest duration by 30s to a maximum of 60s.(source.job==21?(source.level>=74?
Combo Bonus: Increases Beast Gauge by 20:):)
        """
        id = 16462
        name = {'Mythril Tempest', '秘银暴风'}
        combo_action = 41

    class Holmgang(ActionBase):
        """
Brace yourself for an enemy onslaught, preventing most attacks from reducing your HP to less than 1.
Duration: 10s
When a target is selected, halts their movement with chains.
>> 1304, Holmgang, Unable to move until effect fades. Most attacks cannot reduce your HP to less than 1.
>> 1305, Holmgang, Unable to move until effect fades.
>> 88, Holmgang, Unable to move until effect fades.
>> 409, Holmgang, Most attacks cannot reduce your HP to less than 1.
        """
        id = 43
        name = {'死斗', 'Holmgang'}

    class SteelCyclone(ActionBase):
        """
Delivers an attack with a potency of 170 to all nearby enemies.
Beast Gauge Cost: 50
        """
        id = 51
        name = {'Steel Cyclone', '钢铁旋风'}

    class StormsEye(ActionBase):
        """
Delivers an attack with a potency of (source.job==21?(source.level>=84?120:100):100).
Combo Action: Maim
Combo Potency: (source.job==21?(source.level>=84?400:380):380)
Combo Bonus: Grants Surging Tempest, increasing damage dealt by 10%
Duration: 30s
Extends Surging Tempest duration by 30s to a maximum of 60s.(source.level>=30?(source.job==21?
Combo Bonus: Increases Beast Gauge by 10:):)
>> 90, Storm's Eye, Damage dealt is increased.
        """
        id = 45
        name = {"Storm's Eye", '暴风碎'}
        combo_action = 37

    class Infuriate(ActionBase):
        """
Increases Beast Gauge by 50.
(source.job==21?(source.level>=72?Additional Effect: Grants Nascent Chaos
Duration: 30s
:):)Maximum Charges: 2
Can only be executed while in combat.
        """
        id = 52
        name = {'Infuriate', '战嚎'}

    class FellCleave(ActionBase):
        """
Delivers an attack with a potency of 460.
Beast Gauge Cost: 50(source.job==21?(source.level>=80?
※Action changes to Inner Chaos while under the effect of Nascent Chaos.:):)
        """
        id = 3549
        name = {'裂石飞环', 'Fell Cleave'}

    class RawIntuition(ActionBase):
        """
Reduces damage taken by 10%.
Duration: 6s
Additional Effect: Restores HP with each weaponskill successfully delivered
Cure Potency: 400(source.job==21?(source.level>=76?
Shares a recast timer with Nascent Flash.:):)
>> 735, Raw Intuition, Damage taken is reduced and HP is restored with each weaponskill successfully delivered.
        """
        id = 3551
        name = {'Raw Intuition', '原初的直觉'}

    class Equilibrium(ActionBase):
        """
Restores own HP.
Cure Potency: 1,200(source.job==21?(source.level>=84?
Additional Effect: Gradually restores HP
Cure Potency: 200
Duration: 15s:):)
>> 2681, Equilibrium, Regenerating HP over time.
        """
        id = 3552
        name = {'Equilibrium', '泰然自若'}

    class Decimate(ActionBase):
        """
Delivers an attack to all nearby enemies with a potency of 200.
Beast Gauge Cost: 50(source.job==21?(source.level>=72?
※Action changes to Chaotic Cyclone while under the effect of Nascent Chaos.:):)
        """
        id = 3550
        name = {'Decimate', '地毁人亡'}

    class Onslaught(ActionBase):
        """
Rushes target and delivers an attack with a potency of 150.
Maximum Charges: (source.job==21?(source.level>=88?3:2):2)
Cannot be executed while bound.
        """
        id = 7386
        name = {'Onslaught', '猛攻'}

    class Upheaval(ActionBase):
        """
Delivers an attack with a potency of 350.(source.job==21?(source.level>=86?
Shares a recast timer with Orogeny.:):)
        """
        id = 7387
        name = {'动乱', 'Upheaval'}

    class ShakeItOff(ActionBase):
        """
Creates a barrier around self and all nearby party members that absorbs damage totaling 15% of maximum HP.
Dispels Thrill of Battle, Vengeance, and (source.job==21?(source.level>=82?Bloodwhetting:Raw Intuition):Raw Intuition), increasing damage absorbed by 2% for each effect removed. 
Duration: 15s(source.job==21?(source.level>=76?
Additional Effect: Restores own HP and the HP of all nearby party members
Cure Potency: 300:):)
>> 1457, Shake It Off, A highly effective defensive maneuver is nullifying damage.
>> 1993, Shake It Off, A barrier is preventing damage.
        """
        id = 7388
        name = {'摆脱', 'Shake It Off'}

    class InnerRelease(ActionBase):
        """
Grants 3 stacks of Inner Release, each stack allowing the use of Beast Gauge actions without cost and guaranteeing that all attacks are critical and direct hits.
Additional Effect: Nullifies Stun, Sleep, Bind, Heavy, and most knockback and draw-in effects
Duration: 15s
Additional Effect: Extends Surging Tempest duration by 10s to a maximum of 60s(source.job==21?(source.level>=90?
Additional Effect: Grants Primal Rend Ready
Duration: 30s:):)
>> 1177, Inner Release, Beast Gauge consumption is reduced to 0. All weaponskill attacks are both critical and direct hits. All Stun, Sleep, Bind, Heavy, and most knockback and draw-in effects are nullified.
>> 1303, Inner Release, Beast Gauge consumption is reduced to 0. All Stun, Sleep, Bind, Heavy, Silence, knockback, and draw-in effects are nullified.
        """
        id = 7389
        name = {'Inner Release', '原初的解放'}

    class ChaoticCyclone(ActionBase):
        """
Delivers a critical direct hit with a potency of 320 to all nearby enemies.
Additional Effect: Reduces the recast time of Infuriate by 5 seconds
Beast Gauge Cost: 50
Can only be executed while under the effect of Nascent Chaos. Effect fades upon execution.
※This action cannot be assigned to a hotbar.
>> 2078, Chaotic Cyclone, Damage taken is increased.
        """
        id = 16463
        name = {'Chaotic Cyclone', '混沌旋风'}

    class NascentFlash(ActionBase):
        """
Grants Nascent Flash to self and Nascent Glint to target party member.
Nascent Flash Effect: Restores HP with each weaponskill successfully delivered
Cure Potency: 400
Nascent Glint Effect: Restores HP equaling 100% of that recovered by Nascent Flash while also reducing damage taken by 10%
Duration: (source.job==21?(source.level>=82?8:6):6)s
(source.job==21?(source.level>=82?Additional Effect: Grants Stem the Flow to target, reducing damage taken by 10%
Duration: 4s
Additional Effect: Grants Stem the Tide to target, nullifying damage equivalent to a heal of 400 potency
Duration: 20s
:):)Shares a recast timer with (source.job==21?(source.level>=82?Bloodwhetting:Raw Intuition):Raw Intuition).
>> 1857, Nascent Flash, Restoring HP with each weaponskill successfully delivered.
>> 2227, Nascent Flash, Absorbing HP with each physical attack delivered.
>> 2061, Nascent Flash, Absorbing HP with each physical attack delivered. Damage taken is also reduced.
        """
        id = 16464
        name = {'原初的勇猛', 'Nascent Flash'}

    class InnerChaos(ActionBase):
        """
Delivers a critical direct hit with a potency of 650.
Additional Effect: Reduces the recast time of Infuriate by 5 seconds
Beast Gauge Cost: 50
Can only be executed while under the effect of Nascent Chaos. Effect fades upon execution.
※This action cannot be assigned to a hotbar.
>> 2077, Inner Chaos, Damage taken is increased.
        """
        id = 16465
        name = {'狂魂', 'Inner Chaos'}

    class Bloodwhetting(ActionBase):
        """
Reduces damage taken by 10%.
Duration: 8s
Additional Effect: Restores HP with each weaponskill successfully delivered
Cure Potency: 400
Additional Effect: Grants Stem the Flow
Stem the Flow Effect: Reduces damage taken by 10%
Duration: 4s
Additional Effect: Grants Stem the Tide
Stem the Tide Effect: Creates a barrier around self that absorbs damage equivalent to a heal of 400 potency
Duration: 20s
Shares a recast timer with Nascent Flash.
>> 2678, Bloodwhetting, Damage taken is reduced and HP is restored with each weaponskill successfully delivered.
        """
        id = 25751
        name = {'Bloodwhetting'}

    class Orogeny(ActionBase):
        """
Delivers an attack with a potency of 150 to all nearby enemies.
Shares a recast timer with Upheaval.
        """
        id = 25752
        name = {'Orogeny'}

    class PrimalRend(ActionBase):
        """
Delivers a critical direct hit to target and all enemies nearby it with a potency of 700 for the first enemy, and 70% less for all remaining enemies.
Stacks of Inner Release are not consumed upon execution.
Can only be executed while under the effect of Primal Rend Ready, granted by Inner Release.
Cannot be executed while bound.
        """
        id = 25753
        name = {'Primal Rend'}
