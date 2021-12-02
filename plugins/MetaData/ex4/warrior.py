from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class HeavySwing(ActionBase):
        """
        Delivers an attack with a potency of 200.
        """
        id = 31
        name = {"Heavy Swing", "重劈"}

    class Maim(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Heavy Swing Combo Potency: 320(source.level>=30?(source.job==21?(source.job==21?(source.level>=35? Combo Bonus: Increases Beast Gauge by 10:):):):)
        85, Maim, Maim, Damage dealt is increased.
        """
        id = 37
        name = {"Maim", "凶残裂"}
        combo_action = 31

    class Berserk(ActionBase):
        """
        Guarantees that all attacks are critical and direct hits. Duration: 10s(source.level>=50?(source.job==3? Additional Effect: Extends Storm's Eye duration by 15s to a maximum of 60s:(source.job==21? Additional Effect: Extends Storm's Eye duration by 15s to a maximum of 60s:)):)
        86, Berserk, Berserk, All attacks are both critical and direct hits.
        """
        id = 38
        name = {"Berserk", "狂暴"}

    class ThrillOfBattle(ActionBase):
        """
        Increases maximum HP by 20% and restores the amount increased. (source.job==21?(source.level>=78?Additional Effect: Increases HP recovery via healing actions on self by 20% :):)Duration: 10s
        87, Thrill of Battle, Thrill of Battle, Maximum HP is increased. Enhanced Thrill of Battle Effect: HP recovery via healing actions is increased.
        """
        id = 40
        name = {"Thrill of Battle", "战栗"}

    class Overpower(ActionBase):
        """
        Delivers an attack with a potency of 130 to all enemies in a cone before you.
        """
        id = 41
        name = {"Overpower", "超压斧"}

    class StormsPath(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Maim Combo Potency: 420 Combo Bonus: Restores own HP Cure Potency: 250(source.level>=30?(source.job==21?(source.job==21?(source.level>=35? Combo Bonus: Increases Beast Gauge by 20:):):):)
        408, Storm's Path, Storm's Path, Damage dealt is reduced.
        """
        id = 42
        name = {"Storm's Path", "暴风斩"}
        combo_action = 37

    class Holmgang(ActionBase):
        """
        Brace yourself for an enemy onslaught, preventing most attacks from reducing your HP to less than 1. Duration: 8s When a target is selected, halts their movement with chains.
        88, Holmgang, Holmgang, Unable to move until effect fades.
        409, Holmgang, Holmgang, Most attacks cannot reduce your HP to less than 1.
        1304, Holmgang, Holmgang, Unable to move until effect fades. Most attacks cannot reduce your HP to less than 1.
        1305, Holmgang, Holmgang, Unable to move until effect fades.
        """
        id = 43
        name = {"Holmgang", "死斗"}

    class Vengeance(ActionBase):
        """
        Reduces damage taken by 30% and delivers an attack with a potency of 55 every time you suffer physical damage. Duration: 15s
        89, Vengeance, Vengeance, Inflicting a portion of sustained damage back to its source.
        """
        id = 44
        name = {"Vengeance", "复仇"}

    class StormsEye(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Maim Combo Potency: 420 Combo Bonus: Increases damage dealt by 10% Duration: 30s Extends Storm's Eye duration by 30s to a maximum of 60s.(source.level>=30?(source.job==21? Combo Bonus: Increases Beast Gauge by 10:):)
        90, Storm's Eye, Storm's Eye, Damage dealt is increased.
        """
        id = 45
        name = {"Storm's Eye", "暴风碎"}
        combo_action = 37

    class Tomahawk(ActionBase):
        """
        Delivers a ranged attack with a potency of 140. Additional Effect: Increased enmity
        """
        id = 46
        name = {"Tomahawk", "飞斧"}

    class Defiance(ActionBase):
        """
        Significantly increases enmity generation. Effect ends upon reuse.
        91, Defiance, Defiance, Enmity is increased.
        1396, Defiance, Defiance, Damage dealt and taken are reduced.
        """
        id = 48
        name = {"Defiance", "守护"}

    class InnerBeast(ActionBase):
        """
        Delivers an attack with a potency of 350. Beast Gauge Cost: 50
        411, Inner Beast, Inner Beast, Damage taken is reduced.
        1398, Inner Beast, Inner Beast, Damage taken is reduced.
        """
        id = 49
        name = {"Inner Beast", "原初之魂"}

    class SteelCyclone(ActionBase):
        """
        Delivers an attack with a potency of 220 to all nearby enemies. Beast Gauge Cost: 50
        """
        id = 51
        name = {"Steel Cyclone", "钢铁旋风"}

    class Infuriate(ActionBase):
        """
        Increases Beast Gauge by 50. (source.job==21?(source.level>=72?Additional Effect: Grants Nascent Chaos Duration: 30s :):)Maximum Charges: 2 Can only be executed while in combat.
        """
        id = 52
        name = {"Infuriate", "战嚎"}

    class FellCleave(ActionBase):
        """
        Delivers an attack with a potency of 590. Beast Gauge Cost: 50(source.job==21?(source.level>=80? ※Action changes to Inner Chaos while under the effect of Nascent Chaos.:):)
        """
        id = 3549
        name = {"Fell Cleave", "裂石飞环"}

    class Decimate(ActionBase):
        """
        Delivers an attack to all nearby enemies with a potency of 250. Beast Gauge Cost: 50(source.job==21?(source.level>=72? ※Action changes to Chaotic Cyclone while under the effect of Nascent Chaos.:):)
        """
        id = 3550
        name = {"Decimate", "地毁人亡"}

    class RawIntuition(ActionBase):
        """
        Reduces damage taken by 20%. Duration: 6s(source.job==21?(source.level>=76? Shares a recast timer with Nascent Flash.:):)
        735, Raw Intuition, Raw Intuition, Damage taken is reduced.
        """
        id = 3551
        name = {"Raw Intuition", "原初的直觉"}

    class Equilibrium(ActionBase):
        """
        Restores own HP. Cure Potency: 1,200
        """
        id = 3552
        name = {"Equilibrium", "泰然自若"}

    class Onslaught(ActionBase):
        """
        Rushes target and delivers an attack with a potency of 100. Beast Gauge Cost: 20 Cannot be executed while bound.
        """
        id = 7386
        name = {"Onslaught", "猛攻"}

    class Upheaval(ActionBase):
        """
        Delivers an attack with a potency of 450. Beast Gauge Cost: 20
        """
        id = 7387
        name = {"Upheaval", "动乱"}

    class ShakeItOff(ActionBase):
        """
        Creates a barrier around self and all nearby party members that absorbs damage totaling 15% of maximum HP. Dispels Thrill of Battle, Vengeance, and Raw Intuition, increasing damage absorbed by 2% for each effect removed.  Duration: 15s
        1457, Shake It Off, Shake It Off, A highly effective defensive maneuver is nullifying damage.
        1993, Shake It Off, Shake It Off, A barrier is preventing damage.
        """
        id = 7388
        name = {"Shake It Off", "摆脱"}

    class InnerRelease(ActionBase):
        """
        Allows the use of Beast Gauge actions without cost and nullifies Stun, Sleep, Bind, Heavy, and most knockback and draw-in effects. Additional Effect: Guarantees that all attacks are critical and direct hits Duration: 10s Additional Effect: Extends Storm's Eye duration by 15s to a maximum of 60s
        1177, Inner Release, Inner Release, <UIForeground(500)><UIGlow(501)>Beast Gauge</UIGlow></UIForeground> consumption is reduced to 0. All attacks are both critical and direct hits. All <UIForeground(506)><UIGlow(507)>Stun</UIGlow></UIForeground>, <UIForeground(506)><UIGlow(507)>Sleep</UIGlow></UIForeground>, <UIForeground(506)><UIGlow(507)>Bind</UIGlow></UIForeground>, <UIForeground(506)><UIGlow(507)>Heavy</UIGlow></UIForeground>, and most knockback and draw-in effects are nullified.
        1303, Inner Release, Inner Release, <UIForeground(500)><UIGlow(501)>Beast Gauge</UIGlow></UIForeground> consumption is reduced to 0. All <UIForeground(506)><UIGlow(507)>Stun</UIGlow></UIForeground>, <UIForeground(506)><UIGlow(507)>Sleep</UIGlow></UIForeground>, <UIForeground(506)><UIGlow(507)>Bind</UIGlow></UIForeground>, <UIForeground(506)><UIGlow(507)>Heavy</UIGlow></UIForeground>, <UIForeground(506)><UIGlow(507)>Silence</UIGlow></UIForeground>, knockback, and draw-in effects are nullified.
        """
        id = 7389
        name = {"Inner Release", "原初的解放"}

    class MythrilTempest(ActionBase):
        """
        Delivers an attack with a potency of 100 to all nearby enemies. Combo Action: Overpower Combo Potency: 200(source.level>=50?(source.job==3? Combo Bonus: Extends Storm's Eye duration by 30s to a maximum of 60s:(source.job==21? Combo Bonus: Extends Storm's Eye duration by 30s to a maximum of 60s:)):)(source.job==21?(source.level>=74? Combo Bonus: Increases Beast Gauge by 20:):)
        """
        id = 16462
        name = {"Mythril Tempest", "秘银暴风"}
        combo_action = 41

    class ChaoticCyclone(ActionBase):
        """
        Delivers a critical direct hit with a potency of 400 to all nearby enemies. Additional Effect: Reduces the recast time of Infuriate by 5 seconds Beast Gauge Cost: 50 Can only be executed while under the effect of Nascent Chaos. Effect fades upon execution. ※This action cannot be assigned to a hotbar.
        2078, Chaotic Cyclone, Chaotic Cyclone, Damage taken is increased.
        """
        id = 16463
        name = {"Chaotic Cyclone", "混沌旋风"}

    class NascentFlash(ActionBase):
        """
        Grants the effect of Nascent Flash. Also grants target party member Nascent Glint. Nascent Flash Effect: Absorbs damage dealt as HP Nascent Glint Effect: Restores HP equaling 50% of that recovered by Nascent Flash while also reducing damage taken by 10% Duration: 6s Shares a recast timer with Raw Intuition.
        1857, Nascent Flash, Nascent Flash, Absorbing HP with each physical attack delivered.
        2061, Nascent Flash, Nascent Flash, Absorbing HP with each physical attack delivered. Damage taken is also reduced.
        2227, Nascent Flash, Nascent Flash, Absorbing HP with each physical attack delivered.
        """
        id = 16464
        name = {"Nascent Flash", "原初的勇猛"}

    class InnerChaos(ActionBase):
        """
        Delivers a critical direct hit with a potency of 920. Additional Effect: Reduces the recast time of Infuriate by 5 seconds Beast Gauge Cost: 50 Can only be executed while under the effect of Nascent Chaos. Effect fades upon execution. ※This action cannot be assigned to a hotbar.
        2077, Inner Chaos, Inner Chaos, Damage taken is increased.
        """
        id = 16465
        name = {"Inner Chaos", "狂魂"}
