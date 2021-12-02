from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class HeavyShot(ActionBase):
        """
        对目标发动物理攻击 威力：180(source.level>=2?(source.job==5? 追加效果（发动几率20%）：直线射击预备 持续时间：10秒:(source.job==23? 追加效果（发动几率20%）：直线射击预备 持续时间：10秒:)):)

        """
        id = 97
        name = {'Heavy Shot', '强力射击'}

    class StraightShot(ActionBase):
        """
        对目标发动物理攻击 威力：200 发动条件：直线射击预备状态中

        130, 直线射击, Straight Shot, 暴击发动率提高
        """
        id = 98
        name = {'Straight Shot', '直线射击'}

    class VenomousBite(ActionBase):
        """
        对目标发动物理攻击 威力：100 追加效果：中毒 威力：30 持续时间：30秒

        124, 毒咬箭, Venomous Bite, 身中剧毒，体力会逐渐减少
        """
        id = 100
        name = {'Venomous Bite', '毒咬箭'}

    class RagingStrikes(ActionBase):
        """
        一定时间内，自身发动攻击造成的伤害提高10% 持续时间：20秒

        125, 猛者强击, Raging Strikes, 攻击造成的伤害提高
        """
        id = 101
        name = {'Raging Strikes', '猛者强击'}

    class QuickNock(ActionBase):
        """
        向目标所在方向发出扇形范围物理攻击 威力：150(source.job==23?(source.level>=74? 追加效果（发动几率30%）：重置失血箭及死亡箭雨的复唱时间:):)

        """
        id = 106
        name = {'Quick Nock', '连珠箭'}

    class Barrage(ActionBase):
        """
        效果时间内，自身发动的1次单体攻击战技连续发动3次，但该战技的追加效果只发动1次 持续时间：10秒 对自身附加直线射击预备状态 持续时间：10秒

        128, 纷乱箭, Barrage, 自身发动的下一次战技会变为多次攻击
        1407, 纷乱箭, Barrage, 自身发动的下一次战技会变为多次攻击
        """
        id = 107
        name = {'Barrage', '纷乱箭'}

    class Bloodletter(ActionBase):
        """
        对目标发动物理攻击 威力：150(source.level>=45?(source.job==23? 与死亡箭雨共享复唱时间:):)

        """
        id = 110
        name = {'Bloodletter', '失血箭'}

    class RepellingShot(ActionBase):
        """
        射击目标，同时后跳10米距离 止步状态下无法发动

        2017, 后跃射击, Repelling Shot, 战技造成的伤害提高
        """
        id = 112
        name = {'Repelling Shot', '后跃射击'}

    class Windbite(ActionBase):
        """
        对目标发动风属性物理攻击 威力：60 追加效果：风属性持续伤害 威力：40 持续时间：30秒

        129, 风蚀箭, Windbite, 风属性持续伤害，体力逐渐流失
        """
        id = 113
        name = {'Windbite', '风蚀箭'}

    class MagesBallad(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：100 弹唱贤者的叙事谣，令周围30米内的队员攻击伤害提高1% 持续时间：30秒 追加效果（(source.level>=64?(source.job==23?烈毒咬箭或狂风蚀箭:毒咬箭或风蚀箭):毒咬箭或风蚀箭)的持续伤害命中时，发动几率(source.level>=64?(source.job==23?40%:20%):20%)）：诗心 “诗心”效果：重置失血箭及死亡箭雨的复唱时间 该魔法有单独计算的复唱时间，不受其他战技和魔法复唱时间的影响

        135, 贤者的叙事谣, Mage's Ballad, 对一定范围内的队友附加魔力持续恢复效果，自身攻击所造成的伤害降低，并且会持续消耗魔力
        136, 贤者的叙事谣, Mage's Ballad, 魔力持续恢复
        2217, 贤者的叙事谣, Mage's Ballad, 攻击所造成的伤害提高
        """
        id = 114
        name = {'Mage's Ballad', '贤者的叙事谣'}

    class ArmysPaeon(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：100 弹唱军神的赞美歌，令周围30米内的队员直击发动率提高3% 持续时间：30秒 追加效果（(source.level>=64?(source.job==23?烈毒咬箭或狂风蚀箭:毒咬箭或风蚀箭):毒咬箭或风蚀箭)的持续伤害命中时，发动几率(source.level>=64?(source.job==23?40%:20%):20%)）：诗心 “诗心”效果：每档可令自身的自动攻击间隔、战技与魔法的咏唱及复唱时间缩短4% 最大档数：4档 该魔法有单独计算的复唱时间，不受其他战技和魔法复唱时间的影响

        137, 军神的赞美歌, Army's Paeon, 对一定范围内的队友附加技力持续恢复效果，自身攻击所造成的伤害降低，并且会持续消耗魔力
        138, 军神的赞美歌, Army's Paeon, 技力持续恢复
        2214, 军神的赞美歌, Army's Paeon, 战技与魔法的咏唱及复唱时间缩短
        2218, 军神的赞美歌, Army's Paeon, 直击发动率提高
        """
        id = 116
        name = {'Army's Paeon', '军神的赞美歌'}

    class RainOfDeath(ActionBase):
        """
        对目标及其周围敌人发动范围物理攻击 威力：130 与失血箭共享复唱时间

        247, 死亡箭雨, Rain of Death, 回避率降低
        """
        id = 117
        name = {'Rain of Death', '死亡箭雨'}

    class BattleVoice(ActionBase):
        """
        一定时间内，周围队员的直击发动率提高20% 持续时间：20秒 发动条件：正在使用贤者的叙事谣、军神的赞美歌、放浪神的小步舞曲任意一种

        141, 战斗之声, Battle Voice, 直击发动率提高
        """
        id = 118
        name = {'Battle Voice', '战斗之声'}

    class EmpyrealArrow(ActionBase):
        """
        对目标发动物理攻击 威力：230

        """
        id = 3558
        name = {'Empyreal Arrow', '九天连箭'}

    class TheWanderersMinuet(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：100 弹唱放浪神的小步舞曲，令周围30米内的队员暴击发动率提高2% 持续时间：30秒 追加效果（(source.level>=64?(source.job==23?烈毒咬箭或狂风蚀箭:毒咬箭或风蚀箭):毒咬箭或风蚀箭)的持续伤害命中时，发动几率(source.level>=64?(source.job==23?40%:20%):20%)）：诗心 “诗心”效果：可发动完美音调 最大档数：3档 该魔法有单独计算的复唱时间，不受其他战技和魔法复唱时间的影响

        865, 放浪神的小步舞曲, The Wanderer's Minuet, 攻击造成的伤害提高的同时，对弓箭手和吟游诗人的战技附加额外的咏唱时间
        2215, 放浪神的小步舞曲, The Wanderer's Minuet, 攻击所造成的伤害提高
        2216, 放浪神的小步舞曲, The Wanderer's Minuet, 暴击发动率提高
        """
        id = 3559
        name = {'the Wanderer's Minuet', '放浪神的小步舞曲'}

    class IronJaws(ActionBase):
        """
        对目标发动物理攻击 威力：100 追加效果：重置自身对目标施加的(source.level>=64?(source.job==23?烈毒咬箭和狂风蚀箭:毒咬箭和风蚀箭):毒咬箭和风蚀箭)的持续时间 自身没有对目标施加上述持续伤害状态时无效(source.job==23?(source.level>=76? 追加效果（发动几率35%）：直线射击预备 持续时间：10秒:):)

        """
        id = 3560
        name = {'Iron Jaws', '伶牙俐齿'}

    class TheWardensPaean(ActionBase):
        """
        解除一名队员身上部分弱化效果中的一种 如果未能触发该效果，则为该队员张开防护罩 防护罩可免疫一次目标所受到的部分弱化效果中的一种 持续时间：30秒

        866, 光阴神的礼赞凯歌, The Warden's Paean, 下次异常状态效果无效
        """
        id = 3561
        name = {'the Warden's Paean', '光阴神的礼赞凯歌'}

    class Sidewinder(ActionBase):
        """
        对目标发动物理攻击 威力：100 自身对目标附加了(source.level>=64?(source.job==23?烈毒咬箭、狂风蚀箭:毒咬箭、风蚀箭):毒咬箭、风蚀箭)状态时威力提高 1种持续伤害时威力：200 2种持续伤害时威力：350(source.job==23?(source.level>=72? 与影噬箭共享复唱时间:):)

        """
        id = 3562
        name = {'Sidewinder', '侧风诱导箭'}

    class PitchPerfect(ActionBase):
        """
        对目标发动物理攻击 根据自身附加的诗心档数给与相应伤害 诗心1档时威力：100 诗心2档时威力：250 诗心3档时威力：450 发动条件：放浪神的小步舞曲状态中且诗心1档以上

        """
        id = 7404
        name = {'Pitch Perfect', '完美音调'}

    class Troubadour(ActionBase):
        """
        一定时间内，令自身和周围队员所受到的伤害减轻10% 持续时间：15秒 无法与机工士的策动、舞者的防守之桑巴效果共存

        1934, 行吟, Troubadour, 减轻所受到的伤害
        """
        id = 7405
        name = {'Troubadour', '行吟'}

    class CausticBite(ActionBase):
        """
        对目标发动物理攻击 威力：150 追加效果：中毒 威力：40 持续时间：30秒(source.job==23?(source.level>=76? 追加效果（发动几率35%）：直线射击预备 持续时间：10秒:):)

        1200, 烈毒咬箭, Caustic Bite, 身中剧毒，体力会逐渐减少
        1321, 烈毒咬箭, Caustic Bite, 受到持续伤害
        """
        id = 7406
        name = {'Caustic Bite', '烈毒咬箭'}

    class Stormbite(ActionBase):
        """
        对目标发动风属性物理攻击 威力：100 追加效果：风属性持续伤害 威力：50 持续时间：30秒(source.job==23?(source.level>=76? 追加效果（发动几率35%）：直线射击预备 持续时间：10秒:):)

        1201, 狂风蚀箭, Stormbite, 风属性持续伤害，体力逐渐流失
        1322, 狂风蚀箭, Stormbite, 受到持续伤害
        """
        id = 7407
        name = {'Stormbite', '狂风蚀箭'}

    class NaturesMinne(ActionBase):
        """
        令自身或其他一名队员所受的体力恢复效果提高20% 持续时间：15秒

        1202, 大地神的抒情恋歌, Nature's Minne, 自身所受的治疗效果提高
        2178, 大地神的抒情恋歌, Nature's Minne, 减轻所受到的伤害，自身所受体力恢复效果提高
        """
        id = 7408
        name = {'Nature's Minne', '大地神的抒情恋歌'}

    class RefulgentArrow(ActionBase):
        """
        对目标发动物理攻击 威力：340 发动条件：直线射击预备状态中

        """
        id = 7409
        name = {'Refulgent Arrow', '辉煌箭'}

    class Shadowbite(ActionBase):
        """
        对目标及其周围敌人发动范围物理攻击 威力：100 自身对目标附加了烈毒咬箭、狂风蚀箭状态时威力提高 1种持续伤害时威力：160 2种持续伤害时威力：220 与侧风诱导箭共享复唱时间

        """
        id = 16494
        name = {'Shadowbite', '影噬箭'}

    class BurstShot(ActionBase):
        """
        对目标发动物理攻击 威力：250 追加效果（发动几率35%）：直线射击预备 持续时间：10秒

        """
        id = 16495
        name = {'Burst Shot', '爆发射击'}

    class ApexArrow(ActionBase):
        """
        向目标所在方向发出直线范围物理攻击 威力：120～600 发动时会消耗全部的灵魂之声 灵魂之声消耗量越高威力越大 发动条件：灵魂之声20点以上

        """
        id = 16496
        name = {'Apex Arrow', '绝峰箭'}
