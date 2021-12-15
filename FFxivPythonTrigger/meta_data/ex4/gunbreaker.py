from ..base import *


class Status:
    class NoMercy(StatusBase):
        """
Increases damage dealt by 20%.
Duration: 20s
>> 1831, No Mercy, Damage dealt is increased.
        """
        id = 1831
        name = {'无情', 'No Mercy'}
        damage_modify = 1.2

    class BrutalShell(StatusBase):
        """
Delivers an attack with a potency of (source.job==37?(source.level>=84?120:100):100).
Combo Action: Keen Edge
Combo Potency: (source.job==37?(source.level>=84?260:240):240)
Combo Bonus: Restores own HP
Cure Potency: 200(source.job==37?(source.level>=52?
Combo Bonus: Creates a barrier which nullifies damage equaling HP restored
Duration: 30s:):)
>> 1898, Brutal Shell, A highly effective defensive maneuver is nullifying damage.
>> 1997, Brutal Shell, A highly effective defensive maneuver is nullifying damage.
        """
        id = 1898
        name = {'Brutal Shell', '残暴弹'}

    class Camouflage(StatusBase):
        """
Increases parry rate by 50% while reducing damage taken by 10%.
Duration: 20s
>> 1832, Camouflage, Parry rate is increased while damage taken is reduced.
        """
        id = 1832
        name = {'Camouflage', '伪装'}
        taken_damage_modify = 0.9

    class Nebula(StatusBase):
        """
Reduces damage taken by 30%.
Duration: 15s
>> 1834, Nebula, Damage taken is reduced.
        """
        id = 1834
        name = {'Nebula', '星云'}
        taken_damage_modify = 0.7

    class Aurora(StatusBase):
        """
Grants Regen to target.
Cure Potency: 200
Duration: 18s(source.job==37?(source.level>=84?
Maximum Charges: 2:):)
>> 2065, Aurora, Regenerating HP over time.
>> 1835, Aurora, Regenerating HP over time.
        """
        id = 1835
        name = {'Aurora', '极光'}
        cure_potency = 200

    class Superbolide(StatusBase):
        """
Reduces HP to 1 and renders you impervious to most attacks.
Duration: 10s
>> 1836, Superbolide, Impervious to most attacks.
        """
        id = 1836
        name = {'Superbolide', '超火流星'}
        taken_damage_modify = 0

    class SonicBreak(StatusBase):
        """
Delivers an attack with a potency of 300.
Additional Effect: Damage over time
Potency: 60
Duration: 30s
This weaponskill does not share a recast timer with any other actions.
>> 1837, Sonic Break, Sustaining damage over time.
        """
        id = 1837
        name = {'Sonic Break', '音速破'}
        damage_potency = 60

    class ReadyToRip(StatusBase):
        id = 1842
        name = {'Ready To Rip', '撕喉预备'}

    class ReadyToTear(StatusBase):
        id = 1843
        name = {'Ready To Tear', '裂膛预备'}

    class ReadyToGouge(StatusBase):
        id = 1844
        name = {'Ready To Gouge', '穿目预备'}

    class ReadyToBlast(StatusBase):
        id = 2686
        name = {'Ready To Blast'}

    class BowShock(StatusBase):
        """
Delivers an attack with a potency of 150 to all nearby enemies.
Additional Effect: Damage over time
Potency: 60
Duration: 15s
>> 1838, Bow Shock, Sustaining damage over time.
        """
        id = 1838
        name = {'Bow Shock', '弓形冲波'}
        damage_potency = 60

    class HeartOfLight(StatusBase):
        """
Reduces magic damage taken by self and nearby party members by 10%.
Duration: 15s
>> 2000, Heart of Light, Damage taken is reduced.
>> 1839, Heart of Light, Magic damage taken is reduced.
        """
        id = 1839
        name = {'Heart of Light', '光之心'}
        taken_damage_modify = 0.9
        modify_type = magic

    class HeartOfStone(StatusBase):
        """
Reduces damage taken by a party member or self by 15%.
Duration: 7s
Additional Effect: When targeting a party member while under the effect of Brutal Shell, that effect is also granted to the target
Duration: 30s
>> 1840, Heart of Stone, Damage taken is reduced.
        """
        id = 1840
        name = {'石之心', 'Heart of Stone'}
        taken_damage_modify = 0.85

    class HeartOfCorundum(StatusBase):
        """
Reduces damage taken by a party member or self by 15%.
Duration: 8s
        """
        id = 2683
        name = {'Heart of Corundum'}
        taken_damage_modify = 0.85

    class ClarityOfCorundum(StatusBase):
        """
Clarity of Corundum Effect: Reduces damage taken by 15%
Duration: 4s
        """
        id = 2684
        name = {'Clarity of Corundum'}
        taken_damage_modify = 0.85

    class CatharsisOfCorundum(StatusBase):
        """
Catharsis of Corundum Effect: Restores HP when HP falls below 50% or upon effect duration expiration
Cure Potency: 900
        """
        id = 2685
        name = {'Catharsis of Corundum'}
        cure_potency = 900
        over_time_status: bool = False


