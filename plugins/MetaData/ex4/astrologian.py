from ..base import *


class Actions:

    class Malefic(ActionBase):
        """
Deals unaspected damage with a potency of 150.
        """
        id = 3596
        name = {'凶星', 'Malefic'}

    class Benefic(ActionBase):
        """
Restores target's HP.
Cure Potency: (source.job==33?(source.level>=85?500:450):450)(source.level>=36?(source.job==33?
Additional Effect: 15% chance next Benefic II will restore critical HP
Duration: 15s:):)
        """
        id = 3594
        name = {'吉星', 'Benefic'}

    class Combust(ActionBase):
        """
Deals unaspected damage over time.
Potency: 40
Duration: 18s
    838, Combust, Proximity of a theoretical sun is causing damage over time.
        """
        id = 3599
        name = {'烧灼', 'Combust'}

    class Lightspeed(ActionBase):
        """
Reduces cast times for spells by 2.5 seconds.
Duration: 15s
    841, Lightspeed, Spell casting time is reduced.
    1403, Lightspeed, Spell casting time and MP cost are reduced by 100% and 50% respectively.
        """
        id = 3606
        name = {'Lightspeed', '光速'}

    class Helios(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: (source.job==33?(source.level>=85?400:330):330)
        """
        id = 3600
        name = {'阳星', 'Helios'}

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
        name = {'Essential Dignity', '先天禀赋'}

    class BeneficIi(ActionBase):
        """
Restores target's HP.
Cure Potency: (source.job==33?(source.level>=85?800:700):700)
        """
        id = 3610
        name = {'Benefic II', '福星'}

    class Draw(ActionBase):
        """
Draws a card (arcanum) from your divining deck. Only one arcanum can be drawn at a time.
Arcanum effect can be triggered using the action Play.
Additional Effect: Restores 5% of maximum MP
(source.job==33?(source.level>=40?Additional Effect: Grants Clarifying Draw, allowing the execution of Redraw
:):)Maximum Charges: 2
    826, Card Drawn, An arcanum is drawn from the deck.
        """
        id = 3590
        name = {'抽卡', 'Draw'}

    class DiurnalSect(ActionBase):
        """
Adds Regen to certain actions.(source.level>=50?(source.job==33?
Cannot be used with Nocturnal Sect.
Shares a recast timer with Nocturnal Sect.
Effect cannot be removed while in combat.:):)
Effect ends upon reuse.
    839, Diurnal Sect, A <UIForeground(506)><UIGlow(507)>Regen</UIGlow></UIForeground> effect is added to certain actions.
        """
        id = 3604
        name = {'Diurnal Sect', '白昼学派'}

    class TheBalance(ActionBase):
        """
Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Solar Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
    1338, The Balance, Damage dealt is increased.
    829, The Balance, Damage dealt is increased.
    1882, The Balance, Damage dealt is increased.
        """
        id = 4401
        name = {'太阳神之衡', 'the Balance'}

    class TheArrow(ActionBase):
        """
Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Lunar Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
    1884, The Arrow, Damage dealt is increased.
    831, The Arrow, Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
        """
        id = 4402
        name = {'the Arrow', '放浪神之箭'}

    class TheSpear(ActionBase):
        """
Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Celestial Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
    832, The Spear, Critical hit rate is increased.
    1885, The Spear, Damage dealt is increased.
        """
        id = 4403
        name = {'战争神之枪', 'the Spear'}

    class TheBole(ActionBase):
        """
Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Solar Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
    1339, The Bole, Damage taken is reduced.
    1883, The Bole, Damage dealt is increased.
    830, The Bole, Damage taken is reduced.
        """
        id = 4404
        name = {'the Bole', '世界树之干'}

    class TheEwer(ActionBase):
        """
Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Lunar Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
    833, The Ewer, Restoring MP over time.
    1340, The Ewer, Restoring MP over time.
    1886, The Ewer, Damage dealt is increased.
        """
        id = 4405
        name = {'河流神之瓶', 'the Ewer'}

    class TheSpire(ActionBase):
        """
Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles.
Duration: 15s
(source.job==33?(source.level>=50?Additional Effect: Grants a Celestial Sign when used in combat
:):)Only one arcanum effect can be applied to a target at a time.
※This action cannot be assigned to a hotbar.
    834, The Spire, Restoring TP over time.
    1341, The Spire, Restoring TP over time.
    1887, The Spire, Damage dealt is increased.
        """
        id = 4406
        name = {'建筑神之塔', 'the Spire'}

    class Undraw(ActionBase):
        """
Returns the currently drawn arcanum back to your deck.
        """
        id = 9629
        name = {'Undraw', '奥秘卡废弃'}

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
    835, Aspected Benefic, Regenerating HP over time.
        """
        id = 3595
        name = {'Aspected Benefic', '吉星相位'}

    class AspectedBenefic(ActionBase):
        """
Restores target's HP.
Cure Potency: 200
Diurnal Sect Effect: Regen
Cure Potency: 200
Duration: 15s
Effect cannot be stacked.(source.level>=50?(source.job==33?
Nocturnal Sect Effect: Erects a magicked barrier which nullifies damage equaling 250% of the amount of HP restored
Duration: 30s
Effect cannot be stacked with scholar's Galvanize.
Can only be executed while under the effect of Diurnal Sect or Nocturnal Sect.:
Can only be executed while under the effect of Diurnal Sect.):
Can only be executed while under the effect of Diurnal Sect.)
    835, Aspected Benefic, Regenerating HP over time.
        """
        id = 17151
        name = {'Aspected Benefic', '吉星相位'}

    class Redraw(ActionBase):
        """
Draws a different arcanum from your deck.
Can only be executed while under the effect of Clarifying Draw.
        """
        id = 3593
        name = {'重抽', 'Redraw'}

    class AspectedHelios(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: (source.job==33?(source.level>=85?250:200):200)
Additional Effect: Regen
Cure Potency: (source.job==33?(source.level>=85?150:100):100)
Duration: 15s
    836, Aspected Helios, Regenerating HP over time.
        """
        id = 3601
        name = {'Aspected Helios', '阳星相位'}

    class AspectedHelios(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 200
Diurnal Sect Effect: Regen
Cure Potency: 100
Duration: 15s
Effect cannot be stacked.(source.level>=50?(source.job==33?
Nocturnal Sect Effect: Erects a magicked barrier which nullifies damage equaling 125% of the amount of HP restored
Duration: 30s
Effect cannot be stacked with scholar's Galvanize.
Can only be executed while under the effect of Diurnal Sect or Nocturnal Sect.:
Can only be executed while under the effect of Diurnal Sect.):
Can only be executed while under the effect of Diurnal Sect.)
    836, Aspected Helios, Regenerating HP over time.
        """
        id = 17152
        name = {'Aspected Helios', '阳星相位'}

    class Gravity(ActionBase):
        """
Deals unaspected damage with a potency of 120 to target and all enemies nearby it.
        """
        id = 3615
        name = {'重力', 'Gravity'}

    class CombustIi(ActionBase):
        """
Deals unaspected damage over time.
Potency: 50
Duration: 30s
    843, Combust II, Proximity of a theoretical sun is causing damage over time.
        """
        id = 3608
        name = {'Combust II', '炽灼'}

    class NocturnalSect(ActionBase):
        """
Adds a damage-nullifying barrier to certain actions. Also increases MP cost of Aspected Benefic.
Cannot be used with Diurnal Sect.
Shares a recast timer with Diurnal Sect.
Effect cannot be removed while in combat.
Effect ends upon reuse.
    840, Nocturnal Sect, A damage-nullifying barrier effect is added to certain actions.
        """
        id = 3605
        name = {'黑夜学派', 'Nocturnal Sect'}

    class Synastry(ActionBase):
        """
Generate an aetheric bond with target party member. Each time you cast a single-target healing spell on yourself or a party member, the party member with whom you have the bond will also recover HP equaling 40% of the original spell.
Duration: 20s
    845, Synastry, An aetheric bond is created with a party member. Each time a single-target healing spell is cast, that member will recover partial HP.
    846, Synastry, An aetheric bond is created with a party astrologian. Each time a single-target healing spell is cast by the astrologian, you will recover partial HP.
    1336, Synastry, An aetheric bond is created with a party member. Each time a single-target healing spell is cast, that member will recover partial HP.
    1337, Synastry, An aetheric bond is created with a party astrologian. Each time a single-target healing spell is cast by the astrologian, you will recover partial HP.
        """
        id = 3612
        name = {'星位合图', 'Synastry'}

    class MinorArcana(ActionBase):
        """
Draws either the Lord of Crowns or the Lady of Crowns from your divining deck.
Arcanum effect can be triggered using the action Crown Play.
Can only be executed while in combat.
        """
        id = 7443
        name = {'Minor Arcana', '小奥秘卡'}

    class LordOfCrowns(ActionBase):
        """
Deals unaspected damage with a potency of 250 to all nearby enemies.
※This action cannot be assigned to a hotbar.
    1451, Lord of Crowns, Damage dealt is increased.
    1876, Lord of Crowns, Damage dealt is increased.
        """
        id = 7444
        name = {'王冠之领主', 'Lord of Crowns'}

    class LadyOfCrowns(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 400
※This action cannot be assigned to a hotbar.
    1452, Lady of Crowns, Damage taken is reduced.
    1877, Lady of Crowns, Damage dealt is increased.
        """
        id = 7445
        name = {'王冠之贵妇', 'Lady of Crowns'}

    class Divination(ActionBase):
        """
Increases damage dealt by self and nearby party members by 6%.
Duration: 15s
    2034, Divination, Damage dealt is increased while damage taken is reduced.
    1878, Divination, Damage dealt is increased.
        """
        id = 16552
        name = {'Divination', '占卜'}

    class MaleficIi(ActionBase):
        """
Deals unaspected damage with a potency of 160.
        """
        id = 3598
        name = {'Malefic II', '灾星'}

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
    2283, Collective Unconscious, An area of mind attunement is created, reducing damage taken for all who enter.
    847, Collective Unconscious, An area of mind attunement is healing party members.
    848, Collective Unconscious, An area of mind attunement is created, reducing damage taken for all who enter.
    849, Collective Unconscious, Damage taken is reduced.
    1206, Wheel of Fortune, Damage taken is reduced.
    956, Wheel of Fortune, Regenerating HP over time.
        """
        id = 3613
        name = {'命运之轮', 'Collective Unconscious'}

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

    class MaleficIii(ActionBase):
        """
Deals unaspected damage with a potency of 190.
        """
        id = 7442
        name = {'祸星', 'Malefic III'}

    class SleeveDraw(ActionBase):
        """
Draws a card (arcanum) from your divining deck.
You cannot draw an arcanum if you are aligned with its Seal of Arcana. When aligned with all three seals, any arcanum may be drawn.
Additional Effect: Restores 8% of maximum MP
    1926, Sleeve Draw, Draws a new arcanum after executing <UIForeground(500)><UIGlow(501)>Play</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Minor Arcana</UIGlow></UIForeground>, or <UIForeground(500)><UIGlow(501)>Undraw</UIGlow></UIForeground>.
        """
        id = 7448
        name = {'Sleeve Draw', '袖内抽卡'}

    class CombustIii(ActionBase):
        """
Deals unaspected damage over time.
Potency: 55
Duration: 30s
    1881, Combust III, Sustaining damage over time.
    2041, Combust III, Damage dealt and potency of all HP restoration actions are reduced.
        """
        id = 16554
        name = {'Combust III', '焚灼'}

    class MaleficIv(ActionBase):
        """
Deals unaspected damage with a potency of 230.
        """
        id = 16555
        name = {'煞星', 'Malefic IV'}

    class CelestialIntersection(ActionBase):
        """
Restores own or target party member's HP.
Cure Potency: 200
Additional Sect Effect: Erects a magicked barrier which nullifies damage equaling 200% of the amount of HP restored
Duration: 30s(source.job==33?(source.level>=88?
Maximum Charges: 2:):)
        """
        id = 16556
        name = {'Celestial Intersection', '天星交错'}

    class Horoscope(ActionBase):
        """
Reads your fortune and those of nearby party members, granting them Horoscope.
Duration: 10s
Effect upgraded to Horoscope Helios upon receiving the effects of Helios or Aspected Helios.
Duration: 30s
Restores the HP of those under either effect when the cards are read a second time or the effect expires.
Horoscope Cure Potency: 200
Horoscope Helios Cure Potency: 400
    1890, Horoscope, Primed to receive the healing effects of <UIForeground(500)><UIGlow(501)>Horoscope</UIGlow></UIForeground>.
        """
        id = 16557
        name = {'Horoscope', '天宫图'}

    class Horoscope(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Potency is determined by the Horoscope effect of party members. Effect expires upon execution.
Horoscope Potency: 200
Horoscope Helios Potency: 400
    1890, Horoscope, Primed to receive the healing effects of <UIForeground(500)><UIGlow(501)>Horoscope</UIGlow></UIForeground>.
        """
        id = 16558
        name = {'Horoscope', '天宫图'}

    class NeutralSect(ActionBase):
        """
Increases healing magic potency by 20%.
Duration: 20s
Additional Effect: When casting Aspected Benefic or Aspected Helios, erects a magicked barrier which nullifies damage
Aspected Benefic Effect: Nullifies damage equaling 250% of the amount of HP restored
Aspected Helios Effect: Nullifies damage equaling 125% of the amount of HP restored
Duration: 30s
    1892, Neutral Sect, Healing magic potency is increased.
    2044, Neutral Sect, Spell cast and recast times are reduced. <UIForeground(500)><UIGlow(501)>Helios</UIGlow></UIForeground> is upgraded to <UIForeground(500)><UIGlow(501)>Aspected Helios</UIGlow></UIForeground>, while <UIForeground(500)><UIGlow(501)>Benefic</UIGlow></UIForeground> is upgraded to <UIForeground(500)><UIGlow(501)>Aspected Benefic</UIGlow></UIForeground>.
        """
        id = 16559
        name = {'中间学派', 'Neutral Sect'}
