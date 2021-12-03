from ..base import *


class Actions:

    class Ruin(ActionBase):
        """
Deals unaspected damage with a potency of 240.
        """
        id = 163
        name = {'毁灭', 'Ruin'}

    class Gouge(ActionBase):
        """
Deals earth damage with a potency of 40.
※This action cannot be assigned to a hotbar.
        """
        id = 633
        name = {'Gouge', '利爪'}

    class Gust(ActionBase):
        """
Deals wind damage with a potency of 20 to target and all enemies nearby it.
※This action cannot be assigned to a hotbar.
        """
        id = 637
        name = {'突风', 'Gust'}

    class RockBuster(ActionBase):
        """
Deals earth damage with a potency of 60.
※This action cannot be assigned to a hotbar.
        """
        id = 787
        name = {'Rock Buster', '碎岩'}

    class WindBlade(ActionBase):
        """
Deals wind damage with a potency of 30 to target and all enemies nearby it.
※This action cannot be assigned to a hotbar.
        """
        id = 792
        name = {'Wind Blade', '烈风刃'}

    class BurningStrike(ActionBase):
        """
Deals fire damage with a potency of 80.
※This action cannot be assigned to a hotbar.
        """
        id = 798
        name = {'燃火强袭', 'Burning Strike'}

    class Bio(ActionBase):
        """
Deals unaspected damage over time.
Potency: 20
Duration: 30s
    179, Bio, Contagions are spreading, causing damage over time.
        """
        id = 164
        name = {'Bio', '毒菌'}

    class Summon(ActionBase):
        """
Summons a caster-type pet to fight at your side.
Shares a recast timer with (source.job==27?Summon II and Summon III:Summon II).
        """
        id = 165
        name = {'Summon', '召唤'}

    class Physick(ActionBase):
        """
Restores target's HP.
Cure Potency: 400
        """
        id = 16230
        name = {'Physick', '医术'}

    class Miasma(ActionBase):
        """
Deals unaspected damage with a potency of 20.
Additional Effect: Unaspected damage over time
Potency: 20
Duration: 30s
    180, Miasma, Lungs are failing, causing damage over time.
        """
        id = 168
        name = {'Miasma', '瘴气'}

    class Downburst(ActionBase):
        """
Deals wind damage with a potency of 100 to target and all enemies nearby it.
※This action cannot be assigned to a hotbar.
        """
        id = 639
        name = {'Downburst', '下行突风'}

    class AerialSlash(ActionBase):
        """
Deals wind damage with a potency of 150 to target and all enemies nearby it.
※This action cannot be assigned to a hotbar.
        """
        id = 794
        name = {'Aerial Slash', '大气风斩'}

    class CrimsonCyclone(ActionBase):
        """
Deals fire damage with a potency of 250.
※This action cannot be assigned to a hotbar.
        """
        id = 797
        name = {'Crimson Cyclone', '深红旋风'}

    class EgiAssault(ActionBase):
        """
(source.job==27?Orders your Egi to use Aerial Slash if Garuda-Egi is summoned, Crimson Cyclone if Ifrit-Egi is summoned, or Earthen Armor if Titan-Egi is summoned.:Orders your Carbuncle to use Downburst if Emerald Carbuncle is summoned or Glittering Topaz if Topaz Carbuncle is summoned.)
Maximum Charges: 2
Can only be executed while in combat.
        """
        id = 16509
        name = {'Egi Assault', '灵攻I'}

    class GlitteringTopaz(ActionBase):
        """
Creates a barrier around you that absorbs damage totaling 30% of your maximum HP.
Duration: 30s
※This action cannot be assigned to a hotbar.
        """
        id = 16520
        name = {'黄宝石之辉', 'Glittering Topaz'}

    class EarthenArmor(ActionBase):
        """
Creates a barrier around you that absorbs damage totaling 30% of your maximum HP.
Duration: 30s
※This action cannot be assigned to a hotbar.
        """
        id = 16522
        name = {'大地之铠', 'Earthen Armor'}

    class AssaultIGlitteringTopaz(ActionBase):
        """
Orders Topaz Carbuncle to execute Glittering Topaz.
Glittering Topaz Effect: Creates a barrier around you that absorbs damage totaling 30% of your maximum HP
Duration: 30s
Maximum Charges: 2
Can only be executed while in combat.
        """
        id = 16791
        name = {'Assault I: Glittering Topaz', '灵攻I：黄宝石之辉'}

    class AssaultIDownburst(ActionBase):
        """
Orders Emerald Carbuncle to execute Downburst.
Downburst Effect: Deals wind damage with a potency of 100 to target and all enemies nearby it
Maximum Charges: 2
Can only be executed while in combat.
        """
        id = 16793
        name = {'灵攻I：下行突风', 'Assault I: Downburst'}

    class AssaultIEarthenArmor(ActionBase):
        """
Orders Titan-Egi to execute Earthen Armor.
Earthen Armor Effect: Creates a barrier around you that absorbs damage totaling 30% of your maximum HP
Duration: 30s
Maximum Charges: 2
Can only be executed while in combat.
        """
        id = 16795
        name = {'Assault I: Earthen Armor', '灵攻I：大地之铠'}

    class AssaultIAerialSlash(ActionBase):
        """
Orders Garuda-Egi to execute Aerial Slash.
Aerial Slash Effect: Deals wind damage with a potency of 150 to target and all enemies nearby it
Maximum Charges: 2
Can only be executed while in combat.
        """
        id = 16797
        name = {'灵攻I：大气风斩', 'Assault I: Aerial Slash'}

    class AssaultICrimsonCyclone(ActionBase):
        """
Orders Ifrit-Egi to execute Crimson Cyclone.
Crimson Cyclone Effect: Deals fire damage with a potency of 250
Maximum Charges: 2
Can only be executed while in combat.
        """
        id = 16799
        name = {'Assault I: Crimson Cyclone', '灵攻I：深红旋风'}

    class SummonIi(ActionBase):
        """
Summons a support-type pet to fight at your side.
Shares a recast timer with (source.job==27?Summon and Summon III:Summon).
        """
        id = 170
        name = {'Summon II', '召唤II'}

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
        name = {'能量吸收', 'Energy Drain'}

    class BioIi(ActionBase):
        """
Deals unaspected damage over time.
Potency: 30
Duration: 30s
    189, Bio II, Lungs are failing, causing damage over time.
        """
        id = 178
        name = {'猛毒菌', 'Bio II'}

    class Bane(ActionBase):
        """
Spreads a target's Bio and Miasma effects to nearby enemies.
Potency is reduced by 60% for all remaining enemies.
(source.job==27?(source.level>=78?Duration: Full duration of original effects:Duration: Time remaining on original effects
Additional Effect: 15% chance that Bio and Miasma durations reset if shorter than original effect duration):Duration: Time remaining on original effects
Additional Effect: 15% chance that Bio and Miasma durations reset if shorter than original effect duration)
No effect if target is not suffering from Bio or Miasma effects inflicted by you.
        """
        id = 174
        name = {'灾祸', 'Bane'}

    class SummonIii(ActionBase):
        """
Summons an attacker-type pet to fight at your side.
Shares a recast timer with Summon and Summon II.
        """
        id = 180
        name = {'Summon III', '召唤III'}

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

    class RuinIi(ActionBase):
        """
Deals unaspected damage with a potency of 270.
        """
        id = 172
        name = {'毁坏', 'Ruin II'}

    class ShiningTopaz(ActionBase):
        """
Deals earth damage with a potency of 200 to all nearby enemies.
※This action cannot be assigned to a hotbar.
        """
        id = 634
        name = {'Shining Topaz', '黄宝石之光'}

    class MountainBuster(ActionBase):
        """
Deals earth damage with a potency of 250 to all nearby enemies.
※This action cannot be assigned to a hotbar.
        """
        id = 788
        name = {'山崩', 'Mountain Buster'}

    class FlamingCrush(ActionBase):
        """
Deals fire damage to all nearby enemies with a potency of 250 for the first enemy, and 50% less for all remaining enemies.
※This action cannot be assigned to a hotbar.
        """
        id = 800
        name = {'Flaming Crush', '烈焰碎击'}

    class Outburst(ActionBase):
        """
Deals unaspected damage with a potency of 100 to target and all enemies nearby it.
        """
        id = 16511
        name = {'Outburst', '迸裂'}

    class EgiAssaultIi(ActionBase):
        """
(source.job==27?Orders your Egi to use Slipstream if Garuda-Egi is summoned, Flaming Crush if Ifrit-Egi is summoned, or Mountain Buster if Titan-Egi is summoned.:Orders your Carbuncle to use Glittering Emerald if Emerald Carbuncle is summoned or Shining Topaz if Topaz Carbuncle is summoned.)
Maximum Charges: 2
Can only be executed while in combat.
        """
        id = 16512
        name = {'Egi Assault II', '灵攻II'}

    class GlitteringEmerald(ActionBase):
        """
Deals wind damage with a potency of 30 to target and all enemies nearby it.
Additional Effect: Creates a windstorm centered around the target, dealing damage to any enemies who enter
Potency: 30
Duration: 9s
※This action cannot be assigned to a hotbar.
        """
        id = 16521
        name = {'绿宝石之辉', 'Glittering Emerald'}

    class Slipstream(ActionBase):
        """
Deals wind damage with a potency of 50 to target and all enemies nearby it.
Additional Effect: Creates a windstorm centered around the target, dealing damage to any enemies who enter
Potency: 50
Duration: 9s
※This action cannot be assigned to a hotbar.
    1869, Gale Enforcer, Maintaining a localized windstorm.
        """
        id = 16523
        name = {'Slipstream', '螺旋气流'}

    class AssaultIiShiningTopaz(ActionBase):
        """
Orders Topaz Carbuncle to execute Shining Topaz.
Shining Topaz Effect: Deals earth damage with a potency of 200 to all nearby enemies
Maximum Charges: 2
Can only be executed while in combat.
        """
        id = 16792
        name = {'Assault II: Shining Topaz', '灵攻II：黄宝石之光'}

    class AssaultIiGlitteringEmerald(ActionBase):
        """
Orders Emerald Carbuncle to execute Glittering Emerald.
Glittering Emerald Effect: Deals wind damage with a potency of 30 to target and all enemies nearby it
Additional Effect: Creates a windstorm centered around the target, dealing damage to any enemies who enter
Potency: 30
Duration: 9s
Maximum Charges: 2
Can only be executed while in combat.
        """
        id = 16794
        name = {'Assault II: Glittering Emerald', '灵攻II：绿宝石之辉'}

    class AssaultIiMountainBuster(ActionBase):
        """
Orders Titan-Egi to execute Mountain Buster.
Mountain Buster Effect: Deals earth damage with a potency of 250 to all nearby enemies
Maximum Charges: 2
Can only be executed while in combat.
        """
        id = 16796
        name = {'Assault II: Mountain Buster', '灵攻II：山崩'}

    class AssaultIiSlipstream(ActionBase):
        """
Orders Garuda-Egi to execute Slipstream.
Slipstream Effect: Deals wind damage with a potency of 50 to target and all enemies nearby it
Additional Effect: Creates a windstorm centered around the target, dealing damage to any enemies who enter
Potency: 50
Duration: 9s
Maximum Charges: 2
Can only be executed while in combat.
        """
        id = 16798
        name = {'Assault II: Slipstream', '灵攻II：螺旋气流'}

    class AssaultIiFlamingCrush(ActionBase):
        """
Orders Ifrit-Egi to execute Flaming Crush.
Flaming Crush Effect: Deals fire damage to all nearby enemies with a potency of 250 for the first enemy, and 50% less for all remaining enemies
Maximum Charges: 2
Can only be executed while in combat.
        """
        id = 16800
        name = {'Assault II: Flaming Crush', '灵攻II：烈焰碎击'}

    class Enkindle(ActionBase):
        """
Commands pet to use its signature attack.
Can only be executed while in combat.
        """
        id = 184
        name = {'内力迸发', 'Enkindle'}

    class EarthenFury(ActionBase):
        """
Deals earth damage with a potency of 300 to all nearby targets.
Additional Effect: Creates an area of molten earth around the caster, dealing damage to any enemies who enter
Potency: 20 
Duration: 15s
※This action cannot be assigned to a hotbar.
    312, Razed Earth, Jagged shards protrude from the ground, dealing earth damage to any who tread upon them.
        """
        id = 791
        name = {'Earthen Fury', '大地之怒'}

    class AerialBlast(ActionBase):
        """
Deals wind damage with a potency of 350 to target and all enemies nearby it.
※This action cannot be assigned to a hotbar.
        """
        id = 796
        name = {'大气爆发', 'Aerial Blast'}

    class Inferno(ActionBase):
        """
Deals fire damage with a potency of 300 to all enemies in a cone before it.
Additional Effect: Fire damage over time
Potency: 20
Duration: 15s
※This action cannot be assigned to a hotbar.
    314, Inferno, Sustaining fire damage over time.
        """
        id = 801
        name = {'Inferno', '地狱之火炎'}

    class EnkindleEarthenFury(ActionBase):
        """
Orders Titan-Egi to execute Earthen Fury.
Earthen Fury Effect: Deals earth damage with a potency of 300 to all nearby targets
Additional Effect: Creates an area of molten earth around the caster, dealing damage to any enemies who enter
Potency: 20 
Duration: 15s
Can only be executed while in combat.
        """
        id = 16801
        name = {'Enkindle: Earthen Fury', '内力迸发：大地之怒'}

    class EnkindleAerialBlast(ActionBase):
        """
Orders Garuda-Egi to execute Aerial Blast.
Aerial Blast Effect: Deals wind damage with a potency of 350 to target and all enemies nearby it
Can only be executed while in combat.
        """
        id = 16802
        name = {'内力迸发：大气爆发', 'Enkindle: Aerial Blast'}

    class EnkindleInferno(ActionBase):
        """
Orders Ifrit-Egi to execute Inferno.
Inferno Effect: Deals fire damage with a potency of 300 to all enemies in a cone before it
Additional Effect: Fire damage over time
Potency: 20
Duration: 15s
Can only be executed while in combat.
        """
        id = 16803
        name = {'Enkindle: Inferno', '内力迸发：地狱之火炎'}

    class Painflare(ActionBase):
        """
Deals unaspected damage with a potency of 150 to target and all enemies nearby it.
Aetherflow Gauge Cost: 1
        """
        id = 3578
        name = {'痛苦核爆', 'Painflare'}

    class RuinIii(ActionBase):
        """
Deals unaspected damage with a potency of (source.job==27?(source.level>=84?310:300):300).
        """
        id = 3579
        name = {'毁荡', 'Ruin III'}

    class TriDisaster(ActionBase):
        """
Deals unaspected damage with a potency of 150.
Additional Effect: Afflicts target with (source.level>=66?(source.job==27?Bio III and Miasma III:Bio II and Miasma):Bio II and Miasma)
Duration: 30s
        """
        id = 3580
        name = {'三重灾祸', 'Tri-disaster'}

    class DreadwyrmTrance(ActionBase):
        """
Enters Dreadwyrm Trance.
Duration: 15s
Additional Effect: Changes Ruin III to Astral Impulse and Outburst to Astral Flare
Additional Effect: Grants Ruby Arcanum, Topaz Arcanum, and Emerald Arcanum
Can only be executed in combat and while Carbuncle is summoned.
    808, Dreadwyrm Trance, Drawing on the power of Bahamut, increasing magic damage dealt.
        """
        id = 3581
        name = {'龙神附体', 'Dreadwyrm Trance'}

    class Deathflare(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 500 for the first enemy, and 60% less for all remaining enemies.
Can only be executed while in Dreadwyrm Trance.
※This action cannot be assigned to a hotbar.
        """
        id = 3582
        name = {'死星核爆', 'Deathflare'}

    class RuinIv(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 430 for the first enemy, and 60% less for all remaining enemies.
Can only be executed while under the effect of Further Ruin.
        """
        id = 7426
        name = {'Ruin IV', '毁绝'}

    class Aetherpact(ActionBase):
        """
Orders pet to execute Devotion.
Devotion Effect: Increases damage dealt by all party members within a 15-yalm radius by 5%
Duration: 15s
        """
        id = 7423
        name = {'以太契约', 'Aetherpact'}

    class Devotion(ActionBase):
        """
Increases damage dealt by all party members within a 15-yalm radius by 5%.
Duration: 15s
※This action cannot be assigned to a hotbar.
    1213, Devotion, Damage dealt is increased.
        """
        id = 7450
        name = {'Devotion', '灵护'}

    class BioIii(ActionBase):
        """
Deals unaspected damage over time.
Potency: 45
Duration: 30s
    1326, Bio III, Contagions are spreading, causing damage over time.
    1214, Bio III, Contagions are spreading, causing damage over time.
        """
        id = 7424
        name = {'剧毒菌', 'Bio III'}

    class MiasmaIii(ActionBase):
        """
Deals unaspected damage with a potency of 45.
Additional Effect: Unaspected damage over time
Potency: 45
Duration: 30s
    1327, Miasma III, Lungs are failing, causing damage over time and reducing HP recovery.
    1215, Miasma III, Lungs are failing, causing damage over time.
        """
        id = 7425
        name = {'Miasma III', '瘴暍'}

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
        name = {'Wyrmwave', '真龙波'}

    class EnkindleBahamut(ActionBase):
        """
Orders Demi-Bahamut to execute Akh Morn.
Akh Morn Effect: Deals unaspected damage to target and all enemies nearby it with a potency of 1,300 for the first enemy, and 60% less for all remaining enemies
        """
        id = 7429
        name = {'Enkindle Bahamut', '龙神迸发'}

    class AkhMorn(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 1,300 for the first enemy, and 60% less for all remaining enemies.
Can only be executed while Demi-Bahamut is summoned.
※This action cannot be assigned to a hotbar.
        """
        id = 7449
        name = {'死亡轮回', 'Akh Morn'}

    class FirebirdTrance(ActionBase):
        """
Reduces spell casting time by 2.5 seconds.
Duration: 20s
Additional Effect: Resets Tri-disaster recast timer
Additional Effect: Changes Ruin III to Fountain of Fire and Outburst to Brand of Purgatory
Can only be executed after summoning Demi-Bahamut.
Dreadwyrm Trance is changed to Firebird Trance upon Demi-Bahamut leaving the battlefield.
Shares a recast timer with Dreadwyrm Trance.
※This action cannot be assigned to a hotbar.
        """
        id = 16513
        name = {'Firebird Trance', '不死鸟附体'}

    class FountainOfFire(ActionBase):
        """
Deals fire damage with a potency of 430.
Can only be executed while under the effect of Firebird Trance.
※This action cannot be assigned to a hotbar.
    2029, Fountain of Fire, Sustaining fire damage over time.
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
        name = {'Brand of Purgatory', '炼狱之炎'}

    class FirebirdTrance(ActionBase):
        """
Summons Demi-Phoenix to fight by your side, which executes Everlasting Flight as it manifests. Each time you cast a spell on an enemy, Demi-Phoenix will execute Scarlet Flame on the same target.
Duration: 20s
Additional Effect: Reduces spell casting time by 2.5 seconds
Duration: 20s
Additional Effect: Resets Tri-disaster recast timer
Additional Effect: Changes Ruin III to Fountain of Fire and Outburst to Brand of Purgatory
Cannot summon Demi-Phoenix unless a pet is already summoned. Current pet will leave the battlefield while Demi-Phoenix is present, and return once gone.
Can only be executed after summoning Demi-Bahamut.
Dreadwyrm Trance is changed to Firebird Trance upon Demi-Bahamut leaving the battlefield.
Shares a recast timer with Dreadwyrm Trance.
※This action cannot be assigned to a hotbar.
        """
        id = 16549
        name = {'Firebird Trance', '不死鸟附体'}

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
    1868, Everlasting Flight, Regenerating HP over time.
    2030, Everlasting Flight, Regenerating HP over time.
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
        name = {'Revelation', '天启'}

    class ScarletFlame(ActionBase):
        """
Deals fire damage with a potency of 150.
Will only execute while Demi-Phoenix is summoned.
※This action cannot be assigned to a hotbar.
        """
        id = 16519
        name = {'Scarlet Flame', '赤焰'}
