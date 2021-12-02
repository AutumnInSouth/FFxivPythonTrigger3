from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Ruin(ActionBase):
        """
        Deals unaspected damage with a potency of 180.
        """
        id = 163
        name = {"Ruin", "毁灭"}

    class Bio(ActionBase):
        """
        Deals unaspected damage over time. Potency: 20 Duration: 30s
        179, Bio, Bio, Contagions are spreading, causing damage over time.
        """
        id = 164
        name = {"Bio", "毒菌"}

    class Summon(ActionBase):
        """
        Summons a caster-type pet to fight at your side. Shares a recast timer with (source.job==27?Summon II and Summon III:Summon II).
        """
        id = 165
        name = {"Summon", "召唤"}

    class Miasma(ActionBase):
        """
        Deals unaspected damage with a potency of 20. Additional Effect: Unaspected damage over time Potency: 20 Duration: 30s
        180, Miasma, Miasma, Lungs are failing, causing damage over time.
        """
        id = 168
        name = {"Miasma", "瘴气"}

    class SummonIi(ActionBase):
        """
        Summons a support-type pet to fight at your side. Shares a recast timer with (source.job==27?Summon and Summon III:Summon).
        """
        id = 170
        name = {"Summon II", "召唤II"}

    class RuinIi(ActionBase):
        """
        Deals unaspected damage with a potency of 160.
        """
        id = 172
        name = {"Ruin II", "毁坏"}

    class Bane(ActionBase):
        """
        Spreads a target's Bio and Miasma effects to nearby enemies. Potency is reduced by 60% for all remaining enemies. (source.job==27?(source.level>=78?Duration: Full duration of original effects:Duration: Time remaining on original effects Additional Effect: 15% chance that Bio and Miasma durations reset if shorter than original effect duration):Duration: Time remaining on original effects Additional Effect: 15% chance that Bio and Miasma durations reset if shorter than original effect duration) No effect if target is not suffering from Bio or Miasma effects inflicted by you.
        """
        id = 174
        name = {"Bane", "灾祸"}

    class BioIi(ActionBase):
        """
        Deals unaspected damage over time. Potency: 30 Duration: 30s
        189, Bio II, Bio II, Lungs are failing, causing damage over time.
        """
        id = 178
        name = {"Bio II", "猛毒菌"}

    class SummonIii(ActionBase):
        """
        Summons an attacker-type pet to fight at your side. Shares a recast timer with Summon and Summon II.
        """
        id = 180
        name = {"Summon III", "召唤III"}

    class Fester(ActionBase):
        """
        Deals unaspected damage with a potency of 100. Additional Effect: If target is suffering from a Bio or Miasma effect inflicted by you, Fester potency is increased to 200 for one effect, or 300 for both Effect only applies when the original spells were cast by you. Aetherflow Gauge Cost: 1
        """
        id = 181
        name = {"Fester", "溃烂爆发"}

    class Enkindle(ActionBase):
        """
        Commands pet to use its signature attack. Can only be executed while in combat.
        """
        id = 184
        name = {"Enkindle", "内力迸发"}

    class Gouge(ActionBase):
        """
        Deals earth damage with a potency of 40. ※This action cannot be assigned to a hotbar.
        """
        id = 633
        name = {"Gouge", "利爪"}

    class ShiningTopaz(ActionBase):
        """
        Deals earth damage with a potency of 200 to all nearby enemies. ※This action cannot be assigned to a hotbar.
        """
        id = 634
        name = {"Shining Topaz", "黄宝石之光"}

    class Gust(ActionBase):
        """
        Deals wind damage with a potency of 20 to target and all enemies nearby it. ※This action cannot be assigned to a hotbar.
        """
        id = 637
        name = {"Gust", "突风"}

    class Downburst(ActionBase):
        """
        Deals wind damage with a potency of 100 to target and all enemies nearby it. ※This action cannot be assigned to a hotbar.
        """
        id = 639
        name = {"Downburst", "下行突风"}

    class RockBuster(ActionBase):
        """
        Deals earth damage with a potency of 60. ※This action cannot be assigned to a hotbar.
        """
        id = 787
        name = {"Rock Buster", "碎岩"}

    class MountainBuster(ActionBase):
        """
        Deals earth damage with a potency of 250 to all nearby enemies. ※This action cannot be assigned to a hotbar.
        """
        id = 788
        name = {"Mountain Buster", "山崩"}

    class EarthenFury(ActionBase):
        """
        Deals earth damage with a potency of 300 to all nearby targets. Additional Effect: Creates an area of molten earth around the caster, dealing damage to any enemies who enter Potency: 20  Duration: 15s ※This action cannot be assigned to a hotbar.
        """
        id = 791
        name = {"Earthen Fury", "大地之怒"}

    class WindBlade(ActionBase):
        """
        Deals wind damage with a potency of 30 to target and all enemies nearby it. ※This action cannot be assigned to a hotbar.
        """
        id = 792
        name = {"Wind Blade", "烈风刃"}

    class AerialSlash(ActionBase):
        """
        Deals wind damage with a potency of 150 to target and all enemies nearby it. ※This action cannot be assigned to a hotbar.
        """
        id = 794
        name = {"Aerial Slash", "大气风斩"}

    class AerialBlast(ActionBase):
        """
        Deals wind damage with a potency of 350 to target and all enemies nearby it. ※This action cannot be assigned to a hotbar.
        """
        id = 796
        name = {"Aerial Blast", "大气爆发"}

    class CrimsonCyclone(ActionBase):
        """
        Deals fire damage with a potency of 250. ※This action cannot be assigned to a hotbar.
        """
        id = 797
        name = {"Crimson Cyclone", "深红旋风"}

    class BurningStrike(ActionBase):
        """
        Deals fire damage with a potency of 80. ※This action cannot be assigned to a hotbar.
        """
        id = 798
        name = {"Burning Strike", "燃火强袭"}

    class FlamingCrush(ActionBase):
        """
        Deals fire damage to all nearby enemies with a potency of 250 for the first enemy, and 50% less for all remaining enemies. ※This action cannot be assigned to a hotbar.
        """
        id = 800
        name = {"Flaming Crush", "烈焰碎击"}

    class Inferno(ActionBase):
        """
        Deals fire damage with a potency of 300 to all enemies in a cone before it. Additional Effect: Fire damage over time Potency: 20 Duration: 15s ※This action cannot be assigned to a hotbar.
        314, Inferno, Inferno, Sustaining fire damage over time.
        """
        id = 801
        name = {"Inferno", "地狱之火炎"}

    class Painflare(ActionBase):
        """
        Deals unaspected damage with a potency of 130 to target and all enemies nearby it. Aetherflow Gauge Cost: 1
        """
        id = 3578
        name = {"Painflare", "痛苦核爆"}

    class RuinIii(ActionBase):
        """
        Deals unaspected damage with a potency of 200.
        """
        id = 3579
        name = {"Ruin III", "毁荡"}

    class TriDisaster(ActionBase):
        """
        Deals unaspected damage with a potency of 150. Additional Effect: Afflicts target with (source.level>=66?(source.job==27?Bio III and Miasma III:Bio II and Miasma):Bio II and Miasma) Duration: 30s
        """
        id = 3580
        name = {"Tri-disaster", "三重灾祸"}

    class DreadwyrmTrance(ActionBase):
        """
        Reduces spell casting time by 2.5 seconds. Duration: 15s Additional Effect: Resets Tri-disaster recast timer(source.level>=70?(source.job==27? Additional Effect: (source.job==27?(source.level>=72?Grants 2 units of Dreadwyrm Aether when effect ends:Grants 1 unit of Dreadwyrm Aether when effect ends):Grants 1 unit of Dreadwyrm Aether when effect ends) Can only be executed while in combat. Cannot be executed with maximum units of Dreadwyrm Aether or when Demi-Bahamut is summoned.: Can only be executed while in combat.): Can only be executed while in combat.)(source.job==27?(source.level>=72? Shares a recast timer with Firebird Trance.:):)
        808, Dreadwyrm Trance, Dreadwyrm Trance, Drawing on the power of Bahamut, increasing magic damage dealt.
        """
        id = 3581
        name = {"Dreadwyrm Trance", "龙神附体"}

    class Deathflare(ActionBase):
        """
        Deals unaspected damage to target and all enemies nearby it with a potency of 400 for the first enemy, and 50% less for all remaining enemies. Can only be executed while in Dreadwyrm Trance. Dreadwyrm Trance fades upon execution.
        """
        id = 3582
        name = {"Deathflare", "死星核爆"}

    class Aetherpact(ActionBase):
        """
        Orders pet to execute Devotion. Devotion Effect: Increases damage dealt by all party members within a 15-yalm radius by 5% Duration: 15s
        """
        id = 7423
        name = {"Aetherpact", "以太契约"}

    class BioIii(ActionBase):
        """
        Deals unaspected damage over time. Potency: 45 Duration: 30s
        1214, Bio III, Bio III, Contagions are spreading, causing damage over time.
        1326, Bio III, Bio III, Contagions are spreading, causing damage over time.
        """
        id = 7424
        name = {"Bio III", "剧毒菌"}

    class MiasmaIii(ActionBase):
        """
        Deals unaspected damage with a potency of 45. Additional Effect: Unaspected damage over time Potency: 45 Duration: 30s
        1215, Miasma III, Miasma III, Lungs are failing, causing damage over time.
        1327, Miasma III, Miasma III, Lungs are failing, causing damage over time and reducing HP recovery.
        """
        id = 7425
        name = {"Miasma III", "瘴暍"}

    class RuinIv(ActionBase):
        """
        Deals unaspected damage with a potency of 300. Can only be executed while under the effect of Further Ruin. ※This action cannot be assigned to a hotbar.
        """
        id = 7426
        name = {"Ruin IV", "毁绝"}

    class SummonBahamut(ActionBase):
        """
        Summons Demi-Bahamut to fight by your side. Each time you cast a spell on an enemy, Demi-Bahamut will execute Wyrmwave on the same target. Duration: 20s Dreadwyrm Aether Cost: 2 Cannot summon Demi-Bahamut unless a pet is already summoned. Current pet will leave the battlefield while Demi-Bahamut is present, and return once gone. Cannot use while under the effect of Dreadwyrm Trance.
        """
        id = 7427
        name = {"Summon Bahamut", "龙神召唤"}

    class Wyrmwave(ActionBase):
        """
        Deals unaspected damage with a potency of 150. Will only execute while Demi-Bahamut is summoned. ※This action cannot be assigned to a hotbar.
        """
        id = 7428
        name = {"Wyrmwave", "真龙波"}

    class EnkindleBahamut(ActionBase):
        """
        Orders Demi-Bahamut to execute Akh Morn. Akh Morn Effect: Deals unaspected damage to target and all enemies nearby it with a potency of 650 for the first enemy, and 50% less for all remaining enemies(source.job==27?(source.level>=80? Shares a recast timer with Enkindle Phoenix.:):)
        """
        id = 7429
        name = {"Enkindle Bahamut", "龙神迸发"}

    class AkhMorn(ActionBase):
        """
        Deals unaspected damage to target and all enemies nearby it with a potency of 650 for the first enemy, and 50% less for all remaining enemies. Can only be executed while Demi-Bahamut is summoned. ※This action cannot be assigned to a hotbar.
        """
        id = 7449
        name = {"Akh Morn", "死亡轮回"}

    class Devotion(ActionBase):
        """
        Increases damage dealt by all party members within a 15-yalm radius by 5%. Duration: 15s ※This action cannot be assigned to a hotbar.
        1213, Devotion, Devotion, Damage dealt is increased.
        """
        id = 7450
        name = {"Devotion", "灵护"}

    class Physick(ActionBase):
        """
        Restores target's HP. Cure Potency: 400
        """
        id = 16230
        name = {"Physick", "医术"}

    class EnergyDrain(ActionBase):
        """
        Deals unaspected damage with a potency of 100. Additional Effect: Aetherflow II(source.job==27?(source.level>=35? Shares a recast timer with Energy Siphon.:):)
        """
        id = 16508
        name = {"Energy Drain", "能量吸收"}

    class EgiAssault(ActionBase):
        """
        (source.job==27?Orders your Egi to use Aerial Slash if Garuda-Egi is summoned, Crimson Cyclone if Ifrit-Egi is summoned, or Earthen Armor if Titan-Egi is summoned.:Orders your Carbuncle to use Downburst if Emerald Carbuncle is summoned or Glittering Topaz if Topaz Carbuncle is summoned.) Maximum Charges: 2 Can only be executed while in combat.
        """
        id = 16509
        name = {"Egi Assault", "灵攻I"}

    class EnergySiphon(ActionBase):
        """
        Deals unaspected damage with a potency of 40 to target and all enemies nearby it. Additional Effect: Aetherflow II Shares a recast timer with Energy Drain.
        """
        id = 16510
        name = {"Energy Siphon", "能量抽取"}

    class Outburst(ActionBase):
        """
        Deals unaspected damage with a potency of (source.job==27?(source.level>=76?90:70):70) to target and all enemies nearby it.
        """
        id = 16511
        name = {"Outburst", "迸裂"}

    class EgiAssaultIi(ActionBase):
        """
        (source.job==27?Orders your Egi to use Slipstream if Garuda-Egi is summoned, Flaming Crush if Ifrit-Egi is summoned, or Mountain Buster if Titan-Egi is summoned.:Orders your Carbuncle to use Glittering Emerald if Emerald Carbuncle is summoned or Shining Topaz if Topaz Carbuncle is summoned.) Maximum Charges: 2 Can only be executed while in combat.
        """
        id = 16512
        name = {"Egi Assault II", "灵攻II"}

    class FirebirdTrance(ActionBase):
        """
        Reduces spell casting time by 2.5 seconds. Duration: 20s Additional Effect: Resets Tri-disaster recast timer Additional Effect: Changes Ruin III to Fountain of Fire and Outburst to Brand of Purgatory Can only be executed after summoning Demi-Bahamut. Dreadwyrm Trance is changed to Firebird Trance upon Demi-Bahamut leaving the battlefield. Shares a recast timer with Dreadwyrm Trance. ※This action cannot be assigned to a hotbar.
        """
        id = 16513
        name = {"Firebird Trance", "不死鸟附体"}

    class FountainOfFire(ActionBase):
        """
        Deals fire damage with a potency of 250. Additional Effect: Grants Hellish Conduit Duration: 10s Can only be executed while under the effect of Firebird Trance. ※This action cannot be assigned to a hotbar.
        2029, Fountain of Fire, Fountain of Fire, Sustaining fire damage over time.
        """
        id = 16514
        name = {"Fountain of Fire", "灵泉之炎"}

    class BrandOfPurgatory(ActionBase):
        """
        Deals fire damage to target and all enemies nearby it with a potency of 350 for the first enemy, and 50% less for all remaining enemies. Can only be executed while under the effects of both Firebird Trance and Hellish Conduit. ※This action cannot be assigned to a hotbar.
        """
        id = 16515
        name = {"Brand of Purgatory", "炼狱之炎"}

    class EnkindlePhoenix(ActionBase):
        """
        Orders Demi-Phoenix to execute Revelation. Revelation Effect: Deals fire damage to target and all enemies nearby it with a potency of 650 for the first enemy, and 50% less for all remaining enemies Action replaces Enkindle Bahamut while Demi-Phoenix is summoned. Shares a recast timer with Enkindle Bahamut. ※This action cannot be assigned to a hotbar.
        """
        id = 16516
        name = {"Enkindle Phoenix", "不死鸟迸发"}

    class EverlastingFlight(ActionBase):
        """
        Gradually restores own HP and the HP of all nearby party members. Cure Potency: 100 Duration: 21s ※This action cannot be assigned to a hotbar.
        1868, Everlasting Flight, Everlasting Flight, Regenerating HP over time.
        2030, Everlasting Flight, Everlasting Flight, Regenerating HP over time.
        """
        id = 16517
        name = {"Everlasting Flight", "不死鸟之翼"}

    class Revelation(ActionBase):
        """
        Deals fire damage to target and all enemies nearby it with a potency of 650 for the first enemy, and 50% less for all remaining enemies. Can only be executed while Demi-Phoenix is summoned. ※This action cannot be assigned to a hotbar.
        """
        id = 16518
        name = {"Revelation", "天启"}

    class ScarletFlame(ActionBase):
        """
        Deals fire damage with a potency of 150. Will only execute while Demi-Phoenix is summoned. ※This action cannot be assigned to a hotbar.
        """
        id = 16519
        name = {"Scarlet Flame", "赤焰"}

    class GlitteringTopaz(ActionBase):
        """
        Creates a barrier around you that absorbs damage totaling 30% of your maximum HP. Duration: 30s ※This action cannot be assigned to a hotbar.
        """
        id = 16520
        name = {"Glittering Topaz", "黄宝石之辉"}

    class GlitteringEmerald(ActionBase):
        """
        Deals wind damage with a potency of 30 to target and all enemies nearby it. Additional Effect: Creates a windstorm centered around the target, dealing damage to any enemies who enter Potency: 30 Duration: 9s ※This action cannot be assigned to a hotbar.
        """
        id = 16521
        name = {"Glittering Emerald", "绿宝石之辉"}

    class EarthenArmor(ActionBase):
        """
        Creates a barrier around you that absorbs damage totaling 30% of your maximum HP. Duration: 30s ※This action cannot be assigned to a hotbar.
        """
        id = 16522
        name = {"Earthen Armor", "大地之铠"}

    class Slipstream(ActionBase):
        """
        Deals wind damage with a potency of 50 to target and all enemies nearby it. Additional Effect: Creates a windstorm centered around the target, dealing damage to any enemies who enter Potency: 50 Duration: 9s ※This action cannot be assigned to a hotbar.
        """
        id = 16523
        name = {"Slipstream", "螺旋气流"}

    class FirebirdTrance(ActionBase):
        """
        Summons Demi-Phoenix to fight by your side, which executes Everlasting Flight as it manifests. Each time you cast a spell on an enemy, Demi-Phoenix will execute Scarlet Flame on the same target. Duration: 20s Additional Effect: Reduces spell casting time by 2.5 seconds Duration: 20s Additional Effect: Resets Tri-disaster recast timer Additional Effect: Changes Ruin III to Fountain of Fire and Outburst to Brand of Purgatory Cannot summon Demi-Phoenix unless a pet is already summoned. Current pet will leave the battlefield while Demi-Phoenix is present, and return once gone. Can only be executed after summoning Demi-Bahamut. Dreadwyrm Trance is changed to Firebird Trance upon Demi-Bahamut leaving the battlefield. Shares a recast timer with Dreadwyrm Trance. ※This action cannot be assigned to a hotbar.
        """
        id = 16549
        name = {"Firebird Trance", "不死鸟附体"}

    class AssaultIGlitteringTopaz(ActionBase):
        """
        Orders Topaz Carbuncle to execute Glittering Topaz. Glittering Topaz Effect: Creates a barrier around you that absorbs damage totaling 30% of your maximum HP Duration: 30s Maximum Charges: 2 Can only be executed while in combat.
        """
        id = 16791
        name = {"Assault I: Glittering Topaz", "灵攻I：黄宝石之辉"}

    class AssaultIiShiningTopaz(ActionBase):
        """
        Orders Topaz Carbuncle to execute Shining Topaz. Shining Topaz Effect: Deals earth damage with a potency of 200 to all nearby enemies Maximum Charges: 2 Can only be executed while in combat.
        """
        id = 16792
        name = {"Assault II: Shining Topaz", "灵攻II：黄宝石之光"}

    class AssaultIDownburst(ActionBase):
        """
        Orders Emerald Carbuncle to execute Downburst. Downburst Effect: Deals wind damage with a potency of 100 to target and all enemies nearby it Maximum Charges: 2 Can only be executed while in combat.
        """
        id = 16793
        name = {"Assault I: Downburst", "灵攻I：下行突风"}

    class AssaultIiGlitteringEmerald(ActionBase):
        """
        Orders Emerald Carbuncle to execute Glittering Emerald. Glittering Emerald Effect: Deals wind damage with a potency of 30 to target and all enemies nearby it Additional Effect: Creates a windstorm centered around the target, dealing damage to any enemies who enter Potency: 30 Duration: 9s Maximum Charges: 2 Can only be executed while in combat.
        """
        id = 16794
        name = {"Assault II: Glittering Emerald", "灵攻II：绿宝石之辉"}

    class AssaultIEarthenArmor(ActionBase):
        """
        Orders Titan-Egi to execute Earthen Armor. Earthen Armor Effect: Creates a barrier around you that absorbs damage totaling 30% of your maximum HP Duration: 30s Maximum Charges: 2 Can only be executed while in combat.
        """
        id = 16795
        name = {"Assault I: Earthen Armor", "灵攻I：大地之铠"}

    class AssaultIiMountainBuster(ActionBase):
        """
        Orders Titan-Egi to execute Mountain Buster. Mountain Buster Effect: Deals earth damage with a potency of 250 to all nearby enemies Maximum Charges: 2 Can only be executed while in combat.
        """
        id = 16796
        name = {"Assault II: Mountain Buster", "灵攻II：山崩"}

    class AssaultIAerialSlash(ActionBase):
        """
        Orders Garuda-Egi to execute Aerial Slash. Aerial Slash Effect: Deals wind damage with a potency of 150 to target and all enemies nearby it Maximum Charges: 2 Can only be executed while in combat.
        """
        id = 16797
        name = {"Assault I: Aerial Slash", "灵攻I：大气风斩"}

    class AssaultIiSlipstream(ActionBase):
        """
        Orders Garuda-Egi to execute Slipstream. Slipstream Effect: Deals wind damage with a potency of 50 to target and all enemies nearby it Additional Effect: Creates a windstorm centered around the target, dealing damage to any enemies who enter Potency: 50 Duration: 9s Maximum Charges: 2 Can only be executed while in combat.
        """
        id = 16798
        name = {"Assault II: Slipstream", "灵攻II：螺旋气流"}

    class AssaultICrimsonCyclone(ActionBase):
        """
        Orders Ifrit-Egi to execute Crimson Cyclone. Crimson Cyclone Effect: Deals fire damage with a potency of 250 Maximum Charges: 2 Can only be executed while in combat.
        """
        id = 16799
        name = {"Assault I: Crimson Cyclone", "灵攻I：深红旋风"}

    class AssaultIiFlamingCrush(ActionBase):
        """
        Orders Ifrit-Egi to execute Flaming Crush. Flaming Crush Effect: Deals fire damage to all nearby enemies with a potency of 250 for the first enemy, and 50% less for all remaining enemies Maximum Charges: 2 Can only be executed while in combat.
        """
        id = 16800
        name = {"Assault II: Flaming Crush", "灵攻II：烈焰碎击"}

    class EnkindleEarthenFury(ActionBase):
        """
        Orders Titan-Egi to execute Earthen Fury. Earthen Fury Effect: Deals earth damage with a potency of 300 to all nearby targets Additional Effect: Creates an area of molten earth around the caster, dealing damage to any enemies who enter Potency: 20  Duration: 15s Can only be executed while in combat.
        """
        id = 16801
        name = {"Enkindle: Earthen Fury", "内力迸发：大地之怒"}

    class EnkindleAerialBlast(ActionBase):
        """
        Orders Garuda-Egi to execute Aerial Blast. Aerial Blast Effect: Deals wind damage with a potency of 350 to target and all enemies nearby it Can only be executed while in combat.
        """
        id = 16802
        name = {"Enkindle: Aerial Blast", "内力迸发：大气爆发"}

    class EnkindleInferno(ActionBase):
        """
        Orders Ifrit-Egi to execute Inferno. Inferno Effect: Deals fire damage with a potency of 300 to all enemies in a cone before it Additional Effect: Fire damage over time Potency: 20 Duration: 15s Can only be executed while in combat.
        """
        id = 16803
        name = {"Enkindle: Inferno", "内力迸发：地狱之火炎"}
