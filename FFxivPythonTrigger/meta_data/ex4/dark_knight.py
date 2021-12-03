from ..base import *


class Status:
    class ShadowWall(StatusBase):
        """
Reduces damage taken by 30%.
Duration: 15s
    747, Shadow Wall, Damage taken is reduced.
        """
        id = 747
        name = {'暗影墙', 'Shadow Wall'}
        taken_damage_modify = 0.7

    class DarkMind(StatusBase):
        """
Reduces magic vulnerability by 20%.
Duration: 10s
    746, Dark Mind, Magic damage taken is reduced.
        """
        id = 746
        name = {'Dark Mind', '弃明投暗'}
        taken_damage_modify = 0.8
        modify_type = magic

    class SaltedEarth(StatusBase):
        """
Creates a patch of salted earth at your feet, dealing unaspected damage with a potency of 50 to any enemies who enter.
Duration: 15s(source.job==32?(source.level>=86?
※Action changes to Salt and Darkness upon execution.:):)
    749, Salted Earth, The ground is rendered void of all life, dealing unaspected damage to any who tread upon it.
        """
        id = 749
        name = {'腐秽大地', 'Salted Earth'}
        damage_potency = 50
        is_area_status = True

    class DarkMissionary(StatusBase):
        """
Reduces magic damage taken by self and nearby party members by 10%.
Duration: 15s
    2171, Dark Missionary, Damage taken is reduced while HP recovered via healing actions is increased.
    1894, Dark Missionary, Magic damage taken is reduced.
        """
        id = 1894
        name = {'Dark Missionary', '暗黑布道'}
        taken_damage_modify = 0.9
        modify_type = magic

    class Oblation(StatusBase):
        """
Reduces damage taken by a party member or self by 10%.
Duration: 10s
Maximum Charges: 2
        """
        id = 2682
        name = {'Oblation'}
        taken_damage_modify = 0.9


class Actions:
    class HardSlash(ActionBase):
        """
Delivers an attack with a potency of (source.job==32?(source.level>=84?170:150):150).
        """
        id = 3617
        name = {'重斩', 'Hard Slash'}
        attack_type = physic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 170 if source.job == 'DarkKnight' and source.level >= 84 else 150

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
        attack_type = physic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            if source.job == 'DarkKnight' and source.level >= 84:
                self.damage_potency = 120
                self.combo_potency = 260
            else:
                self.damage_potency = 100
                self.combo_potency = 240

    class Unleash(ActionBase):
        """
Deals unaspected damage with a potency of 120 to all nearby enemies.
        """
        id = 3621
        name = {'Unleash', '释放'}
        attack_type = magic
        damage_potency = 120

    class Grit(ActionBase):
        """
Significantly increases enmity generation.
Effect ends upon reuse.
>> 1397, Grit, Damage dealt and taken are reduced.
>> 743, Grit, Enmity is increased.
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
        attack_type = magic
        damage_potency = 150

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
        attack_type = physic
        cure_potency = 300

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            if source.job == 'DarkKnight' and source.level >= 84:
                self.damage_potency = 120
                self.combo_potency = 340
            else:
                self.damage_potency = 100
                self.combo_potency = 320

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
        attack_type = magic
        damage_potency = 130

    class BloodWeapon(ActionBase):
        """
(source.level>=66?(source.job==32?Increases Blood Gauge by 10 and restores MP:Restores MP):Restores MP) upon landing weaponskills or spells.
Effect does not stack when hitting multiple targets with a single attack.
Duration: 10s
>> 742, Blood Weapon, Absorbing MP upon landing weaponskills or spells.
Enhanced Blackblood Effect: Increasing Blood Gauge upon landing weaponskills or spells.
        """
        id = 3625
        name = {'Blood Weapon', '嗜血'}

    class ShadowWall(ActionBase):
        """
Reduces damage taken by 30%.
Duration: 15s
>> 747, Shadow Wall, Damage taken is reduced.
        """
        id = 3636
        name = {'暗影墙', 'Shadow Wall'}
        status_to_target = Status.ShadowWall

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
        attack_type = magic
        damage_potency = 300

    class DarkMind(ActionBase):
        """
Reduces magic vulnerability by 20%.
Duration: 10s
>> 746, Dark Mind, Magic damage taken is reduced.
        """
        id = 3634
        name = {'Dark Mind', '弃明投暗'}
        status_to_target = Status.DarkMind

    class LivingDead(ActionBase):
        """
Grants the effect of Living Dead. When HP is reduced to 0 while under the effect of Living Dead, instead of becoming KO'd, your status will change to Walking Dead.
Living Dead Duration: 10s
While under the effect of Walking Dead, most attacks will not lower your HP below 1. If, before the Walking Dead timer runs out, HP is 100% restored, the effect will fade. If 100% is not restored, you will be KO'd.
Walking Dead Duration: 10s
>> 810, Living Dead, Unable to be KO'd by most attacks. Status changed to Walking Dead in most cases when HP is reduced to 0.
        """
        id = 3638
        name = {'行尸走肉', 'Living Dead'}

    class SaltedEarth(ActionBase):
        """
