# 基类 可不输出
class Action:
    action_id = 0
    cure_potency: int = 0  # 治疗威力
    damage_potency: int = 0  # 伤害威力
    aoe_scale: float = 1.  # 复数目标时副目标的伤害比利
    combo_action: int = 0  # 连击技能 0为无
    direction_require: int = 0  # 身位需求 1为前 2为后 3为侧
    combo_damage_potency: int = 0  # 连击正确伤害威力
    direction_damage_potency: int = 0  # 身位正确伤害威力
    combo_direction_damage_potency: int = 0  # 连击身位正确伤害威力

    status_damage_potency: int = 0  # dot 威力
    status_cure_potency: int = 0  # hot 威力

    def __init__(self, source, target):
        self.source = source
        self.target = target


# 输出例子
class Assize(Action):
    """
    3571 法令 0
    对周围的敌人发动无属性范围魔法攻击 威力：400 追加效果：恢复自身及周围队员的体力 恢复力：400 追加效果：恢复自身最大魔力的5%
    """
    action_id = 0
    damage_potency = 400
    cure_potency = 400


class AeolianEdge(Action):
    """
    2255 旋风刃 2242
    对目标发动物理攻击 威力：100 背面攻击威力：160 连击条件：绝风 连击中威力：420 连击中背面攻击威力：480(source.job==30?(source.level>=62? 连击成功：获得(source.job==30?(source.level>=78?10:5):5)点忍气:):)
    """
    action_id = 2255
    damage_potency = 100
    combo_action = 2242
    direction_require = 2
    combo_damage_potency = 420
    direction_damage_potency = 160
    combo_direction_damage_potency = 480


class ChaosThrust(Action):
    """
    88 樱花怒放 87
    对目标发动物理攻击 威力：100 背面攻击威力：140 连击条件：开膛枪 连击中威力：290 连击中背面攻击威力：330 连击成功：持续伤害 威力：50 持续时间：24秒
    (source.level>=58?(source.job==22? (source.level>=70?(source.job==22?“苍天龙血”或“红莲龙血”状态中连击成功：:“苍天龙血”状态中连击成功：):“苍天龙血”状态中连击成功：)龙尾大回旋效果提高 持续时间：10秒:):)
    """
    action_id = 88
    damage_potency = 100
    combo_action = 87
    direction_require = 2
    combo_damage_potency = 290
    direction_damage_potency = 140
    combo_direction_damage_potency = 330
    status_damage_potency = 50


class Disembowel(Action):
    """
    87 开膛枪 75
    对目标发动物理攻击 威力：(source.job==22?(source.level>=76?150:100):100) 连击条件：精准刺 连击中威力：(source.job==22?(source.level>=76?320:270):270) 连击成功：攻击伤害提高10% 持续时间：30秒
    """
    action_id = 87
    combo_action = 75

    def __init__(self, source, target):
        super().__init__(source, target)
        self.damage_potency = 150 if source.job == 22 and source.level >= 76 else 100
        self.combo_damage_potency = 320 if source.job == 22 and source.level >= 76 else 270


class Bootshine(Action):
    """
    53 连击 0
    对目标发动物理攻击 威力：200 (source.job==20?(source.level>=50?连击效果提高时威力：370 :):)“魔猿身形”中追加效果：背面攻击必定暴击 追加效果：盗龙身形 持续时间：15秒
    """
    action_id = 53

    def __init__(self, source, target):
        super().__init__(source, target)
        self.damage_potency = 370 if source.effects.has(1861) else 200


class MedicaII(Action):
    """
    21888 医济 0
    恢复自身及周围队员的体力 恢复力：200 追加效果：目标体力持续恢复 恢复力：100 持续时间：15秒
    """
    action_id = 21888
    cure_potency = 200
    status_cure_potency = 100


# 无伤害、治疗、dot、hot效果的技能仅输出描述
"""
30 神圣领域 0
一定时间内，除特定攻击之外其他所有对自身发动的攻击均无效 持续时间：10秒
"""
