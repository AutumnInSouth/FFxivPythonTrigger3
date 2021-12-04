from ..base import *

class Status:

    class RadiantAegis(StatusBase):
        id = 2702
        name = {'Radiant Aegis', '守护之光'}


class Actions:

    class Ruin(ActionBase):
        """
Deals unaspected damage with a potency of 240.
        """
        id = 163
        name = {'Ruin', '毁灭'}
        damage_potency = 240
        attack_type = magic

    class SummonCarbuncle(ActionBase):
        """
Summons Carbuncle to your side.
        """
        id = 25798
        name = {'Summon Carbuncle', '宝石兽召唤'}

    class RadiantAegis(ActionBase):
        """
Orders Carbuncle to execute Radiant Aegis.
Radiant Aegis Effect: Creates a barrier around self that absorbs damage totaling 20% of your maximum HP
Duration: 30s
(source.job==27?(source.level>=88?Maximum Charges: 2
:):)Can only be executed while Carbuncle is summoned.
>> 2702, Radiant Aegis, A magicked barrier is nullifying damage.
        """
        id = 25799
        name = {'Radiant Aegis', '守护之光'}

    class RadiantAegis(ActionBase):
        """
Creates a barrier around you that absorbs damage totaling 20% of your maximum HP.
Duration: 30s
※This action cannot be assigned to a hotbar.
>> 2702, Radiant Aegis, A magicked barrier is nullifying damage.
        """
        id = 25841
        name = {'Radiant Aegis', '守护之光'}

    class Physick(ActionBase):
        """
Restores target's HP.
Cure Potency: 400
        """
        id = 16230
        name = {'医术', 'Physick'}

    class Aethercharge(ActionBase):
        """
Grants Aethercharge, increasing the potency of Ruin, Ruin II, and Ruin III by 50, and Outburst by 20.
Duration: 15s
Additional Effect: Grants (source.level>=22?(source.job==26?Ruby Arcanum, Topaz Arcanum, and Emerald Arcanum:(source.job==27?Ruby Arcanum, Topaz Arcanum, and Emerald Arcanum:(source.level>=15?(source.job==26?Ruby Arcanum and Topaz Arcanum:(source.job==27?Ruby Arcanum and Topaz Arcanum:Ruby Arcanum)):Ruby Arcanum))):(source.level>=15?(source.job==26?Ruby Arcanum and Topaz Arcanum:(source.job==27?Ruby Arcanum and Topaz Arcanum:Ruby Arcanum)):Ruby Arcanum))
Can only be executed in combat and while Carbuncle is summoned.
        """
        id = 25800
        name = {'Aethercharge', '以太充能'}

    class SummonRuby(ActionBase):
        """
Summons Ruby Carbuncle, and orders it to execute Glittering Ruby.
Glittering Ruby Effect: Rushes target and deals fire damage with a potency of 400
Additional Effect: Grants 2 stacks of Fire Attunement
Fire Attunement Effect: Gemshine and Precious Brilliance become fire-aspected
Duration: 30s
Can only be executed while under the effect of Ruby Arcanum and Carbuncle is summoned.
        """
        id = 25802
        name = {'Summon Ruby', '红宝石兽召唤'}

    class RubyRuin(ActionBase):
        """
Deals fire damage with a potency of 300.
Fire Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25808
        name = {'Ruby Ruin', '红宝石毁灭'}

    class Gemshine(ActionBase):
        """
Channel the energies of your active elemental attunement to attack your enemy.
Fire Attunement Effect: Deal fire damage to a single target
Earth Attunement Effect: Deal earth damage to a single target
Wind Attunement Effect: Deal wind damage to a single target
        """
        id = 25883
        name = {'Gemshine', '宝石之光'}

    class Fester(ActionBase):
        """
Deals unaspected damage with a potency of 300.
Aetherflow Gauge Cost: 1
        """
        id = 181
        name = {'溃烂爆发', 'Fester'}

    class EnergyDrain(ActionBase):
        """
Deals unaspected damage with a potency of 200.
Additional Effect: Aetherflow II(source.job==27?(source.level>=62?
Additional Effect: Grants Further Ruin
Duration: 60s:):)(source.job==27?(source.level>=52?
Shares a recast timer with Energy Siphon.:):)
        """
        id = 16508
        name = {'能量吸收 - 召唤师', 'Energy Drain - Summoner'}

    class SummonTopaz(ActionBase):
        """