class Actions:
    class KeenEdge(ActionBase):
        """
Delivers an attack with a potency of (source.job==37?(source.level>=84?170:150):150).
        """
        id = 16137
        name = {'Keen Edge', '利刃斩'}
        attack_type = physic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 170 if source and source.job == 37 and source.level >= 84 else 150

    class NoMercy(ActionBase):
        """
Increases damage dealt by 20%.
Duration: 20s
>> 1831, No Mercy, Damage dealt is increased.
        """
        id = 16138
        name = {'无情', 'No Mercy'}
        status_to_target = Status.NoMercy

    class BrutalShell(ActionBase):
        """
Delivers an attack with a potency of (source.job==37?(source.level>=84?120:100):100).
Combo Action: Keen Edge
Combo Potency: (source.job==37?(source.level>=84?260:240):240)
Combo Bonus: Restores own HP
Cure Potency: 200(source.job==37?(source.level>=52?
Combo Bonus: Creates a barrier which nullifies damage equaling HP restored
Duration: 30s:):)
>> 1898, Brutal Shell, A highly effective defensive maneuver is nullifying damage.
>> 1997, Brutal Shell, A highly effective defensive maneuver is nullifying damage.
        """
        id = 16139
        name = {'Brutal Shell', '残暴弹'}
        combo_action = 16137
        attack_type = physic
        cure_potency = 200

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            if source and source.job == 37 and source.level >= 84:
                self.damage_potency = 120
                self.combo_damage_potency = 260
            else:
                self.damage_potency = 100
                self.combo_damage_potency = 240

    class Camouflage(ActionBase):
        """
Increases parry rate by 50% while reducing damage taken by 10%.
Duration: 20s
>> 1832, Camouflage, Parry rate is increased while damage taken is reduced.
        """
        id = 16140
        name = {'Camouflage', '伪装'}
        status_to_target = Status.Camouflage

    class DemonSlice(ActionBase):
        """
Delivers an attack with a potency of 100 to all nearby enemies.
        """
        id = 16141
        name = {'Demon Slice', '恶魔切'}
        attack_type = physic
        damage_potency = 100

    class RoyalGuard(ActionBase):
        """
Significantly increases enmity generation.
Effect ends upon reuse.
>> 392, Royal Guard, Enmity is increased.
>> 1833, Royal Guard, Enmity is increased.
        """
        id = 16142
        name = {'王室亲卫', 'Royal Guard'}

    class LightningShot(ActionBase):
        """
Delivers a ranged attack with a potency of 150.
Additional Effect: Increased enmity
>> 2392, Lightning Shot, Next weaponskill will deal increased damage.
        """
        id = 16143
        name = {'Lightning Shot', '闪雷弹'}
        attack_type = physic
        damage_potency = 150

    class DangerZone(ActionBase):
        """
Delivers an attack with a potency of 250.
        """
        id = 16144
        name = {'危险领域', 'Danger Zone'}
        attack_type = physic
        damage_potency = 250

    class SolidBarrel(ActionBase):
        """
Delivers an attack with a potency of (source.job==37?(source.level>=84?120:100):100).
Combo Action: Brutal Shell
Combo Potency: (source.job==37?(source.level>=84?340:320):320)(source.job==37?(source.level>=30?
Combo Bonus: Adds a Cartridge to your Powder Gauge:):)
        """
        id = 16145
        name = {'Solid Barrel', '迅连斩'}
        combo_action = 16139
        attack_type = physic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            if source and source.job == 37 and source.level >= 84:
                self.damage_potency = 120
                self.combo_damage_potency = 340
            else:
                self.damage_potency = 100
                self.combo_damage_potency = 320

    class BurstStrike(ActionBase):
        """
Delivers an attack with a potency of 380.
(source.job==37?(source.level>=86?Additional Effect: Grants Ready to Blast
Duration: 10s
:):)Cartridge Cost: 1
        """
        id = 16162
        name = {'爆发击', 'Burst Strike'}
        attack_type = physic
        damage_potency = 380

    class Nebula(ActionBase):
        """
Reduces damage taken by 30%.
Duration: 15s
>> 1834, Nebula, Damage taken is reduced.
        """
        id = 16148
        name = {'Nebula', '星云'}
        status_to_target = Status.Nebula

    class DemonSlaughter(ActionBase):
        """
Delivers an attack with a potency of 100 to all nearby enemies.
Combo Action: Demon Slice
Combo Potency: 160
Combo Bonus: Adds a Cartridge to your Powder Gauge
        """
        id = 16149
        name = {'恶魔杀', 'Demon Slaughter'}
        combo_action = 16141
        attack_type = physic
        damage_potency = 100
        combo_damage_potency = 160

    class Aurora(ActionBase):
        """
Grants Regen to target.
Cure Potency: 200
Duration: 18s(source.job==37?(source.level>=84?
Maximum Charges: 2:):)
>> 2065, Aurora, Regenerating HP over time.
>> 1835, Aurora, Regenerating HP over time.
        """
        id = 16151
        name = {'Aurora', '极光'}
        status_to_target = Status.Aurora

    class Superbolide(ActionBase):
        """
Reduces HP to 1 and renders you impervious to most attacks.
Duration: 10s
>> 1836, Superbolide, Impervious to most attacks.
        """
        id = 16152
        name = {'Superbolide', '超火流星'}
        status_to_target = Status.Superbolide

    class SonicBreak(ActionBase):
        """
Delivers an attack with a potency of 300.
Additional Effect: Damage over time
Potency: 60
Duration: 30s
This weaponskill does not share a recast timer with any other actions.
>> 1837, Sonic Break, Sustaining damage over time.
        """
        id = 16153
        name = {'Sonic Break', '音速破'}
        attack_type = physic
        damage_potency = 300

    class RoughDivide(ActionBase):
        """
Delivers a jumping attack with a potency of 150.
Maximum Charges: 2
Cannot be executed while bound.
        """
        id = 16154
        name = {'粗分斩', 'Rough Divide'}
        attack_type = physic
        damage_potency = 150

    class GnashingFang(ActionBase):
        """
Delivers an attack with a potency of 360.
(source.job==37?(source.level>=70?Additional Effect: Grants Ready to Rip
Duration: 10s
:):)Cartridge Cost: 1
This weaponskill does not share a recast timer with any other actions.
        """
        id = 16146
        name = {'烈牙', 'Gnashing Fang'}
        attack_type = physic
        damage_potency = 360

    class SavageClaw(ActionBase):
        """
Delivers an attack with a potency of 440.
Combo Action: Gnashing Fang(source.job==37?(source.level>=70?
Combo Bonus: Grants Ready to Tear
Duration: 10s:):)
※This action cannot be assigned to a hotbar.
        """
        id = 16147
        name = {'Savage Claw', '猛兽爪'}
        combo_action = 16146
        attack_type = physic
        damage_potency = 440

    class WickedTalon(ActionBase):
        """
Delivers an attack with a potency of 520.
Combo Action: Savage Claw(source.job==37?(source.level>=70?
Combo Bonus: Grants Ready to Gouge
Duration: 10s:):)
※This action cannot be assigned to a hotbar.
        """
        id = 16150
        name = {'凶禽爪', 'Wicked Talon'}
        combo_action = 16147
        attack_type = physic
        damage_potency = 520

    class BowShock(ActionBase):
        """
Delivers an attack with a potency of 150 to all nearby enemies.
Additional Effect: Damage over time
Potency: 60
Duration: 15s
>> 1838, Bow Shock, Sustaining damage over time.
        """
        id = 16159
        name = {'Bow Shock', '弓形冲波'}
        attack_type = physic
        damage_potency = 150
        status_to_target = Status.BowShock

    class HeartOfLight(ActionBase):
        """
Reduces magic damage taken by self and nearby party members by 10%.
Duration: 15s
>> 2000, Heart of Light, Damage taken is reduced.
>> 1839, Heart of Light, Magic damage taken is reduced.
        """
        id = 16160
        name = {'Heart of Light', '光之心'}
        status_to_target = Status.HeartOfLight

    class HeartOfStone(ActionBase):
        """
Reduces damage taken by a party member or self by 15%.
Duration: 7s
Additional Effect: When targeting a party member while under the effect of Brutal Shell, that effect is also granted to the target
Duration: 30s
>> 1840, Heart of Stone, Damage taken is reduced.
        """
        id = 16161
        name = {'石之心', 'Heart of Stone'}

    class Continuation(ActionBase):
        """
Allows the firing of successive rounds with your gunblade.
Gnashing Fang may be followed by Jugular Rip.
Savage Claw may be followed by Abdomen Tear.
Wicked Talon may be followed by Eye Gouge.(source.job==37?(source.level>=86?
Burst Strike may be followed by Hypervelocity.:):)
        """
        id = 16155
        name = {'续剑', 'Continuation'}

    class JugularRip(ActionBase):
        """
Delivers an attack with a potency of 180.
Can only be executed when Ready to Rip.
※This action cannot be assigned to a hotbar.
        """
        id = 16156
        name = {'Jugular Rip', '撕喉'}
        attack_type = physic
        damage_potency = 180

    class AbdomenTear(ActionBase):
        """
Delivers an attack with a potency of 220.
Can only be executed when Ready to Tear.
※This action cannot be assigned to a hotbar.
        """
        id = 16157
        name = {'Abdomen Tear', '裂膛'}
        attack_type = physic
        damage_potency = 220

    class EyeGouge(ActionBase):
        """
Delivers an attack with a potency of 260.
Can only be executed when Ready to Gouge.
※This action cannot be assigned to a hotbar.
        """
        id = 16158
        name = {'穿目', 'Eye Gouge'}
        attack_type = physic
        damage_potency = 260

    class FatedCircle(ActionBase):
        """
Delivers an attack with a potency of 290 to all nearby enemies.
Cartridge Cost: 1
        """
        id = 16163
        name = {'命运之环', 'Fated Circle'}
        attack_type = physic
        damage_potency = 290

    class Bloodfest(ActionBase):
        """
Draws aetheric energy from target, adding (source.job==37?(source.level>=88?3:2):2) Cartridges to your Powder Gauge.
        """
        id = 16164
        name = {'Bloodfest', '血壤'}

    class BlastingZone(ActionBase):
        """
Delivers an attack with a potency of 700.
        """
        id = 16165
        name = {'爆破领域', 'Blasting Zone'}
        attack_type = physic
        damage_potency = 700

    class HeartOfCorundum(ActionBase):
        """
Reduces damage taken by a party member or self by 15%.
Duration: 8s
Additional Effect: When targeting a party member while under the effect of Brutal Shell, that effect is also granted to the target
Duration: 30s
Additional Effect: Grants Clarity of Corundum to target
Clarity of Corundum Effect: Reduces damage taken by 15%
Duration: 4s
Additional Effect: Grants Catharsis of Corundum to target
Catharsis of Corundum Effect: Restores HP when HP falls below 50% or upon effect duration expiration
Cure Potency: 900
Duration: 20s
>> 2683, Heart of Corundum, Damage taken is reduced.
        """
        id = 25758
        name = {'Heart of Corundum'}
        status_to_target = Status.HeartOfCorundum, Status.ClarityOfCorundum, Status.CatharsisOfCorundum

    class Hypervelocity(ActionBase):
        """
Delivers an attack with a potency of 180.
Can only be executed when Ready to Blast.
※This action cannot be assigned to a hotbar.
        """
        id = 25759
        name = {'Hypervelocity'}
        attack_type = physic
        damage_potency = 180

    class DoubleDown(ActionBase):
        """
Delivers an attack to all nearby enemies with a potency of 1,200 for the first enemy, and 20% less for all remaining enemies.
Cartridge Cost: 2
This weaponskill does not share a recast timer with any other actions.
        """
        id = 25760
        name = {'Double Down'}
        attack_type = physic
        damage_potency = 1200
        aoe_scale = 0.8
