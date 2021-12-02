from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class RookAutoturret(ActionBase):
        """
        设置车式浮空炮塔进行支援射击 车式浮空炮塔的运转时间随发动该技能时消耗的电能而变动 最长运转时间：15秒 车式浮空炮塔可以通过齐射进行自动攻击 对目标发动物理攻击 威力：80 运转时间结束后，或发动超档车式炮塔后，车式浮空炮塔会被回收 发动条件：电能50点以上 与超档车式炮塔共享复唱时间

        """
        id = 2864
        name = {"Rook Autoturret", "车式浮空炮塔"}

    class SplitShot(ActionBase):
        """
        对目标发动物理攻击 威力：180(source.job==31?(source.level>=30? 追加效果：获得5点枪管热度:):)

        """
        id = 2866
        name = {"Split Shot", "分裂弹"}

    class SlugShot(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：分裂弹或热分裂弹 连击中威力：260(source.job==31?(source.level>=30? 连击成功：获得5点枪管热度:):)

        """
        id = 2868
        name = {"Slug Shot", "独头弹"}
        combo_action = 2866

    class SpreadShot(ActionBase):
        """
        向目标所在方向发出扇形范围物理攻击 威力：180(source.job==31?(source.level>=30? 追加效果：获得5点枪管热度:):)

        """
        id = 2870
        name = {"Spread Shot", "散射"}

    class HotShot(ActionBase):
        """
        对目标发动物理攻击 威力：300 (source.job==31?(source.level>=40?追加效果：获得20点电能 :):)该战技有单独计算的复唱时间

        855, 热弹, Hot Shot, 物理攻击所造成的伤害提高
        """
        id = 2872
        name = {"Hot Shot", "热弹"}

    class CleanShot(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：独头弹或热独头弹 连击中威力：340(source.job==31?(source.level>=30? 连击成功：获得5点枪管热度:):)(source.job==31?(source.level>=40? 连击成功：获得10点电能:):)

        """
        id = 2873
        name = {"Clean Shot", "狙击弹"}
        combo_action = 2868

    class GaussRound(ActionBase):
        """
        对目标发动物理攻击 威力：150 积蓄次数：(source.job==31?(source.level>=74?3:2):2)

        """
        id = 2874
        name = {"Gauss Round", "虹吸弹"}

    class Reassemble(ActionBase):
        """
        效果时间内，自身发动的1次战技必定打出暴击并且直击 该效果不适用于持续伤害等状态 持续时间：5秒

        851, 整备, Reassembled, 下次发动的战技必定打出暴击和直击
        """
        id = 2876
        name = {"Reassemble", "整备"}

    class Wildfire(ActionBase):
        """
        对目标附加野火状态，同时该技能变为起爆 持续时间结束或发动起爆，可以对目标造成伤害 该技能的威力随自身在持续时间内对目标命中的战技次数而变化 每命中1次战技的威力：(source.job==31?(source.level>=78?200:150):150) 持续时间：10秒

        861, 野火, Wildfire, 若受到了来自附加这一状态的机工士发动的战技攻击的话，效果时间结束时会受到伤害
        1323, 野火, Wildfire, 效果时间中积攒自身所造成的部分伤害
        1946, 野火, Wildfire, 对敌人附加了“野火”
        """
        id = 2878
        name = {"Wildfire", "野火"}

    class Ricochet(ActionBase):
        """
        对目标及其周围的敌人发动范围物理攻击 威力：150 攻击复数敌人时，对目标之外的敌人威力降低50% 积蓄次数：(source.job==31?(source.level>=74?3:2):2)

        """
        id = 2890
        name = {"Ricochet", "弹射"}

    class HeatBlast(ActionBase):
        """
        对目标发动物理攻击 威力：220 追加效果：虹吸弹和弹射的复唱时间缩短15秒 发动条件：过热状态 该战技有单独计算的复唱时间，不受装备和状态的影响

        """
        id = 7410
        name = {"Heat Blast", "热冲击"}

    class HeatedSplitShot(ActionBase):
        """
        对目标发动物理攻击 威力：220(source.job==31?(source.level>=30? 追加效果：获得5点枪管热度:):)

        """
        id = 7411
        name = {"Heated Split Shot", "热分裂弹"}

    class HeatedSlugShot(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：热分裂弹 连击中威力：330(source.job==31?(source.level>=30? 连击成功：获得5点枪管热度:):)

        """
        id = 7412
        name = {"Heated Slug Shot", "热独头弹"}
        combo_action = 2866

    class HeatedCleanShot(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：热独头弹 连击中威力：440(source.job==31?(source.level>=30? 连击成功：获得5点枪管热度:):)(source.job==31?(source.level>=40? 连击成功：获得10点电能:):)

        """
        id = 7413
        name = {"Heated Clean Shot", "热狙击弹"}
        combo_action = 2868

    class BarrelStabilizer(ActionBase):
        """
        获得50点枪管热度 发动条件：自身处于战斗状态

        """
        id = 7414
        name = {"Barrel Stabilizer", "枪管加热"}

    class RookOverdrive(ActionBase):
        """
        命令设置的车式浮空炮塔发动超负荷车式炮塔 对目标发动物理攻击 威力：400 该技能的威力受设置车式浮空炮塔时消耗的电能影响 发动后车式浮空炮塔消失 所有者使用超档车式炮塔或车式浮空炮塔的运转时间结束时，车式浮空炮塔会自动执行该技能 发动条件：车式浮空炮塔处于设置状态 与车式浮空炮塔共享复唱时间

        """
        id = 7415
        name = {"Rook Overdrive", "超档车式炮塔"}

    class RookOverload(ActionBase):
        """
        对目标发动物理攻击 威力：400 该技能的威力受设置车式浮空炮塔时消耗的电能影响 发动后车式浮空炮塔消失 所有者使用超档车式炮塔或车式浮空炮塔的运转时间结束时，车式浮空炮塔会自动执行该技能 ※该技能无法设置到热键栏

        """
        id = 7416
        name = {"Rook Overload", "超负荷车式炮塔"}

    class Flamethrower(ActionBase):
        """
        持续向自身前方发出扇形范围攻击 每秒对范围内的敌人造成伤害 威力：100 持续时间：10秒 效果时间内发动技能或进行移动、转身都会立即解除火焰喷射器 发动之后会停止自动攻击 该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间

        1205, 火焰喷射器, Flamethrower, 对前方扇形范围内的敌人持续造成伤害
        1455, 火焰喷射器, Flamethrower, 对前方扇形范围内的敌人持续造成伤害
        1458, 火焰喷射器, Flamethrower Flames, 受到持续伤害
        """
        id = 7418
        name = {"Flamethrower", "火焰喷射器"}

    class AutoCrossbow(ActionBase):
        """
        向目标所在方向发出扇形范围物理攻击 威力：180 发动条件：过热状态 该战技有单独计算的复唱时间，不受装备和状态的影响

        """
        id = 16497
        name = {"Auto Crossbow", "自动弩"}

    class Drill(ActionBase):
        """
        对目标发动物理攻击 威力：700 (source.job==31?(source.level>=72?该战技不仅有单独计算的复唱时间，还会与毒菌冲击共享复唱时间:该战技有单独计算的复唱时间):该战技有单独计算的复唱时间)

        """
        id = 16498
        name = {"Drill", "钻头"}

    class Bioblaster(ActionBase):
        """
        向目标所在方向发出扇形范围物理攻击 威力：60 追加效果：持续伤害 威力：60 持续时间：15秒 该战技不仅有单独计算的复唱时间，还会与钻头共享复唱时间

        1866, 毒菌冲击, Bioblaster, 体力逐渐减少
        2019, 毒菌冲击, Bioblaster, 受到攻击的伤害增加
        """
        id = 16499
        name = {"Bioblaster", "毒菌冲击"}

    class AirAnchor(ActionBase):
        """
        对目标发动物理攻击 威力：700 追加效果：获得20点电能 该战技有单独计算的复唱时间

        """
        id = 16500
        name = {"Air Anchor", "空气锚"}

    class AutomatonQueen(ActionBase):
        """
        启动后式自走人偶 后式自走人偶的运转时间随发动该技能时消耗的电能而变动 最长运转时间：20秒 运转时间结束后，或发动超档后式人偶后，后式自走人偶会被回收 发动条件：电能50点以上 与超档后式人偶共享复唱时间

        """
        id = 16501
        name = {"Automaton Queen", "后式自走人偶"}

    class QueenOverdrive(ActionBase):
        """
        命令设置的后式自走人偶发动打桩枪 对目标发动物理攻击 威力：800 该技能的威力受设置后式自走人偶时消耗的电能影响 发动后后式自走人偶消失 所有者使用超档后式人偶或后式自走人偶的运转时间结束时，后式自走人偶会自动执行该技能 发动条件：后式自走人偶处于设置状态 与后式自走人偶共享复唱时间

        """
        id = 16502
        name = {"Queen Overdrive", "超档后式人偶"}

    class PileBunker(ActionBase):
        """
        对目标发动物理攻击 威力：800 该技能的威力受设置后式自走人偶时消耗的电能影响 发动后后式自走人偶消失 所有者使用超档后式人偶或后式自走人偶的运转时间结束时，后式自走人偶会自动执行该技能 ※该技能无法设置到热键栏

        """
        id = 16503
        name = {"Pile Bunker", "打桩枪"}

    class ArmPunch(ActionBase):
        """
        对目标发动物理攻击 威力：150 ※该技能无法设置到热键栏

        """
        id = 16504
        name = {"Arm Punch", "铁臂拳"}

    class Detonator(ActionBase):
        """
        令敌人附加的野火状态结束，对敌人造成伤害 ※该技能无法设置到热键栏

        """
        id = 16766
        name = {"Detonator", "起爆"}

    class Tactician(ActionBase):
        """
        一定时间内，令自身和周围队员所受到的伤害减轻10% 持续时间：15秒 无法与吟游诗人的行吟、舞者的防守之桑巴效果共存

        1197, 策动, Tactician, 技力持续恢复
        1951, 策动, Tactician, 减轻所受到的伤害
        2177, 策动, Tactician, 减轻所受到的伤害
        """
        id = 16889
        name = {"Tactician", "策动"}

    class RollerDash(ActionBase):
        """
        冲向目标并发动物理攻击 威力：300 ※该技能无法设置到热键栏

        """
        id = 17206
        name = {"Roller Dash", "滚轮冲"}

    class Hypercharge(ActionBase):
        """
        进入过热状态 效果时间内，自身发动的单体战技威力提高20 持续时间：8秒 仅对机工士特职技能有效 发动条件：枪管热度50点

        688, 超荷, Hypercharge, 浮空炮塔系技能有所强化
        """
        id = 17209
        name = {"Hypercharge", "超荷"}