Summons Topaz Carbuncle, and orders it to execute Glittering Topaz.
Glittering Topaz Effect: Rushes target and deals earth damage with a potency of 400
Additional Effect: Grants 4 stacks of Earth Attunement
Earth Attunement Effect: Gemshine and Precious Brilliance become earth-aspected
Duration: 30s
Can only be executed while under the effect of Topaz Arcanum and Carbuncle is summoned.
        """
        id = 25803
        name = {'Summon Topaz', '黄宝石兽召唤'}

    class TopazRuin(ActionBase):
        """
Deals earth damage with a potency of 240.
Earth Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25809
        name = {'Topaz Ruin', '黄宝石毁灭'}

    class SummonEmerald(ActionBase):
        """
Summons Emerald Carbuncle, and orders it to execute Glittering Emerald.
Glittering Emerald Effect: Deals wind damage with a potency of 400
Additional Effect: Grants 4 stacks of Wind Attunement
Wind Attunement Effect: Gemshine and Precious Brilliance become wind-aspected
Duration: 30s
Can only be executed while under the effect of Emerald Arcanum and Carbuncle is summoned.
        """
        id = 25804
        name = {'Summon Emerald', '绿宝石兽召唤'}

    class EmeraldRuin(ActionBase):
        """
Deals wind damage with a potency of 160.
Wind Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25810
        name = {'Emerald Ruin', '绿宝石毁灭'}

    class Outburst(ActionBase):
        """
Deals unaspected damage with a potency of 100 to target and all enemies nearby it.
        """
        id = 16511
        name = {'Outburst', '迸裂'}

    class RubyOutburst(ActionBase):
        """
Deals fire damage with a potency of 140 to target and all enemies nearby it.
Fire Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25814
        name = {'Ruby Outburst', '红宝石迸裂'}

    class TopazOutburst(ActionBase):
        """
Deals earth damage with a potency of 110 to target and all enemies nearby it.
Earth Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25815
        name = {'Topaz Outburst', '黄宝石迸裂'}

    class EmeraldOutburst(ActionBase):
        """
Deals wind damage with a potency of 70 to target and all enemies nearby it.
Wind Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25816
        name = {'Emerald Outburst', '绿宝石迸裂'}

    class PreciousBrilliance(ActionBase):
        """
Channel the energies of your active elemental attunement to attack multiple enemies.
Fire Attunement Effect: Deal fire damage to a target and all enemies nearby it
Earth Attunement Effect: Deal earth damage to a target and all enemies nearby it
Wind Attunement Effect: Deal wind damage to a target and all enemies nearby it
        """
        id = 25884
        name = {'Precious Brilliance', '宝石之耀'}

    class RuinIi(ActionBase):
        """
Deals unaspected damage with a potency of 270.
        """
        id = 172
        name = {'Ruin II', '毁坏'}

    class SummonIfrit(ActionBase):
        """
Summons Ifrit-Egi and orders it to execute (source.job==27?(source.level>=50?Inferno:Burning Strike):Burning Strike).
(source.job==27?(source.level>=50?Inferno Effect: Rushes forward and deals fire damage to all enemies in a 5-yalm cone before it with a potency of 600 for the first enemy, and 60% less for all remaining enemies:Burning Strike Effect: Rushes forward and deals fire damage with a potency of 500):Burning Strike Effect: Rushes forward and deals fire damage with a potency of 500)
Additional Effect: Grants 2 stacks of Fire Attunement
Fire Attunement Effect: Gemshine and Precious Brilliance become fire-aspected
Duration: 30s
(source.job==27?(source.level>=86?Additional Effect: Grants Ifrit's Favor
Effect of Ifrit's Favor ends upon execution of certain summoner actions.
:):)Can only be executed while under the effect of Ruby Arcanum and Carbuncle is summoned.
        """
        id = 25805
        name = {'Summon Ifrit', '火神召唤'}

    class RubyRuinIi(ActionBase):
        """
Deals fire damage with a potency of 340.
Fire Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25811
        name = {'Ruby Ruin II', '红宝石毁坏'}

    class TopazRuinIi(ActionBase):
        """
Deals earth damage with a potency of 270.
Earth Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25812
        name = {'Topaz Ruin II', '黄宝石毁坏'}

    class EmeraldRuinIi(ActionBase):
        """
Deals wind damage with a potency of 170.
Wind Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25813
        name = {'Emerald Ruin II', '绿宝石毁坏'}

    class SummonTitan(ActionBase):
        """
