from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class HeavyShot(ActionBase):
        """
        Delivers an attack with a potency of 180.(source.level>=2?(source.job==5? Additional Effect: 20% chance of becoming Straight Shot Ready Duration: 10s:(source.job==23? Additional Effect: 20% chance of becoming Straight Shot Ready Duration: 10s:)):)
        """
        id = 97
        name = {"Heavy Shot", "强力射击"}

    class StraightShot(ActionBase):
        """
        Delivers an attack with a potency of 200. Can only be executed when Straight Shot Ready.
        130, Straight Shot, Straight Shot, Critical hit rate is increased.
        """
        id = 98
        name = {"Straight Shot", "直线射击"}

    class VenomousBite(ActionBase):
        """
        Delivers an attack with a potency of 100. Additional Effect: Venom Potency: 30 Duration: 30s
        124, Venomous Bite, Venomous Bite, Toxins are causing damage over time.
        """
        id = 100
        name = {"Venomous Bite", "毒咬箭"}

    class RagingStrikes(ActionBase):
        """
        Increases damage dealt by 10%. Duration: 20s
        125, Raging Strikes, Raging Strikes, Damage dealt is increased.
        """
        id = 101
        name = {"Raging Strikes", "猛者强击"}

    class QuickNock(ActionBase):
        """
        Delivers an attack with a potency of 150 to all enemies in a cone before you.(source.job==23?(source.level>=74? Additional Effect: 30% chance the recast timer for Bloodletter and Rain of Death will be reset:):)
        """
        id = 106
        name = {"Quick Nock", "连珠箭"}

    class Barrage(ActionBase):
        """
        Triples the number of strikes for a single-target weaponskill. Additional effects added only once. Duration: 10s Additional Effect: Grants Straight Shot Ready Duration: 10s
        128, Barrage, Barrage, Striking multiple times per weaponskill.
        1407, Barrage, Barrage, Striking multiple times per weaponskill.
        """
        id = 107
        name = {"Barrage", "纷乱箭"}

    class Bloodletter(ActionBase):
        """
        Delivers an attack with a potency of 150.(source.level>=45?(source.job==23? Shares a recast timer with Rain of Death.:):)
        """
        id = 110
        name = {"Bloodletter", "失血箭"}

    class RepellingShot(ActionBase):
        """
        Jump 10 yalms away from current target. Cannot be executed while bound.
        2017, Repelling Shot, Repelling Shot, Damage dealt by weaponskills is increased.
        """
        id = 112
        name = {"Repelling Shot", "后跃射击"}

    class Windbite(ActionBase):
        """
        Deals wind damage with a potency of 60. Additional Effect: Wind damage over time Potency: 40 Duration: 30s
        129, Windbite, Windbite, Wounds are exposed to the elements, causing wind damage over time.
        """
        id = 113
        name = {"Windbite", "风蚀箭"}

    class MagesBallad(ActionBase):
        """
        Deals unaspected damage with a potency of 100. Additional Effect: Grants Mage's Ballad to all party members within 30 yalms, increasing their damage dealt by 1% Duration: 30s Additional Effect: (source.level>=64?(source.job==23?40％:20％):20％) chance to grant Repertoire when damage over time is dealt by (source.level>=64?(source.job==23?Caustic Bite or Stormbite:Venomous Bite or Windbite):Venomous Bite or Windbite) Repertoire Effect: Resets the recast timer of Bloodletter and Rain of Death This action does not share a recast timer with any other actions. Furthermore, the recast timer cannot be affected by other actions.
        135, Mage's Ballad, Mage's Ballad, Using MP to gradually restore the MP of nearby party members. Damage dealt is reduced.
        136, Mage's Ballad, Mage's Ballad, Restoring MP over time.
        2217, Mage's Ballad, Mage's Ballad, Damage dealt is increased.
        """
        id = 114
        name = {"Mage's Ballad", "贤者的叙事谣"}

    class ArmysPaeon(ActionBase):
        """
        Deals unaspected damage with a potency of 100. Additional Effect: Grants Army's Paeon to all party members within 30 yalms, increasing their direct hit rate by 3% Duration: 30s Additional Effect: (source.level>=64?(source.job==23?40％:20％):20％) chance to grant Repertoire when damage over time is dealt by (source.level>=64?(source.job==23?Caustic Bite or Stormbite:Venomous Bite or Windbite):Venomous Bite or Windbite) Repertoire Effect: Reduces weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay by 4% Can be stacked up to 4 times. This action does not share a recast timer with any other actions. Furthermore, the recast timer cannot be affected by other actions.
        137, Army's Paeon, Army's Paeon, Using MP to gradually refresh the TP of self and nearby party members. Damage dealt is reduced.
        138, Army's Paeon, Army's Paeon, Gradually regenerating TP.
        2214, Army's Paeon, Army's Paeon, Weaponskill and spell cast and recast time are reduced.
        2218, Army's Paeon, Army's Paeon, Direct hit rate is increased.
        """
        id = 116
        name = {"Army's Paeon", "军神的赞美歌"}

    class RainOfDeath(ActionBase):
        """
        Delivers an attack with a potency of 130 to target and all enemies nearby it. Shares a recast timer with Bloodletter.
        247, Rain of Death, Rain of Death, Evasion is reduced.
        """
        id = 117
        name = {"Rain of Death", "死亡箭雨"}

    class BattleVoice(ActionBase):
        """
        Increases direct hit rate of all nearby party members by 20%. Duration: 20s Can only be executed while singing Mage's Ballad, Army's Paeon, or the Wanderer's Minuet.
        141, Battle Voice, Battle Voice, Direct hit rate is increased.
        """
        id = 118
        name = {"Battle Voice", "战斗之声"}

    class EmpyrealArrow(ActionBase):
        """
        Delivers an attack with a potency of 230.
        """
        id = 3558
        name = {"Empyreal Arrow", "九天连箭"}

    class TheWanderersMinuet(ActionBase):
        """
        Deals unaspected damage with a potency of 100. Additional Effect: Grants the Wanderer's Minuet to all party members within 30 yalms, increasing their critical hit rate by 2% Duration: 30s Additional Effect: (source.level>=64?(source.job==23?40％:20％):20％) chance to grant Repertoire when damage over time is dealt by (source.level>=64?(source.job==23?Caustic Bite or Stormbite:Venomous Bite or Windbite):Venomous Bite or Windbite) Repertoire Effect: Allows execution of Pitch Perfect Can be stacked up to 3 times. This action does not share a recast timer with any other actions. Furthermore, the recast timer cannot be affected by other actions.
        """
        id = 3559
        name = {"the Wanderer's Minuet", "放浪神的小步舞曲"}

    class IronJaws(ActionBase):
        """
        Delivers an attack with a potency of 100. Additional Effect: If the target is suffering from a (source.level>=64?(source.job==23?Caustic Bite or Stormbite:Venomous Bite or Windbite):Venomous Bite or Windbite) effect inflicted by you, the effect timer is reset(source.job==23?(source.level>=76? Additional Effect: 35% chance of becoming Straight Shot Ready Duration: 10s:):)
        """
        id = 3560
        name = {"Iron Jaws", "伶牙俐齿"}

    class TheWardensPaean(ActionBase):
        """
        Removes one select detrimental effect from self or target party member. If the target is not enfeebled, a barrier is created nullifying the target's next detrimental effect suffered. Duration: 30s
        """
        id = 3561
        name = {"the Warden's Paean", "光阴神的礼赞凯歌"}

    class Sidewinder(ActionBase):
        """
        Delivers an attack with a potency of 100. Additional Effect: If the target is suffering from a (source.level>=64?(source.job==23?Caustic Bite or Stormbite:Venomous Bite or Windbite):Venomous Bite or Windbite) effect inflicted by you, Sidewinder potency is increased to 200 for one effect, or 350 for both(source.job==23?(source.level>=72? Shares a recast timer with Shadowbite.:):)
        """
        id = 3562
        name = {"Sidewinder", "侧风诱导箭"}

    class PitchPerfect(ActionBase):
        """
        Delivers an attack with a potency of 100 when Repertoire stack is 1, 250 when Repertoire stack is 2, and 450 when Repertoire stack is 3. Can only be executed when the Wanderer's Minuet is active.
        """
        id = 7404
        name = {"Pitch Perfect", "完美音调"}

    class Troubadour(ActionBase):
        """
        Reduces damage taken by self and nearby party members by 10%. Duration: 15s Effect cannot be stacked with machinist's Tactician or dancer's Shield Samba.
        1934, Troubadour, Troubadour, Damage taken is reduced.
        """
        id = 7405
        name = {"Troubadour", "行吟"}

    class CausticBite(ActionBase):
        """
        Delivers an attack with a potency of 150. Additional Effect: Poison Potency: 40 Duration: 30s(source.job==23?(source.level>=76? Additional Effect: 35% chance of becoming Straight Shot Ready Duration: 10s:):)
        1200, Caustic Bite, Caustic Bite, Toxins are causing damage over time.
        1321, Caustic Bite, Caustic Bite, Toxins are causing damage over time.
        """
        id = 7406
        name = {"Caustic Bite", "烈毒咬箭"}

    class Stormbite(ActionBase):
        """
        Deals wind damage with a potency of 100. Additional Effect: Wind damage over time Potency: 50 Duration: 30s(source.job==23?(source.level>=76? Additional Effect: 35% chance of becoming Straight Shot Ready Duration: 10s:):)
        1201, Stormbite, Stormbite, Wounds are exposed to the elements, causing wind damage over time.
        1322, Stormbite, Stormbite, Wounds are exposed to the elements, causing damage over time.
        """
        id = 7407
        name = {"Stormbite", "狂风蚀箭"}

    class NaturesMinne(ActionBase):
        """
        Increases HP recovery via healing actions for a party member or self by 20%. Duration: 15s
        1202, Nature's Minne, Nature's Minne, HP recovery via healing actions is increased.
        2178, Nature's Minne, Nature's Minne, Damage taken is reduced while HP recovered via healing actions is increased.
        """
        id = 7408
        name = {"Nature's Minne", "大地神的抒情恋歌"}

    class RefulgentArrow(ActionBase):
        """
        Delivers an attack with a potency of 340. Can only be executed when Straight Shot Ready.
        """
        id = 7409
        name = {"Refulgent Arrow", "辉煌箭"}

    class Shadowbite(ActionBase):
        """
        Delivers an attack with a potency of 100 to target and all enemies nearby it. Additional Effect: If the target is suffering from a Caustic Bite or Stormbite effect inflicted by you, Shadowbite potency is increased to 160 for one effect, or 220 for both Shares a recast timer with Sidewinder.
        """
        id = 16494
        name = {"Shadowbite", "影噬箭"}

    class BurstShot(ActionBase):
        """
        Delivers an attack with a potency of 250. Additional Effect: 35% chance of becoming Straight Shot Ready Duration: 10s
        """
        id = 16495
        name = {"Burst Shot", "爆发射击"}

    class ApexArrow(ActionBase):
        """
        Delivers an attack with a potency of 120 to all enemies in a straight line before you. Soul Voice Gauge Cost: 20  Potency increases up to 600 as Soul Voice Gauge exceeds minimum cost. Consumes Soul Voice Gauge upon execution.
        """
        id = 16496
        name = {"Apex Arrow", "绝峰箭"}
