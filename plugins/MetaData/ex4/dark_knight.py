from ..base import *


class Actions:

    class HardSlash(ActionBase):
        """
Delivers an attack with a potency of (source.job==32?(source.level>=84?170:150):150).
        """
        id = 3617
        name = {'重斩', 'Hard Slash'}

    class SyphonStrike(ActionBase):
        """
Delivers an attack with a potency of (source.job==32?(source.level>=84?120:100):100).
Combo Action: Hard Slash
Combo Potency: (source.job==32?(source.level>=84?260:240):240)
Combo Bonus: Restores MP
        """
        id = 3623
        name = {'吸收斩', 'Syphon Strike'}
        combo_action = 3617

    class Unleash(ActionBase):
        """
Deals unaspected damage with a potency of 120 to all nearby enemies.
        """
        id = 3621
        name = {'Unleash', '释放'}

    class Grit(ActionBase):
        """
Significantly increases enmity generation.
Effect ends upon reuse.
    1397, Grit, Damage dealt and taken are reduced.
    743, Grit, Enmity is increased.
        """
        id = 3629
        name = {'Grit', '深恶痛绝'}

    class Unmend(ActionBase):
        """
Deals unaspected damage with a potency of 150.
Additional Effect: Increased enmity(source.job==32?(source.level>=84?
Additional Effect: Reduces the recast time of Plunge by 5 seconds:):)
        """
        id = 3624
        name = {'伤残', 'Unmend'}

    class Souleater(ActionBase):
        """
Delivers an attack with a potency of (source.job==32?(source.level>=84?120:100):100).
Combo Action: Syphon Strike
Combo Potency: (source.job==32?(source.level>=84?340:320):320)
Combo Bonus: Restores own HP
Cure Potency: 300(source.level>=62?(source.job==32?
Combo Bonus: Increases Blood Gauge by 20:):)
        """
        id = 3632
        name = {'噬魂斩', 'Souleater'}
        combo_action = 3623

    class FloodOfDarkness(ActionBase):
        """
Deals unaspected damage with a potency of 130 to all enemies in a straight line before you.
Additional Effect: Grants Darkside, increasing damage dealt by 10%
Duration: 30s
Extends Darkside duration by 30s to a maximum of 60s.
Shares a recast timer with Edge of Darkness.
        """
        id = 16466
        name = {'暗黑波动', 'Flood of Darkness'}

    class BloodWeapon(ActionBase):
        """
(source.level>=66?(source.job==32?Increases Blood Gauge by 10 and restores MP:Restores MP):Restores MP) upon landing weaponskills or spells.
Effect does not stack when hitting multiple targets with a single attack.
Duration: 10s
    742, Blood Weapon, Absorbing MP upon landing weaponskills or spells. Enhanced Blackblood Effect: Increasing <UIForeground(500)><UIGlow(501)>Blood Gauge</UIGlow></UIForeground> upon landing weaponskills or spells.
        """
        id = 3625
        name = {'嗜血', 'Blood Weapon'}

    class ShadowWall(ActionBase):
        """
Reduces damage taken by 30%.
Duration: 15s
    747, Shadow Wall, Damage taken is reduced.
        """
        id = 3636
        name = {'暗影墙', 'Shadow Wall'}

    class EdgeOfDarkness(ActionBase):
        """
Deals unaspected damage with a potency of 300.
Additional Effect: Grants Darkside, increasing damage dealt by 10%
Duration: 30s
Extends Darkside duration by 30s to a maximum of 60s.
Shares a recast timer with Flood of Darkness.
        """
        id = 16467
        name = {'Edge of Darkness', '暗黑锋'}

    class DarkMind(ActionBase):
        """
Reduces magic vulnerability by 20%.
Duration: 10s
    746, Dark Mind, Magic damage taken is reduced.
        """
        id = 3634
        name = {'Dark Mind', '弃明投暗'}

    class LivingDead(ActionBase):
        """
Grants the effect of Living Dead. When HP is reduced to 0 while under the effect of Living Dead, instead of becoming KO'd, your status will change to Walking Dead.
Living Dead Duration: 10s
While under the effect of Walking Dead, most attacks will not lower your HP below 1. If, before the Walking Dead timer runs out, HP is 100% restored, the effect will fade. If 100% is not restored, you will be KO'd.
Walking Dead Duration: 10s
    810, Living Dead, Unable to be KO'd by most attacks. Status changed to <UIForeground(506)><UIGlow(507)>Walking Dead</UIGlow></UIForeground> in most cases when HP is reduced to 0.
        """
        id = 3638
        name = {'行尸走肉', 'Living Dead'}

    class SaltedEarth(ActionBase):
        """
Creates a patch of salted earth at your feet, dealing unaspected damage with a potency of 50 to any enemies who enter.
Duration: 15s(source.job==32?(source.level>=86?
※Action changes to Salt and Darkness upon execution.:):)
    749, Salted Earth, The ground is rendered void of all life, dealing unaspected damage to any who tread upon it.
        """
        id = 3639
        name = {'腐秽大地', 'Salted Earth'}

    class Plunge(ActionBase):
        """
Delivers a jumping attack with a potency of 150.
(source.job==32?(source.level>=78?Maximum Charges: 2
:):)Cannot be executed while bound.
        """
        id = 3640
        name = {'跳斩', 'Plunge'}

    class AbyssalDrain(ActionBase):
        """
Deals unaspected damage with a potency of 150 to target and all enemies nearby it.
Additional Effect: Restores own HP
Cure Potency: 200
Additional Effect: Restores MP
Shares a recast timer with Carve and Spit.
        """
        id = 3641
        name = {'吸血深渊', 'Abyssal Drain'}

    class CarveAndSpit(ActionBase):
        """
Delivers a threefold attack with a potency of 510.
Additional Effect: Restores MP
Shares a recast timer with Abyssal Drain.
        """
        id = 3643
        name = {'精雕怒斩', 'Carve and Spit'}

    class Bloodspiller(ActionBase):
        """
Delivers an attack with a potency of 500.
Blood Gauge Cost: 50
        """
        id = 7392
        name = {'Bloodspiller', '血溅'}

    class Quietus(ActionBase):
        """
Delivers an attack with a potency of 200 to all nearby enemies.
Blood Gauge Cost: 50
        """
        id = 7391
        name = {'寂灭', 'Quietus'}

    class Delirium(ActionBase):
        """
Grants 3 stacks of Delirium, each stack allowing the execution of Quietus or Bloodspiller without Blackblood cost, restoring MP when landing either weaponskill.
Duration: 15s
    1996, Delirium, Blackblood cost is nullified.
    1972, Delirium, Blackblood cost for <UIForeground(500)><UIGlow(501)>Bloodspiller</UIGlow></UIForeground> and <UIForeground(500)><UIGlow(501)>Quietus</UIGlow></UIForeground> is nullified.
        """
        id = 7390
        name = {'Delirium', '血乱'}

    class TheBlackestNight(ActionBase):
        """
Creates a barrier around target that absorbs damage totaling 25% of target's maximum HP.
Duration: 7s
Grants Dark Arts when barrier is completely absorbed.
Dark Arts Effect: Consume Dark Arts instead of MP to execute (source.job==32?(source.level>=74?Edge of Shadow or Flood of Shadow:Edge of Darkness or Flood of Darkness):Edge of Darkness or Flood of Darkness)
    1178, Blackest Night, An all-encompassing darkness is nullifying damage.
    1308, Blackest Night, An all-encompassing darkness is nullifying damage.
        """
        id = 7393
        name = {'The Blackest Night', '至黑之夜'}

    class StalwartSoul(ActionBase):
        """
Deals unaspected damage with a potency of 100 to all nearby enemies.
Combo Action: Unleash
Combo Potency: 140
Combo Bonus: Restores MP
Combo Bonus: Increases Blood Gauge by 20
        """
        id = 16468
        name = {'刚魂', 'Stalwart Soul'}
        combo_action = 3621

    class FloodOfShadow(ActionBase):
        """
Deals unaspected damage with a potency of 160 to all enemies in a straight line before you.
Additional Effect: Grants Darkside, increasing damage dealt by 10%
Duration: 30s
Extends Darkside duration by 30s to a maximum of 60s.
Shares a recast timer with Edge of Shadow.
    2170, Flood of Shadow, HP recovery via healing actions is reduced.
        """
        id = 16469
        name = {'暗影波动', 'Flood of Shadow'}

    class EdgeOfShadow(ActionBase):
        """
Deals unaspected damage with a potency of 460.
Additional Effect: Grants Darkside, increasing damage dealt by 10%
Duration: 30s
Extends Darkside duration by 30s to a maximum of 60s.
Shares a recast timer with Flood of Shadow.
    2102, Edge of Shadow, HP recovery is reduced.
        """
        id = 16470
        name = {'Edge of Shadow', '暗影锋'}

    class DarkMissionary(ActionBase):
        """
Reduces magic damage taken by self and nearby party members by 10%.
Duration: 15s
    2171, Dark Missionary, Damage taken is reduced while HP recovered via healing actions is increased.
    1894, Dark Missionary, Magic damage taken is reduced.
        """
        id = 16471
        name = {'Dark Missionary', '暗黑布道'}

    class LivingShadow(ActionBase):
        """
Conjure a simulacrum of your darkside to fight alongside you.
Simulacrum Attack Potency: (source.job==32?(source.level>=88?300:240):240)
Duration: 24s
Blood Gauge Cost: 50
(source.job==32?(source.level>=90?Additional Effect: Simulacrum is able to execute Shadowbringer, delivering an attack to all enemies in a straight line before it with a potency of 450 for the first enemy, and 25% less for all remaining enemies.:):)
        """
        id = 16472
        name = {'Living Shadow', '掠影示现'}
