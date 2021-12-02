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
        id = 0  # TODO: unk id
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
        id = 0  # TODO: unk id
        name = {"Knight's Benediction"}
        cure_potency = 250

    class Requiescat(StatusBase):
        id = 1368  # TODO: id may change
        name = {'Requiescat', '安魂祈祷'}

    class ArmsUp(StatusBase):
        id = 1176
        name = {'Arms Up', '武装'}
        taken_damage_modify = .85

    class BladeOfValor(StatusBase):
        id = 0  # TODO: unk id
        name = {'Blade of Valor'}

        def __init__(self, source: 'Actor|None', target: 'Actor|None', source_action: int, is_main_target: bool):
            super().__init__(source, target, source_action, is_main_target)
            self.damage_potency = 80 if is_main_target else 40


class Actions:
    class FastBlade(ActionBase):
        """
        Delivers an attack with a potency of 200.
        """
        id = 9
        name = {'Fast Blade', '先锋剑'}
        damage_potency = 200
        attack_type = physic

    class RiotBlade(ActionBase):
        """
        Delivers an attack with a potency of 170.
        Combo Action: Fast Blade
        Combo Potency: 300
        Combo Bonus: Restores MP
        """
        id = 15
        name = {'Riot Blade', '暴乱剑'}
        combo_action = 'FastBlade'
        damage_potency = 170
        combo_damage_potency = 170
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

    class Sentinel(ActionBase):
        """
        Reduces damage taken by 30%.
        Duration: 15s
        """
        id = 17
        name = {'Sentinel', '预警'}
        status_to_target = Status.Sentinel

    class FightOrFlight(ActionBase):
        """
        Increases physical damage dealt by 25%.
        Duration: 25s
        """
        id = 20
        name = {'Fight or Flight', '战逃反应'}
        status_to_target = Status.FightOrFlight

    class RageOfHalone(ActionBase):
        """
        Delivers an attack with a potency of 100.
        Combo Action: Riot Blade
        Combo Potency: 330
        """
        id = 21
        name = {'Rage of Halone', '战女神之怒'}
        damage_potency = 100
        combo_action = 'RiotBlade'
        combo_damage_potency = 330
        attack_type = physic

    class CircleOfScorn(ActionBase):
        """
        Delivers an attack with a potency of 100 to all nearby enemies.
        Additional Effect: Damage over time
        Potency: 30
        Duration: 15s
        """
        id = 23
        name = {'Circle of Scorn', '厄运流转'}
        damage_potency = 100
        attack_type = physic
        status_to_target = Status.CircleOfScorn

    class ShieldLob(ActionBase):
        """
        Delivers an attack with a potency of 100.
        Additional Effect: Stun
        Duration: 6s
        """
        id = 24
        name = {'Shield Lob', '投盾'}
        damage_potency = 120
        attack_type = physic

    class Cover(ActionBase):
        """
        Take all damage intended for another party member as long as said member remains within 10 yalms.
        Does not activate with certain attacks.
        Duration: 12s
        Oath Gauge Cost: 50
        80, 保护, Cover, 正在保护特定的队员
        1300, 保护, Cover, 正在保护特定的队员，效果中受到的伤害增加
        2412, 保护, Cover, 正在保护特定的对象
        """
        id = 27
        name = {'Cover', '保护'}

    class IronWill(ActionBase):
        """
        Significantly increases enmity generation.
        Effect ends upon reuse.
        79, 钢铁信念, Iron Will, 自身仇恨提高
        393, 钢铁信念, Iron Will, 自身仇恨提高
        """
        id = 28
        name = {'Iron Will', '钢铁信念'}

    class SpiritsWithin(ActionBase):
        """
        Delivers an attack with a potency of 250.
        Additional Effect: Restores MP
        """
        id = 29
        name = {'Spirits Within', '深奥之灵'}
        damage_potency = 250
        attack_type = physic

    class HallowedGround(ActionBase):
        """
        Renders you impervious to most attacks.
        Duration: 10s
        """
        id = 30
        name = {'Hallowed Ground', '神圣领域'}
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
        725, 沥血剑, Goring Blade, 体力逐渐减少
        """
        id = 3538
        name = {'Goring Blade', '沥血剑'}
        damage_potency = 100
        combo_action = 'RiotBlade'
        combo_damage_potency = 250
        status_to_target = Status.GoringBlade
        attack_type = physic

    class RoyalAuthority(ActionBase):
        """
        Delivers an attack with a potency of 130.
        Combo Action: Riot Blade
        Combo Potency: 420
        Combo Bonus: Grants 3 stacks of Sword Oath
        Duration: 30s
        """
        id = 3539
        name = {'Royal Authority', '王权剑'}
        damage_potency = 130
        combo_action = 'RiotBlade'
        combo_damage_potency = 420
        attack_type = physic

    class DivineVeil(ActionBase):
        """
        Upon HP recovery via healing magic cast by self or a party member, a protective barrier is cast on all party members within a radius of 15 yalms.
        Duration: 30s
        Barrier Effect: Prevents damage up to 10% of your maximum HP
        Duration: 30s
        Additional Effect: Restore target's HP
        Cure Potency: 400
        Effect ends upon casting barrier on self and nearby party members.
        726, 圣光幕帘, Divine Veil, 受到治疗魔法时为周围队员附加能够抵消一定伤害的防护罩
        727, 圣光幕帘, Divine Veil, 抵消一定伤害
        2168, 圣光幕帘, Divine Veil, 身附能够抵消一定伤害的防护罩，当防护罩因吸收足量伤害而消失时，会为周围队员附加能够抵消一定伤害的防护罩
        2169, 圣光幕帘, Divine Veil, 抵消一定伤害
        """
        id = 3540
        name = {'Divine Veil', '圣光幕帘'}

    class Clemency(ActionBase):
        """
        Restores target's HP.
        Cure Potency: 1,000
        Additional Effect: Restores to self 50% of HP restored to target if target is a party member
        """
        id = 3541
        name = {'Clemency', '深仁厚泽'}
        cure_potency = 1200
        aoe_scale = .5

    class Sheltron(ActionBase):
        """
        Block incoming attacks.
        Duration: 6s
        Oath Gauge Cost: 50

        728, 盾阵, Sheltron, 下次受到攻击时必定发动格挡
        1856, 盾阵, Sheltron, 受到攻击时必定发动格挡
        """
        id = 3542
        name = {'Sheltron', '盾阵'}
        status_to_target = Status.Sheltron

    class TotalEclipse(ActionBase):
        """
        Delivers an attack with a potency of 100 to all nearby enemies.

        """
        id = 7381
        name = {'Total Eclipse', '全蚀斩'}
        damage_potency = 100
        attack_type = physic

    class Intervention(ActionBase):
        """
        Reduces target party member's damage taken by 10%.
        Duration: 8s
        Additional Effect: Increases damage reduction by an additional 10% if Rampart or Sentinel are active
        Additional Effect: Grants Knight's Resolve to target
        Knight's Resolve Effect: Reduces damage taken by 10%
        Duration: 4s
        Additional Effect: Grants Knight's Benediction to target
        Knight's Benediction Effect: Gradually restores HP
        Cure Potency: 250
        Duration: 12s
        Oath Gauge Cost: 50
        1174, 干预, Intervention, 减轻所受到的伤害
        2020, 干预, Intervention, 减轻所受到的伤害
        """
        id = 7382
        name = {'Intervention', '干预'}
        status_to_target = Status.KnightsResolve, Status.KnightsBenediction

    class Requiescat(ActionBase):
        """
        Deals unaspected damage with a potency of 400.
        Additional Effect: Grants 5 stacks of Requiescat
        Requiescat Effect: Increases the potency of Holy Spirit and Holy Circle and spells will require no cast time
        Duration: 30s
        对目标发动无属性魔法攻击 威力：150～550 自身剩余魔力越高威力越大 追加效果（自身当前魔力在最大魔力的80%以上时）：自身发动攻击魔法的伤害及治疗魔法的治疗量提高50%(source.job==19?(source.level>=78? 同时，咏唱魔法不需要咏唱时间 : ): )持续时间：12秒

        1368, 安魂祈祷, Requiescat, 魔法攻击所造成的伤害及发动治疗魔法的治疗量提高 习得安魂祈祷效果提高后追加效果：咏唱魔法没有任何咏唱时间
        1369, 安魂祈祷, Requiescat, 咏唱魔法时没有任何咏唱时间，并且不会消耗魔力
        """
        id = 7383
        name = {'Requiescat', '安魂祈祷'}
        damage_potency = 400
        attack_type = magic
        status_to_source = Status.Requiescat

    class HolySpirit(ActionBase):
        """
        Deals unaspected damage with a potency of 270.
        Requiescat Potency: 540
        Additional Effect: Restores own HP
        Cure Potency: 400
        对目标发动无属性魔法攻击 威力：350
        """
        id = 7384
        name = {'Holy Spirit', '圣灵'}
        cure_potency = 400

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 540 if source.effects.has(Status.Requiescat.id) else 270

    class PassageOfArms(ActionBase):
        """
        Increases block rate to 100% and creates a designated area in a cone behind you in which party members will only suffer 85% of all damage inflicted.
        Duration: 18s
        Effect ends upon using another action or moving (including facing a different direction).
        Cancels auto-attack upon execution.
        向自身后方扇形范围展开减轻伤害的防护区域 效果时间内自身的格挡发动率变为100%，范围内的队员受到的伤害减轻15% 持续时间：18秒 效果时间内发动技能或进行移动、转身都会立即解除武装戍卫 发动之后会停止自动攻击

        1175, 武装戍卫, Passage of Arms, 产生减轻伤害的防护区域
        """
        id = 7385
        name = {'Passage of Arms', '武装戍卫'}

    class Prominence(ActionBase):
        """
        Delivers an attack with a potency of 100 to all nearby enemies.
        Combo Action: Total Eclipse
        Combo Potency: 170
        Combo Bonus: Restores MP
        对自身周围的敌人发动范围物理攻击 威力：100 连击条件：全蚀斩 连击中威力：220(source.job==19?(source.level>=66? 连击成功：恢复自身魔力:):)

        """
        id = 16457
        name = {'Prominence', '日珥斩'}
        damage_potency = 100
        combo_action = 'TotalEclipse'
        combo_damage_potency = 170
        attack_type = physic

    class HolyCircle(ActionBase):
        """
        Deals unaspected damage with a potency of 130 to all nearby enemies.
        Requiescat Potency: 300
        Additional Effect: Restores own HP
        Cure Potency: 400
        对自身周围的敌人发动无属性范围魔法攻击 威力：250
        """
        id = 16458
        name = {'Holy Circle', '圣环'}
        cure_potency = 400

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 300 if source.effects.has(Status.Requiescat.id) else 130

    class Confiteor(ActionBase):
        """
        Deals unaspected damage with a potency of 900 to target and all enemies nearby it.
        Can only be executed while under the effect of Requiescat. Effect fades upon execution.
        对目标及其周围的敌人发动无属性范围魔法攻击 威力：800 发动后会取消安魂祈祷状态 发动条件：安魂祈祷状态中

        2076, 悔罪, Confiteor, 发动攻击所造成的伤害及自身发动的体力恢复效果降低
        """
        id = 16459
        name = {'Confiteor', '悔罪'}
        damage_potency = 900
        attack_type = magic

    class Atonement(ActionBase):
        """
        Delivers an attack with a potency of 420.
        Additional Effect: Restores MP
        Can only be executed while under the effect of Sword Oath.
        对目标发动物理攻击 威力：550 追加效果：恢复自身魔力 发动条件：忠义之剑

        """
        id = 16460
        name = {'Atonement', '赎罪剑'}
        damage_potency = 420
        attack_type = physic

    class Intervene(ActionBase):
        """
        Rushes target and delivers an attack with a potency of 150.
        Maximum Charges: 2
        Cannot be executed while bound.
        冲向目标并发动物理攻击 威力：200 积蓄次数：2 止步状态下无法发动
        """
        id = 16461
        name = {'Intervene', '调停'}
        damage_potency = 150
        attack_type = physic

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
        id = 0  # TODO: unk id
        name = {'Holy Sheltron'}
        status_to_target = Status.KnightsResolve, Status.KnightsBenediction

    class Expiacion(ActionBase):
        """
        Delivers an attack to target and all enemies nearby it with a potency of 300 for the first enemy, and 50% less for all remaining enemies.
        Additional Effect: Restores MP
        """
        id = 0  # TODO: unk id
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
        id = 0  # TODO: unk id
        name = {'Blade of Faith'}
        damage_potency = 250
        attack_type = magic
        aoe_scale = .5
        combo_action = 'Confiteor'

    class BladeOfTruth(ActionBase):
        """
        Deals unaspected damage to target and all enemies nearby it with a potency of 350 for the first enemy, and 50% less for all remaining enemies.
        Combo Action: Blade of Faith
        Combo Bonus: Restores MP
        """
        id = 0  # TODO: unk id
        name = {'Blade of Truth'}
        damage_potency = 350
        attack_type = magic
        aoe_scale = .5
        combo_action = 'BladeOfFaith'

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
        id = 0  # TODO: unk id
        name = {'Blade of Valor'}
        damage_potency = 420
        attack_type = magic
        aoe_scale = .5
        combo_action = 'BladeOfTruth'
        status_to_target = Status.BladeOfValor
