from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class HeavySwing(ActionBase):
        """
        对目标发动物理攻击 威力：200

        """
        id = 31
        name = {'Heavy Swing', '重劈'}

    class Maim(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：重劈 连击中威力：320(source.level>=30?(source.job==21?(source.job==21?(source.level>=35? 连击成功：获得10点兽魂:):):):)

        85, 凶残裂, Maim, 攻击所造成的伤害提高
        """
        id = 37
        name = {'Maim', '凶残裂'}
        combo_action = 31

    class Berserk(ActionBase):
        """
        一定时间内，自身攻击必定暴击并且直击 持续时间：10秒(source.level>=50?(source.job==3? 追加效果：暴风碎的持续时间延长15秒 最多可延长至60秒:(source.job==21? 追加效果：暴风碎的持续时间延长15秒 最多可延长至60秒:)):)

        86, 狂暴, Berserk, 自身攻击必定暴击并且直击
        """
        id = 38
        name = {'Berserk', '狂暴'}

    class ThrillOfBattle(ActionBase):
        """
        一定时间内，自身的最大体力提高20% (source.job==21?(source.level>=78?同时，自身所受的体力恢复效果提高20% :):)发动时恢复最大体力的20% 持续时间：10秒

        87, 战栗, Thrill of Battle, 体力最大值提高 习得战栗效果提高后追加效果：自身所受的治疗效果提高
        """
        id = 40
        name = {'Thrill of Battle', '战栗'}

    class Overpower(ActionBase):
        """
        向目标所在方向发出扇形范围物理攻击 威力：130

        """
        id = 41
        name = {'Overpower', '超压斧'}

    class StormsPath(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：凶残裂 连击中威力：420 连击成功：恢复自身体力 恢复力：250(source.level>=30?(source.job==21?(source.job==21?(source.level>=35? 连击成功：获得20点兽魂:):):):)

        408, 暴风斩, Storm's Path, 攻击所造成的伤害降低
        """
        id = 42
        name = {'Storm's Path', '暴风斩'}
        combo_action = 37

    class Holmgang(ActionBase):
        """
        效果中除特定攻击之外其他所有对自身发动的攻击均无法令体力减少到1以下 当目标为敌人时，禁止目标移动 持续时间：8秒

        88, 死斗, Holmgang, 无法自由移动，受到伤害也不会解除
        409, 死斗, Holmgang, 除特定攻击之外其他所有对自身发动的攻击均无法令体力减少到1以下
        1304, 死斗, Holmgang, 无法自由移动，受到伤害也不会解除 另外，除特定攻击之外其他所有对自身发动的攻击均无法令体力减少到1以下
        1305, 死斗, Holmgang, 无法自由移动，受到伤害也不会解除
        """
        id = 43
        name = {'Holmgang', '死斗'}

    class Vengeance(ActionBase):
        """
        一定时间内，令自身所受到的伤害减轻30%，同时受到物理攻击时会给予对方反击伤害 威力：55 持续时间：15秒

        89, 复仇, Vengeance, 受到物理攻击时会发动反击
        """
        id = 44
        name = {'Vengeance', '复仇'}

    class StormsEye(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：凶残裂 连击中威力：420 连击成功：攻击伤害提高10% 持续时间：30秒 若自身已经附加暴风碎状态，则持续时间延长30秒 最多可延长至60秒 此外狂暴(source.level>=30?(source.job==21?以及秘银暴风:):)也能延长暴风碎的持续时间 (source.level>=30?(source.job==21? 连击成功：获得10点兽魂:):)

        90, 暴风碎, Storm's Eye, 攻击所造成的伤害提高
        """
        id = 45
        name = {'Storm's Eye', '暴风碎'}
        combo_action = 37

    class Tomahawk(ActionBase):
        """
        对目标发动远距离物理攻击 威力：140 追加效果：提升仇恨

        """
        id = 46
        name = {'Tomahawk', '飞斧'}

    class Defiance(ActionBase):
        """
        极大幅度增加战斗时获得的仇恨量 再次发动时则取消该状态 持续时间：永久

        91, 守护, Defiance, 自身仇恨提高
        1396, 守护, Defiance, 以攻击力降低为代价减少自身所受到的伤害
        """
        id = 48
        name = {'Defiance', '守护'}

    class InnerBeast(ActionBase):
        """
        对目标发动物理攻击 威力：350 发动条件：兽魂50点

        411, 原初之魂, Inner Beast, 减轻所受到的伤害
        1398, 原初之魂, Inner Beast, 减轻所受到的伤害
        """
        id = 49
        name = {'Inner Beast', '原初之魂'}

    class SteelCyclone(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：220 发动条件：兽魂50点

        """
        id = 51
        name = {'Steel Cyclone', '钢铁旋风'}

    class Infuriate(ActionBase):
        """
        获得50点兽魂 (source.job==21?(source.level>=72?追加效果：原初的混沌 持续时间：30秒 :):)积蓄次数：2 发动条件：自身处于战斗状态

        """
        id = 52
        name = {'Infuriate', '战嚎'}

    class FellCleave(ActionBase):
        """
        对目标发动物理攻击 威力：590 (source.job==21?(source.level>=80?该技能在原初的混沌状态中会变为狂魂 :):)发动条件：兽魂50点

        """
        id = 3549
        name = {'Fell Cleave', '裂石飞环'}

    class Decimate(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：250 (source.job==21?(source.level>=72?该技能在原初的混沌状态中会变为混沌旋风 :):)发动条件：兽魂50点

        """
        id = 3550
        name = {'Decimate', '地毁人亡'}

    class RawIntuition(ActionBase):
        """
        一定时间内，自身所受的伤害减轻20% 持续时间：6秒(source.job==21?(source.level>=76? 与原初的勇猛共享复唱时间:):)

        735, 原初的直觉, Raw Intuition, 减轻所受到的伤害
        """
        id = 3551
        name = {'Raw Intuition', '原初的直觉'}

    class Equilibrium(ActionBase):
        """
        恢复自身体力 恢复力：1200

        """
        id = 3552
        name = {'Equilibrium', '泰然自若'}

    class Onslaught(ActionBase):
        """
        冲向目标并发动物理攻击 威力：100 发动条件：兽魂20点 止步状态下无法发动

        """
        id = 7386
        name = {'Onslaught', '猛攻'}

    class Upheaval(ActionBase):
        """
        对目标发动物理攻击 威力：450 发动条件：兽魂20点

        """
        id = 7387
        name = {'Upheaval', '动乱'}

    class ShakeItOff(ActionBase):
        """
        为自身与周围队员附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于目标最大体力15%的伤害量 另外，自身处于“战栗”“复仇”“原初的直觉”状态时，每解除一个状态，防护罩的效果量上升2% 持续时间：15秒

        1457, 摆脱, Shake It Off, 抵消一定伤害
        1993, 摆脱, Shake It Off, 抵消一定伤害
        """
        id = 7388
        name = {'Shake It Off', '摆脱'}

    class InnerRelease(ActionBase):
        """
        一定时间内不需要消耗兽魂就可以发动特定技能，且自身攻击必定暴击并且直击 效果时间内，自身不会受到眩晕、睡眠、止步、加重和除特定攻击之外其他所有击退、吸引的影响 持续时间：10秒 追加效果：暴风碎的持续时间延长15秒 最多可延长至60秒

        1177, 原初的解放, Inner Release, 兽魂不会消耗，自身攻击必定暴击并且直击，不受眩晕、睡眠、止步、加重和除特定攻击之外其他所有击退、吸引的效果影响
        1303, 原初的解放, Inner Release, 兽魂不会消耗，不受眩晕、睡眠、止步、加重、沉默、击退、吸引的效果影响
        """
        id = 7389
        name = {'Inner Release', '原初的解放'}

    class MythrilTempest(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：100 连击条件：超压斧 连击中威力：200(source.level>=50?(source.job==3? 连击成功：暴风碎的持续时间延长30秒 最多可延长至60秒:(source.job==21? 连击成功：暴风碎的持续时间延长30秒 最多可延长至60秒:)):)(source.job==21?(source.level>=74? 连击成功：获得20点兽魂:):)

        """
        id = 16462
        name = {'Mythril Tempest', '秘银暴风'}
        combo_action = 41

    class ChaoticCyclone(ActionBase):
        """
        对自身周围的敌人发动范围物理攻击 威力：400 该技能必定暴击并且直击 追加效果：战嚎的复唱时间缩短5秒 发动后会取消原初的混沌状态 发动条件：原初的混沌状态中且兽魂50点 ※该技能无法设置到热键栏

        2078, 混沌旋风, Chaotic Cyclone, 受到攻击的伤害增加
        """
        id = 16463
        name = {'Chaotic Cyclone', '混沌旋风'}

    class NascentFlash(ActionBase):
        """
        对自身附加原初的勇猛状态 当指定一名队员为目标时，为自身附加原初的勇猛状态，为目标附加原初的武猛状态 原初的勇猛效果：自身的物理攻击命中后恢复体力 原初的武猛效果：恢复战士自身恢复量50%的体力 同时，受到的伤害减轻10% 持续时间：6秒 与原初的直觉共享复唱时间

        1857, 原初的勇猛, Nascent Flash, 自身的物理攻击命中时会吸收体力
        2061, 原初的勇猛, Nascent Flash, 自身的物理攻击命中时会吸收体力 另外受到攻击的伤害减少
        2227, 原初的勇猛, Nascent Flash, 自身的物理攻击命中时会吸收体力
        """
        id = 16464
        name = {'Nascent Flash', '原初的勇猛'}

    class InnerChaos(ActionBase):
        """
        对目标发动物理攻击 威力：920 该技能必定暴击并且直击 追加效果：战嚎的复唱时间缩短5秒 发动后会取消原初的混沌状态 发动条件：原初的混沌状态中且兽魂50点 ※该技能无法设置到热键栏

        2077, 狂魂, Inner Chaos, 受到攻击的伤害增加
        """
        id = 16465
        name = {'Inner Chaos', '狂魂'}
