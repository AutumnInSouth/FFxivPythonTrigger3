from ..base import *


class Status:
    class Combust(StatusBase):
        """
Deals unaspected damage over time.
Potency: 40
Duration: 18s
>> 838, Combust, Proximity of a theoretical sun is causing damage over time.
        """
        id = 838
        name = {'烧灼', 'Combust'}
        damage_potency = 40

    class Lightspeed(StatusBase):
        """
Reduces cast times for spells by 2.5 seconds.
Duration: 15s
>> 841, Lightspeed, Spell casting time is reduced.
>> 1403, Lightspeed, Spell casting time and MP cost are reduced by 100% and 50% respectively.
        """
        id = 841
        name = {'光速', 'Lightspeed'}

    class TheBalance(StatusBase):
        """
Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Solar Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
>> 1882, The Balance, Damage dealt is increased.
        """
        id = 1882
        name = {'the Balance', '太阳神之衡'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None', source_action: int, is_main_target: bool):
            super().__init__(source, target, source_action, is_main_target)
            self.damage_modify = 1.06 if target and target.job.is_melee else 1.03

    class TheArrow(StatusBase):
        """
Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Lunar Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
>> 1884, The Arrow, Damage dealt is increased.
        """
        id = 1884
        name = {'放浪神之箭', 'the Arrow'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None', source_action: int, is_main_target: bool):
            super().__init__(source, target, source_action, is_main_target)
            self.damage_modify = 1.06 if target and target.job.is_melee else 1.03

    class TheSpear(StatusBase):
        """
Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Celestial Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
>> 1885, The Spear, Damage dealt is increased.
        """
        id = 1885
        name = {'the Spear', '战争神之枪'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None', source_action: int, is_main_target: bool):
            super().__init__(source, target, source_action, is_main_target)
            self.damage_modify = 1.06 if target and target.job.is_melee else 1.03

    class TheBole(StatusBase):
        """
Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Solar Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
>> 1883, The Bole, Damage dealt is increased.
        """
        id = 1883
        name = {'世界树之干', 'the Bole'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None', source_action: int, is_main_target: bool):
            super().__init__(source, target, source_action, is_main_target)
            self.damage_modify = 1.03 if target and target.job.is_melee else 1.06

    class TheEwer(StatusBase):
        """
Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Lunar Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
>> 1886, The Ewer, Damage dealt is increased.
        """
        id = 1886
        name = {'the Ewer', '河流神之瓶'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None', source_action: int, is_main_target: bool):
            super().__init__(source, target, source_action, is_main_target)
            self.damage_modify = 1.03 if target and target.job.is_melee else 1.06

    class TheSpire(StatusBase):
        """
Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Celestial Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
>> 834, The Spire, Restoring TP over time.
>> 1341, The Spire, Restoring TP over time.
>> 1887, The Spire, Damage dealt is increased.
        """
        id = 1887
        name = {'建筑神之塔', 'the Spire'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None', source_action: int, is_main_target: bool):
            super().__init__(source, target, source_action, is_main_target)
            self.damage_modify = 1.03 if target and target.job.is_melee else 1.06

    class AspectedBenefic(StatusBase):
        """
Restores target's HP.
Cure Potency: (source.job==33?(source.level>=85?250:200):200)
Additional Effect: Regen
Cure Potency: (source.job==33?(source.level>=85?250:200):200)
Duration: 15s
>> 835, Aspected Benefic, Regenerating HP over time.
        """
        id = 835
        name = {'吉星相位', 'Aspected Benefic'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None', source_action: int, is_main_target: bool):
            super().__init__(source, target, source_action, is_main_target)
            self.cure_potency = 250 if source and source.job == 33 and source.level >= 85 else 200

    class AspectedHelios(StatusBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: (source.job==33?(source.level>=85?250:200):200)
Additional Effect: Regen
Cure Potency: (source.job==33?(source.level>=85?150:100):100)
Duration: 15s
>> 836, Aspected Helios, Regenerating HP over time.
        """
        id = 836
        name = {'Aspected Helios', '阳星相位'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None', source_action: int, is_main_target: bool):
            super().__init__(source, target, source_action, is_main_target)
            self.cure_potency = 150 if source and source.job == 33 and source.level >= 85 else 100

    class CombustII(StatusBase):
        """
Deals unaspected damage over time.
Potency: 50
Duration: 30s
>> 843, Combust II, Proximity of a theoretical sun is causing damage over time.
        """
        id = 843
        name = {'炽灼', 'Combust II'}
        damage_potency = 50

    class Divination(StatusBase):
        """
Increases damage dealt by self and nearby party members by 6%.
Duration: 15s
>> 2034, Divination, Damage dealt is increased while damage taken is reduced.
>> 1878, Divination, Damage dealt is increased.
        """
        id = 1878
        name = {'Divination', '占卜'}
        damage_modify = 1.06

    """
Grants an effect using the astrosigns read from your divining deck.
Can only be executed after reading three astrosigns.
Effects granted are determined by the number of different types of astrosigns read.
1 Sign Type: Grants Harmony of Spirit
2 Sign Types: Grants Harmony of Spirit and Harmony of Body
3 Sign Types: Grants Harmony of Spirit, Harmony of Body, and Harmony of Mind
Duration: 15s
Harmony of Spirit Effect: Gradually restores own MP
Potency: 50
Harmony of Body Effect: Reduces spell cast time and recast time, and auto-attack delay by 10%
Harmony of Mind Effect: Increases damage dealt and healing potency by 5%
    """

    class HarmonyOfSpirit(StatusBase):
        id = 2714
        name = {'Harmony of Spirit'}

    class HarmonyOfBody(StatusBase):
        id = 2715
        name = {'Harmony of Body'}

    class HarmonyOfMind(StatusBase):
        id = 2716
        name = {'Harmony of Mind'}
        damage_modify = 1.05
        cure_modify = 1.05

    class WheelOfFortune(StatusBase):
        id = 956
        name = {'Wheel of Fortune'}
        cure_potency = 100

    class CollectiveUnconscious(StatusBase):
        """
Creates a celestial ring around the caster.
Additional Effect: Reduces damage taken by 10% and applies Wheel of Fortune to self and any party members who enter
Duration: 18s
Wheel of Fortune Effect: Regen
Cure Potency: 100
Duration: 15s
Effect ends upon using another action or moving (including facing a different direction).
Cancels auto-attack upon execution.
>> 2283, Collective Unconscious, An area of mind attunement is created, reducing damage taken for all who enter.
>> 847, Collective Unconscious, An area of mind attunement is healing party members.
>> 848, Collective Unconscious, An area of mind attunement is created, reducing damage taken for all who enter.
>> 849, Collective Unconscious, Damage taken is reduced.
        """
        id = 849
        name = {'Collective Unconscious', '命运之轮'}
        taken_damage_modify = 1

    class Opposition(StatusBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 200
Additional Effect: Regen
Cure Potency: 100
Duration: 15s
        """
        id = 1879  # TODO:maybe 2070?
        name = {'Opposition'}
        cure_potency = 100

    class EarthlyDominance(StatusBase):
        id = 1224
        name = {'Earthly Dominance', '地星主宰'}

    class GiantDominance(StatusBase):
        id = 1248
        name = {'Giant Dominance', '巨星主宰'}

    class CombustIII(StatusBase):
        """
Deals unaspected damage over time.
Potency: 55
Duration: 30s
>> 1881, Combust III, Sustaining damage over time.
>> 2041, Combust III, Damage dealt and potency of all HP restoration actions are reduced.
        """
        id = 1881
        name = {'焚灼', 'Combust III'}
        damage_potency = 55

    class Horoscope(StatusBase):
        id = 1890
        name = {'Horoscope', '天宫图'}
        cure_potency = 200
        over_time_status = False

    class HoroscopeHelios(StatusBase):
        id = 1891
        name = {'Horoscope Helios', '阳星天宫图'}
        cure_potency = 400
        over_time_status = False


class Actions:
    class Malefic(ActionBase):
        """
Deals unaspected damage with a potency of 150.
        """
        id = 3596
        name = {'Malefic', '凶星'}
        damage_potency = 150
        attack_type = magic

    class Benefic(ActionBase):
        """
Restores target's HP.
Cure Potency: (source.job==33?(source.level>=85?500:450):450)(source.level>=36?(source.job==33?
Additional Effect: 15% chance next Benefic II will restore critical HP
Duration: 15s:):)
        """
        id = 3594
        name = {'吉星', 'Benefic'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.cure_potency = 500 if source and source.job == 33 and source.level >= 85 else 450

    class Combust(ActionBase):
        """
Deals unaspected damage over time.
Potency: 40
Duration: 18s
>> 838, Combust, Proximity of a theoretical sun is causing damage over time.
        """
        id = 3599
        name = {'烧灼', 'Combust'}
        status_to_target = Status.Combust

    class Lightspeed(ActionBase):
        """
Reduces cast times for spells by 2.5 seconds.
Duration: 15s
>> 841, Lightspeed, Spell casting time is reduced.
>> 1403, Lightspeed, Spell casting time and MP cost are reduced by 100% and 50% respectively.
        """
        id = 3606
        name = {'光速', 'Lightspeed'}
        status_to_target = Status.Lightspeed

    class Helios(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: (source.job==33?(source.level>=85?400:330):330)
        """
        id = 3600
        name = {'Helios', '阳星'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.cure_potency = 400 if source and source.job == 33 and source.level >= 85 else 330

    class Ascend(ActionBase):
        """
Resurrects target to a weakened state.
        """
        id = 3603
        name = {'Ascend', '生辰'}

    class EssentialDignity(ActionBase):
        """
Restores target's HP.
Cure Potency: 400
Potency increases up to 900 as the target's HP decreases, reaching its maximum value when the target has 30% HP or less.(source.job==33?(source.level>=78?
Maximum Charges: 2:):)
        """
        id = 3614
        name = {'先天禀赋', 'Essential Dignity'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            if target:
                self.cure_potency = int(400 + (900 - 400) * target.current_hp / target.max_hp)
            else:
                self.cure_potency = 400

    class BeneficII(ActionBase):
        """
Restores target's HP.
Cure Potency: (source.job==33?(source.level>=85?800:700):700)
        """
        id = 3610
        name = {'福星', 'Benefic II'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.cure_potency = 800 if source and source.job == 33 and source.level >= 85 else 700

    class Draw(ActionBase):
        """
Draws a card (arcanum) from your divining deck. Only one arcanum can be drawn at a time.
Arcanum effect can be triggered using the action Play.
Additional Effect: Restores 5% of maximum MP
(source.job==33?(source.level>=40?Additional Effect: Grants Clarifying Draw, allowing the execution of Redraw
:):)Maximum Charges: 2
        """
        id = 3590
        name = {'抽卡', 'Draw'}

    class TheBalance(ActionBase):
        """
Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Solar Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
>> 1338, The Balance, Damage dealt is increased.
>> 829, The Balance, Damage dealt is increased.
>> 1882, The Balance, Damage dealt is increased.
        """
        id = 4401
        name = {'the Balance', '太阳神之衡'}
        status_to_target = Status.TheBalance

    class TheArrow(ActionBase):
        """
Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Lunar Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
>> 1884, The Arrow, Damage dealt is increased.
>> 831, The Arrow, Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
        """
        id = 4402
        name = {'放浪神之箭', 'the Arrow'}
        status_to_target = Status.TheArrow

    class TheSpear(ActionBase):
        """
Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Celestial Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
>> 832, The Spear, Critical hit rate is increased.
>> 1885, The Spear, Damage dealt is increased.
        """
        id = 4403
        name = {'the Spear', '战争神之枪'}
        status_to_target = Status.TheSpear

    class TheBole(ActionBase):
        """
Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Solar Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
>> 1339, The Bole, Damage taken is reduced.
>> 1883, The Bole, Damage dealt is increased.
>> 830, The Bole, Damage taken is reduced.
        """
        id = 4404
        name = {'世界树之干', 'the Bole'}
        status_to_target = Status.TheBole

    class TheEwer(ActionBase):
        """
Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Lunar Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
>> 833, The Ewer, Restoring MP over time.
>> 1340, The Ewer, Restoring MP over time.
>> 1886, The Ewer, Damage dealt is increased.
        """
        id = 4405
        name = {'the Ewer', '河流神之瓶'}
        status_to_target = Status.TheEwer

    class TheSpire(ActionBase):
        """
Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Celestial Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
>> 834, The Spire, Restoring TP over time.
>> 1341, The Spire, Restoring TP over time.
>> 1887, The Spire, Damage dealt is increased.
        """
        id = 4406
        name = {'建筑神之塔', 'the Spire'}
        status_to_target = Status.TheSpire

    class Undraw(ActionBase):
        """
Returns the currently drawn arcanum back to your deck.
        """
        id = 9629
        name = {'奥秘卡废弃', 'Undraw'}

    class Play(ActionBase):
        """
Triggers the effect of your drawn arcanum.
        """
        id = 17055
        name = {'出卡', 'Play'}

    class AspectedBenefic(ActionBase):
        """
Restores target's HP.
Cure Potency: (source.job==33?(source.level>=85?250:200):200)
Additional Effect: Regen
Cure Potency: (source.job==33?(source.level>=85?250:200):200)
Duration: 15s
>> 835, Aspected Benefic, Regenerating HP over time.
        """
        id = 3595
        name = {'吉星相位', 'Aspected Benefic'}
        status_to_target = Status.AspectedBenefic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.cure_potency = 250 if source and source.job == 33 and source.level >= 85 else 200

    class Redraw(ActionBase):
        """
Draws a different arcanum from your deck.
Can only be executed while under the effect of Clarifying Draw.
        """
        id = 3593
        name = {'Redraw', '重抽'}

    class AspectedHelios(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: (source.job==33?(source.level>=85?250:200):200)
Additional Effect: Regen
Cure Potency: (source.job==33?(source.level>=85?150:100):100)
Duration: 15s
>> 836, Aspected Helios, Regenerating HP over time.
        """
        id = 3601
        name = {'Aspected Helios', '阳星相位'}
        status_to_target = Status.AspectedHelios

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.cure_potency = 250 if source and source.job == 33 and source.level >= 85 else 200

    class Gravity(ActionBase):
        """
Deals unaspected damage with a potency of 120 to target and all enemies nearby it.
        """
        id = 3615
        name = {'Gravity', '重力'}
        damage_potency = 120
        attack_type = magic

    class CombustII(ActionBase):
        """
Deals unaspected damage over time.
Potency: 50
Duration: 30s
>> 843, Combust II, Proximity of a theoretical sun is causing damage over time.
        """
        id = 3608
        name = {'炽灼', 'Combust II'}
        status_to_target = Status.CombustII
        attack_type = magic

    class Synastry(ActionBase):
        """
Generate an aetheric bond with target party member. Each time you cast a single-target healing spell on yourself or a party member, the party member with whom you have the bond will also recover HP equaling 40% of the original spell.
Duration: 20s
>> 845, Synastry, An aetheric bond is created with a party member. Each time a single-target healing spell is cast, that member will recover partial HP.
>> 846, Synastry, An aetheric bond is created with a party astrologian. Each time a single-target healing spell is cast by the astrologian, you will recover partial HP.
>> 1336, Synastry, An aetheric bond is created with a party member. Each time a single-target healing spell is cast, that member will recover partial HP.
>> 1337, Synastry, An aetheric bond is created with a party astrologian. Each time a single-target healing spell is cast by the astrologian, you will recover partial HP.
        """
        id = 3612
        name = {'星位合图', 'Synastry'}

    class Divination(ActionBase):
        """
Increases damage dealt by self and nearby party members by 6%.
Duration: 15s
>> 2034, Divination, Damage dealt is increased while damage taken is reduced.
>> 1878, Divination, Damage dealt is increased.
        """
        id = 16552
        name = {'Divination', '占卜'}
        status_to_target = Status.Divination

    class Astrodyne(ActionBase):
        """
Grants an effect using the astrosigns read from your divining deck.
Can only be executed after reading three astrosigns.
Effects granted are determined by the number of different types of astrosigns read.
1 Sign Type: Grants Harmony of Spirit
2 Sign Types: Grants Harmony of Spirit and Harmony of Body
3 Sign Types: Grants Harmony of Spirit, Harmony of Body, and Harmony of Mind
Duration: 15s
Harmony of Spirit Effect: Gradually restores own MP
Potency: 50
Harmony of Body Effect: Reduces spell cast time and recast time, and auto-attack delay by 10%
Harmony of Mind Effect: Increases damage dealt and healing potency by 5%
        """
        id = 25870
        name = {'Astrodyne'}
        status_to_target = Status.HarmonyOfSpirit, Status.HarmonyOfBody, Status.HarmonyOfMind

    class MaleficIi(ActionBase):
        """
Deals unaspected damage with a potency of 160.
        """
        id = 3598
        name = {'灾星', 'Malefic II'}
        damage_potency = 160
        attack_type = magic

    class CollectiveUnconscious(ActionBase):
        """
Creates a celestial ring around the caster.
Additional Effect: Reduces damage taken by 10% and applies Wheel of Fortune to self and any party members who enter
Duration: 18s
Wheel of Fortune Effect: Regen
Cure Potency: 100
Duration: 15s
Effect ends upon using another action or moving (including facing a different direction).
Cancels auto-attack upon execution.
>> 2283, Collective Unconscious, An area of mind attunement is created, reducing damage taken for all who enter.
>> 847, Collective Unconscious, An area of mind attunement is healing party members.
>> 848, Collective Unconscious, An area of mind attunement is created, reducing damage taken for all who enter.
>> 849, Collective Unconscious, Damage taken is reduced.
        """
        id = 3613
        name = {'Collective Unconscious', '命运之轮'}
        status_to_target = Status.WheelOfFortune, Status.CollectiveUnconscious

    class CelestialOpposition(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 200
Additional Effect: Regen
Cure Potency: 100
Duration: 15s
        """
        id = 16553
        name = {'天星冲日', 'Celestial Opposition'}
        cure_potency = 200
        status_to_target = Status.Opposition

    class EarthlyStar(ActionBase):
        """
Deploys an Earthly Star in the designated area and grants the effect of Earthly Dominance.
Duration: 10s
Executing Stellar Detonation while under the effect of Earthly Dominance creates a Stellar Burst dealing unaspected damage with a potency of 205 to all nearby enemies. Also restores own HP and the HP of all nearby party members.
Cure Potency: 540
After 10s, Earthly Dominance effect is changed to Giant Dominance.
Duration: 10s
Waiting 10s or executing Stellar Detonation while under the effect of Giant Dominance creates a Stellar Explosion dealing unaspected damage with a potency of 310 to all nearby enemies. Also restores own HP and the HP of all nearby party members.
Cure Potency: 720
        """
        id = 7439
        name = {'地星', 'Earthly Star'}

    class StellarDetonation(ActionBase):
        """
While under the effect of Earthly Dominance, detonates the currently deployed Earthly Star, creating a Stellar Burst that deals unaspected damage with a potency of 205 to all nearby enemies.
Additional Effect: Restores own HP and the HP of all nearby party members
Cure Potency: 540
While under the effect of Giant Dominance, detonates the currently deployed Earthly Star, creating a Stellar Explosion that deals unaspected damage with a potency of 310 to all nearby enemies.
Additional Effect: Restores own HP and the HP of all nearby party members
Cure Potency: 720
        """
        id = 8324
        name = {'Stellar Detonation', '星体爆轰'}

    class StellarBurst(ActionBase):
        id = 7441
        name = {'Stellar Burst', '星体破裂'}
        attack_type = magic
        cure_potency = 540
        damage_potency = 205

    class StellarExplosion(ActionBase):
        id = 7441
        name = {'Stellar Explosion', '星体爆炸'}
        attack_type = magic
        cure_potency = 720
        damage_potency = 310

    class MaleficIII(ActionBase):
        """
Deals unaspected damage with a potency of 190.
        """
        id = 7442
        name = {'Malefic III', '祸星'}
        damage_potency = 190
        attack_type = magic

    class MinorArcana(ActionBase):
        """
Draws either the Lord of Crowns or the Lady of Crowns from your divining deck.
Arcanum effect can be triggered using the action Crown Play.
Can only be executed while in combat.
        """
        id = 7443
        name = {'小奥秘卡', 'Minor Arcana'}

    class LordOfCrowns(ActionBase):
        """
Deals unaspected damage with a potency of 250 to all nearby enemies.
※This action cannot be assigned to a hotbar.
        """
        id = 7444
        name = {'Lord of Crowns', '王冠之领主'}
        damage_potency = 250
        attack_type = magic

    class LadyOfCrowns(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 400
※This action cannot be assigned to a hotbar.
        """
        id = 7445
        name = {'王冠之贵妇', 'Lady of Crowns'}
        cure_potency = 400

    class CrownPlay(ActionBase):
        """
Triggers the effect of your drawn arcanum.
        """
        id = 25869
        name = {'Crown Play'}

    class CombustIII(ActionBase):
        """
Deals unaspected damage over time.
Potency: 55
Duration: 30s
>> 1881, Combust III, Sustaining damage over time.
>> 2041, Combust III, Damage dealt and potency of all HP restoration actions are reduced.
        """
        id = 16554
        name = {'焚灼', 'Combust III'}
        attack_type = magic
        status_to_target = Status.CombustIII

    class MaleficIv(ActionBase):
        """
Deals unaspected damage with a potency of 230.
        """
        id = 16555
        name = {'煞星', 'Malefic IV'}
        attack_type = magic
        damage_potency = 230

    class CelestialIntersection(ActionBase):
        """
Restores own or target party member's HP.
Cure Potency: 200
Additional Sect Effect: Erects a magicked barrier which nullifies damage equaling 200% of the amount of HP restored
Duration: 30s(source.job==33?(source.level>=88?
Maximum Charges: 2:):)
        """
        id = 16556
        name = {'天星交错', 'Celestial Intersection'}
        cure_potency = 200

    class Horoscope(ActionBase):
        """
Reads your fortune and those of nearby party members, granting them Horoscope.
Duration: 10s
Effect upgraded to Horoscope Helios upon receiving the effects of Helios or Aspected Helios.
Duration: 30s
Restores the HP of those under either effect when the cards are read a second time or the effect expires.
Horoscope Cure Potency: 200
Horoscope Helios Cure Potency: 400
>> 1890, Horoscope, Primed to receive the healing effects of Horoscope.
        """
        id = 16557
        name = {'天宫图', 'Horoscope'}

    class HoroscopeExecute(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Potency is determined by the Horoscope effect of party members. Effect expires upon execution.
Horoscope Potency: 200
Horoscope Helios Potency: 400
>> 1890, Horoscope, Primed to receive the healing effects of Horoscope.
        """
        id = 16558
        name = {'天宫图（执行）', 'Horoscope(Execute)'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.cure_potency = 400 if target and target.effects.has(Status.HoroscopeHelios.id) else 200

    class NeutralSect(ActionBase):
        """
Increases healing magic po tency by 20%.
Duration: 20s
Additional Effect: When casting Aspected Benefic or Aspected Helios, erects a magicked barrier which nullifies damage
Aspected Benefic Effect: Nullifies damage equaling 250% of the amount of HP restored
Aspected Helios Effect: Nullifies damage equaling 125% of the amount of HP restored
Duration: 30s
>> 1921, Neutral Sect, A magicked barrier is nullifying damage.
>> 1892, Neutral Sect, Healing magic potency is increased.
>> 2044, Neutral Sect, Spell cast and recast times are reduced.
Helios is upgraded to Aspected Helios, while Benefic is upgraded to Aspected Benefic.
        """
        id = 16559
        name = {'Neutral Sect', '中间学派'}

    class FallMalefic(ActionBase):
        """
Deals unaspected damage with a potency of 250.
        """
        id = 25871
        name = {'Fall Malefic'}

    class GravityIi(ActionBase):
        """
Deals unaspected damage with a potency of 130 to target and all enemies nearby it.
        """
        id = 25872
        name = {'Gravity II'}

    class Exaltation(ActionBase):
        """
Reduces damage taken by self or target party member by 10%.
Duration: 8s
Additional Effect: Restores HP at the end of the effect's duration
Cure Potency: 500
>> 2717, Exaltation, Damage taken is reduced.
        """
        id = 25873
        name = {'Exaltation'}

    class Macrocosmos(ActionBase):
        """
Deals unaspected damage to all nearby enemies with a potency of 250 for the first enemy, and 40% less for all remaining enemies.
Additional Effect: Grants Macrocosmos to self and all nearby party members
Duration: 15s
Action changes to Microcosmos upon execution.
For the effect's duration, 50% of damage taken is compiled.
Restores HP equal to a cure of 200 potency plus compiled damage when the effect expires or upon execution of Microcosmos.
Amount restored cannot exceed the target's maximum HP.
This action does not share a recast timer with any other actions.
>> 2718, Macrocosmos, Restores HP when effect duration expires or the astrologian who granted this effect executes Microcosmos. Healing potency is based on damage taken and compiled over the duration of the effect.
        """
        id = 25874
        name = {'Macrocosmos'}

    class Microcosmos(ActionBase):
        """
Triggers the healing effect of Macrocosmos, restoring HP equal to a cure of 200 potency plus 50% of compiled damage.
Amount restored cannot exceed the target's maximum HP.
        """
        id = 25875
        name = {'Microcosmos'}
