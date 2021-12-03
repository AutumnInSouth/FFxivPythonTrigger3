from ..base import *


class Status:
    class FightOrFlight(StatusBase):
        id = 76
        name = {'Fight or Flight', '战逃反应'}
        damage_modify = 1.25
        modify_type = physic

    class Sheltron(StatusBase):
        id = 1856
        name = {'Sheltron', '盾阵'}

    class Sentinel(StatusBase):
        id = 74
        name = {'Sentinel', '预警'}
        taken_damage_modify = 0.7

    class CircleOfScorn(StatusBase):
        id = 248
        name = {'Circle of Scorn', '厄运流转'}
        damage_potency = 30

    class HallowedGround(StatusBase):
        id = 82  # TODO: id may be 1302
        name = {'Hallowed Ground', '神圣领域'}
        taken_damage_modify = 0

    class GoringBlade(StatusBase):
        id = 725
        name = {'Goring Blade', '沥血剑'}
        damage_potency = 65

    class KnightsResolve(StatusBase):
        id = 2675
        name = {"Knight's Resolve"}

        def __init__(self, source: 'Actor|None', target: 'Actor|None', source_action: int, is_main_target: bool):
            super().__init__(source, target, source_action, is_main_target)
            if source_action == Actions.HolySheltron.id:
                self.taken_damage_modify = 0.85
            else:
                self.taken_damage_modify = 0.9
                for eid, effect in source.effects.get_items():
                    if eid == 74 or eid == 71:  # TODO: Rampart may be 71 1191 1987
                        self.taken_damage_modify -= .1
                        break

    class KnightsBenediction(StatusBase):
        id = 2676
        name = {"Knight's Benediction"}
        cure_potency = 250

    class Requiescat(StatusBase):
        id = 1368
        name = {'Requiescat', '安魂祈祷'}

    class ArmsUp(StatusBase):
        id = 1176
        name = {'Arms Up', '武装'}
        taken_damage_modify = .85

    class BladeOfValor(StatusBase):
        id = 2721
        name = {'Blade of Valor'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None', source_action: int, is_main_target: bool):
            super().__init__(source, target, source_action, is_main_target)
            self.damage_potency = 80 if is_main_target else 40


class Actions:
    class FastBlade(ActionBase):
        """
Delivers an attack with a potency of (source.job==19?(source.level>=84?200:150):150).
        """
        id = 9
        name = {'先锋剑', 'Fast Blade'}
        attack_type = physic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 200 if source.job == 'Paladin' and source.level >= 84 else 150

    class FightOrFlight(ActionBase):
        """
Increases physical damage dealt by 25%.
Duration: 25s
    76, Fight or Flight, Physical damage dealt is increased.
        """
        id = 20
        name = {'战逃反应', 'Fight or Flight'}
        status_to_target = Status.FightOrFlight

    class RiotBlade(ActionBase):
        """
Delivers an attack with a potency of (source.job==19?(source.level>=84?170:100):100).
Combo Action: Fast Blade
Combo Potency: (source.job==19?(source.level>=84?300:230):230)(source.job==19?(source.level>=58?
Combo Bonus: Restores MP:):)
        """
        id = 15
        name = {'Riot Blade', '暴乱剑'}
        combo_action = 9
        damage_potency = 170
        combo_damage_potency = 300
        attack_type = physic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 170 if source.job == 'Paladin' and source.level >= 84 else 100
            self.combo_damage_potency = 300 if source.job == 'Paladin' and source.level >= 84 else 230

    class TotalEclipse(ActionBase):
        """
Delivers an attack with a potency of 100 to all nearby enemies.
        """
        id = 7381
        name = {'Total Eclipse', '全蚀斩'}
        damage_potency = 100
        attack_type = physic

    class ShieldBash(ActionBase):
        """
Delivers an attack with a potency of 100.
Additional Effect: Stun
Duration: 6s
        """
        id = 16
        name = {'Shield Bash', '盾牌猛击'}
        damage_potency = 100
        attack_type = physic

    class IronWill(ActionBase):
        """
Significantly increases enmity generation.
Effect ends upon reuse.
    393, Iron Will, Enmity is increased.
    79, Iron Will, Enmity is increased.
        """
        id = 28
        name = {'钢铁信念', 'Iron Will'}

    class ShieldLob(ActionBase):
        """
Delivers a ranged attack with a potency of 100.
Additional Effect: Increased enmity
        """
        id = 24
        name = {'投盾', 'Shield Lob'}
        damage_potency = 120
        attack_type = physic

    class RageOfHalone(ActionBase):
        """
Delivers an attack with a potency of 100.
Combo Action: Riot Blade
Combo Potency: 330
    1370, Rage of Halone, Damage dealt and potency of all HP restoration actions are reduced.
        """
        id = 21
        name = {'战女神之怒', 'Rage of Halone'}
        combo_action = 15
        damage_potency = 100
        combo_damage_potency = 330
        attack_type = physic

    class SpiritsWithin(ActionBase):
        """
Delivers an attack with a potency of 250.(source.job==19?(source.level>=58?
Additional Effect: Restores MP:):)
        """
        id = 29
        name = {'Spirits Within', '深奥之灵'}
        damage_potency = 250
        attack_type = physic

    class Sheltron(ActionBase):
        """
Block incoming attacks.
Duration: (source.job==19?(source.level>=74?6:4):4)s
Oath Gauge Cost: 50
    728, Sheltron, Next attack will be blocked.
    1856, Sheltron, Blocking incoming attacks.
        """
        id = 3542
        name = {'Sheltron', '盾阵'}
        status_to_target = Status.Sheltron

    class Sentinel(ActionBase):
        """
Reduces damage taken by 30%.
Duration: 15s
    74, Sentinel, Damage taken is reduced.
        """
        id = 17
        name = {'预警', 'Sentinel'}
        status_to_target = Status.Sentinel

    class Prominence(ActionBase):
        """
Delivers an attack with a potency of 100 to all nearby enemies.
Combo Action: Total Eclipse
Combo Potency: 170(source.job==19?(source.level>=66?
Combo Bonus: Restores MP:):)
        """
        id = 16457
        name = {'Prominence', '日珥斩'}
        combo_action = 7381
        damage_potency = 100
        combo_damage_potency = 170
        attack_type = physic

    class Cover(ActionBase):
        """
Take all damage intended for another party member as long as said member remains within 10 yalms.
Does not activate with certain attacks.
Duration: 12s
Oath Gauge Cost: 50
    80, Cover, Protecting a party member.
    1300, Cover, Protecting a party member. Damage taken is increased.
    2412, Cover, Protecting an ally.
        """
        id = 27
        name = {'Cover', '保护'}

    class CircleOfScorn(ActionBase):
        """
Delivers an attack with a potency of 100 to all nearby enemies.
Additional Effect: Damage over time
Potency: 30
Duration: 15s
    248, Circle of Scorn, Wounds are bleeding, causing damage over time.
        """
        id = 23
        name = {'厄运流转', 'Circle of Scorn'}
        damage_potency = 100
        attack_type = physic
        status_to_target = Status.CircleOfScorn

    class HallowedGround(ActionBase):
        """
Renders you impervious to most attacks.
Duration: 10s
    82, Hallowed Ground, Impervious to most attacks.
    1302, Hallowed Ground, Impervious to most attacks.
        """
        id = 30
        name = {'神圣领域', 'Hallowed Ground'}
        status_to_target = Status.HallowedGround

    class GoringBlade(ActionBase):
        """
Delivers an attack with a potency of 100.
Combo Action: Riot Blade
Combo Potency: 250
Combo Bonus: Damage over time
Potency: 65
Duration: 21s
Damage over time effect cannot be stacked with that of Blade of Valor.
    725, Goring Blade, Wounds are bleeding, causing damage over time.
        """
        id = 3538
        name = {'沥血剑', 'Goring Blade'}
        combo_action = 15
        damage_potency = 100
        combo_damage_potency = 250
        status_to_target = Status.GoringBlade
        attack_type = physic

    class DivineVeil(ActionBase):
        """
Upon HP recovery via healing magic cast by self or a party member, a protective barrier is cast on all party members within a radius of 15 yalms.
Duration: 30s
Barrier Effect: Prevents damage up to 10% of your maximum HP
Duration: 30s
(source.job==19?(source.level>=88?Additional Effect: Restore target's HP
Cure Potency: 400
:):)Effect ends upon casting barrier on self and nearby party members.
    726, Divine Veil, Upon HP recovery via healing magic, a damage-reducing barrier is created.
    727, Divine Veil, A holy barrier is nullifying damage.
    2168, Divine Veil, A holy barrier is nullifying damage. When barrier is completely absorbed, creates a barrier around all nearby party members.
    2169, Divine Veil, A holy barrier is nullifying damage.
        """
        id = 3540
        name = {'圣光幕帘', 'Divine Veil'}
        cure_potency = 400

    class Clemency(ActionBase):
        """
Restores target's HP.
Cure Potency: 1,000
Additional Effect: Restores to self 50% of HP restored to target if target is a party member
        """
        id = 3541
        name = {'Clemency', '深仁厚泽'}
        cure_potency = 1000
        aoe_scale = 0.5

    class RoyalAuthority(ActionBase):
        """
Delivers an attack with a potency of (source.job==19?(source.level>=84?130:100):100).
Combo Action: Riot Blade
Combo Potency: (source.job==19?(source.level>=84?420:390):390)(source.job==19?(source.level>=76?
Combo Bonus: Grants 3 stacks of Sword Oath
Duration: 30s:):)
        """
        id = 3539
        name = {'Royal Authority', '王权剑'}
        combo_action = 15
        attack_type = physic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 130 if source.job == 'Paladin' and source.level >= 84 else 100
            self.combo_damage_potency = 420 if source.job == 'Paladin' and source.level >= 84 else 390

    class Intervention(ActionBase):
        """
Reduces target party member's damage taken by 10%.
Duration: (source.job==19?(source.level>=82?8:6):6)s
Additional Effect: Increases damage reduction by an additional 10% if Rampart or Sentinel are active
(source.job==19?(source.level>=82?Additional Effect: Grants Knight's Resolve to target
Knight's Resolve Effect: Reduces damage taken by 10%
Duration: 4s
Additional Effect: Grants Knight's Benediction to target
Knight's Benediction Effect: Gradually restores HP
Cure Potency: 250
Duration: 12s
:):)Oath Gauge Cost: 50
    2020, Intervention, Damage taken is reduced.
    1174, Intervention, Damage taken is reduced.
        """
        id = 7382
        name = {'干预', 'Intervention'}
        status_to_target = Status.KnightsResolve, Status.KnightsBenediction

    class HolySpirit(ActionBase):
        """
Deals unaspected damage with a potency of (source.job==19?(source.level>=84?270:250):250).(source.job==19?(source.level>=68?
Requiescat Potency: (source.job==19?(source.level>=84?540:500):500):):)(source.job==19?(source.level>=84?
Additional Effect: Restores own HP
Cure Potency: 400:):)
        """
        id = 7384
        name = {'圣灵', 'Holy Spirit'}
        cure_potency = 400
        attack_type = magic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            if source.effects.has(Status.Requiescat.id):
                self.damage_potency = 540 if source.job == 'Paladin' and source.level >= 84 else 500  # TODO:original value
            else:
                self.damage_potency = 270 if source.job == 'Paladin' and source.level >= 84 else 250  # TODO:original value

    class Requiescat(ActionBase):
        """
Deals unaspected damage with a potency of 400.
Additional Effect: Grants 5 stacks of Requiescat
Requiescat Effect: Increases the potency of Holy Spirit and Holy Circle and spells will require no cast time
Duration: 30s
    1368, Requiescat, Potency of <UIForeground(500)><UIGlow(501)>Holy Spirit</UIGlow></UIForeground> and <UIForeground(500)><UIGlow(501)>Holy Circle</UIGlow></UIForeground> is increased and spells require no time to cast.
    1369, Requiescat, Spells require no time to cast and consume no MP.
        """
        id = 7383
        name = {'Requiescat', '安魂祈祷'}
        damage_potency = 400
        attack_type = magic

    class PassageOfArms(ActionBase):
        """
Increases block rate to 100% and creates a designated area in a cone behind you in which party members will only suffer 85% of all damage inflicted.
Duration: 18s
Effect ends upon using another action or moving (including facing a different direction).
Cancels auto-attack upon execution.
    1175, Passage of Arms, An area of land has been granted protection, reducing damage taken for all who enter.
        """
        id = 7385
        name = {'武装戍卫', 'Passage of Arms'}

    class HolyCircle(ActionBase):
        """
Deals unaspected damage with a potency of 130 to all nearby enemies.
Requiescat Potency: 300(source.job==19?(source.level>=84?
Additional Effect: Restores own HP
Cure Potency: 400:):)
        """
        id = 16458
        name = {'圣环', 'Holy Circle'}
        cure_potency = 400
        attack_type = magic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 300 if source.effects.has(Status.Requiescat.id) else 130

    class Intervene(ActionBase):
        """
Rushes target and delivers an attack with a potency of 150.
Maximum Charges: 2
Cannot be executed while bound.
        """
        id = 16461
        name = {'Intervene', '调停'}
        damage_potency = 150
        attack_type = physic

    class Atonement(ActionBase):
        """
Delivers an attack with a potency of (source.job==19?(source.level>=84?420:390):390).
Additional Effect: Restores MP
Can only be executed while under the effect of Sword Oath.
        """
        id = 16460
        name = {'赎罪剑', 'Atonement'}
        attack_type = physic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 420 if source.job == 'Paladin' and source.level >= 84 else 390

    class Confiteor(ActionBase):
        """
Deals unaspected damage with a potency of 900 to target and all enemies nearby it.
Can only be executed while under the effect of Requiescat. Effect fades upon execution.(source.job==19?(source.level>=90?
※Action changes to Blade of Faith upon execution.:):)
    2076, Confiteor, Damage dealt and potency of all HP restoration actions are reduced.
        """
        id = 16459
        name = {'Confiteor', '悔罪'}
        damage_potency = 900
        attack_type = magic

    class HolySheltron(ActionBase):
        """
Block incoming attacks.
Duration: 8s
Additional Effect: Grants Knight's Resolve
Knight's Resolve Effect: Reduces damage taken by 15%
Duration: 4s
Additional Effect: Grants Knight's Benediction
Knight's Benediction Effect: Gradually restores HP
Cure Potency: 250
Duration: 12s
Oath Gauge Cost: 50
        """
        id = 25746
        name = {'Holy Sheltron'}
        status_to_target = Status.KnightsResolve, Status.KnightsBenediction

    class Expiacion(ActionBase):
        """
Delivers an attack to target and all enemies nearby it with a potency of 300 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Restores MP
        """
        id = 25747
        name = {'Expiacion'}
        damage_potency = 300
        attack_type = physic
        aoe_scale = .5

    class BladeOfFaith(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 250 for the first enemy, and 50% less for all remaining enemies.
Combo Action: Confiteor
Combo Bonus: Restores MP
        """
        id = 25748
        name = {'Blade of Faith'}
        damage_potency = 250
        attack_type = magic
        aoe_scale = .5
        combo_action = 16459

    class BladeOfTruth(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 350 for the first enemy, and 50% less for all remaining enemies.
Combo Action: Blade of Faith
Combo Bonus: Restores MP
        """
        id = 25749
        name = {'Blade of Truth'}
        damage_potency = 350
        attack_type = magic
        aoe_scale = .5
        combo_action = 25746

    class BladeOfValor(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 420 for the first enemy, and 50% less for all remaining enemies.
Combo Action: Blade of Truth
Combo Bonus: Restores MP
Combo Bonus: Damage over time
Potency: 80 for the first enemy, and 50% less for all remaining enemies
Duration: 21s
Damage over time effect cannot be stacked with that of Goring Blade.
        """
        id = 25750
        name = {'Blade of Valor'}
        damage_potency = 420
        attack_type = magic
        aoe_scale = .5
        combo_action = 25747
        status_to_target = Status.BladeOfValor
