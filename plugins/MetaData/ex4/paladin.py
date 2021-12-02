from ..base import ActionBase, StatusBase, physic, magic


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
        id = 82  # 1302
        name = {'Hallowed Ground', '神圣领域'}
        taken_damage_modify = 0


class Actions:
    class FastBlade(ActionBase):
        """
        对目标发动物理攻击 威力：200

        """
        id = 9
        name = {'Fast Blade', '先锋剑'}
        damage_potency = 200
        attack_type = physic

    class RiotBlade(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：先锋剑 连击中威力：300(source.job==19?(source.level>=58? 连击成功：恢复自身魔力:):)

        """
        combo_action = 9
        damage_potency = 170
        combo_damage_potency = 170
        attack_type = physic

    class ShieldBash(ActionBase):
        """
        对目标发动物理攻击 威力：110 追加效果：眩晕 持续时间：6秒

        """
        id = 16
        name = {'Shield Bash', '盾牌猛击'}
        damage_potency = 100
        attack_type = physic

    class Sentinel(ActionBase):
        """
        一定时间内，将自身所受的伤害减轻30% 持续时间：15秒

        74, 预警, Sentinel, 减轻所受到的伤害
        """
        id = 17
        name = {'Sentinel', '预警'}
        status_to_target = Status.Sentinel

    class FightOrFlight(ActionBase):
        """
        一定时间内，自身发动物理攻击造成的伤害提高25% 持续时间：25秒

        76, 战逃反应, Fight or Flight, 物理攻击所造成的伤害提高
        """
        id = 20
        name = {'Fight or Flight', '战逃反应'}
        status_to_target = Status.FightOrFlight

    class RageOfHalone(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：暴乱剑 连击中威力：350

        1370, 战女神之怒, Rage of Halone, 发动攻击所造成的伤害及自身发动的体力恢复效果降低
        """
        id = 21
        name = {'Rage of Halone', '战女神之怒'}
        damage_potency = 100
        combo_action = 15
        combo_damage_potency = 330
        attack_type = physic

    class CircleOfScorn(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：120 追加效果：持续伤害 威力：35 持续时间：15秒

        248, 厄运流转, Circle of Scorn, 体力逐渐减少
        """
        id = 23
        name = {'Circle of Scorn', '厄运流转'}
        damage_potency = 100
        attack_type = physic
        status_to_target = Status.CircleOfScorn

    class ShieldLob(ActionBase):
        """
        对目标发动远距离物理攻击 威力：120 追加效果：提升仇恨

        """
        id = 24
        name = {'Shield Lob', '投盾'}
        damage_potency = 120
        attack_type = physic

    class Cover(ActionBase):
        """
        替目标队员承受来自敌人的攻击 但对部分攻击无效 持续时间：12秒 与目标的距离不能超过10米 效果发动条件：忠义50点

        80, 保护, Cover, 正在保护特定的队员
        1300, 保护, Cover, 正在保护特定的队员，效果中受到的伤害增加
        2412, 保护, Cover, 正在保护特定的对象
        """
        id = 27
        name = {'Cover', '保护'}

    class IronWill(ActionBase):
        """
        极大幅度增加战斗时获得的仇恨量 再次发动时则取消该状态 持续时间：永久

        79, 钢铁信念, Iron Will, 自身仇恨提高
        393, 钢铁信念, Iron Will, 自身仇恨提高
        """
        id = 28
        name = {'Iron Will', '钢铁信念'}

    class SpiritsWithin(ActionBase):
        """
        对目标发动物理攻击 威力：100～370 自身剩余体力越高威力越大(source.job==19?(source.level>=58? 追加效果：恢复自身魔力:):)

        """
        id = 29
        name = {'Spirits Within', '深奥之灵'}
        damage_potency = 250
        attack_type = physic

    class HallowedGround(ActionBase):
        """
        一定时间内，除特定攻击之外其他所有对自身发动的攻击均无效 持续时间：10秒

        82, 神圣领域, Hallowed Ground, 除特定攻击之外其他所有攻击均无效化
        1302, 神圣领域, Hallowed Ground, 除特定攻击之外其他所有攻击均无效化
        """
        id = 30
        name = {'Hallowed Ground', '神圣领域'}
        status_to_target = Status.HallowedGround

    class GoringBlade(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：暴乱剑 连击中威力：390 连击成功：持续伤害 威力：85 持续时间：21秒

        725, 沥血剑, Goring Blade, 体力逐渐减少
        """
        id = 3538
        name = {'Goring Blade', '沥血剑'}

    class RoyalAuthority(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：暴乱剑 连击中威力：550(source.job==19?(source.level>=76? 连击成功：3档忠义之剑 持续时间：15秒:):)

        """
        id = 3539
        name = {'Royal Authority', '王权剑'}

    class DivineVeil(ActionBase):
        """
        自身受到自身及队员的治疗魔法时，为周围15米内的队员张开防护罩 持续时间：30秒 受到治疗效果的同时，该技能效果消失 防护罩效果（受到攻击时）：抵消相当于骑士自身最大体力10%的伤害量 持续时间：30秒

        726, 圣光幕帘, Divine Veil, 受到治疗魔法时为周围队员附加能够抵消一定伤害的防护罩
        727, 圣光幕帘, Divine Veil, 抵消一定伤害
        2168, 圣光幕帘, Divine Veil, 身附能够抵消一定伤害的防护罩，当防护罩因吸收足量伤害而消失时，会为周围队员附加能够抵消一定伤害的防护罩
        2169, 圣光幕帘, Divine Veil, 抵消一定伤害
        """
        id = 3540
        name = {'Divine Veil', '圣光幕帘'}

    class Clemency(ActionBase):
        """
        恢复目标的体力 恢复力：1200 追加效果：对小队队员发动该技能时，自身恢复目标所恢复体力的一半

        """
        id = 3541
        name = {'Clemency', '深仁厚泽'}

    class Sheltron(ActionBase):
        """
        一定时间内，受到攻击必定发动格挡 持续时间：(source.job==19?(source.level>=74?6:4):4)秒 发动条件：忠义50点

        728, 盾阵, Sheltron, 下次受到攻击时必定发动格挡
        1856, 盾阵, Sheltron, 受到攻击时必定发动格挡
        """
        id = 3542
        name = {'Sheltron', '盾阵'}
        status_to_target = Status.Sheltron

    class TotalEclipse(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：120

        """
        id = 7381
        name = {'Total Eclipse', '全蚀斩'}
        damage_potency = 100
        attack_type = physic

    class Intervention(ActionBase):
        """
        指定一名队员，令其受到的伤害减轻10% 持续时间：6秒 追加效果：自身处于铁壁、预警状态时，目标也会获得50%的效果 追加效果发动条件：铁壁或预警状态中 发动条件：忠义50点

        1174, 干预, Intervention, 减轻所受到的伤害
        2020, 干预, Intervention, 减轻所受到的伤害
        """
        id = 7382
        name = {'Intervention', '干预'}

    class Requiescat(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：150～550 自身剩余魔力越高威力越大 追加效果（自身当前魔力在最大魔力的80%以上时）：自身发动攻击魔法的伤害及治疗魔法的治疗量提高50%(source.job==19?(source.level>=78? 同时，咏唱魔法不需要咏唱时间 : ): )持续时间：12秒

        1368, 安魂祈祷, Requiescat, 魔法攻击所造成的伤害及发动治疗魔法的治疗量提高 习得安魂祈祷效果提高后追加效果：咏唱魔法没有任何咏唱时间
        1369, 安魂祈祷, Requiescat, 咏唱魔法时没有任何咏唱时间，并且不会消耗魔力
        """
        id = 7383
        name = {'Requiescat', '安魂祈祷'}

    class HolySpirit(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：350

        """
        id = 7384
        name = {'Holy Spirit', '圣灵'}

    class PassageOfArms(ActionBase):
        """
        向自身后方扇形范围展开减轻伤害的防护区域 效果时间内自身的格挡发动率变为100%，范围内的队员受到的伤害减轻15% 持续时间：18秒 效果时间内发动技能或进行移动、转身都会立即解除武装戍卫 发动之后会停止自动攻击

        1175, 武装戍卫, Passage of Arms, 产生减轻伤害的防护区域
        """
        id = 7385
        name = {'Passage of Arms', '武装戍卫'}

    class Prominence(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：100 连击条件：全蚀斩 连击中威力：220(source.job==19?(source.level>=66? 连击成功：恢复自身魔力:):)

        """
        id = 16457
        name = {'Prominence', '日珥斩'}
        damage_potency = 100
        combo_action = 7381
        combo_damage_potency = 170
        attack_type = physic

    class HolyCircle(ActionBase):
        """
        对自身周围的敌人发动无属性范围魔法攻击 威力：250

        """
        id = 16458
        name = {'Holy Circle', '圣环'}

    class Confiteor(ActionBase):
        """
        对目标及其周围的敌人发动无属性范围魔法攻击 威力：800 发动后会取消安魂祈祷状态 发动条件：安魂祈祷状态中

        2076, 悔罪, Confiteor, 发动攻击所造成的伤害及自身发动的体力恢复效果降低
        """
        id = 16459
        name = {'Confiteor', '悔罪'}

    class Atonement(ActionBase):
        """
        对目标发动物理攻击 威力：550 追加效果：恢复自身魔力 发动条件：忠义之剑

        """
        id = 16460
        name = {'Atonement', '赎罪剑'}

    class Intervene(ActionBase):
        """
        冲向目标并发动物理攻击 威力：200 积蓄次数：2 止步状态下无法发动

        """
        id = 16461
        name = {'Intervene', '调停'}
