from ..base import *


class Actions:

    class TrueThrust(ActionBase):
        """
Delivers an attack with a potency of (source.job==22?(source.level>=76?230:170):170).(source.job==22?(source.level>=76?
※Action changes to Raiden Thrust while under the effect of Draconian Fire.:):)
        """
        id = 75
        name = {'True Thrust', '精准刺'}

    class VorpalThrust(ActionBase):
        """
Delivers an attack with a potency of (source.job==22?(source.level>=76?130:100):100).
Combo Action: True Thrust
Combo Potency: (source.job==22?(source.level>=76?280:250):250)
        """
        id = 78
        name = {'贯通刺', 'Vorpal Thrust'}
        combo_action = 75

    class LifeSurge(ActionBase):
        """
Ensures critical damage for first weaponskill used while Life Surge is active.
Duration: 5s
Effect cannot be applied to damage over time.
Additional Effect: Absorbs a portion of damage dealt as HP(source.job==22?(source.level>=88?
Maximum Charges: 2:):)
    116, Life Surge, Next weaponskill will result in a critical hit with a portion of the resulting damage being absorbed as HP.
    2175, Life Surge, Next weaponskill will deal increased damage.
        """
        id = 83
        name = {'龙剑', 'Life Surge'}

    class PiercingTalon(ActionBase):
        """
Delivers a ranged attack with a potency of 150.
        """
        id = 90
        name = {'Piercing Talon', '贯穿尖'}

    class Disembowel(ActionBase):
        """
Delivers an attack with a potency of (source.job==22?(source.level>=76?140:100):100).
Combo Action: True Thrust
Combo Potency: (source.job==22?(source.level>=76?250:210):210)
Combo Bonus: Grants Power Surge
Power Surge Effect: Increases damage dealt by 10%
Duration: 30s
    121, Disembowel, Piercing resistance is reduced.
    1914, Disembowel, Damage dealt is increased.
        """
        id = 87
        name = {'Disembowel', '开膛枪'}
        combo_action = 75

    class FullThrust(ActionBase):
        """
Delivers an attack with a potency of 100.
Combo Action: Vorpal Thrust
Combo Potency: 400(source.level>=56?(source.job==22?
Combo Bonus: Grants Sharper Fang and Claw
Duration: 30s
Effect of Sharper Fang and Claw ends upon execution of any melee weaponskill.:):)
        """
        id = 84
        name = {'直刺', 'Full Thrust'}
        combo_action = 78

    class LanceCharge(ActionBase):
        """
Increases damage dealt by 10%.
Duration: 20s
    1864, Lance Charge, Damage dealt is increased.
        """
        id = 85
        name = {'猛枪', 'Lance Charge'}

    class Jump(ActionBase):
        """
Delivers a jumping attack with a potency of (source.job==22?(source.level>=54?320:250):250). Returns you to your original position after the attack is made.
(source.level>=68?(source.job==22?Additional Effect: Grants Dive Ready
Duration: 15s
:):)Cannot be executed while bound.
        """
        id = 92
        name = {'跳跃', 'Jump'}

    class ElusiveJump(ActionBase):
        """
Executes a jump to a location 15 yalms behind you.
Cannot be executed while bound.
        """
        id = 94
        name = {'回避跳跃', 'Elusive Jump'}

    class DoomSpike(ActionBase):
        """
Delivers an attack with a potency of 110 to all enemies in a straight line before you.(source.job==22?(source.level>=82?
※Action changes to Draconian Fury when under the effect of Draconian Fire.:):)
        """
        id = 86
        name = {'死天枪', 'Doom Spike'}

    class SpineshatterDive(ActionBase):
        """
Delivers a jumping attack with a potency of (source.job==22?(source.level>=54?250:190):190).
(source.job==22?(source.level>=84?Maximum Charges: 2
:):)Cannot be executed while bound.
        """
        id = 95
        name = {'Spineshatter Dive', '破碎冲'}

    class ChaosThrust(ActionBase):
        """
Delivers an attack with a potency of 100.
140 when executed from a target's rear.
Combo Action: Disembowel
Combo Potency: 220
Rear Combo Potency: 260
Combo Bonus: Damage over time
Potency: 40
Duration: 24s(source.level>=58?(source.job==22?
Combo Bonus: Grants Enhanced Wheeling Thrust
Duration: 30s
Effect of Enhanced Wheeling Thrust ends upon execution of any melee weaponskill.:):)
    1312, Chaos Thrust, Sustaining damage over time, as well as increased damage from target who executed <UIForeground(500)><UIGlow(501)>Chaos Thrust</UIGlow></UIForeground>.
    118, Chaos Thrust, Wounds are bleeding, causing damage over time.
        """
        id = 88
        name = {'Chaos Thrust', '樱花怒放'}
        combo_action = 87

    class DragonfireDive(ActionBase):
        """
Delivers a jumping fire-based attack with a potency of 300 to target and all enemies nearby it.
Cannot be executed while bound.
        """
        id = 96
        name = {'龙炎冲', 'Dragonfire Dive'}

    class BattleLitany(ActionBase):
        """
Increases critical hit rate of self and nearby party members by 10%.
Duration: 15s
    786, Battle Litany, Critical hit rate is increased.
    1414, Battle Litany, Damage dealt is increased.
        """
        id = 3557
        name = {'战斗连祷', 'Battle Litany'}

    class BloodOfTheDragon(ActionBase):
        """
(source.job==22?(source.level>=74?Increases potency of High Jump and Spineshatter Dive by 30%.
Duration: (source.job==22?(source.level>=54?30:20):20)s:Increases potency of Jump and Spineshatter Dive by 30%.
Duration: (source.job==22?(source.level>=54?30:20):20)s):Increases potency of Jump and Spineshatter Dive by 30%.
Duration: (source.job==22?(source.level>=54?30:20):20)s)(source.job==22?(source.level>=56?(source.level>=58?
Additional Effect: Grants Sharper Fang and Claw upon successfully executing Full Thrust, or Enhanced Wheeling Thrust upon successfully executing Chaos Thrust
Duration: 10s
Effects end upon use or upon using a weaponskill other than Fang and Claw or Wheeling Thrust.:
Additional Effect: Grants Sharper Fang and Claw upon successfully executing Full Thrust
Duration: 10s
Effect ends upon use or upon using a weaponskill other than Fang and Claw.):):)(source.level>=70?(source.job==22?
Cannot be executed while under the effect of Life of the Dragon.:):)
    736, Blood of the Dragon, Potency of <UIForeground(500)><UIGlow(501)>Jump</UIGlow></UIForeground> and <UIForeground(500)><UIGlow(501)>Spineshatter Dive</UIGlow></UIForeground> are increased.
        """
        id = 3553
        name = {'苍天龙血', 'Blood of the Dragon'}

    class FangAndClaw(ActionBase):
        """
Delivers an attack with a potency of 260.
300 when executed from a target's flank.
Can only be executed while under the effect of Sharper Fang and Claw.
        """
        id = 3554
        name = {'龙牙龙爪', 'Fang and Claw'}

    class WheelingThrust(ActionBase):
        """
Delivers an attack with a potency of 260.
300 when executed from a target's rear.
Can only be executed while under the effect of Enhanced Wheeling Thrust.
        """
        id = 3556
        name = {'龙尾大回旋', 'Wheeling Thrust'}

    class Geirskogul(ActionBase):
        """
Delivers an attack to all enemies in a straight line before you with a potency of (source.job==22?(source.level>=90?250:200):200) for the first enemy, and 30% less for all remaining enemies.(source.level>=70?(source.job==22?
Additional Effect: Grants Life of the Dragon while under the full gaze of the first brood
※Action changes to Nastrond while under the effect of Life of the Dragon.:):)
        """
        id = 3555
        name = {'Geirskogul', '武神枪'}

    class SonicThrust(ActionBase):
        """
Delivers an attack with a potency of 100 to all enemies in a straight line before you.
Combo Action: Doom Spike
Combo Potency: 120
Combo Bonus: Grants Power Surge
Power Surge Effect: Increases damage dealt by 10%
Duration: 30s
        """
        id = 7397
        name = {'音速刺', 'Sonic Thrust'}
        combo_action = 86

    class DragonSight(ActionBase):
        """
Grants Right Eye to self, increasing damage dealt by 10%. Also grants target party member Left Eye, increasing damage dealt by 5% as long as target remains within 12 yalms.
Duration: 20s
        """
        id = 7398
        name = {'Dragon Sight', '巨龙视线'}

    class MirageDive(ActionBase):
        """
Delivers an attack with a potency of 200.
(source.level>=70?(source.job==22?Additional Effect: Strengthens the gaze of your Dragon Gauge by 1
:):)Can only be executed when Dive Ready.
        """
        id = 7399
        name = {'Mirage Dive', '幻象冲'}

    class Nastrond(ActionBase):
        """
Delivers an attack to all enemies in a straight line before you with a potency of (source.job==22?(source.level>=90?350:300):300) for the first enemy, and 30% less for all remaining enemies.
Can only be executed while under the effect of Life of the Dragon.
※This action cannot be assigned to a hotbar.
        """
        id = 7400
        name = {'死者之岸', 'Nastrond'}

    class CoerthanTorment(ActionBase):
        """
Delivers an attack with a potency of 100 to all enemies in a straight line before you.
Combo Action: Sonic Thrust
Combo Potency: 150(source.job==22?(source.level>=82?
Combo Bonus: Grants Draconian Fire
Duration: 30s:):)
        """
        id = 16477
        name = {'Coerthan Torment', '山境酷刑'}
        combo_action = 7397

    class HighJump(ActionBase):
        """
Delivers a jumping attack with a potency of 400. Returns you to your original position after the attack is made.
Additional Effect: Grants Dive Ready
Duration: 15s
Cannot be executed while bound.
        """
        id = 16478
        name = {'High Jump', '高跳'}

    class RaidenThrust(ActionBase):
        """
Delivers an attack with a potency of 260.
(source.job==22?(source.level>=90?Additional Effect: Sharpens the Firstminds' Focus by 1
:):)Can only be executed while under the effect of Draconian Fire.
※This action cannot be assigned to a hotbar.
        """
        id = 16479
        name = {'龙眼雷电', 'Raiden Thrust'}

    class Stardiver(ActionBase):
        """
Delivers a jumping fire-based attack to target and all enemies nearby it with a potency of 500 for the first enemy, and 30% less for all remaining enemies.
Can only be executed while under the effect of Life of the Dragon.
Cannot be executed while bound.
        """
        id = 16480
        name = {'坠星冲', 'Stardiver'}