Creates a patch of salted earth at your feet, dealing unaspected damage with a potency of 50 to any enemies who enter.
Duration: 15s(source.job==32?(source.level>=86?
※Action changes to Salt and Darkness upon execution.:):)
>> 749, Salted Earth, The ground is rendered void of all life, dealing unaspected damage to any who tread upon it.
        """
        id = 3639
        name = {'腐秽大地', 'Salted Earth'}
        status_to_target = Status.SaltedEarth

    class Plunge(ActionBase):
        """
Delivers a jumping attack with a potency of 150.
(source.job==32?(source.level>=78?Maximum Charges: 2
:):)Cannot be executed while bound.
        """
        id = 3640
        name = {'跳斩', 'Plunge'}
        attack_type = physic
        damage_potency = 150

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
        attack_type = magic
        damage_potency = 150
        cure_potency = 200

    class CarveAndSpit(ActionBase):
        """
Delivers a threefold attack with a potency of 510.
Additional Effect: Restores MP
Shares a recast timer with Abyssal Drain.
        """
        id = 3643
        name = {'精雕怒斩', 'Carve and Spit'}
        attack_type = physic
        damage_potency = 510

    class Bloodspiller(ActionBase):
        """
Delivers an attack with a potency of 500.
Blood Gauge Cost: 50
        """
        id = 7392
        name = {'Bloodspiller', '血溅'}
        attack_type = physic
        damage_potency = 500

    class Quietus(ActionBase):
        """
Delivers an attack with a potency of 200 to all nearby enemies.
Blood Gauge Cost: 50
        """
        id = 7391
        name = {'寂灭', 'Quietus'}
        attack_type = physic
        damage_potency = 200

    class Delirium(ActionBase):
        """
Grants 3 stacks of Delirium, each stack allowing the execution of Quietus or Bloodspiller without Blackblood cost, restoring MP when landing either weaponskill.
Duration: 15s
>> 1972, Delirium, Blackblood cost for Bloodspiller and Quietus is nullified.
>> 748, Delirium, Intelligence is reduced.
>> 1996, Delirium, Blackblood cost is nullified.
        """
        id = 7390
        name = {'血乱', 'Delirium'}

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
        damage_potency = 100
        combo_action = 3621
        combo_potency = 140
        attack_type = magic

    class FloodOfShadow(ActionBase):
        """
Deals unaspected damage with a potency of 160 to all enemies in a straight line before you.
Additional Effect: Grants Darkside, increasing damage dealt by 10%
Duration: 30s
Extends Darkside duration by 30s to a maximum of 60s.
Shares a recast timer with Edge of Shadow.
>> 2170, Flood of Shadow, HP recovery via healing actions is reduced.
        """
        id = 16469
        name = {'暗影波动', 'Flood of Shadow'}
        attack_type = magic
        damage_potency = 160

    class EdgeOfShadow(ActionBase):
        """
Deals unaspected damage with a potency of 460.
Additional Effect: Grants Darkside, increasing damage dealt by 10%
Duration: 30s
Extends Darkside duration by 30s to a maximum of 60s.
Shares a recast timer with Flood of Shadow.
>> 2102, Edge of Shadow, HP recovery is reduced.
        """
        id = 16470
        name = {'Edge of Shadow', '暗影锋'}
        attack_type = magic
        damage_potency = 460

    class DarkMissionary(ActionBase):
        """
Reduces magic damage taken by self and nearby party members by 10%.
Duration: 15s
>> 2171, Dark Missionary, Damage taken is reduced while HP recovered via healing actions is increased.
>> 1894, Dark Missionary, Magic damage taken is reduced.
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
        name = {'掠影示现', 'Living Shadow'}

    class Oblation(ActionBase):
        """
Reduces damage taken by a party member or self by 10%.
Duration: 10s
Maximum Charges: 2
>> 2682, Oblation, Damage taken is reduced.
        """
        id = 25754
        name = {'Oblation'}
        status_to_target = Status.Oblation

    class SaltAndDarkness(ActionBase):
        """
All enemies standing in the corrupted patch of Salted Earth take additional unaspected damage with a potency of 500 for the first enemy, and 50% less for all remaining enemies.
※This action cannot be assigned to a hotbar.
        """
        id = 25755
        name = {'Salt and Darkness'}

    class Shadowbringer(ActionBase):
        """
Deals unaspected damage to all enemies in a straight line before you with a potency of 600 for the first enemy, and 50% less for all remaining enemies.
Maximum Charges: 2
Can only be executed while under the effect of Darkside.
        """
        id = 25757
        name = {'Shadowbringer'}
        attack_type = magic
        damage_potency = 600
        aoe_scale = 0.5
