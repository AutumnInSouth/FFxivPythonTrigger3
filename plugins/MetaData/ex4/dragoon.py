from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class TrueThrust(ActionBase):
        """
        Delivers an attack with a potency of (source.job==22?(source.level>=76?290:210):210).(source.job==22?(source.level>=76? ※Action changes to Raiden Thrust when Raiden Thrust Ready.:):)
        """
        id = 75
        name = {"True Thrust", "精准刺"}

    class VorpalThrust(ActionBase):
        """
        Delivers an attack with a potency of (source.job==22?(source.level>=76?140:100):100). Combo Action: True Thrust Combo Potency: (source.job==22?(source.level>=76?350:310):310)
        """
        id = 78
        name = {"Vorpal Thrust", "贯通刺"}
        combo_action = 75

    class LifeSurge(ActionBase):
        """
        Ensures critical damage for first weaponskill used while Life Surge is active. Duration: 5s Effect cannot be applied to damage over time. Additional Effect: Absorbs a portion of damage dealt as HP
        116, Life Surge, Life Surge, Next weaponskill will result in a critical hit with a portion of the resulting damage being absorbed as HP.
        2175, Life Surge, Life Surge, Next weaponskill will deal increased damage.
        """
        id = 83
        name = {"Life Surge", "龙剑"}

    class FullThrust(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Vorpal Thrust Combo Potency: 530(source.level>=56?(source.job==22? Combo Bonus: Grants Sharper Fang and Claw if under the effect of (source.level>=70?(source.job==22?Blood of the Dragon or Life of the Dragon:Blood of the Dragon):Blood of the Dragon) Duration: 10s:):)
        """
        id = 84
        name = {"Full Thrust", "直刺"}
        combo_action = 78

    class LanceCharge(ActionBase):
        """
        Increases damage dealt by 15%. Duration: 20s
        1864, Lance Charge, Lance Charge, Damage dealt is increased.
        """
        id = 85
        name = {"Lance Charge", "猛枪"}

    class DoomSpike(ActionBase):
        """
        Delivers an attack with a potency of 170 to all enemies in a straight line before you.
        """
        id = 86
        name = {"Doom Spike", "死天枪"}

    class Disembowel(ActionBase):
        """
        Delivers an attack with a potency of (source.job==22?(source.level>=76?150:100):100). Combo Action: True Thrust Combo Potency: (source.job==22?(source.level>=76?320:270):270) Combo Bonus: Increases damage dealt by 10% Duration: 30s
        121, Disembowel, Disembowel, Piercing resistance is reduced.
        1914, Disembowel, Disembowel, Damage dealt is increased.
        """
        id = 87
        name = {"Disembowel", "开膛枪"}
        combo_action = 75

    class ChaosThrust(ActionBase):
        """
        Delivers an attack with a potency of 100. 140 when executed from a target's rear. Combo Action: Disembowel Combo Potency: 290 Rear Combo Potency: 330 Combo Bonus: Damage over time Potency: 50 Duration: 24s(source.level>=58?(source.job==22? Combo Bonus: Grants Enhanced Wheeling Thrust if under the effect of (source.level>=70?(source.job==22?Blood of the Dragon or Life of the Dragon:Blood of the Dragon):Blood of the Dragon) Duration: 10s:):)
        118, Chaos Thrust, Chaos Thrust, Wounds are bleeding, causing damage over time.
        1312, Chaos Thrust, Chaos Thrust, Sustaining damage over time, as well as increased damage from target who executed <UIForeground(500)><UIGlow(501)>Chaos Thrust</UIGlow></UIForeground>.
        """
        id = 88
        name = {"Chaos Thrust", "樱花怒放"}
        combo_action = 87

    class PiercingTalon(ActionBase):
        """
        Delivers a ranged attack with a potency of 150.
        """
        id = 90
        name = {"Piercing Talon", "贯穿尖"}

    class Jump(ActionBase):
        """
        Delivers a jumping attack with a potency of 310. Returns you to your original position after the attack is made. (source.level>=68?(source.job==22?Additional Effect: Grants Dive Ready Duration: 15s :):)Cannot be executed while bound.
        """
        id = 92
        name = {"Jump", "跳跃"}

    class ElusiveJump(ActionBase):
        """
        Executes a jump to a location 15 yalms behind you. Cannot be executed while bound.
        """
        id = 94
        name = {"Elusive Jump", "回避跳跃"}

    class SpineshatterDive(ActionBase):
        """
        Delivers a jumping attack with a potency of 240. Cannot be executed while bound.
        """
        id = 95
        name = {"Spineshatter Dive", "破碎冲"}

    class DragonfireDive(ActionBase):
        """
        Delivers a jumping fire-based attack with a potency of 380 to target and all enemies nearby it. Cannot be executed while bound.
        """
        id = 96
        name = {"Dragonfire Dive", "龙炎冲"}

    class BloodOfTheDragon(ActionBase):
        """
        (source.job==22?(source.level>=74?Increases potency of High Jump and Spineshatter Dive by 30%. Duration: (source.job==22?(source.level>=78?30:20):20)s:Increases potency of Jump and Spineshatter Dive by 30%. Duration: (source.job==22?(source.level>=78?30:20):20)s):Increases potency of Jump and Spineshatter Dive by 30%. Duration: (source.job==22?(source.level>=78?30:20):20)s)(source.job==22?(source.level>=56?(source.level>=58? Additional Effect: Grants Sharper Fang and Claw upon successfully executing Full Thrust, or Enhanced Wheeling Thrust upon successfully executing Chaos Thrust Duration: 10s Effects end upon use or upon using a weaponskill other than Fang and Claw or Wheeling Thrust.: Additional Effect: Grants Sharper Fang and Claw upon successfully executing Full Thrust Duration: 10s Effect ends upon use or upon using a weaponskill other than Fang and Claw.):):)(source.level>=70?(source.job==22? Cannot be executed while under the effect of Life of the Dragon.:):)
        736, Blood of the Dragon, Blood of the Dragon, Potency of <UIForeground(500)><UIGlow(501)>Jump</UIGlow></UIForeground> and <UIForeground(500)><UIGlow(501)>Spineshatter Dive</UIGlow></UIForeground> are increased.
        """
        id = 3553
        name = {"Blood of the Dragon", "苍天龙血"}

    class FangAndClaw(ActionBase):
        """
        Delivers an attack with a potency of 340. 380 when executed from a target's flank. Can only be executed while under the effects of Sharper Fang and Claw (source.level>=70?(source.job==22?and either Blood of the Dragon or Life of the Dragon:and Blood of the Dragon):and Blood of the Dragon). Additional Effect: Extends Blood of the Dragon duration by 10s to a maximum of 30s
        """
        id = 3554
        name = {"Fang and Claw", "龙牙龙爪"}

    class Geirskogul(ActionBase):
        """
        Delivers an attack with a potency of 300 to all enemies in a straight line before you. Can only be executed while under the effect of Blood of the Dragon.(source.level>=70?(source.job==22? Additional Effect: Changes Blood of the Dragon to Life of the Dragon while under the full gaze of the first brood ※Action changes to Nastrond while under the effect of Life of the Dragon.:):)
        """
        id = 3555
        name = {"Geirskogul", "武神枪"}

    class WheelingThrust(ActionBase):
        """
        Delivers an attack with a potency of 340. 380 when executed from a target's rear. Can only be executed while under the effects of Enhanced Wheeling Thrust (source.level>=70?(source.job==22?and either Blood of the Dragon or Life of the Dragon:and Blood of the Dragon):and Blood of the Dragon). Additional Effect: Extends Blood of the Dragon duration by 10s to a maximum of 30s
        """
        id = 3556
        name = {"Wheeling Thrust", "龙尾大回旋"}

    class BattleLitany(ActionBase):
        """
        Increases critical hit rate of self and nearby party members by 10%. Duration: 20s
        786, Battle Litany, Battle Litany, Critical hit rate is increased.
        1414, Battle Litany, Battle Litany, Damage dealt is increased.
        """
        id = 3557
        name = {"Battle Litany", "战斗连祷"}

    class SonicThrust(ActionBase):
        """
        Delivers an attack with a potency of 100 to all enemies in a straight line before you. Combo Action: Doom Spike Combo Potency: 200 Combo Bonus: Extends Blood of the Dragon duration by 10s to a maximum of 30s
        """
        id = 7397
        name = {"Sonic Thrust", "音速刺"}
        combo_action = 86

    class DragonSight(ActionBase):
        """
        Grants Right Eye to self, increasing damage dealt by 10%. Also grants target party member Left Eye, increasing damage dealt by 5% as long as target remains within 12 yalms. Duration: 20s
        """
        id = 7398
        name = {"Dragon Sight", "巨龙视线"}

    class MirageDive(ActionBase):
        """
        Delivers an attack with a potency of 300. (source.level>=70?(source.job==22?Additional Effect: Strengthens the gaze of your Dragon Gauge by 1 if under the effect of Blood of the Dragon or Life of the Dragon :):)Can only be executed when Dive Ready.
        """
        id = 7399
        name = {"Mirage Dive", "幻象冲"}

    class Nastrond(ActionBase):
        """
        Delivers an attack with a potency of 400 to all enemies in a straight line before you. Can only be executed while under the effect of Life of the Dragon. ※This action cannot be assigned to a hotbar.
        """
        id = 7400
        name = {"Nastrond", "死者之岸"}

    class CoerthanTorment(ActionBase):
        """
        Delivers an attack with a potency of 100 to all enemies in a straight line before you. Combo Action: Sonic Thrust Combo Potency: 230 Combo Bonus: Extends Blood of the Dragon duration by 10s to a maximum of 30s
        """
        id = 16477
        name = {"Coerthan Torment", "山境酷刑"}
        combo_action = 7397

    class HighJump(ActionBase):
        """
        Delivers a jumping attack with a potency of 400. Returns you to your original position after the attack is made. Additional Effect: Grants Dive Ready Duration: 15s Cannot be executed while bound.
        """
        id = 16478
        name = {"High Jump", "高跳"}

    class RaidenThrust(ActionBase):
        """
        Delivers an attack with a potency of 330. Can only be executed when Raiden Thrust Ready. ※This action cannot be assigned to a hotbar.
        """
        id = 16479
        name = {"Raiden Thrust", "龙眼雷电"}

    class Stardiver(ActionBase):
        """
        Delivers a jumping fire-based attack to target and all enemies nearby it with a potency of 600 for the first enemy, and 30% less for all remaining enemies. Can only be executed while under the effect of Life of the Dragon. Cannot be executed while bound.
        """
        id = 16480
        name = {"Stardiver", "坠星冲"}
