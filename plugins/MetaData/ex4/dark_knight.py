from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class HardSlash(ActionBase):
        """
        Delivers an attack with a potency of 200.
        """
        id = 3617
        name = {"Hard Slash", "重斩"}

    class Unleash(ActionBase):
        """
        Deals unaspected damage with a potency of 150 to all nearby enemies.
        """
        id = 3621
        name = {"Unleash", "释放"}

    class SyphonStrike(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Hard Slash Combo Potency: 300 Combo Bonus: Restores MP
        """
        id = 3623
        name = {"Syphon Strike", "吸收斩"}
        combo_action = 3617

    class Unmend(ActionBase):
        """
        Deals unaspected damage with a potency of 150. Additional Effect: Increased enmity
        """
        id = 3624
        name = {"Unmend", "伤残"}

    class BloodWeapon(ActionBase):
        """
        (source.level>=66?(source.job==32?Increases Blood Gauge by 10 and restores MP:Restores MP):Restores MP) upon landing weaponskills or spells. Effect does not stack when hitting multiple targets with a single attack. Duration: 10s
        742, Blood Weapon, Blood Weapon, Absorbing MP upon landing weaponskills or spells. Enhanced Blackblood Effect: Increasing <UIForeground(500)><UIGlow(501)>Blood Gauge</UIGlow></UIForeground> upon landing weaponskills or spells.
        """
        id = 3625
        name = {"Blood Weapon", "嗜血"}

    class Grit(ActionBase):
        """
        Significantly increases enmity generation. Effect ends upon reuse.
        743, Grit, Grit, Enmity is increased.
        1397, Grit, Grit, Damage dealt and taken are reduced.
        """
        id = 3629
        name = {"Grit", "深恶痛绝"}

    class Souleater(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Syphon Strike Combo Potency: 400 Combo Bonus: Restores own HP Cure Potency: 300(source.level>=62?(source.job==32? Combo Bonus: Increases Blood Gauge by 20:):)
        """
        id = 3632
        name = {"Souleater", "噬魂斩"}
        combo_action = 3623

    class DarkMind(ActionBase):
        """
        Reduces magic vulnerability by 20%. Duration: 10s
        746, Dark Mind, Dark Mind, Magic damage taken is reduced.
        """
        id = 3634
        name = {"Dark Mind", "弃明投暗"}

    class ShadowWall(ActionBase):
        """
        Reduces damage taken by 30%. Duration: 15s
        747, Shadow Wall, Shadow Wall, Damage taken is reduced.
        """
        id = 3636
        name = {"Shadow Wall", "暗影墙"}

    class LivingDead(ActionBase):
        """
        Grants the effect of Living Dead. When HP is reduced to 0 while under the effect of Living Dead, instead of becoming KO'd, your status will change to Walking Dead. Living Dead Duration: 10s While under the effect of Walking Dead, most attacks will not lower your HP below 1. If, before the Walking Dead timer runs out, HP is 100% restored, the effect will fade. If 100% is not restored, you will be KO'd. Walking Dead Duration: 10s
        810, Living Dead, Living Dead, Unable to be KO'd by most attacks. Status changed to <UIForeground(506)><UIGlow(507)>Walking Dead</UIGlow></UIForeground> in most cases when HP is reduced to 0.
        """
        id = 3638
        name = {"Living Dead", "行尸走肉"}

    class SaltedEarth(ActionBase):
        """
        Creates a patch of salted earth, dealing unaspected damage with a potency of 60 to any enemies who enter. Duration: 15s
        749, Salted Earth, Salted Earth, The ground is rendered void of all life, dealing unaspected damage to any who tread upon it.
        """
        id = 3639
        name = {"Salted Earth", "腐秽大地"}

    class Plunge(ActionBase):
        """
        Delivers a jumping attack with a potency of 200. (source.job==32?(source.level>=78?Maximum Charges: 2 :):)Cannot be executed while bound.
        """
        id = 3640
        name = {"Plunge", "跳斩"}

    class AbyssalDrain(ActionBase):
        """
        Deals unaspected damage with a potency of 200 to target and all enemies nearby it. Additional Effect: Restores own HP Cure Potency: 200
        """
        id = 3641
        name = {"Abyssal Drain", "吸血深渊"}

    class CarveAndSpit(ActionBase):
        """
        Delivers a threefold attack with a potency of 450. Additional Effect: Restores MP
        """
        id = 3643
        name = {"Carve and Spit", "精雕怒斩"}

    class Delirium(ActionBase):
        """
        Allows the execution of Quietus and Bloodspiller without cost, restoring MP when landing either weaponskill. Duration: 10s
        748, Delirium, Delirium, Intelligence is reduced.
        1972, Delirium, Delirium, Blackblood cost for <UIForeground(500)><UIGlow(501)>Bloodspiller</UIGlow></UIForeground> and <UIForeground(500)><UIGlow(501)>Quietus</UIGlow></UIForeground> is nullified.
        1996, Delirium, Delirium, Blackblood cost is nullified.
        """
        id = 7390
        name = {"Delirium", "血乱"}

    class Quietus(ActionBase):
        """
        Delivers an attack with a potency of 210 to all nearby enemies. Blood Gauge Cost: 50
        """
        id = 7391
        name = {"Quietus", "寂灭"}

    class Bloodspiller(ActionBase):
        """
        Delivers an attack with a potency of 600. Blood Gauge Cost: 50
        """
        id = 7392
        name = {"Bloodspiller", "血溅"}

    class TheBlackestNight(ActionBase):
        """
        Creates a barrier around target that absorbs damage totaling 25% of target's maximum HP. Duration: 7s Grants Dark Arts when barrier is completely absorbed. Dark Arts Effect: Consume Dark Arts instead of MP to execute (source.job==32?(source.level>=74?Edge of Shadow or Flood of Shadow:Edge of Darkness or Flood of Darkness):Edge of Darkness or Flood of Darkness)
        """
        id = 7393
        name = {"The Blackest Night", "至黑之夜"}

    class FloodOfDarkness(ActionBase):
        """
        Deals unaspected damage with a potency of 250 to all enemies in a straight line before you. Additional Effect: Grants Darkside, increasing damage dealt by 10% Duration: 30s Extends Darkside duration by 30s to a maximum of 60s. Shares a recast timer with Edge of Darkness.
        """
        id = 16466
        name = {"Flood of Darkness", "暗黑波动"}

    class EdgeOfDarkness(ActionBase):
        """
        Deals unaspected damage with a potency of 350. Additional Effect: Grants Darkside, increasing damage dealt by 10% Duration: 30s Extends Darkside duration by 30s to a maximum of 60s. Shares a recast timer with Flood of Darkness.
        """
        id = 16467
        name = {"Edge of Darkness", "暗黑锋"}

    class StalwartSoul(ActionBase):
        """
        Deals unaspected damage with a potency of 100 to all nearby enemies. Combo Action: Unleash Combo Potency: 160 Combo Bonus: Restores MP Combo Bonus: Increases Blood Gauge by 20
        """
        id = 16468
        name = {"Stalwart Soul", "刚魂"}
        combo_action = 3621

    class FloodOfShadow(ActionBase):
        """
        Deals unaspected damage with a potency of 300 to all enemies in a straight line before you. Additional Effect: Grants Darkside, increasing damage dealt by 10% Duration: 30s Extends Darkside duration by 30s to a maximum of 60s. Shares a recast timer with Edge of Shadow.
        2170, Flood of Shadow, Flood of Shadow, HP recovery via healing actions is reduced.
        """
        id = 16469
        name = {"Flood of Shadow", "暗影波动"}

    class EdgeOfShadow(ActionBase):
        """
        Deals unaspected damage with a potency of 500. Additional Effect: Grants Darkside, increasing damage dealt by 10% Duration: 30s Extends Darkside duration by 30s to a maximum of 60s. Shares a recast timer with Flood of Shadow.
        2102, Edge of Shadow, Edge of Shadow, HP recovery is reduced.
        """
        id = 16470
        name = {"Edge of Shadow", "暗影锋"}

    class DarkMissionary(ActionBase):
        """
        Reduces magic damage taken by self and nearby party members by 10%. Duration: 15s
        1894, Dark Missionary, Dark Missionary, Magic damage taken is reduced.
        2171, Dark Missionary, Dark Missionary, Damage taken is reduced while HP recovered via healing actions is increased.
        """
        id = 16471
        name = {"Dark Missionary", "暗黑布道"}

    class LivingShadow(ActionBase):
        """
        Conjure a simulacrum of your darkside to fight alongside you. Simulacrum Attack Potency: 300 Duration: 24s Blood Gauge Cost: 50
        """
        id = 16472
        name = {"Living Shadow", "掠影示现"}
