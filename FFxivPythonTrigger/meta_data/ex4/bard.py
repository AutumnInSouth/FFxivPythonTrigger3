from ..base import *


class Status:
    class RagingStrikes(StatusBase):
        """
Increases damage dealt by 15%.
Duration: 20s
    125, Raging Strikes, Damage dealt is increased.
        """
        id = 125
        name = {'Raging Strikes', '猛者强击'}
        damage_potency = 1.15

    class VenomousBite(StatusBase):
        """
Delivers an attack with a potency of 100.
Additional Effect: Venom
Potency: 15
Duration: 45s
    124, Venomous Bite, Toxins are causing damage over time.
        """
        id = 124
        name = {'毒咬箭', 'Venomous Bite'}
        damage_potency = 15

    class Windbite(StatusBase):
        """
Deals wind damage with a potency of 60.
Additional Effect: Wind damage over time
Potency: 20
Duration: 45s
    129, Windbite, Wounds are exposed to the elements, causing wind damage over time.
        """
        id = 129
        name = {'Windbite', '风蚀箭'}
        damage_potency = 20

    class MagesBallad(StatusBase):
        """
Deals unaspected damage with a potency of 100.
Additional Effect: Grants Mage's Ballad to self and all party members within 30 yalms, increasing damage dealt by 1%
Duration: 45s
Additional Effect: 80% chance to grant Repertoire
Repertoire Effect: Reduces the recast time of both Bloodletter and Rain of Death by 7.5s(source.job==23?(source.level>=90?
Additional Effect: Grants Mage's Coda:):)
    135, Mage's Ballad, Using MP to gradually restore the MP of nearby party members. Damage dealt is reduced.
    136, Mage's Ballad, Restoring MP over time.
    2217, Mage's Ballad, Damage dealt is increased.
        """
        id = 2217
        name = {'贤者的叙事谣', "Mage's Ballad"}
        damage_modify = 1.01

    class ArmysPaeon(StatusBase):
        """
Deals unaspected damage with a potency of 100.
Additional Effect: Grants Army's Paeon to self and all party members within 30 yalms, increasing direct hit rate by 3%
Duration: 45s
Additional Effect: 80% chance to grant Repertoire
Repertoire Effect: Reduces weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay by 4%
Can be stacked up to 4 times.(source.job==23?(source.level>=90?
Additional Effect: Grants Army's Coda:):).
    2218, Army's Paeon, Direct hit rate is increased.
        """
        id = 2218
        name = {"Army's Paeon", '军神的赞美歌'}
        direct_rate = .03

    class BattleVoice(StatusBase):
        """
Increases direct hit rate of self and all nearby party members by 20%.
Duration: 15s
Can only be executed while singing Mage's Ballad, Army's Paeon, or the Wanderer's Minuet.
    141, Battle Voice, Direct hit rate is increased.
        """
        id = 141
        name = {'战斗之声', 'Battle Voice'}
        direct_rate = .2

    class TheWanderersMinuet(StatusBase):
        """
Deals unaspected damage with a potency of 100.
Additional Effect: Grants the Wanderer's Minuet to self and all party members within 30 yalms, increasing critical hit rate by 2%
Duration: 45s
Additional Effect: 80% chance to grant Repertoire
Repertoire Effect: Allows execution of Pitch Perfect
Can be stacked up to 3 times.(source.job==23?(source.level>=90?
Additional Effect: Grants Wanderer's Coda:):)
    2216, The Wanderer's Minuet, Critical hit rate is increased.
        """
        id = 2216
        name = {'放浪神的小步舞曲', "the Wanderer's Minuet"}
        critical_rate = .02

    class Troubadour(StatusBase):
        """
Reduces damage taken by self and nearby party members by 10%.
Duration: 15s
Effect cannot be stacked with machinist's Tactician or dancer's Shield Samba.
    1934, Troubadour, Damage taken is reduced.
        """
        id = 1934
        name = {'Troubadour', '行吟'}
        taken_damage_modify = .9

    class CausticBite(StatusBase):
        """
Delivers an attack with a potency of 150.
Additional Effect: Poison
Potency: 20
Duration: 45s(source.job==23?(source.level>=76?
Additional Effect: 35% chance of becoming Straight Shot Ready
Duration: 30s:):)
>> 1200, Caustic Bite, Toxins are causing damage over time.
>> 1321, Caustic Bite, Toxins are causing damage over time.
        """
        id = 1200
        name = {'Caustic Bite', '烈毒咬箭'}
        damage_potency = 20

    class Stormbite(StatusBase):
        """
Deals wind damage with a potency of 100.
Additional Effect: Wind damage over time
Potency: 25
Duration: 45s(source.job==23?(source.level>=76?
Additional Effect: 35% chance of becoming Straight Shot Ready
Duration: 30s:):)
>> 1201, Stormbite, Wounds are exposed to the elements, causing wind damage over time.
>> 1322, Stormbite, Wounds are exposed to the elements, causing damage over time.
        """
        id = 1201
        name = {'Stormbite', '狂风蚀箭'}
        damage_potency = 25

    class NaturesMinne(StatusBase):
        """
Increases HP recovery via healing actions for a party member or self by 20%.
Duration: 15s
>> 1202, Nature's Minne, HP recovery via healing actions is increased.
>> 2178, Nature's Minne, Damage taken is reduced while HP recovered via healing actions is increased.
        """
        id = 1202
        name = {"Nature's Minne", '大地神的抒情恋歌'}
        cure_modify = 1.2

    class Barrage(StatusBase):
        """
Triples the number of strikes for a single-target weaponskill. Additional effects added only once.
Duration: 10s
(source.job==23?(source.level>=72?Additional Effect: Increases the potency of Shadowbite to 270
:):)Additional Effect: Grants Straight Shot Ready
Duration: 30s
>> 128, Barrage, Striking multiple times per weaponskill.
>> 1407, Barrage, Striking multiple times per weaponskill.
        """
        id = 128
        name = {'纷乱箭', 'Barrage'}

    class RadiantFinale(StatusBase):
        """
Increases damage dealt by self and nearby party members.
Duration: 15s
Effectiveness is determined by the number of different Coda active in the Song Gauge.
1 Coda: 2%
2 Coda: 4%
3 Coda: 6%
Can only be executed when at least 1 coda is active.
>> 2722, Radiant Finale, Playing a most radiant finale.
>> 2964, Radiant Finale, Damage dealt is increased.
        """
        id = 2722
        name = {'Radiant Finale'}
        damage_modify = 1.02  # TODO: 无法获取其他人的量谱数据，无法判断准确数值

    class ShadowbiteReady(StatusBase):
        id = 3002
        name = {'Shadowbite Ready'}

    class StraightShotReady(StatusBase):
        id = 122
        name = {'Straight Shot Ready', '直线射击预备'}

    class BlastArrowReady(StatusBase):
        id = 2692
        name = {'Blast Arrow Ready'}


