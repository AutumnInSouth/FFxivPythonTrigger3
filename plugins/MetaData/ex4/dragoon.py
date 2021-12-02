from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class TrueThrust(ActionBase):
        """
        对目标发动物理攻击 威力：(source.job==22?(source.level>=76?290:210):210)

        """
        id = 75
        name = {"True Thrust", "精准刺"}

    class VorpalThrust(ActionBase):
        """
        对目标发动物理攻击 威力：(source.job==22?(source.level>=76?140:100):100) 连击条件：精准刺 连击中威力：(source.job==22?(source.level>=76?350:310):310)

        """
        id = 78
        name = {"Vorpal Thrust", "贯通刺"}
        combo_action = 75

    class LifeSurge(ActionBase):
        """
        效果时间内，自身发动的1次战技必定打出暴击，并且恢复自身体力 该效果不适用于持续伤害等状态 持续时间：5秒

        116, 龙剑, Life Surge, 下次发动的战技必定打出暴击，并且附带吸收体力的效果
        2175, 龙剑, Life Surge, 下次发动的战技造成的伤害提高
        """
        id = 83
        name = {"Life Surge", "龙剑"}

    class FullThrust(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：贯通刺 连击中威力：530(source.level>=56?(source.job==22? (source.level>=70?(source.job==22?“苍天龙血”或“红莲龙血”状态中连击成功：:“苍天龙血”状态中连击成功：):“苍天龙血”状态中连击成功：)龙牙龙爪效果提高 持续时间：10秒:):)

        """
        id = 84
        name = {"Full Thrust", "直刺"}
        combo_action = 78

    class LanceCharge(ActionBase):
        """
        一定时间内，自身发动攻击造成的伤害提高15% 持续时间：20秒

        1864, 猛枪, Lance Charge, 攻击所造成的伤害提高
        """
        id = 85
        name = {"Lance Charge", "猛枪"}

    class DoomSpike(ActionBase):
        """
        向目标所在方向发出直线范围物理攻击 威力：170

        """
        id = 86
        name = {"Doom Spike", "死天枪"}

    class Disembowel(ActionBase):
        """
        对目标发动物理攻击 威力：(source.job==22?(source.level>=76?150:100):100) 连击条件：精准刺 连击中威力：(source.job==22?(source.level>=76?320:270):270) 连击成功：攻击伤害提高10% 持续时间：30秒

        121, 开膛枪, Disembowel, 突刺耐性降低
        1914, 开膛枪, Disembowel, 攻击所造成的伤害提高
        """
        id = 87
        name = {"Disembowel", "开膛枪"}
        combo_action = 75

    class ChaosThrust(ActionBase):
        """
        对目标发动物理攻击 威力：100 背面攻击威力：140 连击条件：开膛枪 连击中威力：290 连击中背面攻击威力：330 连击成功：持续伤害 威力：50 持续时间：24秒(source.level>=58?(source.job==22? (source.level>=70?(source.job==22?“苍天龙血”或“红莲龙血”状态中连击成功：:“苍天龙血”状态中连击成功：):“苍天龙血”状态中连击成功：)龙尾大回旋效果提高 持续时间：10秒:):)

        118, 樱花怒放, Chaos Thrust, 体力逐渐减少
        1312, 樱花怒放, Chaos Thrust, 受到持续伤害，持续时间中受到为自己附加此状态的玩家的攻击时伤害增加
        """
        id = 88
        name = {"Chaos Thrust", "樱花怒放"}
        combo_action = 87

    class PiercingTalon(ActionBase):
        """
        对目标发动远程物理攻击 威力：150

        """
        id = 90
        name = {"Piercing Talon", "贯穿尖"}

    class Jump(ActionBase):
        """
        跳起接近目标并发动物理攻击 威力：310 攻击之后回到原位 (source.level>=68?(source.job==22?追加效果：幻象冲预备 持续时间：15秒 :):)止步状态下无法发动

        """
        id = 92
        name = {"Jump", "跳跃"}

    class ElusiveJump(ActionBase):
        """
        向身后跳出15米距离 止步状态下无法发动

        """
        id = 94
        name = {"Elusive Jump", "回避跳跃"}

    class SpineshatterDive(ActionBase):
        """
        跳起接近目标并发动物理攻击 威力：240 止步状态下无法发动

        """
        id = 95
        name = {"Spineshatter Dive", "破碎冲"}

    class DragonfireDive(ActionBase):
        """
        跳起接近目标并发动火属性范围攻击 威力：380 止步状态下无法发动

        """
        id = 96
        name = {"Dragonfire Dive", "龙炎冲"}

    class BloodOfTheDragon(ActionBase):
        """
        (source.job==22?(source.level>=74?一定时间内，高跳和破碎冲的威力提高30% 持续时间：(source.job==22?(source.level>=78?30:20):20)秒:一定时间内，跳跃和破碎冲的威力提高30% 持续时间：(source.job==22?(source.level>=78?30:20):20)秒):一定时间内，跳跃和破碎冲的威力提高30% 持续时间：(source.job==22?(source.level>=78?30:20):20)秒)(source.job==22?(source.level>=56?(source.level>=58? 直刺成功时追加效果：龙牙龙爪效果提高 持续时间：10秒 樱花怒放成功时追加效果：龙尾大回旋效果提高 持续时间：10秒 以上两种状态在苍天龙血状态消失或执行了其他战技时自动解除: 直刺成功时追加效果：龙牙龙爪效果提高 持续时间：10秒 龙牙龙爪效果提高状态在苍天龙血状态消失或执行了龙牙龙爪以外的其他战技时自动解除):):)(source.level>=70?(source.job==22? 发动条件：非红莲龙血状态中:):)

        736, 苍天龙血, Blood of the Dragon, 跳跃和破碎冲的威力提高
        """
        id = 3553
        name = {"Blood of the Dragon", "苍天龙血"}

    class FangAndClaw(ActionBase):
        """
        对目标发动物理攻击 威力：340 侧面攻击威力：380 追加效果：苍天龙血的持续时间延长10秒 最多可延长至30秒 发动条件：(source.level>=70?(source.job==22?苍天龙血或红莲龙血:苍天龙血):苍天龙血)及龙牙龙爪效果提高状态中

        """
        id = 3554
        name = {"Fang and Claw", "龙牙龙爪"}

    class Geirskogul(ActionBase):
        """
        向目标所在方向发出直线范围物理攻击 威力：300 发动条件：苍天龙血状态中(source.level>=70?(source.job==22? 追加效果：苍天龙血变为红莲龙血 发动条件：龙眼2档:):)

        """
        id = 3555
        name = {"Geirskogul", "武神枪"}

    class WheelingThrust(ActionBase):
        """
        对目标发动物理攻击 威力：340 背面攻击威力：380 追加效果：苍天龙血的持续时间延长10秒 最多可延长至30秒 发动条件：(source.level>=70?(source.job==22?苍天龙血或红莲龙血:苍天龙血):苍天龙血)及龙尾大回旋效果提高状态中

        """
        id = 3556
        name = {"Wheeling Thrust", "龙尾大回旋"}

    class BattleLitany(ActionBase):
        """
        一定时间内，自身与周围队员的暴击发动率提高10% 持续时间：20秒

        786, 战斗连祷, Battle Litany, 暴击发动率提高
        1414, 战斗连祷, Battle Litany, 造成的伤害提高
        """
        id = 3557
        name = {"Battle Litany", "战斗连祷"}

    class SonicThrust(ActionBase):
        """
        向目标所在方向发出直线范围物理攻击 威力：100 连击条件：死天枪 连击中威力：200 连击成功：苍天龙血的持续时间延长10秒 最多可延长至30秒

        """
        id = 7397
        name = {"Sonic Thrust", "音速刺"}
        combo_action = 86

    class DragonSight(ActionBase):
        """
        为自身附加巨龙右眼状态 当指定一名队员为目标时，为自身附加巨龙右眼状态，为目标附加巨龙左眼状态 巨龙右眼效果：攻击伤害提高10% 巨龙左眼效果：攻击伤害提高5% 持续时间：20秒 与目标的距离超过12米无法发动巨龙左眼的效果

        """
        id = 7398
        name = {"Dragon Sight", "巨龙视线"}

    class MirageDive(ActionBase):
        """
        对目标发动物理攻击 威力：300 (source.level>=70?(source.job==22?“苍天龙血”或“红莲龙血”状态中追加效果：龙眼 :):)发动条件：发动(source.job==22?(source.level>=74?跳跃、高跳:跳跃):跳跃)后对自身附加的幻象冲预备状态中

        """
        id = 7399
        name = {"Mirage Dive", "幻象冲"}

    class Nastrond(ActionBase):
        """
        向目标所在方向发出直线范围物理攻击 威力：400 发动条件：红莲龙血状态中 ※该技能无法设置到热键栏

        """
        id = 7400
        name = {"Nastrond", "死者之岸"}

    class CoerthanTorment(ActionBase):
        """
        向目标所在方向发出直线范围物理攻击 威力：100 连击条件：音速刺 连击中威力：230 连击成功：苍天龙血的持续时间延长10秒 最多可延长至30秒 

        """
        id = 16477
        name = {"Coerthan Torment", "山境酷刑"}
        combo_action = 7397

    class HighJump(ActionBase):
        """
        跳起接近目标并发动物理攻击 威力：400 攻击之后回到原位 追加效果：幻象冲预备 持续时间：15秒 止步状态下无法发动

        """
        id = 16478
        name = {"High Jump", "高跳"}

    class RaidenThrust(ActionBase):
        """
        对目标发动物理攻击 威力：330 发动条件：龙眼雷电预备状态中 ※该技能无法设置到热键栏

        """
        id = 16479
        name = {"Raiden Thrust", "龙眼雷电"}

    class Stardiver(ActionBase):
        """
        跳起接近目标并发动火属性范围物理攻击 威力：600 攻击复数敌人时，对目标之外的敌人威力降低30% 止步状态下无法发动 发动条件：红莲龙血状态中

        """
        id = 16480
        name = {"Stardiver", "坠星冲"}
