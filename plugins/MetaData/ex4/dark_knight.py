from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class HardSlash(ActionBase):
        """
        对目标发动物理攻击 威力：200

        """
        id = 3617
        name = {'Hard Slash', '重斩'}

    class Unleash(ActionBase):
        """
        对自身周围的敌人发动无属性范围魔法攻击 威力：150

        """
        id = 3621
        name = {'Unleash', '释放'}

    class SyphonStrike(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：重斩 连击中威力：300 连击成功：恢复自身魔力

        """
        id = 3623
        name = {'Syphon Strike', '吸收斩'}
        combo_action = 3617

    class Unmend(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：150 追加效果：提升仇恨

        """
        id = 3624
        name = {'Unmend', '伤残'}

    class BloodWeapon(ActionBase):
        """
        一定时间内，自身的战技及魔法命中时可以恢复魔力 (source.level>=66?(source.job==32?同时获得10点暗血 :):)当范围攻击命中复数敌人时，效果只发动1次 持续时间：10秒

        742, 嗜血, Blood Weapon, 自身的战技及魔法命中时可以恢复魔力 习得暗血II后追加效果：自身的战技及魔法命中时可以获得暗血
        """
        id = 3625
        name = {'Blood Weapon', '嗜血'}

    class Grit(ActionBase):
        """
        极大幅度增加战斗时获得的仇恨量 再次发动时则取消该状态 持续时间：永久

        743, 深恶痛绝, Grit, 自身仇恨提高
        1397, 深恶痛绝, Grit, 以攻击力降低为代价减少自身所受到的伤害
        """
        id = 3629
        name = {'Grit', '深恶痛绝'}

    class Souleater(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：吸收斩 连击中威力：400 连击成功：恢复自身体力 恢复力：300 (source.level>=62?(source.job==32?连击成功：获得20点暗血:):)

        """
        id = 3632
        name = {'Souleater', '噬魂斩'}
        combo_action = 3623

    class DarkMind(ActionBase):
        """
        一定时间内，令自身所受到的魔法伤害减轻20% 持续时间：10秒

        746, 弃明投暗, Dark Mind, 减轻所受到的魔法伤害
        """
        id = 3634
        name = {'Dark Mind', '弃明投暗'}

    class ShadowWall(ActionBase):
        """
        一定时间内，自身受到的伤害减轻30% 持续时间：15秒

        747, 暗影墙, Shadow Wall, 减轻所受到的伤害
        """
        id = 3636
        name = {'Shadow Wall', '暗影墙'}

    class LivingDead(ActionBase):
        """
        对自身附加行尸走肉状态 效果中受到致命伤也不会陷入无法战斗状态，代价是自身体力降为1且该状态变为死而不僵状态 持续时间：10秒 死而不僵效果：所有对自身发动的攻击均无法令体力减少到1以下 效果中得到相当于自身最大体力100%的恢复量即可解除该状态 如恢复量不足以解除状态直到持续时间结束，自身将陷入无法战斗状态 持续时间：10秒 以上两种状态均对部分攻击无效

        810, 行尸走肉, Living Dead, 受到致命伤害时体力减为1，并附加死而不僵状态 但是对部分攻击无效
        """
        id = 3638
        name = {'Living Dead', '行尸走肉'}

    class SaltedEarth(ActionBase):
        """
        以指定地点为中心产生腐秽区域 所有进入该区域的目标都会受到无属性伤害 威力：60 持续时间：15秒

        749, 腐秽大地, Salted Earth, 在地上产生造成无属性伤害的危险区
        """
        id = 3639
        name = {'Salted Earth', '腐秽大地'}

    class Plunge(ActionBase):
        """
        跃向目标并发动物理攻击 威力：200 (source.job==32?(source.level>=78?积蓄次数：2 :):)止步状态下无法发动

        """
        id = 3640
        name = {'Plunge', '跳斩'}

    class AbyssalDrain(ActionBase):
        """
        以目标为中心发动无属性范围魔法攻击 威力：200 追加效果：恢复自身体力 恢复力：200

        """
        id = 3641
        name = {'Abyssal Drain', '吸血深渊'}

    class CarveAndSpit(ActionBase):
        """
        对目标发动物理攻击 威力：450 追加效果：恢复自身魔力

        """
        id = 3643
        name = {'Carve and Spit', '精雕怒斩'}

    class Delirium(ActionBase):
        """
        一定时间内，不需要消耗暗血就可以发动寂灭和血溅 寂灭和血溅命中时恢复自身魔力 持续时间：10秒

        1972, 血乱, Delirium, 不需要消耗暗血就可以发动血溅和寂灭
        1996, 血乱, Delirium, 不消耗暗血
        """
        id = 7390
        name = {'Delirium', '血乱'}

    class Quietus(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：210 发动条件：暗血50点

        """
        id = 7391
        name = {'Quietus', '寂灭'}

    class Bloodspiller(ActionBase):
        """
        对目标发动物理攻击 威力：600 发动条件：暗血50点

        """
        id = 7392
        name = {'Bloodspiller', '血溅'}

    class TheBlackestNight(ActionBase):
        """
        为自身或一名队员附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于目标最大体力25%的伤害量 持续时间：7秒 防护罩因吸收到足够的伤害而消失时，暗黑骑士自身附加暗技状态 暗技效果：用暗技代替魔力发动(source.job==32?(source.level>=74?暗影波动及暗影锋:暗黑波动及暗黑锋):暗黑波动及暗黑锋)

        1178, 至黑之夜, Blackest Night, 抵消一定伤害
        1308, 至黑之夜, Blackest Night, 抵消一定伤害
        """
        id = 7393
        name = {'The Blackest Night', '至黑之夜'}

    class FloodOfDarkness(ActionBase):
        """
        向目标所在方向发出无属性直线范围魔法攻击 威力：250 追加效果：暗黑 持续时间：30秒 暗黑效果：攻击伤害提高10% 若自身已经附加暗黑状态，则持续时间延长30秒 最多可延长至60秒 与暗黑锋共享复唱时间

        """
        id = 16466
        name = {'Flood of Darkness', '暗黑波动'}

    class EdgeOfDarkness(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：350 追加效果：暗黑 持续时间：30秒 暗黑效果：攻击伤害提高10% 若自身已经附加暗黑状态，则持续时间延长30秒 最多可延长至60秒 与暗黑波动共享复唱时间

        """
        id = 16467
        name = {'Edge of Darkness', '暗黑锋'}

    class StalwartSoul(ActionBase):
        """
        对自身周围的敌人发动无属性范围魔法攻击 威力：100 连击条件：释放 连击中威力：160 连击成功：恢复自身魔力 连击成功：获得20点暗血

        """
        id = 16468
        name = {'Stalwart Soul', '刚魂'}
        combo_action = 3621

    class FloodOfShadow(ActionBase):
        """
        向目标所在方向发出无属性直线范围魔法攻击 威力：300 追加效果：暗黑 持续时间：30秒 暗黑效果：攻击伤害提高10% 若自身已经附加暗黑状态，则持续时间延长30秒 最多可延长至60秒 与暗影锋共享复唱时间

        2170, 暗影波动, Flood of Shadow, 自身所受的体力恢复效果降低
        """
        id = 16469
        name = {'Flood of Shadow', '暗影波动'}

    class EdgeOfShadow(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：500 追加效果：暗黑 持续时间：30秒 暗黑效果：攻击伤害提高10% 若自身已经附加暗黑状态，则持续时间延长30秒 最多可延长至60秒 与暗影波动共享复唱时间

        2102, 暗影锋, Edge of Shadow, 自身所受的体力恢复效果降低
        """
        id = 16470
        name = {'Edge of Shadow', '暗影锋'}

    class DarkMissionary(ActionBase):
        """
        一定时间内，令自身和周围队员所受到的魔法伤害减轻10% 持续时间：15秒

        1894, 暗黑布道, Dark Missionary, 减轻所受到的魔法伤害
        2171, 暗黑布道, Dark Missionary, 减轻所受到的伤害，自身所受体力恢复效果提高
        """
        id = 16471
        name = {'Dark Missionary', '暗黑布道'}

    class LivingShadow(ActionBase):
        """
        令“英雄的掠影”变为实体与自身并肩作战 持续时间：24秒 英雄的掠影的攻击威力：300 发动条件：暗血50点

        """
        id = 16472
        name = {'Living Shadow', '掠影示现'}