class Actions:
    class HeavyShot(ActionBase):
        """
Delivers an attack with a potency of 160.(source.level>=2?(source.job==5?
Additional Effect: 20% chance of becoming Straight Shot Ready
Duration: 30s:(source.job==23?
Additional Effect: 20% chance of becoming Straight Shot Ready
Duration: 30s:)):)
        """
        id = 97
        name = {'强力射击', 'Heavy Shot'}
        attack_type = physic
        damage_potency = 160

    class StraightShot(ActionBase):
        """
Delivers an attack with a potency of 200.
Can only be executed when Straight Shot Ready.
>> 130, Straight Shot, Critical hit rate is increased.
        """
        id = 98
        name = {'直线射击', 'Straight Shot'}
        attack_type = physic
        damage_potency = 200

    class RagingStrikes(ActionBase):
        """
Increases damage dealt by 15%.
Duration: 20s
>> 125, Raging Strikes, Damage dealt is increased.
        """
        id = 101
        name = {'Raging Strikes', '猛者强击'}
        status_to_target = Status.RagingStrikes

    class VenomousBite(ActionBase):
        """
Delivers an attack with a potency of 100.
Additional Effect: Venom
Potency: 15
Duration: 45s
>> 124, Venomous Bite, Toxins are causing damage over time.
        """
        id = 100
        name = {'毒咬箭', 'Venomous Bite'}
        attack_type = physic
        damage_potency = 100

    class Bloodletter(ActionBase):
        """
Delivers an attack with a potency of 110.
Maximum Charges: (source.job==23?(source.level>=84?3:2):2)(source.level>=45?(source.job==23?
Shares a recast timer with Rain of Death.:):)
        """
        id = 110
        name = {'失血箭', 'Bloodletter'}
        attack_type = physic
        damage_potency = 110

    class RepellingShot(ActionBase):
        """
Jump 10 yalms away from current target.
Cannot be executed while bound.
>> 2017, Repelling Shot, Damage dealt by weaponskills is increased.
        """
        id = 112
        name = {'Repelling Shot', '后跃射击'}

    class QuickNock(ActionBase):
        """
Delivers an attack with a potency of 110 to all enemies in a cone before you.(source.job==23?(source.level>=72?
Additional Effect: 35% chance of becoming Shadowbite Ready
Duration: 30s:):)
        """
        id = 106
        name = {'Quick Nock', '连珠箭'}
        attack_type = physic
        damage_potency = 110

    class Windbite(ActionBase):
        """
Deals wind damage with a potency of 60.
Additional Effect: Wind damage over time
Potency: 20
Duration: 45s
>> 129, Windbite, Wounds are exposed to the elements, causing wind damage over time.
        """
        id = 113
        name = {'Windbite', '风蚀箭'}
        attack_type = physic
        damage_potency = 60
        status_to_target = Status.Windbite

    class MagesBallad(ActionBase):
        """
Deals unaspected damage with a potency of 100.
Additional Effect: Grants Mage's Ballad to self and all party members within 30 yalms, increasing damage dealt by 1%
Duration: 45s
Additional Effect: 80% chance to grant Repertoire
Repertoire Effect: Reduces the recast time of both Bloodletter and Rain of Death by 7.5s(source.job==23?(source.level>=90?
Additional Effect: Grants Mage's Coda:):)
>> 135, Mage's Ballad, Using MP to gradually restore the MP of nearby party members. Damage dealt is reduced.
>> 136, Mage's Ballad, Restoring MP over time.
>> 2217, Mage's Ballad, Damage dealt is increased.
        """
        id = 114
        name = {'贤者的叙事谣', "Mage's Ballad"}
        attack_type = magic
        damage_potency = 100
        status_to_target = Status.MagesBallad

    class TheWardensPaean(ActionBase):
        """
Removes one select detrimental effect from self or target party member. If the target is not enfeebled, a barrier is created nullifying the target's next detrimental effect suffered.
Duration: 30s
        """
        id = 3561
        name = {"the Warden's Paean", '光阴神的礼赞凯歌'}

    class Barrage(ActionBase):
        """
Triples the number of strikes for a single-target weaponskill. Additional effects added only once.
Duration: 10s
(source.job==23?(source.level>=72?Additional Effect: Increases the potency of Shadowbite to 270
:):)Additional Effect: Grants Straight Shot Ready
Duration: 30s
>> 128, Barrage, Striking multiple times per weaponskill.
>> 1407, Barrage, Striking multiple times per weaponskill.
        """
        id = 107
        name = {'纷乱箭', 'Barrage'}
        status_to_target = Status.Barrage

    class ArmysPaeon(ActionBase):
        """
Deals unaspected damage with a potency of 100.
Additional Effect: Grants Army's Paeon to self and all party members within 30 yalms, increasing direct hit rate by 3%
Duration: 45s
Additional Effect: 80% chance to grant Repertoire
Repertoire Effect: Reduces weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay by 4%
Can be stacked up to 4 times.(source.job==23?(source.level>=90?
Additional Effect: Grants Army's Coda:):)
>> 2214, Army's Paeon, Weaponskill and spell cast and recast time are reduced.
>> 137, Army's Paeon, Using MP to gradually refresh the TP of self and nearby party members. Damage dealt is reduced.
>> 2218, Army's Paeon, Direct hit rate is increased.
>> 138, Army's Paeon, Gradually regenerating TP.
        """
        id = 116
        name = {"Army's Paeon", '军神的赞美歌'}
        attack_type = magic
        damage_potency = 100
        status_to_target = Status.ArmysPaeon

    class RainOfDeath(ActionBase):
        """
Delivers an attack with a potency of 100 to target and all enemies nearby it.
Maximum Charges: (source.job==23?(source.level>=84?3:2):2)
Shares a recast timer with Bloodletter.
>> 247, Rain of Death, Evasion is reduced.
        """
        id = 117
        name = {'Rain of Death', '死亡箭雨'}
        attack_type = physic
        damage_potency = 100

    class BattleVoice(ActionBase):
        """
Increases direct hit rate of self and all nearby party members by 20%.
Duration: 15s
Can only be executed while singing Mage's Ballad, Army's Paeon, or the Wanderer's Minuet.
>> 141, Battle Voice, Direct hit rate is increased.
        """
        id = 118
        name = {'战斗之声', 'Battle Voice'}
        status_to_target = Status.BattleVoice

    class TheWanderersMinuet(ActionBase):
        """
Deals unaspected damage with a potency of 100.
Additional Effect: Grants the Wanderer's Minuet to self and all party members within 30 yalms, increasing critical hit rate by 2%
Duration: 45s
Additional Effect: 80% chance to grant Repertoire
Repertoire Effect: Allows execution of Pitch Perfect
Can be stacked up to 3 times.(source.job==23?(source.level>=90?
Additional Effect: Grants Wanderer's Coda:):)
    865, The Wanderer's Minuet, Damage dealt is increased while cast time is added to all archer and bard weaponskills.
    2215, The Wanderer's Minuet, Damage dealt is increased.
    2216, The Wanderer's Minuet, Critical hit rate is increased.
        """
        id = 3559
        name = {'放浪神的小步舞曲', "the Wanderer's Minuet"}
        attack_type = magic
        damage_potency = 100
        status_to_target = Status.TheWanderersMinuet

    class PitchPerfect(ActionBase):
        """
Delivers an attack to the target. Potency varies with number of Repertoire stacks.
1 Repertoire Stack: 100
2 Repertoire Stacks: 220
3 Repertoire Stacks: 360
Can only be executed when the Wanderer's Minuet is active.
        """
        id = 7404
        name = {'完美音调', 'Pitch Perfect'}
        attack_type = physic
        # TODO: 无法获取其他人的量谱数据，无法判断准确数值

    class EmpyrealArrow(ActionBase):
        """
Delivers an attack with a potency of 200.
        """
        id = 3558
        name = {'Empyreal Arrow', '九天连箭'}
        attack_type = physic
        damage_potency = 200

    class IronJaws(ActionBase):
        """
Delivers an attack with a potency of 100.
Additional Effect: If the target is suffering from a (source.level>=64?(source.job==23?Caustic Bite or Stormbite:Venomous Bite or Windbite):Venomous Bite or Windbite) effect inflicted by you, the effect timer is reset(source.job==23?(source.level>=76?
Additional Effect: 35% chance of becoming Straight Shot Ready
Duration: 30s:):)
        """
        id = 3560
        name = {'伶牙俐齿', 'Iron Jaws'}
        attack_type = physic
        damage_potency = 100

    class Sidewinder(ActionBase):
        """
Delivers an attack with a potency of 300.
        """
        id = 3562
        name = {'Sidewinder', '侧风诱导箭'}
        attack_type = physic
        damage_potency = 300

    class Troubadour(ActionBase):
        """
Reduces damage taken by self and nearby party members by 10%.
Duration: 15s
Effect cannot be stacked with machinist's Tactician or dancer's Shield Samba.
>> 1934, Troubadour, Damage taken is reduced.
        """
        id = 7405
        name = {'Troubadour', '行吟'}
        status_to_target = Status.Troubadour

    class CausticBite(ActionBase):
        """
Delivers an attack with a potency of 150.
Additional Effect: Poison
Potency: 20
Duration: 45s(source.job==23?(source.level>=76?
Additional Effect: 35% chance of becoming Straight Shot Ready
Duration: 30s:):)
>> 1200, Caustic Bite, Toxins are causing damage over time.
>> 1321, Caustic Bite, Toxins are causing damage over time.
        """
        id = 7406
        name = {'Caustic Bite', '烈毒咬箭'}
        attack_type = physic
        damage_potency = 150
        status_to_target = Status.CausticBite

    class Stormbite(ActionBase):
        """
Deals wind damage with a potency of 100.
Additional Effect: Wind damage over time
Potency: 25
Duration: 45s(source.job==23?(source.level>=76?
Additional Effect: 35% chance of becoming Straight Shot Ready
Duration: 30s:):)
>> 1201, Stormbite, Wounds are exposed to the elements, causing wind damage over time.
>> 1322, Stormbite, Wounds are exposed to the elements, causing damage over time.
        """
        id = 7407
        name = {'Stormbite', '狂风蚀箭'}
        attack_type = physic
        damage_potency = 100
        status_to_target = Status.Stormbite

    class NaturesMinne(ActionBase):
        """
Increases HP recovery via healing actions for a party member or self by 20%.
Duration: 15s
>> 1202, Nature's Minne, HP recovery via healing actions is increased.
>> 2178, Nature's Minne, Damage taken is reduced while HP recovered via healing actions is increased.
        """
        id = 7408
        name = {"Nature's Minne", '大地神的抒情恋歌'}
        status_to_target = Status.NaturesMinne

    class RefulgentArrow(ActionBase):
        """
Delivers an attack with a potency of 280.
Can only be executed when Straight Shot Ready.
        """
        id = 7409
        name = {'辉煌箭', 'Refulgent Arrow'}
        attack_type = physic
        damage_potency = 280

    class Shadowbite(ActionBase):
        """
Delivers an attack with a potency of 170 to target and all enemies nearby it.
Barrage Potency: 270
Can only be executed when Shadowbite Ready.
        """
        id = 16494
        name = {'影噬箭', 'Shadowbite'}
        attack_type = physic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 270 if source.effects.has(Status.Barrage.id) else 170

    class BurstShot(ActionBase):
        """
Delivers an attack with a potency of 220.
Additional Effect: 35% chance of becoming Straight Shot Ready
Duration: 30s
        """
        id = 16495
        name = {'爆发射击', 'Burst Shot'}
        attack_type = physic
        damage_potency = 220

    class ApexArrow(ActionBase):
        """
Delivers an attack with a potency of 100 to all enemies in a straight line before you.
Soul Voice Gauge Cost: 20
Potency increases up to 500 as Soul Voice Gauge exceeds minimum cost.
(source.job==23?(source.level>=86?Additional Effect: Grants Blast Arrow Ready upon execution while Soul Voice Gauge is 80 or higher
Duration: 10s
:):)Consumes Soul Voice Gauge upon execution.(source.job==23?(source.level>=86?
※Action changes to Blast Arrow while under the effect of Blast Arrow Ready.:):)
        """
        id = 16496
        name = {'Apex Arrow', '绝峰箭'}
        attack_type = physic
        # TODO: 无法获取其他人的量谱数据，无法判断准确数值

    class Ladonsbite(ActionBase):
        """
Delivers an attack with a potency of 130 to all enemies in a cone before you.
Additional Effect: 35% chance of becoming Shadowbite Ready
Duration: 30s
        """
        id = 25783
        name = {'Ladonsbite'}
        attack_type = physic
        damage_potency = 130

    class BlastArrow(ActionBase):
        """
Delivers an attack to all enemies in a straight line before you with a potency of 600 for the first enemy, and 60% less for all remaining enemies.
Can only be executed while under the effect of Blast Arrow Ready.
※This action cannot be assigned to a hotbar.
        """
        id = 25784
        name = {'Blast Arrow'}
        attack_type = physic
        damage_potency = 600
        aoe_scale = .4

    class RadiantFinale(ActionBase):
        """
Increases damage dealt by self and nearby party members.
Duration: 15s
Effectiveness is determined by the number of different Coda active in the Song Gauge.
1 Coda: 2%
2 Coda: 4%
3 Coda: 6%
Can only be executed when at least 1 coda is active.
>> 2722, Radiant Finale, Playing a most radiant finale.
>> 2964, Radiant Finale, Damage dealt is increased.
        """
        id = 25785
        name = {'Radiant Finale'}
        status_to_target = Status.RadiantFinale
