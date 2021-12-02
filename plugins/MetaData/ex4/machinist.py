from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class RookAutoturret(ActionBase):
        """
        Deploys a single-target battle turret which attacks using Volley Fire, dealing damage with a potency of 80. Battery Gauge Cost: 50 Duration increases as Battery Gauge exceeds required cost at time of deployment, up to a maximum of 15 seconds. Consumes Battery Gauge upon execution. Shuts down when time expires or upon execution of Rook Overdrive. Shares a recast timer with Rook Overdrive.
        """
        id = 2864
        name = {"Rook Autoturret", "车式浮空炮塔"}

    class SplitShot(ActionBase):
        """
        Delivers an attack with a potency of 180.(source.job==31?(source.level>=30? Additional Effect: Increases Heat Gauge by 5:):)
        """
        id = 2866
        name = {"Split Shot", "分裂弹"}

    class SlugShot(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Split Shot or Heated Split Shot Combo Potency: 260(source.job==31?(source.level>=30? Combo Bonus: Increases Heat Gauge by 5:):)
        """
        id = 2868
        name = {"Slug Shot", "独头弹"}
        combo_action = 2866

    class SpreadShot(ActionBase):
        """
        Delivers an attack with a potency of 180 to all enemies in a cone before you.(source.job==31?(source.level>=30? Additional Effect: Increases Heat Gauge by 5:):)
        """
        id = 2870
        name = {"Spread Shot", "散射"}

    class HotShot(ActionBase):
        """
        Delivers an attack with a potency of 300.(source.job==31?(source.level>=40? Additional Effect: Increases Battery Gauge by 20:):) This weaponskill does not share a recast timer with any other actions.
        855, Hot Shot, Hot Shot, Physical damage dealt is increased.
        """
        id = 2872
        name = {"Hot Shot", "热弹"}

    class CleanShot(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Slug Shot or Heated Slug Shot Combo Potency: 340(source.job==31?(source.level>=30? Combo Bonus: Increases Heat Gauge by 5:):)(source.job==31?(source.level>=40? Combo Bonus: Increases Battery Gauge by 10:):)
        """
        id = 2873
        name = {"Clean Shot", "狙击弹"}
        combo_action = 2868

    class GaussRound(ActionBase):
        """
        Delivers an attack with a potency of 150. Maximum Charges: (source.job==31?(source.level>=74?3:2):2)
        """
        id = 2874
        name = {"Gauss Round", "虹吸弹"}

    class Reassemble(ActionBase):
        """
        Guarantees that next weaponskill is a critical direct hit. Duration: 5s This action does not affect damage over time effects.
        """
        id = 2876
        name = {"Reassemble", "整备"}

    class Wildfire(ActionBase):
        """
        Covers target's body in a slow-burning pitch. Action is changed to Detonator for the duration of the effect. Deals damage when time expires or upon executing Detonator. Potency is increased by (source.job==31?(source.level>=78?200:150):150) for each of your own weaponskills you land prior to the end of the effect. Duration: 10s
        861, Wildfire, Wildfire, Damage is being accumulated with each weaponskill landed by the machinist who applied the effect.
        1323, Wildfire, Wildfire, A portion of damage dealt is being stored.
        1946, Wildfire, Wildfire, Currently afflicting an enemy with <UIForeground(506)><UIGlow(507)>Wildfire</UIGlow></UIForeground>.
        """
        id = 2878
        name = {"Wildfire", "野火"}

    class Ricochet(ActionBase):
        """
        Deals damage to all nearby enemies with a potency of 150 for the first enemy, and 50% less for all remaining enemies. Maximum Charges: (source.job==31?(source.level>=74?3:2):2)
        """
        id = 2890
        name = {"Ricochet", "弹射"}

    class HeatBlast(ActionBase):
        """
        Delivers an attack with a potency of 220. Additional Effect: Reduces the recast time of both Gauss Round and Ricochet by 15s Can only be executed when firearm is Overheated. Recast timer cannot be affected by status effects or gear attributes.
        """
        id = 7410
        name = {"Heat Blast", "热冲击"}

    class HeatedSplitShot(ActionBase):
        """
        Delivers an attack with a potency of 220.(source.job==31?(source.level>=30? Additional Effect: Increases Heat Gauge by 5:):)
        """
        id = 7411
        name = {"Heated Split Shot", "热分裂弹"}

    class HeatedSlugShot(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Heated Split Shot Combo Potency: 330(source.job==31?(source.level>=30? Combo Bonus: Increases Heat Gauge by 5:):)
        """
        id = 7412
        name = {"Heated Slug Shot", "热独头弹"}
        combo_action = 2866

    class HeatedCleanShot(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Heated Slug Shot Combo Potency: 440(source.job==31?(source.level>=30? Combo Bonus: Increases Heat Gauge by 5:):)(source.job==31?(source.level>=40? Combo Bonus: Increases Battery Gauge by 10:):)
        """
        id = 7413
        name = {"Heated Clean Shot", "热狙击弹"}
        combo_action = 2868

    class BarrelStabilizer(ActionBase):
        """
        Increases Heat Gauge by 50. Can only be executed while in combat.
        """
        id = 7414
        name = {"Barrel Stabilizer", "枪管加热"}

    class RookOverdrive(ActionBase):
        """
        Orders the rook autoturret to use Rook Overload. Rook Overload Potency: 400 Potency increases as Battery Gauge exceeds required cost at time of deployment. The rook autoturret shuts down after execution. If this action is not used manually while the rook autoturret is active, it will be triggered automatically immediately before shutting down. Shares a recast timer with Rook Autoturret.
        """
        id = 7415
        name = {"Rook Overdrive", "超档车式炮塔"}

    class RookOverload(ActionBase):
        """
        Delivers an attack with a potency of 400. Potency increases as Battery Gauge exceeds required cost at time of deployment. The rook autoturret shuts down after execution. If this action is not used manually while the rook autoturret is active, it will be triggered automatically immediately before shutting down. ※This action cannot be assigned to a hotbar.
        """
        id = 7416
        name = {"Rook Overload", "超负荷车式炮塔"}

    class Flamethrower(ActionBase):
        """
        Delivers damage over time to all enemies in a cone before you. Potency: 100 Duration: 10s Effect ends upon using another action or moving (including facing a different direction). Cancels auto-attack upon execution. Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.
        1205, Flamethrower, Flamethrower, Emitting a gout of searing flames in a cone before you, dealing damage over time.
        1455, Flamethrower, Flamethrower, Emitting a gout of searing flames in a cone, dealing damage over time.
        """
        id = 7418
        name = {"Flamethrower", "火焰喷射器"}

    class AutoCrossbow(ActionBase):
        """
        Delivers an attack with a potency of 180 to all enemies in a cone before you. Can only be executed when firearm is Overheated. Recast timer cannot be affected by status effects or gear attributes.
        """
        id = 16497
        name = {"Auto Crossbow", "自动弩"}

    class Drill(ActionBase):
        """
        Delivers an attack with a potency of 700. (source.job==31?(source.level>=72?Shares a recast timer with Bioblaster.:This action does not share a recast timer with any other actions.):This action does not share a recast timer with any other actions.)
        """
        id = 16498
        name = {"Drill", "钻头"}

    class Bioblaster(ActionBase):
        """
        Delivers an attack with a potency of 60 to all enemies in a cone before you. Additional Effect: Damage over time Potency: 60 Duration: 15s Shares a recast timer with Drill.
        1866, Bioblaster, Bioblaster, Sustaining damage over time.
        2019, Bioblaster, Bioblaster, Damage taken is increased.
        """
        id = 16499
        name = {"Bioblaster", "毒菌冲击"}

    class AirAnchor(ActionBase):
        """
        Delivers an attack with a potency of 700. Additional Effect: Increases Battery Gauge by 20 This action does not share a recast timer with any other actions.
        """
        id = 16500
        name = {"Air Anchor", "空气锚"}

    class AutomatonQueen(ActionBase):
        """
        Deploys an Automaton Queen to fight at your side. Battery Gauge Cost: 50 Duration increases as Battery Gauge exceeds minimum cost at time of deployment, up to a maximum of 20 seconds. Consumes Battery Gauge upon execution. Shuts down when time expires or upon execution of Queen Overdrive. Shares a recast timer with Queen Overdrive.
        """
        id = 16501
        name = {"Automaton Queen", "后式自走人偶"}

    class QueenOverdrive(ActionBase):
        """
        Orders the Automaton Queen to use Pile Bunker. Pile Bunker Potency: 800 Potency increases as Battery Gauge exceeds required cost at time of deployment. The Automaton Queen shuts down after execution. If this action is not used manually while the Automaton Queen is active, it will be triggered automatically immediately before shutting down. Shares a recast timer with Automaton Queen.
        """
        id = 16502
        name = {"Queen Overdrive", "超档后式人偶"}

    class PileBunker(ActionBase):
        """
        Delivers an attack with a potency of 800. Potency increases as Battery Gauge exceeds required cost at time of deployment. The Automaton Queen shuts down after execution. If this action is not used manually while the Automaton Queen is active, it will be triggered automatically immediately before shutting down. ※This action cannot be assigned to a hotbar.
        """
        id = 16503
        name = {"Pile Bunker", "打桩枪"}

    class ArmPunch(ActionBase):
        """
        Delivers an attack with a potency of 150. ※This action cannot be assigned to a hotbar.
        """
        id = 16504
        name = {"Arm Punch", "铁臂拳"}

    class Detonator(ActionBase):
        """
        Ends the effect of Wildfire, dealing damage to the target. ※This action cannot be assigned to a hotbar.
        """
        id = 16766
        name = {"Detonator", "起爆"}

    class Tactician(ActionBase):
        """
        Reduces damage taken by self and nearby party members by 10%. Duration: 15s Effect cannot be stacked with bard's Troubadour or dancer's Shield Samba.
        1197, Tactician, Tactician, Gradually regenerating TP.
        1951, Tactician, Tactician, Damage taken is reduced.
        2177, Tactician, Tactician, Damage taken is reduced.
        """
        id = 16889
        name = {"Tactician", "策动"}

    class RollerDash(ActionBase):
        """
        Rushes target and delivers an attack with a potency of 300. ※This action cannot be assigned to a hotbar.
        """
        id = 17206
        name = {"Roller Dash", "滚轮冲"}

    class Hypercharge(ActionBase):
        """
        Releases the energy building in your firearm, causing it to become Overheated, increasing the potency of single-target weaponskills by 20. Duration: 8s Heat Gauge Cost: 50 Overheated effect only applicable to machinist job actions.
        688, Hypercharge, Hypercharge, Battle turret is overcharged.
        """
        id = 17209
        name = {"Hypercharge", "超荷"}
