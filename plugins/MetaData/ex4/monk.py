from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Bootshine(ActionBase):
        """
        对目标发动物理攻击 威力：200 (source.job==20?(source.level>=50?连击效果提高时威力：370 :):)“魔猿身形”中追加效果：背面攻击必定暴击 追加效果：盗龙身形 持续时间：15秒

        """
        id = 53
        name = {'Bootshine', '连击'}

    class TrueStrike(ActionBase):
        """
        对目标发动物理攻击 威力：270 背面攻击威力：300 追加效果：猛豹身形 持续时间：15秒 发动条件：盗龙身形状态中

        """
        id = 54
        name = {'True Strike', '正拳'}

    class SnapPunch(ActionBase):
        """
        对目标发动物理攻击 威力：270 侧面攻击威力：300 追加效果：魔猿身形 持续时间：15秒 发动条件：猛豹身形状态中

        """
        id = 56
        name = {'Snap Punch', '崩拳'}

    class FistsOfEarth(ActionBase):
        """
        令自身受到的伤害减轻10% 再次发动时则取消该状态 持续时间：永久 无法与红莲体势、疾风体势同时使用 与红莲体势、疾风体势共享复唱时间

        104, 金刚体势, Fists of Earth, 减轻所受到的伤害
        2006, 金刚体势, Fists of Earth, 减轻所受到的伤害
        """
        id = 60
        name = {'Fists of Earth', '金刚体势'}

    class TwinSnakes(ActionBase):
        """
        对目标发动物理攻击 威力：230 侧面攻击威力：260 追加效果：攻击伤害提高10% 持续时间：15秒 追加效果：猛豹身形 持续时间：15秒 发动条件：盗龙身形状态中

        101, 双掌打, Twin Snakes, 攻击所造成的伤害提高
        """
        id = 61
        name = {'Twin Snakes', '双掌打'}

    class ArmOfTheDestroyer(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：110 “魔猿身形”中威力：140 追加效果：盗龙身形 持续时间：15秒

        """
        id = 62
        name = {'Arm of the Destroyer', '破坏神冲'}

    class FistsOfFire(ActionBase):
        """
        令自身攻击造成的伤害提高(source.job==20?(source.level>=72?10:5):5)% 再次发动时则取消该状态 持续时间：永久 无法与金刚体势、疾风体势同时使用 与金刚体势、疾风体势共享复唱时间

        103, 红莲体势, Fists of Fire, 攻击所造成的伤害提高
        2005, 红莲体势, Fists of Fire, 攻击所造成的伤害提高
        """
        id = 63
        name = {'Fists of Fire', '红莲体势'}

    class Mantra(ActionBase):
        """
        一定时间内，自身与周围队员所受的体力恢复效果提高10% 持续时间：15秒

        102, 真言, Mantra, 自身所受的治疗效果提高
        """
        id = 65
        name = {'Mantra', '真言'}

    class Demolish(ActionBase):
        """
        对目标发动物理攻击 威力：80 背面攻击威力：110 追加效果：持续伤害 威力：80 持续时间：18秒 追加效果：魔猿身形 持续时间：15秒 发动条件：猛豹身形状态中

        246, 破碎拳, Demolish, 体力逐渐减少
        1309, 破碎拳, Demolish, 受到持续伤害，持续时间中受到为自己附加此状态的玩家的攻击时伤害增加
        """
        id = 66
        name = {'Demolish', '破碎拳'}

    class PerfectBalance(ActionBase):
        """
        对自身附加6档的震脚状态 持续时间：15秒 震脚效果：可以无视身形要求发动战技

        110, 震脚, Perfect Balance, 能够打出三种身形的所有招式
        """
        id = 69
        name = {'Perfect Balance', '震脚'}

    class Rockbreaker(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：150 追加效果：魔猿身形 持续时间：15秒 发动条件：猛豹身形状态中

        """
        id = 70
        name = {'Rockbreaker', '地烈劲'}

    class ShoulderTackle(ActionBase):
        """
        冲向目标并发动物理攻击 威力：100 (source.job==20?(source.level>=66?积蓄次数：2 :):)止步状态下无法发动

        """
        id = 71
        name = {'Shoulder Tackle', '罗刹冲'}

    class FistsOfWind(ActionBase):
        """
        令自身移动速度提高 再次发动时则取消该状态 持续时间：永久 无法与金刚体势、红莲体势同时使用 与金刚体势、红莲体势共享复唱时间

        105, 疾风体势, Fists of Wind, 移动速度提高
        2007, 疾风体势, Fists of Wind, 战技的复唱时间缩短
        """
        id = 73
        name = {'Fists of Wind', '疾风体势'}

    class DragonKick(ActionBase):
        """
        对目标发动物理攻击 威力：230 侧面攻击威力：260 “魔猿身形”中追加效果：连击效果提高 持续时间：30秒 追加效果：盗龙身形 持续时间：15秒

        98, 双龙脚, Dragon Kick, 打击耐性降低
        """
        id = 74
        name = {'Dragon Kick', '双龙脚'}

    class TornadoKick(ActionBase):
        """
        对目标发动物理攻击 威力：400

        """
        id = 3543
        name = {'Tornado Kick', '斗魂旋风脚'}

    class ElixirField(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：250

        """
        id = 3545
        name = {'Elixir Field', '苍气炮'}

    class Meditation(ActionBase):
        """
        对自身附加斗气状态，最多可以积累5档 持续时间：永久 自身处于非战斗状态时直接获得5档斗气 与战技共享复唱时间

        793, 斗气, First Chakra, 体内积蓄着斗气
        """
        id = 3546
        name = {'Meditation', '斗气'}

    class TheForbiddenChakra(ActionBase):
        """
        对目标发动物理攻击 威力：340 发动后会取消斗气状态 发动条件：自身处于战斗状态且斗气5档 与万象斗气圈共享复唱时间 ※该技能无法设置到热键栏

        """
        id = 3547
        name = {'the Forbidden Chakra', '阴阳斗气斩'}

    class FormShift(ActionBase):
        """
        对自身附加无相身形状态 持续时间：15秒 无相身形效果：可以无视身形要求发动战技，同时触发追加效果

        """
        id = 4262
        name = {'Form Shift', '演武'}

    class RiddleOfEarth(ActionBase):
        """
        对自身附加3档的金刚极意状态 持续时间结束或发动3次战技后取消该状态 持续时间：10秒 金刚极意效果：自身所受的伤害减轻10%，同时无视技能的方向要求 积蓄次数：3

        1179, 金刚极意, Riddle of Earth, 减轻所受到的一部分伤害，且无视自身技能的方向要求
        1310, 金刚极意, Riddle of Earth, 受到一定量的伤害时会发动金刚极意
        2008, 金刚极意, Riddle of Earth, 抵消一定伤害
        """
        id = 7394
        name = {'Riddle of Earth', '金刚极意'}

    class RiddleOfFire(ActionBase):
        """
        一定时间内，自身发动攻击造成的伤害提高25% 持续时间：20秒

        1181, 红莲极意, Riddle of Fire, 攻击所造成的伤害提高
        1413, 红莲极意, Riddle of Fire, 自身发动的下一次战技所造成的伤害提高
        """
        id = 7395
        name = {'Riddle of Fire', '红莲极意'}

    class Brotherhood(ActionBase):
        """
        为自身与周围队员附加义结金兰：斗气状态 自身与周围队员发动战技与魔法时有20%几率为自身附加1档斗气 为自身与周围队员附加义结金兰：攻击状态 发动攻击造成的伤害提高5% 持续时间：15秒

        """
        id = 7396
        name = {'Brotherhood', '义结金兰'}

    class Four-pointFury(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：140 追加效果：双掌打的持续时间延长10秒 最多可延长至15秒 追加效果：猛豹身形 持续时间：15秒 发动条件：盗龙身形状态中

        """
        id = 16473
        name = {'Four-point Fury', '四面脚'}

    class Enlightenment(ActionBase):
        """
        向目标所在方向发出直线范围物理攻击 威力：220 发动后会取消斗气状态 发动条件：自身处于战斗状态且斗气5档 与阴阳斗气斩共享复唱时间

        """
        id = 16474
        name = {'Enlightenment', '万象斗气圈'}

    class Anatman(ActionBase):
        """
        令自身附加的身形与双掌打的持续时间恢复到最大值，同时暂停持续时间的流逝 效果时间内发动技能或进行移动、转身都会立即解除无我 发动之后会停止自动攻击 持续时间：30秒 该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间

        1862, 无我, Anatman, 身形和双掌打的效果时间停止流逝
        """
        id = 16475
        name = {'Anatman', '无我'}

    class Six-sidedStar(ActionBase):
        """
        对目标发动物理攻击 威力：540 追加效果：提高自身的移动速度 持续时间：5秒 该战技有单独计算的复唱时间，发动后其他战技与魔法会产生与该战技相同的复唱时间

        2514, 六合星导脚, Six-sided Star, 移动速度提高
        """
        id = 16476
        name = {'Six-sided Star', '六合星导脚'}
