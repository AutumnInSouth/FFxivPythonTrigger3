from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Fire(ActionBase):
        """
        对目标发动火属性魔法攻击 威力：180 追加效果：星极火 持续时间：15秒 在处于灵极冰状态时只会解除该状态 持续时间：15秒 (source.level>=42?(source.job==7? 追加效果（发动几率40%）：下次发动爆炎不消耗魔力，同时也没有咏唱时间 持续时间：18秒:(source.job==25? 追加效果（发动几率40%）：下次发动爆炎不消耗魔力，同时也没有咏唱时间 持续时间：18秒:)):)

        """
        id = 141
        name = {"Fire", "火炎"}

    class Blizzard(ActionBase):
        """
        对目标发动冰属性魔法攻击 威力：180 追加效果：灵极冰 持续时间：15秒 在处于星极火状态时只会解除该状态 持续时间：15秒

        """
        id = 142
        name = {"Blizzard", "冰结"}

    class Thunder(ActionBase):
        """
        对目标发动雷属性魔法攻击 威力：30 追加效果：雷属性持续伤害 威力：40 持续时间：18秒 自身对目标附加的雷系魔法持续伤害效果同时只能存在一种(source.level>=28?(source.job==7? 追加效果（持续伤害每次起效时，发动几率10%）： 下次发动的雷系魔法咏唱时间与消耗魔力均为0 且命中时的威力会加算持续伤害的总和 持续时间：18秒:(source.job==25? 追加效果（持续伤害每次起效时，发动几率10%）： 下次发动的雷系魔法咏唱时间与消耗魔力均为0 且命中时的威力会加算持续伤害的总和 持续时间：18秒:)):)

        161, 闪雷, Thunder, 雷属性持续伤害，体力逐渐流失
        1324, 闪雷, Thunder, 受到持续伤害
        """
        id = 144
        name = {"Thunder", "闪雷"}

    class Sleep(ActionBase):
        """
        令目标及其周围的敌人陷入睡眠状态 持续时间：30秒 发动之后会停止自动攻击

        """
        id = 145
        name = {"Sleep", "催眠"}

    class BlizzardIi(ActionBase):
        """
        对周围的敌人发动冰属性范围魔法攻击 威力：50 追加效果：灵极冰 持续时间：15秒 在处于星极火状态时只会解除该状态 持续时间：15秒

        """
        id = 146
        name = {"Blizzard II", "冰冻"}

    class FireIi(ActionBase):
        """
        对目标及其周围的敌人发动火属性范围魔法攻击 威力：80 追加效果：星极火 持续时间：15秒 在处于灵极冰状态时只会解除该状态 持续时间：15秒

        """
        id = 147
        name = {"Fire II", "烈炎"}

    class Transpose(ActionBase):
        """
        自身处于星极火或灵极冰的状态时迅速切换到另一状态的初级阶段

        """
        id = 149
        name = {"Transpose", "星灵移位"}

    class FireIii(ActionBase):
        """
        对目标发动火属性魔法攻击 威力：240 追加效果：星极火最大档数 持续时间：15秒 在处于灵极冰状态时会同时解除该状态

        """
        id = 152
        name = {"Fire III", "爆炎"}

    class ThunderIii(ActionBase):
        """
        对目标发动雷属性魔法攻击 威力：70 追加效果：雷属性持续伤害 威力：40 持续时间：24秒 自身对目标附加的雷系魔法持续伤害效果同时只能存在一种(source.level>=28?(source.job==7? 追加效果（持续伤害每次起效时，发动几率10%）： 下次发动的雷系魔法咏唱时间与消耗魔力均为0 且命中时的威力会加算持续伤害的总和 持续时间：18秒:(source.job==25? 追加效果（持续伤害每次起效时，发动几率10%）： 下次发动的雷系魔法咏唱时间与消耗魔力均为0 且命中时的威力会加算持续伤害的总和 持续时间：18秒:)):)

        163, 暴雷, Thunder III, 雷属性持续伤害，体力逐渐流失
        """
        id = 153
        name = {"Thunder III", "暴雷"}

    class BlizzardIii(ActionBase):
        """
        对目标发动冰属性魔法攻击 威力：240 追加效果：灵极冰最大档数 持续时间：15秒 在处于星极火状态时会同时解除该状态

        """
        id = 154
        name = {"Blizzard III", "冰封"}

    class AetherialManipulation(ActionBase):
        """
        指定一名队员为目标，自身快速移动到目标身边 止步状态下无法发动

        """
        id = 155
        name = {"Aetherial Manipulation", "以太步"}

    class Scathe(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：100 追加效果（发动几率20%）：伤害变为2倍

        """
        id = 156
        name = {"Scathe", "崩溃"}

    class Manaward(ActionBase):
        """
        为自身张开一个防护罩，在一定时间内能抵消相当于最大体力30%的伤害量 抵消的伤害量超过上限时防护罩自动消失 持续时间：20秒

        168, 魔罩, Manaward, 抵消一定伤害
        1989, 魔罩, Manaward, 抵消一定伤害
        """
        id = 157
        name = {"Manaward", "魔罩"}

    class Manafont(ActionBase):
        """
        恢复最大魔力的30%

        """
        id = 158
        name = {"Manafont", "魔泉"}

    class Freeze(ActionBase):
        """
        对目标及其周围的敌人发动冰属性范围魔法攻击 威力：100 追加效果：灵极冰最大档数 持续时间：15秒 在处于星极火状态时会同时解除该状态(source.job==25?(source.level>=68? 追加效果：1档灵极心 灵极心效果：抵消星极火状态中发动火系魔法增加的魔力消耗 另外，发动核爆时会消耗全部的灵极心将魔力消耗降为2/3:):)

        """
        id = 159
        name = {"Freeze", "玄冰"}

    class Flare(ActionBase):
        """
        对目标及其周围的敌人发动火属性范围魔法攻击 威力：260 攻击复数敌人时，对目标之外的敌人威力降低40% 追加效果：星极火最大档数 持续时间：15秒 在处于灵极冰状态时会同时解除该状态

        """
        id = 162
        name = {"Flare", "核爆"}

    class LeyLines(ActionBase):
        """
        在自身脚下产生黑魔纹 黑魔纹效果：自身的自动攻击间隔、魔法的咏唱及复唱时间缩短15% 持续时间：30秒

        737, 黑魔纹, Ley Lines, 在地上产生黑魔纹
        """
        id = 3573
        name = {"Ley Lines", "黑魔纹"}

    class Sharpcast(ActionBase):
        """
        效果时间内，自身发动的1次“崩溃”或“火炎”或“雷系魔法”必定触发“崩溃的追加效果”“火苗”“雷云” 持续时间：15秒

        867, 激情咏唱, Sharpcast, 下次咏唱的崩溃、火炎以及雷系魔法必定触发“崩溃的追加效果”“火苗”“雷云”
        """
        id = 3574
        name = {"Sharpcast", "激情咏唱"}

    class Enochian(ActionBase):
        """
        一定时间内，自身发动魔法攻击造成的伤害提高(source.job==25?(source.level>=78?15:(source.level>=70?(source.job==25?10:5):5)):(source.level>=70?(source.job==25?10:5):5))%(source.job==25?(source.level>=58?(source.level>=60? 同时可以咏唱冰澈、炽炎(source.job==25?(source.level>=72?、绝望:):)(source.job==25?(source.level>=76?、灵极魂:):) : 同时可以咏唱冰澈 ):):)星极火及灵极冰状态全部消失时天语状态也会同时消失 (source.level>=70?(source.job==25?追加效果：天语状态持续30秒可对自身附加通晓状态(source.job==25?(source.level>=80? 最大档数：2档 持续时间：永久 : 持续时间：永久 ): 持续时间：永久 ):):)发动条件：星极火或灵极冰状态中

        868, 天语, Enochian, 魔法攻击所造成的伤害提高
        """
        id = 3575
        name = {"Enochian", "天语"}

    class BlizzardIv(ActionBase):
        """
        对目标发动冰属性魔法攻击 威力：300 追加效果：3档灵极心 灵极心效果：抵消星极火状态中发动火系魔法增加的魔力消耗(source.level>=68?(source.job==25? 另外，发动核爆时会消耗全部的灵极心将魔力消耗降为2/3:):) 发动条件：天语及灵极冰状态中

        """
        id = 3576
        name = {"Blizzard IV", "冰澈"}

    class FireIv(ActionBase):
        """
        对目标发动火属性魔法攻击 威力：300 发动条件：天语及星极火状态中

        """
        id = 3577
        name = {"Fire IV", "炽炎"}

    class BetweenTheLines(ActionBase):
        """
        快速移动到自身留下的黑魔纹中心 止步状态下无法发动

        """
        id = 7419
        name = {"Between the Lines", "魔纹步"}

    class ThunderIv(ActionBase):
        """
        对目标及其周围敌人发动雷属性范围魔法攻击 威力：50 追加效果：雷属性持续伤害 威力：30 持续时间：18秒 自身对目标附加的雷系魔法持续伤害效果同时只能存在一种 追加效果（持续伤害每次起效时，发动几率3%）：下次发动的雷系魔法咏唱时间与消耗魔力均为0 且命中时的威力会加算持续伤害的总和 持续时间：18秒

        1210, 霹雷, Thunder IV, 雷属性持续伤害，体力逐渐流失
        """
        id = 7420
        name = {"Thunder IV", "霹雷"}

    class Triplecast(ActionBase):
        """
        效果时间内，前3次咏唱的魔法没有任何咏唱时间 持续时间：15秒

        1211, 三连咏唱, Triplecast, 咏唱魔法不需要咏唱时间
        """
        id = 7421
        name = {"Triplecast", "三连咏唱"}

    class Foul(ActionBase):
        """
        对目标及其周围敌人发动无属性范围魔法攻击 威力：650 攻击复数敌人时，对目标之外的敌人威力降低25% 发动条件：通晓

        """
        id = 7422
        name = {"Foul", "秽浊"}

    class ThunderIi(ActionBase):
        """
        对目标及其周围敌人发动雷属性范围魔法攻击 威力：30 追加效果：雷属性持续伤害 威力：30 持续时间：12秒 自身对目标附加的雷系魔法持续伤害效果同时只能存在一种(source.level>=28?(source.job==7? 追加效果（持续伤害每次起效时，发动几率3%）： 下次发动的雷系魔法咏唱时间与消耗魔力均为0 且命中时的威力会加算持续伤害的总和 持续时间：18秒:(source.job==25? 追加效果（持续伤害每次起效时，发动几率3%）： 下次发动的雷系魔法咏唱时间与消耗魔力均为0 且命中时的威力会加算持续伤害的总和 持续时间：18秒:)):)

        162, 震雷, Thunder II, 雷属性持续伤害，体力逐渐流失
        2075, 震雷, Thunder II, 受到持续伤害
        """
        id = 7447
        name = {"Thunder II", "震雷"}

    class Despair(ActionBase):
        """
        对目标发动火属性魔法攻击 威力：380 追加效果：星极火最大档数 持续时间：15秒 发动条件：天语及星极火状态中

        """
        id = 16505
        name = {"Despair", "绝望"}

    class UmbralSoul(ActionBase):
        """
        对自身附加灵极冰状态及1档灵极心 灵极心效果：抵消星极火状态中发动火系魔法增加的魔力消耗 另外，发动核爆时会消耗全部的灵极心将魔力消耗降为2/3 发动条件：天语及灵极冰状态中

        """
        id = 16506
        name = {"Umbral Soul", "灵极魂"}

    class Xenoglossy(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：750 发动条件：通晓

        """
        id = 16507
        name = {"Xenoglossy", "异言"}
