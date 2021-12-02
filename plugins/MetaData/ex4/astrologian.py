from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Draw(ActionBase):
        """
        Draws a card (arcanum) from your divining deck. Only one arcanum can be drawn at a time. Arcanum effect can be triggered using (source.job==33?(source.level>=50?either Play or Minor Arcana:the action Play):the action Play). Additional Effect: Restores 8% of maximum MP
        """
        id = 3590
        name = {"Draw", "抽卡"}

    class Redraw(ActionBase):
        """
        Draws a different arcanum from your deck. Maximum Charges: 3
        """
        id = 3593
        name = {"Redraw", "重抽"}

    class Benefic(ActionBase):
        """
        Restores target's HP. Cure Potency: 400(source.level>=36?(source.job==33? Additional Effect: 15% chance next Benefic II will restore critical HP Duration: 15s:):)
        """
        id = 3594
        name = {"Benefic", "吉星"}

    class AspectedBenefic(ActionBase):
        """
        Restores target's HP. Cure Potency: 200 Diurnal Sect Effect: Regen Cure Potency: 200 Duration: 15s Effect cannot be stacked.(source.level>=50?(source.job==33? Nocturnal Sect Effect: Erects a magicked barrier which nullifies damage equaling 250% of the amount of HP restored Duration: 30s Effect cannot be stacked with scholar's Galvanize. Can only be executed while under the effect of Diurnal Sect or Nocturnal Sect.: Can only be executed while under the effect of Diurnal Sect.): Can only be executed while under the effect of Diurnal Sect.)
        835, Aspected Benefic, Aspected Benefic, Regenerating HP over time.
        """
        id = 3595
        name = {"Aspected Benefic", "吉星相位"}

    class Malefic(ActionBase):
        """
        Deals unaspected damage with a potency of 150.
        """
        id = 3596
        name = {"Malefic", "凶星"}

    class MaleficIi(ActionBase):
        """
        Deals unaspected damage with a potency of 170.
        """
        id = 3598
        name = {"Malefic II", "灾星"}

    class Combust(ActionBase):
        """
        Deals unaspected damage over time. Potency: 40 Duration: 18s
        838, Combust, Combust, Proximity of a theoretical sun is causing damage over time.
        """
        id = 3599
        name = {"Combust", "烧灼"}

    class Helios(ActionBase):
        """
        Restores own HP and the HP of all nearby party members. Cure Potency: 330
        """
        id = 3600
        name = {"Helios", "阳星"}

    class AspectedHelios(ActionBase):
        """
        Restores own HP and the HP of all nearby party members. Cure Potency: 200 Diurnal Sect Effect: Regen Cure Potency: 100 Duration: 15s Effect cannot be stacked.(source.level>=50?(source.job==33? Nocturnal Sect Effect: Erects a magicked barrier which nullifies damage equaling 125% of the amount of HP restored Duration: 30s Effect cannot be stacked with scholar's Galvanize. Can only be executed while under the effect of Diurnal Sect or Nocturnal Sect.: Can only be executed while under the effect of Diurnal Sect.): Can only be executed while under the effect of Diurnal Sect.)
        836, Aspected Helios, Aspected Helios, Regenerating HP over time.
        """
        id = 3601
        name = {"Aspected Helios", "阳星相位"}

    class Ascend(ActionBase):
        """
        Resurrects target to a weakened state.
        """
        id = 3603
        name = {"Ascend", "生辰"}

    class DiurnalSect(ActionBase):
        """
        Adds Regen to certain actions.(source.level>=50?(source.job==33? Cannot be used with Nocturnal Sect. Shares a recast timer with Nocturnal Sect. Effect cannot be removed while in combat.:):) Effect ends upon reuse.
        839, Diurnal Sect, Diurnal Sect, A <UIForeground(506)><UIGlow(507)>Regen</UIGlow></UIForeground> effect is added to certain actions.
        """
        id = 3604
        name = {"Diurnal Sect", "白昼学派"}

    class NocturnalSect(ActionBase):
        """
        Adds a damage-nullifying barrier to certain actions. Also increases MP cost of Aspected Benefic. Cannot be used with Diurnal Sect. Shares a recast timer with Diurnal Sect. Effect cannot be removed while in combat. Effect ends upon reuse.
        840, Nocturnal Sect, Nocturnal Sect, A damage-nullifying barrier effect is added to certain actions.
        """
        id = 3605
        name = {"Nocturnal Sect", "黑夜学派"}

    class Lightspeed(ActionBase):
        """
        Reduces cast times for spells by 2.5 seconds. Duration: 15s
        841, Lightspeed, Lightspeed, Spell casting time is reduced.
        1403, Lightspeed, Lightspeed, Spell casting time and MP cost are reduced by 100% and 50% respectively.
        """
        id = 3606
        name = {"Lightspeed", "光速"}

    class CombustIi(ActionBase):
        """
        Deals unaspected damage over time. Potency: 50 Duration: 30s
        843, Combust II, Combust II, Proximity of a theoretical sun is causing damage over time.
        """
        id = 3608
        name = {"Combust II", "炽灼"}

    class BeneficIi(ActionBase):
        """
        Restores target's HP. Cure Potency: 700
        """
        id = 3610
        name = {"Benefic II", "福星"}

    class Synastry(ActionBase):
        """
        Generate an aetheric bond with target party member. Each time you cast a single-target healing spell on yourself or a party member, the party member with whom you have the bond will also recover HP equaling 40% of the original spell. Duration: 20s
        845, Synastry, Synastry, An aetheric bond is created with a party member. Each time a single-target healing spell is cast, that member will recover partial HP.
        846, Synastry, Synastry, An aetheric bond is created with a party astrologian. Each time a single-target healing spell is cast by the astrologian, you will recover partial HP.
        1336, Synastry, Synastry, An aetheric bond is created with a party member. Each time a single-target healing spell is cast, that member will recover partial HP.
        1337, Synastry, Synastry, An aetheric bond is created with a party astrologian. Each time a single-target healing spell is cast by the astrologian, you will recover partial HP.
        """
        id = 3612
        name = {"Synastry", "星位合图"}

    class CollectiveUnconscious(ActionBase):
        """
        Creates a celestial ring around the caster. Diurnal Sect Effect: Reduces damage taken by 10% and applies Wheel of Fortune to self and any party members who enter Duration: 18s Wheel of Fortune Effect (Diurnal): Regen Cure Potency: 100 Duration: 15s Nocturnal Sect Effect: Grants healing over time and applies Wheel of Fortune to self and any party members who enter Cure Potency: 100 Duration: 18s Wheel of Fortune Effect (Nocturnal): Reduces damage taken by 10% Duration: 20s Effect ends upon using another action or moving (including facing a different direction). Cancels auto-attack upon execution. Can only be executed while under the effect of Diurnal Sect or Nocturnal Sect.
        847, Collective Unconscious, Collective Unconscious, An area of mind attunement is healing party members.
        848, Collective Unconscious, Collective Unconscious, An area of mind attunement is created, reducing damage taken for all who enter.
        849, Collective Unconscious, Collective Unconscious, Damage taken is reduced.
        2283, Collective Unconscious, Collective Unconscious, An area of mind attunement is created, reducing damage taken for all who enter.
        """
        id = 3613
        name = {"Collective Unconscious", "命运之轮"}

    class EssentialDignity(ActionBase):
        """
        Restores target's HP. Cure Potency: 400 Potency increases up to 1,100 as the target's HP decreases.(source.job==33?(source.level>=78? Maximum Charges: 2:):)
        """
        id = 3614
        name = {"Essential Dignity", "先天禀赋"}

    class Gravity(ActionBase):
        """
        Deals unaspected damage with a potency of 140 to target and all enemies nearby it.
        """
        id = 3615
        name = {"Gravity", "重力"}

    class TheBalance(ActionBase):
        """
        Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles. Duration: 15s (source.job==33?(source.level>=50?Additional Effect: Grants a Solar Seal when used in combat :):) ※This action cannot be assigned to a hotbar.
        """
        id = 4401
        name = {"the Balance", "太阳神之衡"}

    class TheArrow(ActionBase):
        """
        Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles. Duration: 15s (source.job==33?(source.level>=50?Additional Effect: Grants a Lunar Seal when used in combat :):) ※This action cannot be assigned to a hotbar.
        """
        id = 4402
        name = {"the Arrow", "放浪神之箭"}

    class TheSpear(ActionBase):
        """
        Increases damage dealt by a party member or self by 6% if target is melee DPS or tank, or 3% for all other roles. Duration: 15s (source.job==33?(source.level>=50?Additional Effect: Grants a Celestial Seal when used in combat :):) ※This action cannot be assigned to a hotbar.
        """
        id = 4403
        name = {"the Spear", "战争神之枪"}

    class TheBole(ActionBase):
        """
        Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles. Duration: 15s (source.job==33?(source.level>=50?Additional Effect: Grants a Solar Seal when used in combat :):) ※This action cannot be assigned to a hotbar.
        """
        id = 4404
        name = {"the Bole", "世界树之干"}

    class TheEwer(ActionBase):
        """
        Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles. Duration: 15s (source.job==33?(source.level>=50?Additional Effect: Grants a Lunar Seal when used in combat :):) ※This action cannot be assigned to a hotbar.
        """
        id = 4405
        name = {"the Ewer", "河流神之瓶"}

    class TheSpire(ActionBase):
        """
        Increases damage dealt by a party member or self by 6% if target is ranged DPS or healer, or 3% for all other roles. Duration: 15s (source.job==33?(source.level>=50?Additional Effect: Grants a Celestial Seal when used in combat :):) ※This action cannot be assigned to a hotbar.
        """
        id = 4406
        name = {"the Spire", "建筑神之塔"}

    class EarthlyStar(ActionBase):
        """
        Deploys an Earthly Star in the designated area and grants the effect of Earthly Dominance. Duration: 10s Executing Stellar Detonation while under the effect of Earthly Dominance creates a Stellar Burst dealing unaspected damage with a potency of 100 to all nearby enemies. Also restores own HP and the HP of all nearby party members. Cure Potency: 540 After 10s, Earthly Dominance effect is changed to Giant Dominance. Duration: 10s Waiting 10s or executing Stellar Detonation while under the effect of Giant Dominance creates a Stellar Explosion dealing unaspected damage with a potency of 150 to all nearby enemies. Also restores own HP and the HP of all nearby party members. Cure Potency: 720
        """
        id = 7439
        name = {"Earthly Star", "地星"}

    class MaleficIii(ActionBase):
        """
        Deals unaspected damage with a potency of 210.
        """
        id = 7442
        name = {"Malefic III", "祸星"}

    class MinorArcana(ActionBase):
        """
        Converts currently drawn arcanum into the Lord of Crowns when Balance, Arrow, or Spear, or the Lady of Crowns when Bole, Ewer, or Spire. Only one arcanum effect can be applied to a target at a time.
        """
        id = 7443
        name = {"Minor Arcana", "小奥秘卡"}

    class LordOfCrowns(ActionBase):
        """
        Increases damage dealt by a party member or self by 8% if target is melee DPS or tank, or 4% for all other roles. Duration: 15s ※This action cannot be assigned to a hotbar.
        1451, Lord of Crowns, Lord of Crowns, Damage dealt is increased.
        1876, Lord of Crowns, Lord of Crowns, Damage dealt is increased.
        """
        id = 7444
        name = {"Lord of Crowns", "王冠之领主"}

    class LadyOfCrowns(ActionBase):
        """
        Increases damage dealt by a party member or self by 8% if target is ranged DPS or healer, or 4% for all other roles. Duration: 15s ※This action cannot be assigned to a hotbar.
        1452, Lady of Crowns, Lady of Crowns, Damage taken is reduced.
        1877, Lady of Crowns, Lady of Crowns, Damage dealt is increased.
        """
        id = 7445
        name = {"Lady of Crowns", "王冠之贵妇"}

    class SleeveDraw(ActionBase):
        """
        Draws a card (arcanum) from your divining deck. You cannot draw an arcanum if you are aligned with its Seal of Arcana. When aligned with all three seals, any arcanum may be drawn. Additional Effect: Restores 8% of maximum MP
        1926, Sleeve Draw, Sleeve Draw, Draws a new arcanum after executing <UIForeground(500)><UIGlow(501)>Play</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Minor Arcana</UIGlow></UIForeground>, or <UIForeground(500)><UIGlow(501)>Undraw</UIGlow></UIForeground>.
        """
        id = 7448
        name = {"Sleeve Draw", "袖内抽卡"}

    class StellarDetonation(ActionBase):
        """
        While under the effect of Earthly Dominance, detonates the currently deployed Earthly Star, creating a Stellar Burst that deals unaspected damage with a potency of 100 to all nearby enemies. Additional Effect: Restores own HP and the HP of all nearby party members Cure Potency: 540 While under the effect of Giant Dominance, detonates the currently deployed Earthly Star, creating a Stellar Explosion that deals unaspected damage with a potency of 150 to all nearby enemies. Additional Effect: Restores own HP and the HP of all nearby party members Cure Potency: 720
        """
        id = 8324
        name = {"Stellar Detonation", "星体爆轰"}

    class Undraw(ActionBase):
        """
        Returns the currently drawn arcanum back to your deck.
        """
        id = 9629
        name = {"Undraw", "奥秘卡废弃"}

    class Divination(ActionBase):
        """
        Increases damage dealt by self and nearby party members. Duration: 15s Can only be executed after obtaining three Seals of Arcana by playing at least three arcanum. Effectiveness is determined by the number of different types of seals in play. 1 Seal Type: 4% 2 Seal Types: 5% 3 Seal Types: 6%
        1878, Divination, Divination, Damage dealt is increased.
        2034, Divination, Divination, Damage dealt is increased while damage taken is reduced.
        """
        id = 16552
        name = {"Divination", "占卜"}

    class CelestialOpposition(ActionBase):
        """
        Restores own HP and the HP of all nearby party members. Cure Potency: 200 Diurnal Sect Effect: Regen Cure Potency: 100 Duration: 15s Effect cannot be stacked. Nocturnal Sect Effect: Erects a magicked barrier which nullifies damage equaling 125% of the amount of HP restored Duration: 30s Can only be executed while under the effect of Diurnal Sect or Nocturnal Sect.
        """
        id = 16553
        name = {"Celestial Opposition", "天星冲日"}

    class CombustIii(ActionBase):
        """
        Deals unaspected damage over time. Potency: 60 Duration: 30s
        1881, Combust III, Combust III, Sustaining damage over time.
        2041, Combust III, Combust III, Damage dealt and potency of all HP restoration actions are reduced.
        """
        id = 16554
        name = {"Combust III", "焚灼"}

    class MaleficIv(ActionBase):
        """
        Deals unaspected damage with a potency of 250.
        """
        id = 16555
        name = {"Malefic IV", "煞星"}

    class CelestialIntersection(ActionBase):
        """
        Restores own or target party member's HP. Cure Potency: 200 Diurnal Sect Effect: Erects a magicked barrier which nullifies damage equaling 200% of the amount of HP restored Duration: 30s Nocturnal Sect Effect: Regen Cure Potency: 150 Duration: 15s Effect cannot be stacked. Can only be executed while under the effect of Diurnal Sect or Nocturnal Sect.
        """
        id = 16556
        name = {"Celestial Intersection", "天星交错"}

    class Horoscope(ActionBase):
        """
        Reads your fortune and those of nearby party members, granting them Horoscope. Duration: 10s Effect upgraded to Horoscope Helios upon receiving the effects of Helios or Aspected Helios. Duration: 30s Restores the HP of those under either effect when the cards are read a second time or the effect expires. Horoscope Cure Potency: 200 Horoscope Helios Cure Potency: 400
        1890, Horoscope, Horoscope, Primed to receive the healing effects of <UIForeground(500)><UIGlow(501)>Horoscope</UIGlow></UIForeground>.
        """
        id = 16557
        name = {"Horoscope", "天宫图"}

    class Horoscope(ActionBase):
        """
        Restores own HP and the HP of all nearby party members. Potency is determined by the Horoscope effect of party members. Effect expires upon execution. Horoscope Potency: 200 Horoscope Helios Potency: 400
        1890, Horoscope, Horoscope, Primed to receive the healing effects of <UIForeground(500)><UIGlow(501)>Horoscope</UIGlow></UIForeground>.
        """
        id = 16558
        name = {"Horoscope", "天宫图"}

    class NeutralSect(ActionBase):
        """
        Increases healing magic potency by 20%. Additional Effect: Aspected Helios and Aspected Benefic receive the effects of both Diurnal Sect and Nocturnal Sect Duration: 20s
        1892, Neutral Sect, Neutral Sect, Healing magic potency is increased.
        2044, Neutral Sect, Neutral Sect, Spell cast and recast times are reduced. <UIForeground(500)><UIGlow(501)>Helios</UIGlow></UIForeground> is upgraded to <UIForeground(500)><UIGlow(501)>Aspected Helios</UIGlow></UIForeground>, while <UIForeground(500)><UIGlow(501)>Benefic</UIGlow></UIForeground> is upgraded to <UIForeground(500)><UIGlow(501)>Aspected Benefic</UIGlow></UIForeground>.
        """
        id = 16559
        name = {"Neutral Sect", "中间学派"}

    class Play(ActionBase):
        """
        Triggers the effect of your drawn arcanum. Only one arcanum effect can be applied to a target at a time.
        """
        id = 17055
        name = {"Play", "出卡"}

    class AspectedBenefic(ActionBase):
        """
        Restores target's HP. Cure Potency: 200 Diurnal Sect Effect: Regen Cure Potency: 200 Duration: 15s Effect cannot be stacked.(source.level>=50?(source.job==33? Nocturnal Sect Effect: Erects a magicked barrier which nullifies damage equaling 250% of the amount of HP restored Duration: 30s Effect cannot be stacked with scholar's Galvanize. Can only be executed while under the effect of Diurnal Sect or Nocturnal Sect.: Can only be executed while under the effect of Diurnal Sect.): Can only be executed while under the effect of Diurnal Sect.)
        835, Aspected Benefic, Aspected Benefic, Regenerating HP over time.
        """
        id = 17151
        name = {"Aspected Benefic", "吉星相位"}

    class AspectedHelios(ActionBase):
        """
        Restores own HP and the HP of all nearby party members. Cure Potency: 200 Diurnal Sect Effect: Regen Cure Potency: 100 Duration: 15s Effect cannot be stacked.(source.level>=50?(source.job==33? Nocturnal Sect Effect: Erects a magicked barrier which nullifies damage equaling 125% of the amount of HP restored Duration: 30s Effect cannot be stacked with scholar's Galvanize. Can only be executed while under the effect of Diurnal Sect or Nocturnal Sect.: Can only be executed while under the effect of Diurnal Sect.): Can only be executed while under the effect of Diurnal Sect.)
        836, Aspected Helios, Aspected Helios, Regenerating HP over time.
        """
        id = 17152
        name = {"Aspected Helios", "阳星相位"}
