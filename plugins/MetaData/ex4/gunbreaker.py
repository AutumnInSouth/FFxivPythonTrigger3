from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class KeenEdge(ActionBase):
        """
        对目标发动物理攻击 威力：200

        """
        id = 16137
        name = {"Keen Edge", "利刃斩"}

    class NoMercy(ActionBase):
        """
        一定时间内，自身发动攻击造成的伤害提高20% 持续时间：20秒

        1831, 无情, No Mercy, 攻击所造成的伤害提高
        """
        id = 16138
        name = {"No Mercy", "无情"}

    class BrutalShell(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：利刃斩 连击中威力：300 连击成功：恢复自身体力 恢复力：200(source.job==37?(source.level>=52? 同时为自身附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于恢复量100%的伤害 持续时间：30秒:):)

        1898, 残暴弹, Brutal Shell, 抵消一定伤害
        1997, 残暴弹, Brutal Shell, 抵消一定伤害
        """
        id = 16139
        name = {"Brutal Shell", "残暴弹"}
        combo_action = 16137

    class Camouflage(ActionBase):
        """
        一定时间内，自身的招架发动率提高50%，所受的伤害减轻10% 持续时间：20秒

        1832, 伪装, Camouflage, 招架发动率提高，减轻所受到的伤害
        """
        id = 16140
        name = {"Camouflage", "伪装"}

    class DemonSlice(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：150

        """
        id = 16141
        name = {"Demon Slice", "恶魔切"}

    class RoyalGuard(ActionBase):
        """
        极大幅度增加战斗时获得的仇恨量 再次发动时则取消该状态 持续时间：永久

        392, 王室亲卫, Royal Guard, 自身仇恨提高
        1833, 王室亲卫, Royal Guard, 自身仇恨提高
        """
        id = 16142
        name = {"Royal Guard", "王室亲卫"}

    class LightningShot(ActionBase):
        """
        对目标发动远距离物理攻击 威力：150 追加效果：提升仇恨

        2392, 闪雷弹, Lightning Shot, 下次发动战技造成的伤害提高
        """
        id = 16143
        name = {"Lightning Shot", "闪雷弹"}

    class DangerZone(ActionBase):
        """
        对目标发动物理攻击 威力：350

        """
        id = 16144
        name = {"Danger Zone", "危险领域"}

    class SolidBarrel(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：残暴弹 连击中威力：400(source.job==37?(source.level>=30? 连击成功：晶壤:):)

        """
        id = 16145
        name = {"Solid Barrel", "迅连斩"}
        combo_action = 16139

    class GnashingFang(ActionBase):
        """
        对目标发动物理攻击 威力：450 (source.job==37?(source.level>=70?追加效果：撕喉预备 持续时间：10秒 :):)发动条件：晶壤 该战技有单独计算的复唱时间

        """
        id = 16146
        name = {"Gnashing Fang", "烈牙"}

    class SavageClaw(ActionBase):
        """
        对目标发动物理攻击 威力：550 连击条件：烈牙 (source.job==37?(source.level>=70?追加效果：裂膛预备 持续时间：10秒 :):)发动条件：满足连击条件

        """
        id = 16147
        name = {"Savage Claw", "猛兽爪"}
        combo_action = 16146

    class Nebula(ActionBase):
        """
        一定时间内，将自身所受的伤害减轻30% 持续时间：15秒

        1834, 星云, Nebula, 减轻所受到的伤害
        """
        id = 16148
        name = {"Nebula", "星云"}

    class DemonSlaughter(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：100 连击条件：恶魔切 连击中威力：250 连击成功：晶壤

        """
        id = 16149
        name = {"Demon Slaughter", "恶魔杀"}
        combo_action = 16141

    class WickedTalon(ActionBase):
        """
        对目标发动物理攻击 威力：650 连击条件：猛兽爪 (source.job==37?(source.level>=70?追加效果：穿目预备 持续时间：10秒 :):)发动条件：满足连击条件

        """
        id = 16150
        name = {"Wicked Talon", "凶禽爪"}
        combo_action = 16147

    class Aurora(ActionBase):
        """
        令目标体力持续恢复 恢复力：200 持续时间：18秒

        1835, 极光, Aurora, 体力会随时间逐渐恢复
        2065, 极光, Aurora, 体力会随时间逐渐恢复
        """
        id = 16151
        name = {"Aurora", "极光"}

    class Superbolide(ActionBase):
        """
        发动该技能后，自身的体力降为1，同时在持续时间内，除一部分特定攻击之外，免除自身受到的任何伤害 持续时间：8秒

        1836, 超火流星, Superbolide, 除特定攻击之外其他所有攻击均无效化
        """
        id = 16152
        name = {"Superbolide", "超火流星"}

    class SonicBreak(ActionBase):
        """
        对目标发动物理攻击 威力：300 追加效果：持续伤害 威力：90 持续时间：30秒 该战技有单独计算的复唱时间

        1837, 音速破, Sonic Break, 体力逐渐减少
        """
        id = 16153
        name = {"Sonic Break", "音速破"}

    class RoughDivide(ActionBase):
        """
        跃向目标并发动物理攻击 威力：200 积蓄次数：2 止步状态下无法发动

        """
        id = 16154
        name = {"Rough Divide", "粗分斩"}

    class Continuation(ActionBase):
        """
        对目标发动追击 使用烈牙后可以发动撕喉，使用猛兽爪后可以发动裂膛，使用凶禽爪后可以发动穿目

        """
        id = 16155
        name = {"Continuation", "续剑"}

    class JugularRip(ActionBase):
        """
        对目标发动物理攻击 威力：260 发动条件：撕喉预备状态中 ※该技能无法设置到热键栏

        """
        id = 16156
        name = {"Jugular Rip", "撕喉"}

    class AbdomenTear(ActionBase):
        """
        对目标发动物理攻击 威力：280 发动条件：裂膛预备状态中 ※该技能无法设置到热键栏

        """
        id = 16157
        name = {"Abdomen Tear", "裂膛"}

    class EyeGouge(ActionBase):
        """
        对目标发动物理攻击 威力：300 发动条件：穿目预备状态中 ※该技能无法设置到热键栏

        """
        id = 16158
        name = {"Eye Gouge", "穿目"}

    class BowShock(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：200 追加效果：持续伤害 威力：90 持续时间：15秒

        1838, 弓形冲波, Bow Shock, 体力逐渐减少
        """
        id = 16159
        name = {"Bow Shock", "弓形冲波"}

    class HeartOfLight(ActionBase):
        """
        一定时间内，令自身和周围队员所受到的魔法伤害减轻10% 持续时间：15秒

        1839, 光之心, Heart of Light, 减轻所受到的魔法伤害
        2000, 光之心, Heart of Light, 受到攻击的伤害减少
        """
        id = 16160
        name = {"Heart of Light", "光之心"}

    class HeartOfStone(ActionBase):
        """
        令自身或一名队员受到的伤害减轻15% 持续时间：7秒 追加效果：对队员使用时，若自身附加了残暴弹状态，则目标队员也会附加该状态 持续时间：30秒

        1840, 石之心, Heart of Stone, 减轻所受到的伤害
        """
        id = 16161
        name = {"Heart of Stone", "石之心"}

    class BurstStrike(ActionBase):
        """
        对目标发动物理攻击 威力：500 发动条件：晶壤

        """
        id = 16162
        name = {"Burst Strike", "爆发击"}

    class FatedCircle(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：320 发动条件：晶壤

        """
        id = 16163
        name = {"Fated Circle", "命运之环"}

    class Bloodfest(ActionBase):
        """
        以一名敌人为目标 对自身附加2档晶壤

        """
        id = 16164
        name = {"Bloodfest", "血壤"}

    class BlastingZone(ActionBase):
        """
        对目标发动物理攻击 威力：800

        """
        id = 16165
        name = {"Blasting Zone", "爆破领域"}