Summons Titan-Egi and orders it to execute (source.job==27?(source.level>=50?Earthen Fury:Rock Buster):Rock Buster).
(source.job==27?(source.level>=50?Earthen Fury Effect: Rushes forward and deals earth damage to all enemies within 5 yalms with a potency of 600 for the first enemy, and 60% less for all remaining enemies:Rock Buster Effect: Rushes forward and deals earth damage with a potency of 500):Rock Buster Effect: Rushes forward and deals earth damage with a potency of 500)
Additional Effect: Grants 4 stacks of Earth Attunement
Earth Attunement Effect: Gemshine and Precious Brilliance become earth-aspected
Duration: 30s
Can only be executed while under the effect of Topaz Arcanum and Carbuncle is summoned.
        """
        id = 25806
        name = {'Summon Titan', '土神召唤'}

    class Painflare(ActionBase):
        """
Deals unaspected damage with a potency of 150 to target and all enemies nearby it.
Aetherflow Gauge Cost: 1
        """
        id = 3578
        name = {'Painflare', '痛苦核爆'}

    class SummonGaruda(ActionBase):
        """
Summons Garuda-Egi and orders it to execute (source.job==27?(source.level>=50?Aerial Blast:Aerial Slash):Aerial Slash).
(source.job==27?(source.level>=50?Aerial Blast Effect: Deals wind damage to target and all enemies within 5 yalms with a potency of 600 for the first enemy, and 60% less for all remaining enemies:Aerial Slash Effect: Deals wind damage with a potency of 100 to target and all enemies nearby it):Aerial Slash Effect: Deals wind damage with a potency of 100 to target and all enemies nearby it)
Additional Effect: Grants 4 stacks of Wind Attunement
Wind Attunement Effect: Gemshine and Precious Brilliance become wind-aspected
Duration: 30s
(source.job==27?(source.level>=86?Additional Effect: Grants Garuda's Favor
Effect of Garuda's Favor ends upon execution of certain summoner actions.
:):)Can only be executed while under the effect of Emerald Arcanum and Carbuncle is summoned.
        """
        id = 25807
        name = {'Summon Garuda', '风神召唤'}

    class EnergySiphon(ActionBase):
        """
Deals unaspected damage with a potency of 100 to target and all enemies nearby it.
Additional Effect: Aetherflow II
(source.job==27?(source.level>=62?Additional Effect: Grants Further Ruin
Duration: 60s
:):)Shares a recast timer with Energy Drain.
        """
        id = 16510
        name = {'Energy Siphon', '能量抽取'}

    class RuinIii(ActionBase):
        """
Deals unaspected damage with a potency of (source.job==27?(source.level>=84?310:300):300).
        """
        id = 3579
        name = {'Ruin III', '毁荡'}

    class RubyRuinIii(ActionBase):
        """
Deals fire damage with a potency of 360.
Fire Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25817
        name = {'Ruby Ruin III', '红宝石毁荡'}

    class TopazRuinIii(ActionBase):
        """
Deals earth damage with a potency of 300.
Earth Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25818
        name = {'Topaz Ruin III', '黄宝石毁荡'}

    class EmeraldRuinIii(ActionBase):
        """
