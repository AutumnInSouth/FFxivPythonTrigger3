from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Stone(ActionBase):
        """
        对目标发动土属性魔法攻击 威力：140

        """
        id = 119
        name = {'Stone', '飞石'}

    class Cure(ActionBase):
        """
        恢复目标的体力 恢复力：450(source.level>=32?(source.job==6? 追加效果（发动几率15%）：令下次发动的救疗不消耗魔力 持续时间：15秒:(source.job==24? 追加效果（发动几率15%）：令下次发动的救疗不消耗魔力 持续时间：15秒:)):)

        """
        id = 120
        name = {'Cure', '治疗'}

    class Aero(ActionBase):
        """
        对目标发动风属性魔法攻击 威力：50 追加效果：风属性持续伤害 威力：30 持续时间：18秒

        143, 疾风, Aero, 风属性持续伤害，体力逐渐流失
        """
        id = 121
        name = {'Aero', '疾风'}

    class Medica(ActionBase):
        """
        恢复自身及周围队员的体力 恢复力：300

        """
        id = 124
        name = {'Medica', '医治'}

    class Raise(ActionBase):
        """
        令无法战斗的目标以衰弱状态重新振作起来

        148, 复活, Raise, 接受别人发动的复活
        1140, 复活, Raise, 可选择在原地复活
        """
        id = 125
        name = {'Raise', '复活'}

    class StoneIi(ActionBase):
        """
        对目标发动土属性魔法攻击 威力：200

        """
        id = 127
        name = {'Stone II', '坚石'}

    class CureIii(ActionBase):
        """
        恢复目标及其周围队员的体力 恢复力：550

        """
        id = 131
        name = {'Cure III', '愈疗'}

    class AeroIi(ActionBase):
        """
        对目标发动风属性魔法攻击 威力：60 追加效果：风属性持续伤害 威力：60 持续时间：18秒

        144, 烈风, Aero II, 风属性持续伤害，体力逐渐流失
        """
        id = 132
        name = {'Aero II', '烈风'}

    class MedicaIi(ActionBase):
        """
        恢复自身及周围队员的体力 恢复力：200 追加效果：目标体力持续恢复 恢复力：100 持续时间：15秒

        150, 医济, Medica II, 体力会随时间逐渐恢复
        """
        id = 133
        name = {'Medica II', '医济'}

    class FluidAura(ActionBase):
        """
        对目标造成止步效果 持续时间：6秒

        """
        id = 134
        name = {'Fluid Aura', '水流环'}

    class CureIi(ActionBase):
        """
        恢复目标的体力 恢复力：700

        """
        id = 135
        name = {'Cure II', '救疗'}

    class PresenceOfMind(ActionBase):
        """
        一定时间内，自身的自动攻击间隔、魔法的咏唱及复唱时间缩短20% 持续时间：15秒

        157, 神速咏唱, Presence of Mind, 自动攻击间隔时间缩短，魔法的咏唱时间和复唱时间缩短
        """
        id = 136
        name = {'Presence of Mind', '神速咏唱'}

    class Regen(ActionBase):
        """
        令目标体力持续恢复 恢复力：200 持续时间：18秒

        158, 再生, Regen, 体力会随时间逐渐恢复
        1330, 再生, Regen, 体力会随时间逐渐恢复
        """
        id = 137
        name = {'Regen', '再生'}

    class Holy(ActionBase):
        """
        对周围的敌人发动无属性范围魔法攻击 威力：140 追加效果：眩晕 持续时间：4秒

        """
        id = 139
        name = {'Holy', '神圣'}

    class Benediction(ActionBase):
        """
        令目标体力完全恢复

        """
        id = 140
        name = {'Benediction', '天赐祝福'}

    class StoneIii(ActionBase):
        """
        对目标发动土属性魔法攻击 威力：240

        """
        id = 3568
        name = {'Stone III', '垒石'}

    class Asylum(ActionBase):
        """
        以指定地点为中心产生治疗区域 效果时间内，持续恢复进入该区域的自身及队员的体力 恢复力：100 持续时间：24秒(source.job==24?(source.level>=78? 追加效果：区域内的自身和队员所受的体力恢复效果提高10%:):)

        739, 庇护所, Asylum, 产生能够令范围内队员恢复体力的区域
        1911, 庇护所, Asylum, 产生能够令范围内队员恢复体力的区域
        1912, 庇护所, Asylum, 自身所受的治疗效果提高
        """
        id = 3569
        name = {'Asylum', '庇护所'}

    class Tetragrammaton(ActionBase):
        """
        恢复目标的体力 恢复力：700

        """
        id = 3570
        name = {'Tetragrammaton', '神名'}

    class Assize(ActionBase):
        """
        对周围的敌人发动无属性范围魔法攻击 威力：400 追加效果：恢复自身及周围队员的体力 恢复力：400 追加效果：恢复自身最大魔力的5%

        """
        id = 3571
        name = {'Assize', '法令'}

    class ThinAir(ActionBase):
        """
        一定时间内发动技能消耗的魔力降低100% 持续时间：12秒

        1217, 无中生有, Thin Air, 发动技能时不会消耗魔力
        """
        id = 7430
        name = {'Thin Air', '无中生有'}

    class StoneIv(ActionBase):
        """
        对目标发动土属性魔法攻击 威力：280

        """
        id = 7431
        name = {'Stone IV', '崩石'}

    class DivineBenison(ActionBase):
        """
        为自身或一名队员附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于500恢复力的伤害量 持续时间：15秒

        1218, 神祝祷, Divine Benison, 抵消一定伤害
        1404, 神祝祷, Divine Benison, 抵消一定伤害
        """
        id = 7432
        name = {'Divine Benison', '神祝祷'}

    class PlenaryIndulgence(ActionBase):
        """
        为自身与周围队员附加告解状态 持续时间：10秒 在状态中使用医治、愈疗、医济、狂喜之心，会使目标产生额外的恢复效果 恢复力：200

        """
        id = 7433
        name = {'Plenary Indulgence', '全大赦'}

    class AfflatusSolace(ActionBase):
        """
        恢复目标的体力 恢复力：700 (source.job==24?(source.level>=74?追加效果：血百合开放 :):)发动条件：治疗百合

        2036, 安慰之心, Afflatus Solace, 体力会随时间逐渐恢复
        """
        id = 16531
        name = {'Afflatus Solace', '安慰之心'}

    class Dia(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：120 追加效果：无属性持续伤害 威力：60 持续时间：30秒

        1871, 天辉, Dia, 体力逐渐减少
        2035, 天辉, Dia, 受到攻击的伤害增加
        """
        id = 16532
        name = {'Dia', '天辉'}

    class Glare(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：300

        """
        id = 16533
        name = {'Glare', '闪耀'}

    class AfflatusRapture(ActionBase):
        """
        恢复自身及周围队员的体力 恢复力：300 追加效果：血百合开放 发动条件：治疗百合

        """
        id = 16534
        name = {'Afflatus Rapture', '狂喜之心'}

    class AfflatusMisery(ActionBase):
        """
        对目标及其周围的敌人发动无属性范围魔法攻击 威力：900 攻击复数敌人时，对目标之外的敌人威力降低25% 发动条件：血百合完全开放

        """
        id = 16535
        name = {'Afflatus Misery', '苦难之心'}

    class Temperance(ActionBase):
        """
        一定时间内，自身发动治疗魔法的治疗量提高20%，自身与30米以内的队员受到的伤害减轻10% 持续时间：20秒

        1872, 节制, Temperance, 治疗魔法的治疗量提高，且减少周围队员受到的伤害
        1873, 节制, Temperance, 减轻所受到的伤害
        2037, 节制, Temperance, 发动攻击所造成的伤害及自身发动的体力恢复效果提高，周围队员所受伤害减轻
        2038, 节制, Temperance, 减轻所受到的伤害
        """
        id = 16536
        name = {'Temperance', '节制'}
