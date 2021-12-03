from ..base import *


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

    class StraightShot(ActionBase):
        """
Delivers an attack with a potency of 200.
Can only be executed when Straight Shot Ready.
    130, Straight Shot, Critical hit rate is increased.
        """
        id = 98
        name = {'直线射击', 'Straight Shot'}

    class RagingStrikes(ActionBase):
        """
Increases damage dealt by 15%.
Duration: 20s
    125, Raging Strikes, Damage dealt is increased.
        """
        id = 101
        name = {'Raging Strikes', '猛者强击'}

    class VenomousBite(ActionBase):
        """
Delivers an attack with a potency of 100.
Additional Effect: Venom
Potency: 15
Duration: 45s
    124, Venomous Bite, Toxins are causing damage over time.
        """
        id = 100
        name = {'毒咬箭', 'Venomous Bite'}

    class Bloodletter(ActionBase):
        """
Delivers an attack with a potency of 110.
Maximum Charges: (source.job==23?(source.level>=84?3:2):2)(source.level>=45?(source.job==23?
Shares a recast timer with Rain of Death.:):)
        """
        id = 110
        name = {'失血箭', 'Bloodletter'}

    class RepellingShot(ActionBase):
        """
Jump 10 yalms away from current target.
Cannot be executed while bound.
    2017, Repelling Shot, Damage dealt by weaponskills is increased.
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

    class Windbite(ActionBase):
        """
Deals wind damage with a potency of 60.
Additional Effect: Wind damage over time
Potency: 20
Duration: 45s
    129, Windbite, Wounds are exposed to the elements, causing wind damage over time.
        """
        id = 113
        name = {'Windbite', '风蚀箭'}

    class MagesBallad(ActionBase):
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
        id = 114
        name = {'贤者的叙事谣', "Mage's Ballad"}

    class TheWardensPaean(ActionBase):
        """
Removes one select detrimental effect from self or target party member. If the target is not enfeebled, a barrier is created nullifying the target's next detrimental effect suffered.
Duration: 30s
    866, The Warden's Paean, Impervious to the next enfeeblement.
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
    128, Barrage, Striking multiple times per weaponskill.
    1407, Barrage, Striking multiple times per weaponskill.
        """
        id = 107
        name = {'纷乱箭', 'Barrage'}

    class ArmysPaeon(ActionBase):
        """
Deals unaspected damage with a potency of 100.
Additional Effect: Grants Army's Paeon to self and all party members within 30 yalms, increasing direct hit rate by 3%
Duration: 45s
Additional Effect: 80% chance to grant Repertoire
Repertoire Effect: Reduces weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay by 4%
Can be stacked up to 4 times.(source.job==23?(source.level>=90?
Additional Effect: Grants Army's Coda:):)
    2214, Army's Paeon, Weaponskill and spell cast and recast time are reduced.
    137, Army's Paeon, Using MP to gradually refresh the TP of self and nearby party members. Damage dealt is reduced.
    2218, Army's Paeon, Direct hit rate is increased.
    138, Army's Paeon, Gradually regenerating TP.
        """
        id = 116
        name = {"Army's Paeon", '军神的赞美歌'}

    class RainOfDeath(ActionBase):
        """
Delivers an attack with a potency of 100 to target and all enemies nearby it.
Maximum Charges: (source.job==23?(source.level>=84?3:2):2)
Shares a recast timer with Bloodletter.
    247, Rain of Death, Evasion is reduced.
        """
        id = 117
        name = {'Rain of Death', '死亡箭雨'}

    class BattleVoice(ActionBase):
        """
Increases direct hit rate of self and all nearby party members by 20%.
Duration: 15s
Can only be executed while singing Mage's Ballad, Army's Paeon, or the Wanderer's Minuet.
    141, Battle Voice, Direct hit rate is increased.
        """
        id = 118
        name = {'战斗之声', 'Battle Voice'}

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

    class EmpyrealArrow(ActionBase):
        """
Delivers an attack with a potency of 200.
        """
        id = 3558
        name = {'Empyreal Arrow', '九天连箭'}

    class IronJaws(ActionBase):
        """
Delivers an attack with a potency of 100.
Additional Effect: If the target is suffering from a (source.level>=64?(source.job==23?Caustic Bite or Stormbite:Venomous Bite or Windbite):Venomous Bite or Windbite) effect inflicted by you, the effect timer is reset(source.job==23?(source.level>=76?
Additional Effect: 35% chance of becoming Straight Shot Ready
Duration: 30s:):)
        """
        id = 3560
        name = {'伶牙俐齿', 'Iron Jaws'}

    class Sidewinder(ActionBase):
        """
Delivers an attack with a potency of 300.
        """
        id = 3562
        name = {'Sidewinder', '侧风诱导箭'}

    class Troubadour(ActionBase):
        """
Reduces damage taken by self and nearby party members by 10%.
Duration: 15s
Effect cannot be stacked with machinist's Tactician or dancer's Shield Samba.
    1934, Troubadour, Damage taken is reduced.
        """
        id = 7405
        name = {'Troubadour', '行吟'}

    class CausticBite(ActionBase):
        """
Delivers an attack with a potency of 150.
Additional Effect: Poison
Potency: 20
Duration: 45s(source.job==23?(source.level>=76?
Additional Effect: 35% chance of becoming Straight Shot Ready
Duration: 30s:):)
    1200, Caustic Bite, Toxins are causing damage over time.
    1321, Caustic Bite, Toxins are causing damage over time.
        """
        id = 7406
        name = {'Caustic Bite', '烈毒咬箭'}

    class Stormbite(ActionBase):
        """
Deals wind damage with a potency of 100.
Additional Effect: Wind damage over time
Potency: 25
Duration: 45s(source.job==23?(source.level>=76?
Additional Effect: 35% chance of becoming Straight Shot Ready
Duration: 30s:):)
    1201, Stormbite, Wounds are exposed to the elements, causing wind damage over time.
    1322, Stormbite, Wounds are exposed to the elements, causing damage over time.
        """
        id = 7407
        name = {'Stormbite', '狂风蚀箭'}

    class NaturesMinne(ActionBase):
        """
Increases HP recovery via healing actions for a party member or self by 20%.
Duration: 15s
    1202, Nature's Minne, HP recovery via healing actions is increased.
    2178, Nature's Minne, Damage taken is reduced while HP recovered via healing actions is increased.
        """
        id = 7408
        name = {'大地神的抒情恋歌', "Nature's Minne"}

    class RefulgentArrow(ActionBase):
        """
Delivers an attack with a potency of 280.
Can only be executed when Straight Shot Ready.
        """
        id = 7409
        name = {'辉煌箭', 'Refulgent Arrow'}

    class Shadowbite(ActionBase):
        """
Delivers an attack with a potency of 170 to target and all enemies nearby it.
Barrage Potency: 270
Can only be executed when Shadowbite Ready.
        """
        id = 16494
        name = {'Shadowbite', '影噬箭'}

    class BurstShot(ActionBase):
        """
Delivers an attack with a potency of 220.
Additional Effect: 35% chance of becoming Straight Shot Ready
Duration: 30s
        """
        id = 16495
        name = {'爆发射击', 'Burst Shot'}

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