Deals wind damage with a potency of 180.
Wind Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25819
        name = {'Emerald Ruin III', '绿宝石毁荡'}

    class DreadwyrmTrance(ActionBase):
        """
Enters Dreadwyrm Trance.
Duration: 15s
Additional Effect: Changes Ruin III to Astral Impulse and Outburst to Astral Flare
Additional Effect: Grants Ruby Arcanum, Topaz Arcanum, and Emerald Arcanum
Can only be executed in combat and while Carbuncle is summoned.
>> 808, Dreadwyrm Trance, Drawing on the power of Bahamut, increasing magic damage dealt.
        """
        id = 3581
        name = {'龙神附体', 'Dreadwyrm Trance'}

    class AstralImpulse(ActionBase):
        """
Deals unaspected damage with a potency of 430.
Can only be executed while in Dreadwyrm Trance.
※This action cannot be assigned to a hotbar.
        """
        id = 25820
        name = {'Astral Impulse', '星极脉冲'}

    class AstralFlare(ActionBase):
        """
Deals unaspected damage with a potency of 180 to target and all enemies nearby it.
Can only be executed while in Dreadwyrm Trance.
※This action cannot be assigned to a hotbar.
        """
        id = 25821
        name = {'Astral Flare', '星极核爆'}

    class Deathflare(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 500 for the first enemy, and 60% less for all remaining enemies.
Can only be executed while in Dreadwyrm Trance.
※This action cannot be assigned to a hotbar.
        """
        id = 3582
        name = {'Deathflare', '死星核爆'}

    class AstralFlow(ActionBase):
        """
Channel the energies of your active trance(source.job==27?(source.level>=86? or elemental favor:):) to perform one of several actions.
Dreadwyrm Trance Effect: Action changes to Deathflare(source.job==27?(source.level>=80?
Firebird Trance Effect: Action changes to Rekindle:):)(source.job==27?(source.level>=86?
Ifrit's Favor Effect: Action changes to Crimson Cyclone
Titan's Favor Effect: Action changes to Mountain Buster
Garuda's Favor Effect: Action changes to Slipstream:):)
        """
        id = 25822
        name = {'Astral Flow' ,'星极超流'}

    class RuinIv(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 430 for the first enemy, and 60% less for all remaining enemies.
Can only be executed while under the effect of Further Ruin.
        """
        id = 7426
        name = {'毁绝', 'Ruin IV'}

    class SearingLight(ActionBase):
        """
Orders Carbuncle to execute Searing Light.
Searing Light Effect: Increases damage dealt by self and nearby party members by 3%
Duration: 30s
Can only be executed in combat and while Carbuncle is summoned.
>> 2703, Searing Light, Damage dealt is increased.
        """
        id = 25801
        name = {'Searing Light', '炽热之光'}

    class SearingLight(ActionBase):
        """
Increases damage dealt by self and nearby party members by 3%.
Duration: 30s
※This action cannot be assigned to a hotbar.
>> 2703, Searing Light, Damage dealt is increased.
        """
        id = 25842
        name = {'Searing Light', '炽热之光'}

    class SummonBahamut(ActionBase):
        """
Enters Dreadwyrm Trance and summons Demi-Bahamut to fight your target.
Demi-Bahamut will execute Wyrmwave automatically on the targets attacked by you after summoning.
Increases enmity in target when Demi-Bahamut is summoned.
Duration: 15s
Additional Effect: Changes Ruin III to Astral Impulse and (source.job==27?(source.level>=74?Tri-disaster:Outburst):Outburst) to Astral Flare
Additional Effect: Grants Ruby Arcanum, Topaz Arcanum, and Emerald Arcanum
Can only be executed in combat and while Carbuncle is summoned.
        """
        id = 7427
        name = {'Summon Bahamut', '龙神召唤'}

    class Wyrmwave(ActionBase):
        """
Deals unaspected damage with a potency of 150.
Will only execute while Demi-Bahamut is summoned.
※This action cannot be assigned to a hotbar.
        """
        id = 7428
        name = {'真龙波', 'Wyrmwave'}

    class EnkindleBahamut(ActionBase):
        """
Orders Demi-Bahamut to execute Akh Morn.
Akh Morn Effect: Deals unaspected damage to target and all enemies nearby it with a potency of 1,300 for the first enemy, and 60% less for all remaining enemies
        """
        id = 7429
        name = {'龙神迸发', 'Enkindle Bahamut'}

    class AkhMorn(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 1,300 for the first enemy, and 60% less for all remaining enemies.
Can only be executed while Demi-Bahamut is summoned.
※This action cannot be assigned to a hotbar.
        """
        id = 7449
        name = {'死亡轮回', 'Akh Morn'}

    class RubyRite(ActionBase):
        """
Deals fire damage with a potency of (source.job==27?(source.level>=84?430:420):420).
Fire Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25823
        name = {'Ruby Rite', '红宝石之仪'}

    class TopazRite(ActionBase):
        """
Deals earth damage with a potency of (source.job==27?(source.level>=84?330:320):320).
(source.job==27?(source.level>=86?Additional Effect: Grants Titan's Favor
Effect of Titan's Favor ends upon execution of certain summoner actions.
:):)Earth Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25824
        name = {'Topaz Rite', '黄宝石之仪'}

    class EmeraldRite(ActionBase):
        """
Deals wind damage with a potency of (source.job==27?(source.level>=84?230:220):220).
Wind Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25825
        name = {'Emerald Rite', '绿宝石之仪'}

    class TriDisaster(ActionBase):
        """
Deals unaspected damage with a potency of 120 to target and all enemies nearby it.
        """
        id = 25826
        name = {'Tri-disaster', '三重灾祸'}

    class RubyDisaster(ActionBase):
        """
Deals fire damage with a potency of 170 to target and all enemies nearby it.
Fire Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25827
        name = {'Ruby Disaster', '红宝石三重灾祸'}

    class TopazDisaster(ActionBase):
        """
Deals earth damage with a potency of 130 to target and all enemies nearby it.
Earth Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25828
        name = {'Topaz Disaster', '黄宝石三重灾祸'}

    class EmeraldDisaster(ActionBase):
        """
Deals wind damage with a potency of 90 to target and all enemies nearby it.
Wind Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25829
        name = {'Emerald Disaster', '绿宝石三重灾祸'}

    class FountainOfFire(ActionBase):
        """
Deals fire damage with a potency of 430.
Can only be executed while under the effect of Firebird Trance.
※This action cannot be assigned to a hotbar.
>> 2029, Fountain of Fire, Sustaining fire damage over time.
        """
        id = 16514
        name = {'Fountain of Fire', '灵泉之炎'}

    class BrandOfPurgatory(ActionBase):
        """
Deals fire damage with a potency of 180 to target and all enemies nearby it.
Can only be executed while under the effect of Firebird Trance.
※This action cannot be assigned to a hotbar.
        """
        id = 16515
        name = {'炼狱之炎', 'Brand of Purgatory'}

    class EnkindlePhoenix(ActionBase):
        """
Orders Demi-Phoenix to execute Revelation.
Revelation Effect: Deals fire damage to target and all enemies nearby it with a potency of 1,300 for the first enemy, and 60% less for all remaining enemies
Action replaces Enkindle Bahamut while Demi-Phoenix is summoned.
※This action cannot be assigned to a hotbar.
        """
        id = 16516
        name = {'不死鸟迸发', 'Enkindle Phoenix'}

    class EverlastingFlight(ActionBase):
        """
Gradually restores own HP and the HP of all nearby party members.
Cure Potency: 100
Duration: 21s
※This action cannot be assigned to a hotbar.
>> 1868, Everlasting Flight, Regenerating HP over time.
>> 2030, Everlasting Flight, Regenerating HP over time.
        """
        id = 16517
        name = {'不死鸟之翼', 'Everlasting Flight'}

    class Revelation(ActionBase):
        """
Deals fire damage to target and all enemies nearby it with a potency of 1,300 for the first enemy, and 60% less for all remaining enemies.
Can only be executed while Demi-Phoenix is summoned.
※This action cannot be assigned to a hotbar.
        """
        id = 16518
        name = {'天启', 'Revelation'}

    class ScarletFlame(ActionBase):
        """
Deals fire damage with a potency of 150.
Will only execute while Demi-Phoenix is summoned.
※This action cannot be assigned to a hotbar.
        """
        id = 16519
        name = {'Scarlet Flame', '赤焰'}

    class Rekindle(ActionBase):
        """
Restores own or target party member's HP.
Cure Potency: 400
Additional Effect: Grants Rekindle to target
Duration: 30s
Rekindle Effect: Healing over time when HP falls below 75% or upon effect duration expiration
Cure Potency: 200
Duration: 15s
Can only be executed while in Firebird Trance.
※This action cannot be assigned to a hotbar.
>> 2704, Rekindle, Undying Flame will be triggered upon HP falling below a certain level or expiration of effect duration.
        """
        id = 25830
        name = {'Rekindle', '再生之炎'}

    class SummonPhoenix(ActionBase):
        """
Enters Firebird Trance and summons Demi-Phoenix to fight by your side, which executes Everlasting Flight as it manifests.
Demi-Phoenix will execute Scarlet Flame automatically on the targets attacked by you after summoning.
Increases enmity in target when Demi-Phoenix is summoned.
Duration: 15s
Additional Effect: Changes Ruin III to Fountain of Fire and Tri-disaster to Brand of Purgatory
Additional Effect: Grants Ruby Arcanum, Topaz Arcanum, and Emerald Arcanum
Can only be executed in combat and while Carbuncle is summoned.
        """
        id = 25831
        name = {'Summon Phoenix', '不死鸟召唤'}

    class RubyCatastrophe(ActionBase):
        """
Deals fire damage with a potency of 180 to target and all enemies nearby it.
Fire Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25832
        name = {'Ruby Catastrophe', '红宝石之灾'}

    class TopazCatastrophe(ActionBase):
        """
Deals earth damage with a potency of 140 to target and all enemies nearby it.
(source.job==27?(source.level>=86?Additional Effect: Grants Titan's Favor
Effect of Titan's Favor ends upon execution of certain summoner actions.
:):)Earth Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25833
        name = {'Topaz Catastrophe', '黄宝石之灾'}

    class EmeraldCatastrophe(ActionBase):
        """
Deals wind damage with a potency of 100 to target and all enemies nearby it.
Wind Attunement Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 25834
        name = {'Emerald Catastrophe', '绿宝石之灾'}

    class CrimsonCyclone(ActionBase):
        """
Rushes forward and delivers a fire attack to target and all enemies nearby it with a potency of 430 for the first enemy, and 65% less for all remaining enemies.
Can only be executed while under the effect of Ifrit's Favor.
Cannot be executed while bound.
※Action changes to Crimson Strike upon execution.
※This action cannot be assigned to a hotbar.
        """
        id = 25835
        name = {'Crimson Cyclone', '深红旋风'}

    class MountainBuster(ActionBase):
        """
Deals earth damage to target and all enemies nearby it with a potency of 150 for the first enemy, and 70% less for all remaining enemies.
Can only be executed while under the effect of Titan's Favor.
※This action cannot be assigned to a hotbar.
        """
        id = 25836
        name = {'Mountain Buster', '山崩'}

    class Slipstream(ActionBase):
        """
Deals wind damage to target and all enemies nearby it with a potency of 430 for the first enemy, and 65% less for all remaining enemies.
Additional Effect: Creates a windstorm centered around the target, dealing damage to any enemies who enter
Potency: 30
Duration: 15s
Can only be executed while under the effect of Garuda's Favor.
※This action cannot be assigned to a hotbar.
>> 2706, Slipstream, Maintaining a localized windstorm.
        """
        id = 25837
        name = {'Slipstream', '螺旋气流'}

    class CrimsonStrike(ActionBase):
        """
Deals fire damage to target and all enemies nearby it with a potency of 430 for the first enemy, and 65% less for all remaining enemies.
Combo Action: Crimson Cyclone
※This action cannot be assigned to a hotbar.
        """
        id = 25885
        name = {'Crimson Strike', '深红强袭'}
        combo_action = 25835

    class SummonIfritIi(ActionBase):
        """
Summons Ruby Ifrit and orders it to execute Inferno.
Inferno Effect: Deals fire damage to target and all enemies within 5 yalms with a potency of 700 for the first enemy, and 60% less for all remaining enemies
Additional Effect: Grants 2 stacks of Fire Attunement
Duration: 30s
Fire Attunement Effect: Gemshine and Precious Brilliance become fire-aspected
Additional Effect: Grants Ifrit's Favor
Effect of Ifrit's Favor ends upon execution of certain summoner actions.
Can only be executed while under the effect of Ruby Arcanum and Carbuncle is summoned.
        """
        id = 25838
        name = {'Summon Ifrit II', '火神召唤II'}

    class SummonTitanIi(ActionBase):
        """
Summons Topaz Titan and orders it to execute Earthen Fury.
Earthen Fury Effect: Deals earth damage to target and all enemies within 5 yalms with a potency of 700 for the first enemy, and 60% less for all remaining enemies
Additional Effect: Grants 4 stacks of Earth Attunement
Duration: 30s
Earth Attunement Effect: Gemshine and Precious Brilliance become earth-aspected
Can only be executed while under the effect of Topaz Arcanum and Carbuncle is summoned.
        """
        id = 25839
        name = {'Summon Titan II', '土神召唤II'}

    class SummonGarudaIi(ActionBase):
        """
Summons Emerald Garuda and orders it to execute Aerial Blast.
Aerial Blast Effect: Deals wind damage to target and all enemies within 5 yalms with a potency of 700 for the first enemy, and 60% less for all remaining enemies
Additional Effect: Grants 4 stacks of Wind Attunement
Duration: 30s
Wind Attunement Effect: Gemshine and Precious Brilliance become wind-aspected
Additional Effect: Grants Garuda's Favor
Effect of Garuda's Favor ends upon execution of certain summoner actions.
Can only be executed while under the effect of Emerald Arcanum and Carbuncle is summoned.
        """
        id = 25840
        name = {'Summon Garuda II', '风神召唤II'}
