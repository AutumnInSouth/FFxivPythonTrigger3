from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Cascade(ActionBase):
        """
        Delivers an attack with a potency of 250. Additional Effect: 50% chance of granting Flourishing Cascade Duration: 20s ※Action changes to Emboite while dancing.
        """
        id = 15989
        name = {"Cascade", "瀑泻"}

    class Fountain(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Cascade Combo Potency: 300 Combo Bonus: 50% chance of granting Flourishing Fountain Duration: 20s ※Action changes to Entrechat while dancing.
        """
        id = 15990
        name = {"Fountain", "喷泉"}
        combo_action = 15989

    class ReverseCascade(ActionBase):
        """
        Delivers an attack with a potency of 300. (source.job==38?(source.level>=30?Additional Effect: 50% chance of granting a Fourfold Feather :):)Can only be executed while under the effect of Flourishing Cascade. ※Action changes to Jete while dancing.
        """
        id = 15991
        name = {"Reverse Cascade", "逆瀑泻"}

    class Fountainfall(ActionBase):
        """
        Delivers an attack with a potency of 350. Additional Effect: 50% chance of granting a Fourfold Feather Can only be executed while under the effect of Flourishing Fountain. ※Action changes to Pirouette while dancing.
        """
        id = 15992
        name = {"Fountainfall", "坠喷泉"}

    class Windmill(ActionBase):
        """
        Delivers an attack with a potency of 150 to all nearby enemies. Additional Effect: 50% chance of granting Flourishing Windmill Duration: 20s
        """
        id = 15993
        name = {"Windmill", "风车"}

    class Bladeshower(ActionBase):
        """
        Delivers an attack with a potency of 100 to all nearby enemies. Combo Action: Windmill Combo Potency: 200 Combo Bonus: 50% chance of granting Flourishing Shower Duration: 20s
        """
        id = 15994
        name = {"Bladeshower", "落刃雨"}
        combo_action = 15993

    class RisingWindmill(ActionBase):
        """
        Delivers an attack to all nearby enemies with a potency of 300 for the first enemy, and 50% less for all remaining enemies. Additional Effect: 50% chance of granting a Fourfold Feather Can only be executed while under the effect of Flourishing Windmill.
        """
        id = 15995
        name = {"Rising Windmill", "升风车"}

    class Bloodshower(ActionBase):
        """
        Delivers an attack to all nearby enemies with a potency of 350 for the first enemy, and 50% less for all remaining enemies. Additional Effect: 50% chance of granting a Fourfold Feather Can only be executed while under the effect of Flourishing Shower.
        """
        id = 15996
        name = {"Bloodshower", "落血雨"}

    class StandardStep(ActionBase):
        """
        Begin dancing, granting yourself Standard Step. Duration: 15s Action changes to Standard Finish while dancing. Only Standard Finish, En Avant, step actions, role actions, Sprint, and Limit Break can be performed while dancing. Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
        1818, Standard Step, Standard Step, Caught up in the dance and only able to execute step actions, role actions, Sprint, Limit Break, <UIForeground(500)><UIGlow(501)>Standard Finish</UIGlow></UIForeground>, and <UIForeground(500)><UIGlow(501)>En Avant</UIGlow></UIForeground>.
        2023, Standard Step, Standard Step, Caught up in the dance and only able to execute step actions, additional actions, <UIForeground(500)><UIGlow(501)>Head Graze</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Bolt</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Medical Kit</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Standard Finish</UIGlow></UIForeground>, and <UIForeground(500)><UIGlow(501)>En Avant</UIGlow></UIForeground>.
        """
        id = 15997
        name = {"Standard Step", "标准舞步"}

    class TechnicalStep(ActionBase):
        """
        Begin dancing, granting yourself Technical Step. Duration: 15s Action changes to Technical Finish while dancing. Only Technical Finish, En Avant, step actions, role actions, Sprint, and Limit Break can be performed while dancing. Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions.
        1819, Technical Step, Technical Step, Caught up in the dance and only able to execute step actions, role actions, Sprint, Limit Break, <UIForeground(500)><UIGlow(501)>Technical Finish</UIGlow></UIForeground>, and <UIForeground(500)><UIGlow(501)>En Avant</UIGlow></UIForeground>.
        2049, Technical Step, Technical Step, Caught up in the dance and only able to execute step actions, additional actions, <UIForeground(500)><UIGlow(501)>Technical Finish</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>En Avant</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Head Graze</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Bolt</UIGlow></UIForeground>, and <UIForeground(500)><UIGlow(501)>Medical Kit</UIGlow></UIForeground>.
        """
        id = 15998
        name = {"Technical Step", "技巧舞步"}

    class Emboite(ActionBase):
        """
        Perform an emboite. When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased. Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions. ※This action cannot be assigned to a hotbar.
        """
        id = 15999
        name = {"Emboite", "蔷薇曲脚步"}

    class Entrechat(ActionBase):
        """
        Perform an entrechat. When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased. Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions. ※This action cannot be assigned to a hotbar.
        """
        id = 16000
        name = {"Entrechat", "小鸟交叠跳"}

    class Jete(ActionBase):
        """
        Perform a jete. When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased. Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions. ※This action cannot be assigned to a hotbar.
        """
        id = 16001
        name = {"Jete", "绿叶小踢腿"}

    class Pirouette(ActionBase):
        """
        Perform a pirouette. When performed together with other step actions, in sequence, the potency of Standard Finish and Technical Finish is increased. Triggers the cooldown of step and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions. ※This action cannot be assigned to a hotbar.
        """
        id = 16002
        name = {"Pirouette", "金冠趾尖转"}

    class StandardFinish(ActionBase):
        """
        Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies. 0 steps: 500 1 step: 750 2 steps: 1,000 (source.job==38?(source.level>=76?Step Bonus: Grants Standard Finish and Esprit to self and party member designated as your Dance Partner:Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner):Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner) Damage bonus of Standard Finish varies with number of successful steps. 1 step: 2% 2 steps: 5% Duration: 60s Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions. ※This action cannot be assigned to a hotbar.
        1821, Standard Finish, Standard Finish, Damage dealt is increased.
        2024, Standard Finish, Standard Finish, Weaponskill and spell cast and recast time are reduced.
        2105, Standard Finish, Standard Finish, Damage dealt is increased.
        2113, Standard Finish, Standard Finish, Weaponskill and spell cast and recast time are reduced.
        """
        id = 16003
        name = {"Standard Finish", "标准舞步结束"}

    class TechnicalFinish(ActionBase):
        """
        Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies. 0 steps: 500 1 step: 750 2 steps: 1,000 3 steps: 1,250 4 steps: 1,500 (source.job==38?(source.level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members) Damage bonus of Technical Finish varies with number of successful steps. 1 step: 1% 2 steps: 2% 3 steps: 3% 4 steps: 5% Duration: 20s Additional Effect: Activates the Esprit Gauge Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions. ※This action cannot be assigned to a hotbar.
        1822, Technical Finish, Technical Finish, Damage dealt is increased.
        2050, Technical Finish, Technical Finish, Weaponskill and spell cast and recast time are reduced.
        """
        id = 16004
        name = {"Technical Finish", "技巧舞步结束"}

    class SaberDance(ActionBase):
        """
        Delivers an attack to target and all enemies nearby it with a potency of 600 for the first enemy, and 50% less for all remaining enemies. Esprit Gauge Cost: 50
        2022, Saber Dance, Saber Dance, Damage dealt is increased.
        """
        id = 16005
        name = {"Saber Dance", "剑舞"}

    class ClosedPosition(ActionBase):
        """
        Grants you Closed Position and designates a party member as your Dance Partner, allowing you to share the effects of Standard Finish, Devilment, and Curing Waltz with said party member. Effect ends upon reuse.
        1823, Closed Position, Closed Position, Sharing the effects of certain actions with target party member.
        2026, Closed Position, Closed Position, Sharing the effects of certain actions with target party member.
        """
        id = 16006
        name = {"Closed Position", "闭式舞姿"}

    class FanDance(ActionBase):
        """
        Delivers an attack with a potency of 150. Additional Effect: 50% chance of granting Flourishing Fan Dance Duration: 20s Can only be executed while in possession of Fourfold Feathers.
        """
        id = 16007
        name = {"Fan Dance", "扇舞·序"}

    class FanDanceIi(ActionBase):
        """
        Delivers an attack with a potency of 100 to all nearby enemies. Additional Effect: 50% chance of granting Flourishing Fan Dance Duration: 20s Can only be executed while in possession of Fourfold Feathers.
        """
        id = 16008
        name = {"Fan Dance II", "扇舞·破"}

    class FanDanceIii(ActionBase):
        """
        Delivers an attack to target and all enemies nearby it with a potency of 200 for the first enemy, and 50% less for all remaining enemies. Can only be executed while under the effect of Flourishing Fan Dance.
        2052, Fan Dance III, Fan Dance III, Damage taken is reduced.
        """
        id = 16009
        name = {"Fan Dance III", "扇舞·急"}

    class EnAvant(ActionBase):
        """
        Quickly dash 10 yalms forward. (source.job==38?(source.level>=68?Maximum Charges: (source.job==38?(source.level>=78?3:2):2) :):)Cannot be executed while bound.
        2048, En Avant, En Avant, <UIForeground(500)><UIGlow(501)>Cascade</UIGlow></UIForeground> is upgraded to <UIForeground(500)><UIGlow(501)>Reverse Cascade</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Fountain</UIGlow></UIForeground> is upgraded to <UIForeground(500)><UIGlow(501)>Fountainfall</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Windmill</UIGlow></UIForeground> is upgraded to <UIForeground(500)><UIGlow(501)>Rising Windmill</UIGlow></UIForeground>, and <UIForeground(500)><UIGlow(501)>Bladeshower</UIGlow></UIForeground> is upgraded to <UIForeground(500)><UIGlow(501)>Bloodshower</UIGlow></UIForeground>.
        """
        id = 16010
        name = {"En Avant", "前冲步"}

    class Devilment(ActionBase):
        """
        Increases critical hit rate and direct hit rate by 20%. Duration: 20s Additional Effect: Party member designated as your Dance Partner will also receive the effect of Devilment
        1825, Devilment, Devilment, Critical hit rate and direct hit rate are increased.
        """
        id = 16011
        name = {"Devilment", "进攻之探戈"}

    class ShieldSamba(ActionBase):
        """
        Reduces damage taken by self and nearby party members by 10%. Duration: 15s Effect cannot be stacked with bard's Troubadour or machinist's Tactician.
        1826, Shield Samba, Shield Samba, Damage taken is reduced.
        """
        id = 16012
        name = {"Shield Samba", "防守之桑巴"}

    class Flourish(ActionBase):
        """
        Grants you the effects of Flourishing Cascade, Flourishing Fountain, Flourishing Windmill, Flourishing Shower, and Flourishing Fan Dance.
        """
        id = 16013
        name = {"Flourish", "百花争艳"}

    class Improvisation(ActionBase):
        """
        Dance to the beat of your own drum, granting Improvisation to self. Improvisation Effect: Continuously increases Esprit Gauge while in combat Duration: 15s The speed at which the gauge increases varies with the number of nearby party members. Furthermore, HP recovery via healing actions for self and nearby party members is increased by 10%. Effect ends upon using another action or moving (including facing a different direction). Cancels auto-attack upon execution.
        1827, Improvisation, Improvisation, Dancing to the beat of your own drum. Accumulates <UIForeground(506)><UIGlow(507)>Esprit</UIGlow></UIForeground> while dancing in combat.
        1828, Improvisation, Improvisation, Healing magic potency is increased.
        """
        id = 16014
        name = {"Improvisation", "即兴表演"}

    class CuringWaltz(ActionBase):
        """
        Restores own HP and the HP of all nearby party members. Cure Potency: 300 Additional Effect: Party member designated as your Dance Partner will also heal self and nearby party members
        """
        id = 16015
        name = {"Curing Waltz", "治疗之华尔兹"}

    class SingleStandardFinish(ActionBase):
        """
        Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies. 0 steps: 500 1 step: 750 2 steps: 1,000 (source.job==38?(source.level>=76?Step Bonus: Grants Standard Finish and Esprit to self and party member designated as your Dance Partner:Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner):Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner) Damage bonus of Standard Finish varies with number of successful steps. 1 step: 2% 2 steps: 5% Duration: 60s Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions. ※This action cannot be assigned to a hotbar.
        """
        id = 16191
        name = {"Single Standard Finish", "单色标准舞步结束"}

    class DoubleStandardFinish(ActionBase):
        """
        Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies. 0 steps: 500 1 step: 750 2 steps: 1,000 (source.job==38?(source.level>=76?Step Bonus: Grants Standard Finish and Esprit to self and party member designated as your Dance Partner:Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner):Step Bonus: Grants Standard Finish to self and party member designated as your Dance Partner) Damage bonus of Standard Finish varies with number of successful steps. 1 step: 2% 2 steps: 5% Duration: 60s Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions. ※This action cannot be assigned to a hotbar.
        """
        id = 16192
        name = {"Double Standard Finish", "双色标准舞步结束"}

    class SingleTechnicalFinish(ActionBase):
        """
        Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies. 0 steps: 500 1 step: 750 2 steps: 1,000 3 steps: 1,250 4 steps: 1,500  (source.job==38?(source.level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members) Damage bonus of Technical Finish varies with number of successful steps. 1 step: 1% 2 steps: 2% 3 steps: 3% 4 steps: 5% Duration: 20s Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions. ※This action cannot be assigned to a hotbar.
        """
        id = 16193
        name = {"Single Technical Finish", "单色技巧舞步结束"}

    class DoubleTechnicalFinish(ActionBase):
        """
        Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies. 0 steps: 500 1 step: 750 2 steps: 1,000 3 steps: 1,250 4 steps: 1,500  (source.job==38?(source.level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members) Damage bonus of Technical Finish varies with number of successful steps. 1 step: 1% 2 steps: 2% 3 steps: 3% 4 steps: 5% Duration: 20s Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions. ※This action cannot be assigned to a hotbar.
        """
        id = 16194
        name = {"Double Technical Finish", "双色技巧舞步结束"}

    class TripleTechnicalFinish(ActionBase):
        """
        Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies. 0 steps: 500 1 step: 750 2 steps: 1,000 3 steps: 1,250 4 steps: 1,500  (source.job==38?(source.level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members) Damage bonus of Technical Finish varies with number of successful steps. 1 step: 1% 2 steps: 2% 3 steps: 3% 4 steps: 5% Duration: 20s Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions. ※This action cannot be assigned to a hotbar.
        """
        id = 16195
        name = {"Triple Technical Finish", "三色技巧舞步结束"}

    class QuadrupleTechnicalFinish(ActionBase):
        """
        Delivers an attack to all nearby enemies. Potency varies with number of successful steps, dealing full potency for the first enemy, and 75% less for all remaining enemies. 0 steps: 500 1 step: 750 2 steps: 1,000 3 steps: 1,250 4 steps: 1,500  (source.job==38?(source.level>=76?Step Bonus: Grants Technical Finish and Esprit to self and party members:Step Bonus: Grants Technical Finish to self and party members):Step Bonus: Grants Technical Finish to self and party members) Damage bonus of Technical Finish varies with number of successful steps. 1 step: 1% 2 steps: 2% 3 steps: 3% 4 steps: 5% Duration: 20s Triggers the cooldown of weaponskills, step actions, and finish actions upon execution. Cannot be executed during the cooldown of weaponskills, step actions, or finish actions. ※This action cannot be assigned to a hotbar.
        """
        id = 16196
        name = {"Quadruple Technical Finish", "四色技巧舞步结束"}

    class Ending(ActionBase):
        """
        Ends dance with your partner.
        """
        id = 18073
        name = {"Ending", "解除闭式舞姿"}
