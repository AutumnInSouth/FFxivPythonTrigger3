from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Hakaze(ActionBase):
        """
        对目标发动物理攻击 威力：200(source.level>=62?(source.job==34? 追加效果：获得5点剑气:):)

        """
        id = 7477
        name = {'Hakaze', '刃风'}

    class Jinpu(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：刃风 连击中威力：320 连击成功：攻击伤害提高(source.job==34?(source.level>=78?13:10):10)% 持续时间：40秒(source.level>=62?(source.job==34? 连击成功：获得5点剑气:):)

        1298, 阵风, Jinpu, 攻击所造成的伤害提高
        """
        id = 7478
        name = {'Jinpu', '阵风'}
        combo_action = 7477

    class Shifu(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：刃风 连击中威力：320 连击成功：自身的自动攻击间隔、战技与魔法的咏唱及复唱时间缩短(source.job==34?(source.level>=78?13:10):10)% 持续时间：40秒(source.level>=62?(source.job==34? 连击成功：获得5点剑气:):)

        1299, 士风, Shifu, 自动攻击间隔、战技与魔法的咏唱及复唱时间缩短
        """
        id = 7479
        name = {'Shifu', '士风'}
        combo_action = 7477

    class Yukikaze(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：刃风 连击中威力：360 (source.level>=52?(source.job==34?连击成功：获得雪之闪与(source.level>=62?(source.job==34?15:10):10)点剑气:连击成功：雪之闪):连击成功：雪之闪)

        1227, 雪风, Yukikaze, 斩击耐性降低
        1318, 雪风, Yukikaze, 受到附加此效果的玩家攻击的伤害增加
        """
        id = 7480
        name = {'Yukikaze', '雪风'}
        combo_action = 7477

    class Gekko(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：阵风 连击中威力：480 (source.level>=52?(source.job==34?连击中背面攻击追加效果：获得5点剑气 :):)(source.level>=62?(source.job==34?连击成功：获得月之闪与5点剑气:连击成功：月之闪):连击成功：月之闪)

        """
        id = 7481
        name = {'Gekko', '月光'}
        combo_action = 7478

    class Kasha(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：士风 连击中威力：480 (source.level>=52?(source.job==34?连击中侧面攻击追加效果：获得5点剑气 :):)(source.level>=62?(source.job==34?连击成功：获得花之闪与5点剑气:连击成功：花之闪):连击成功：花之闪)

        """
        id = 7482
        name = {'Kasha', '花车'}
        combo_action = 7479

    class Fuga(ActionBase):
        """
        向目标所在方向发出扇形范围物理攻击 威力：100(source.level>=62?(source.job==34? 追加效果：获得5点剑气:):)

        """
        id = 7483
        name = {'Fuga', '风雅'}

    class Mangetsu(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：100 连击条件：风雅 连击中威力：160 连击成功：阵风的持续时间延长15秒 最多可延长至40秒 (source.level>=52?(source.job==34?连击成功：获得月之闪与(source.level>=62?(source.job==34?10:5):5)点剑气:连击成功：月之闪):连击成功：月之闪)

        """
        id = 7484
        name = {'Mangetsu', '满月'}
        combo_action = 7483

    class Oka(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：100 连击条件：风雅 连击中威力：160 连击成功：士风的持续时间延长15秒 最多可延长至40秒 (source.level>=52?(source.job==34?连击成功：获得花之闪与(source.level>=62?(source.job==34?10:5):5)点剑气:连击成功：花之闪):连击成功：花之闪)

        """
        id = 7485
        name = {'Oka', '樱花'}
        combo_action = 7483

    class Enpi(ActionBase):
        """
        对目标发动远距离物理攻击 威力：100(source.level>=56?(source.job==34? “燕飞效果提高”状态中威力：320:):)(source.level>=52?(source.job==34? 追加效果：获得(source.level>=62?(source.job==34?10:5):5)点剑气:):)

        """
        id = 7486
        name = {'Enpi', '燕飞'}

    class MidareSetsugekka(ActionBase):
        """
        对目标发动物理攻击 威力：800 (source.job==34?(source.level>=80?追加效果：剑压 最大档数：3档 持续时间：永久 :):) ※该技能无法设置到热键栏

        """
        id = 7487
        name = {'Midare Setsugekka', '纷乱雪月花'}

    class TenkaGoken(ActionBase):
        """
        向目标所在方向发出扇形范围物理攻击 威力：360 (source.job==34?(source.level>=80?追加效果：剑压 最大档数：3档 持续时间：永久 :):) ※该技能无法设置到热键栏

        """
        id = 7488
        name = {'Tenka Goken', '天下五剑'}

    class Higanbana(ActionBase):
        """
        对目标发动物理攻击 威力：250 追加效果：持续伤害 威力：40 持续时间：60秒 (source.job==34?(source.level>=80?追加效果：剑压 最大档数：3档 持续时间：永久 :):) ※该技能无法设置到热键栏

        1228, 彼岸花, Higanbana, 体力逐渐减少
        1319, 彼岸花, Higanbana, 受到持续伤害，同时自身所受的体力恢复效果降低
        """
        id = 7489
        name = {'Higanbana', '彼岸花'}

    class HissatsuShinten(ActionBase):
        """
        对目标发动物理攻击 威力：320 发动条件：剑气25点

        """
        id = 7490
        name = {'Hissatsu: Shinten', '必杀剑·震天'}

    class HissatsuKyuten(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：150 发动条件：剑气25点

        """
        id = 7491
        name = {'Hissatsu: Kyuten', '必杀剑·九天'}

    class HissatsuGyoten(ActionBase):
        """
        冲向目标并发动物理攻击 威力：100 发动条件：剑气10点 止步状态下无法发动

        """
        id = 7492
        name = {'Hissatsu: Gyoten', '必杀剑·晓天'}

    class HissatsuYaten(ActionBase):
        """
        对目标发动物理攻击 威力：100 追加效果：后跳10米距离 追加效果：燕飞效果提高 持续时间：15秒 发动条件：剑气10点 止步状态下无法发动

        """
        id = 7493
        name = {'Hissatsu: Yaten', '必杀剑·夜天'}

    class HissatsuKaiten(ActionBase):
        """
        效果时间内发动的第1个战技威力提高50% 持续时间：10秒 发动条件：剑气20点

        1229, 必杀剑·回天, Kaiten, 下次发动战技造成的伤害提高
        """
        id = 7494
        name = {'Hissatsu: Kaiten', '必杀剑·回天'}

    class Hagakure(ActionBase):
        """
        将闪转换为剑气 每一道闪可转换10点剑气 发动条件：雪之闪或月之闪或花之闪状态中

        """
        id = 7495
        name = {'Hagakure', '叶隐'}

    class HissatsuGuren(ActionBase):
        """
        向目标所在方向发出直线范围物理攻击 威力：850 发动条件：剑气50点(source.job==34?(source.level>=72? 与必杀剑·闪影共享复唱时间:):)

        """
        id = 7496
        name = {'Hissatsu: Guren', '必杀剑·红莲'}

    class Meditate(ActionBase):
        """
        进入默想状态持续获得剑气 持续时间：15秒 (source.job==34?(source.level>=80?追加效果：连续叠加剑压状态 最大档数：3档 持续时间：永久 :):)效果时间内发动技能或进行移动、转身都会立即解除默想 发动之后会停止自动攻击 (source.job==34?(source.level>=80?非战斗中无法获得剑气，也不会附加剑压状态:非战斗中无法获得剑气):非战斗中无法获得剑气) 该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间

        1231, 默想, Meditate, 持续获得剑气
        """
        id = 7497
        name = {'Meditate', '默想'}

    class ThirdEye(ActionBase):
        """
        一定时间内，受到的第一次攻击伤害减轻10% 持续时间：3秒(source.level>=58?(source.job==34? 追加效果：成功减轻伤害后对自身附加开眼状态 持续时间：15秒:):)

        1232, 心眼, Third Eye, 下次受到攻击时所受到的伤害减轻
        """
        id = 7498
        name = {'Third Eye', '心眼'}

    class MeikyoShisui(ActionBase):
        """
        一定时间内，战技无需连击条件即可连击成功 持续时间结束或发动3次居合术之外的战技后取消该状态 持续时间：15秒

        1233, 明镜止水, Meikyo Shisui, 达成战技连击的条件
        1320, 明镜止水, Meikyo Shisui, 将战技的连击置换到最终阶段
        """
        id = 7499
        name = {'Meikyo Shisui', '明镜止水'}

    class HissatsuSeigan(ActionBase):
        """
        对目标发动物理攻击 威力：220 发动条件：剑气15点 发动条件：开眼状态中 与慈眼共享复唱时间

        """
        id = 7501
        name = {'Hissatsu: Seigan', '必杀剑·星眼'}

    class MercifulEyes(ActionBase):
        """
        恢复自身体力 恢复力：200 发动条件：开眼状态中 与必杀剑·星眼共享复唱时间

        """
        id = 7502
        name = {'Merciful Eyes', '慈眼'}

    class Iaijutsu(ActionBase):
        """
        根据闪的数量发动居合术 1闪：彼岸花 2闪：天下五剑 3闪：纷乱雪月花

        """
        id = 7867
        name = {'Iaijutsu', '居合术'}

    class HissatsuSenei(ActionBase):
        """
        对目标发动物理攻击 威力：1100 发动条件：剑气50点 与必杀剑·红莲共享复唱时间

        """
        id = 16481
        name = {'Hissatsu: Senei', '必杀剑·闪影'}

    class Ikishoten(ActionBase):
        """
        获得50点剑气 发动条件：自身处于战斗状态

        """
        id = 16482
        name = {'Ikishoten', '意气冲天'}

    class Tsubame-gaeshi(ActionBase):
        """
        发动上一次使用的居合术 发动条件：居合术使用完毕 该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间

        """
        id = 16483
        name = {'Tsubame-gaeshi', '燕回返'}

    class KaeshiHiganbana(ActionBase):
        """
        对目标发动物理攻击 威力：375 追加效果：持续伤害 威力：60 持续时间：60秒 无法与彼岸花的持续伤害叠加 (source.job==34?(source.level>=80?追加效果：剑压 最大档数：3档 持续时间：永久 :):)该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间 ※该技能无法设置到热键栏

        """
        id = 16484
        name = {'Kaeshi: Higanbana', '回返彼岸花'}

    class KaeshiGoken(ActionBase):
        """
        向目标所在方向发出扇形范围物理攻击 威力：540 (source.job==34?(source.level>=80?追加效果：剑压 最大档数：3档 持续时间：永久 :):)该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间 ※该技能无法设置到热键栏

        """
        id = 16485
        name = {'Kaeshi: Goken', '回返五剑'}

    class KaeshiSetsugekka(ActionBase):
        """
        对目标发动物理攻击 威力：1200 (source.job==34?(source.level>=80?追加效果：剑压 最大档数：3档 持续时间：永久 :):)该能力不仅有单独计算的复唱时间，还会与战技共享复唱时间 ※该技能无法设置到热键栏

        """
        id = 16486
        name = {'Kaeshi: Setsugekka', '回返雪月花'}

    class Shoha(ActionBase):
        """
        对目标发动物理攻击 威力：400 发动时会消耗全部的剑压 发动条件：剑压3档 自身处于战斗状态时使用默想、居合术、燕回返技能，可以获得剑压 最大档数：3档 持续时间：永久

        """
        id = 16487
        name = {'Shoha', '照破'}
