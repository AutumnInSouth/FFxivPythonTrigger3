from ..base import *


class Actions:

    class KeenEdge(ActionBase):
        """
Delivers an attack with a potency of (source.job==37?(source.level>=84?170:150):150).
>> 1145, Keen Edge, Sustaining damage over time in exchange for dealing increased damage to targets.
        """
        id = 16137
        name = {'Keen Edge', '利刃斩'}

    class NoMercy(ActionBase):
        """
Increases damage dealt by 20%.
Duration: 20s
>> 1831, No Mercy, Damage dealt is increased.
        """
        id = 16138
        name = {'No Mercy', '无情'}

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
        name = {'残暴弹', 'Brutal Shell'}
        combo_action = 16137

    class Camouflage(ActionBase):
        """
Increases parry rate by 50% while reducing damage taken by 10%.
Duration: 20s
>> 1832, Camouflage, Parry rate is increased while damage taken is reduced.
        """
        id = 16140
        name = {'伪装', 'Camouflage'}

    class DemonSlice(ActionBase):
        """
Delivers an attack with a potency of 100 to all nearby enemies.
        """
        id = 16141
        name = {'恶魔切', 'Demon Slice'}

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

    class DangerZone(ActionBase):
        """
Delivers an attack with a potency of 250.
        """
        id = 16144
        name = {'Danger Zone', '危险领域'}

    class SolidBarrel(ActionBase):
        """
Delivers an attack with a potency of (source.job==37?(source.level>=84?120:100):100).
Combo Action: Brutal Shell
Combo Potency: (source.job==37?(source.level>=84?340:320):320)(source.job==37?(source.level>=30?
Combo Bonus: Adds a Cartridge to your Powder Gauge:):)
        """
        id = 16145
        name = {'迅连斩', 'Solid Barrel'}
        combo_action = 16139

    class BurstStrike(ActionBase):
        """
Delivers an attack with a potency of 380.
(source.job==37?(source.level>=86?Additional Effect: Grants Ready to Blast
Duration: 10s
:):)Cartridge Cost: 1
        """
        id = 16162
        name = {'Burst Strike', '爆发击'}

    class Nebula(ActionBase):
        """
Reduces damage taken by 30%.
Duration: 15s
>> 1834, Nebula, Damage taken is reduced.
        """
        id = 16148
        name = {'星云', 'Nebula'}

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

    class Superbolide(ActionBase):
        """
Reduces HP to 1 and renders you impervious to most attacks.
Duration: 10s
>> 1836, Superbolide, Impervious to most attacks.
        """
        id = 16152
        name = {'Superbolide', '超火流星'}

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

    class RoughDivide(ActionBase):
        """
Delivers a jumping attack with a potency of 150.
Maximum Charges: 2
Cannot be executed while bound.
        """
        id = 16154
        name = {'粗分斩', 'Rough Divide'}

    class GnashingFang(ActionBase):
        """
Delivers an attack with a potency of 360.
(source.job==37?(source.level>=70?Additional Effect: Grants Ready to Rip
Duration: 10s
:):)Cartridge Cost: 1
This weaponskill does not share a recast timer with any other actions.
        """
        id = 16146
        name = {'Gnashing Fang', '烈牙'}

    class SavageClaw(ActionBase):
        """
Delivers an attack with a potency of 440.
Combo Action: Gnashing Fang(source.job==37?(source.level>=70?
Combo Bonus: Grants Ready to Tear
Duration: 10s:):)
※This action cannot be assigned to a hotbar.
        """
        id = 16147
        name = {'猛兽爪', 'Savage Claw'}
        combo_action = 16146

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

    class HeartOfLight(ActionBase):
        """
Reduces magic damage taken by self and nearby party members by 10%.
Duration: 15s
>> 2000, Heart of Light, Damage taken is reduced.
>> 1839, Heart of Light, Magic damage taken is reduced.
        """
        id = 16160
        name = {'Heart of Light', '光之心'}

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

    class AbdomenTear(ActionBase):
        """
Delivers an attack with a potency of 220.
Can only be executed when Ready to Tear.
※This action cannot be assigned to a hotbar.
        """
        id = 16157
        name = {'Abdomen Tear', '裂膛'}

    class EyeGouge(ActionBase):
        """
Delivers an attack with a potency of 260.
Can only be executed when Ready to Gouge.
※This action cannot be assigned to a hotbar.
        """
        id = 16158
        name = {'Eye Gouge', '穿目'}

    class FatedCircle(ActionBase):
        """
Delivers an attack with a potency of 290 to all nearby enemies.
Cartridge Cost: 1
        """
        id = 16163
        name = {'命运之环', 'Fated Circle'}

    class Bloodfest(ActionBase):
        """
Draws aetheric energy from target, adding (source.job==37?(source.level>=88?3:2):2) Cartridges to your Powder Gauge.
        """
        id = 16164
        name = {'血壤', 'Bloodfest'}

    class BlastingZone(ActionBase):
        """
Delivers an attack with a potency of 700.
        """
        id = 16165
        name = {'爆破领域', 'Blasting Zone'}

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

    class Hypervelocity(ActionBase):
        """
Delivers an attack with a potency of 180.
Can only be executed when Ready to Blast.
※This action cannot be assigned to a hotbar.
        """
        id = 25759
        name = {'Hypervelocity'}

    class DoubleDown(ActionBase):
        """
Delivers an attack to all nearby enemies with a potency of 1,200 for the first enemy, and 20% less for all remaining enemies.
Cartridge Cost: 2
This weaponskill does not share a recast timer with any other actions.
        """
        id = 25760
        name = {'Double Down'}
