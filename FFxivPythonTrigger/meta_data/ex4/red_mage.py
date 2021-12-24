from ..base import *


class Status:
    class Acceleration(StatusBase):
        """
Ensures the next (source.job==35?(source.level>=82?Verthunder III, Veraero III:Verthunder, Veraero):Verthunder, Veraero), or (source.job==35?(source.level>=66?Impact:Scatter):Scatter) can be cast immediately.
Duration: 20s
Additional Effect: Increases the potency of (source.job==35?(source.level>=66?Impact:Scatter):Scatter) by 50
Additional Effect: Ensures (source.job==35?(source.level>=82?Verthunder III and Veraero III:Verthunder and Veraero):Verthunder and Veraero) trigger Verfire Ready or Verstone Ready respectively(source.job==35?(source.level>=88?
Maximum Charges: 2:):)
>> 1238, Acceleration, Next (source.job==35?(source.level>=82?Verthunder III, Veraero III:Verthunder, Veraero):Verthunder, Veraero), or (source.job==35?(source.level>=66?Impact:Scatter):Scatter) can be cast immediately.
Potency of (source.job==35?(source.level>=66?Impact:Scatter):Scatter) is increased, and (source.job==35?(source.level>=82?Verthunder III and Veraero III:Verthunder and Veraero):Verthunder and Veraero) trigger Verfire Ready or Verstone Ready respectively.
        """
        id = 1238
        name = {'Acceleration', '促进'}

    class VerstoneReady(StatusBase):
        id = 1235
        name = {'Verstone Ready', '赤飞石预备'}

    class VerfireReady(StatusBase):
        id = 1234
        name = {'Verfire Ready', '赤火炎预备'}

    class EmboldenSelf(StatusBase):
        id = 1239
        name = {'Embolden(self)', '鼓励(自己)'}
        damage_modify = 1.05
        modify_type = magic

    class EmboldenParty(StatusBase):
        id = 1297  # 2282?
        name = {'Embolden(party)', '鼓励(队伍)'}
        damage_modify = 1.05

    class Manafication(StatusBase):
        id = 1971
        name = {'Manafication', '倍增'}
        damage_modify = 1.05
        modify_type = magic

    class MagickBarrier(StatusBase):
        id = 2707
        name = {'Magick Barrier'}
        taken_damage_modify = .9
        taken_cure_modify = 1.05

    class Dualcast(StatusBase):
        id = 1249
        name = {'Dualcast', '连续咏唱'}


class Actions:
    class Riposte(ActionBase):
        """
Delivers an attack with a potency of 130.(source.level>=2?(source.job==35?
Action upgraded to Enchanted Riposte if both Black Mana and White Mana are at 20 or more.:):)
        """
        id = 7504
        name = {'回刺', 'Riposte'}
        attack_type = physic
        damage_potency = 130

    class EnchantedRiposte(ActionBase):
        """
Deals unaspected damage with a potency of 220.
(source.job==35?(source.level>=68?Additional Effect: Grants a Mana Stack
:):)Balance Gauge Cost: 20 Black Mana
Balance Gauge Cost: 20 White Mana
※This action cannot be assigned to a hotbar.
        """
        id = 7527
        name = {'Enchanted Riposte', '魔回刺'}
        attack_type = magic
        damage_potency = 220

    class Jolt(ActionBase):
        """
Deals unaspected damage with a potency of 170.
Additional Effect: Increases both Black Mana and White Mana by 2
        """
        id = 7503
        name = {'摇荡', 'Jolt'}
        attack_type = magic
        damage_potency = 170

    class Verthunder(ActionBase):
        """
Deals lightning damage with a potency of (source.job==35?(source.level>=62?360:300):300).
Additional Effect: Increases Black Mana by 6(source.level>=26?(source.job==35?
Additional Effect: 50% chance of becoming Verfire Ready
Duration: 30s:):)
        """
        id = 7505
        name = {'赤闪雷', 'Verthunder'}
        attack_type = magic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 360 if source and source.job == 35 and source.level >= 62 else 300

    class CorpsACorps(ActionBase):
        """
Rushes target and delivers an attack with a potency of 130.
Maximum Charges: 2
Cannot be executed while bound.
>> 2012, Corps-a-corps, A barrier is preventing damage.
        """
        id = 7506
        name = {'Corps-a-corps', '短兵相接'}
        attack_type = physic
        damage_potency = 130

    class Veraero(ActionBase):
        """
Deals wind damage with a potency of (source.job==35?(source.level>=62?360:300):300).
Additional Effect: Increases White Mana by 6(source.level>=30?(source.job==35?
Additional Effect: 50% chance of becoming Verstone Ready
Duration: 30s:):)
        """
        id = 7507
        name = {'Veraero', '赤疾风'}
        attack_type = magic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 360 if source and source.job == 35 and source.level >= 62 else 300

    class Scatter(ActionBase):
        """
Deals unaspected damage with a potency of 120 to target and all enemies nearby it.
(source.job==35?(source.level>=50?Acceleration Potency: 170:):)
Additional Effect: Increases both Black Mana and White Mana by 3
        """
        id = 7509
        name = {'散碎', 'Scatter'}
        attack_type = magic
        damage_potency = 120

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 170 if source and source.effects.has(Status.Acceleration.id) else 120

    class VerthunderIi(ActionBase):
        """
Deals lightning damage with a potency of (source.job==35?(source.level>=84?140:(source.job==35?(source.level>=74?120:100):100)):(source.job==35?(source.level>=74?120:100):100)) to target and all enemies nearby it.
Additional Effect: Increases Black Mana by 7
        """
        id = 16524
        name = {'Verthunder II', '赤震雷'}
        attack_type = magic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            if source and source.job == 35:
                if source.level >= 84:
                    self.damage_potency = 140
                elif source.level >= 74:
                    self.damage_potency = 120
                else:
                    self.damage_potency = 100
            else:
                self.damage_potency = 100

    class VeraeroIi(ActionBase):
        """
Deals wind damage with a potency of (source.job==35?(source.level>=84?140:(source.job==35?(source.level>=74?120:100):100)):(source.job==35?(source.level>=74?120:100):100)) to target and all enemies nearby it.
Additional Effect: Increases White Mana by 7
        """
        id = 16525
        name = {'赤烈风', 'Veraero II'}
        attack_type = magic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            if source and source.job == 35:
                if source.level >= 84:
                    self.damage_potency = 140
                elif source.level >= 74:
                    self.damage_potency = 120
                else:
                    self.damage_potency = 100
            else:
                self.damage_potency = 100

    class Verfire(ActionBase):
        """
Deals fire damage with a potency of (source.job==35?(source.level>=84?330:(source.job==35?(source.level>=62?300:260):260)):(source.job==35?(source.level>=62?300:260):260)).
Additional Effect: Increases Black Mana by 5
Can only be executed while Verfire Ready is active.
        """
        id = 7510
        name = {'赤火炎', 'Verfire'}
        attack_type = magic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            if source and source.job == 35:
                if source.level >= 84:
                    self.damage_potency = 330
                elif source.level >= 62:
                    self.damage_potency = 300
                else:
                    self.damage_potency = 260
            else:
                self.damage_potency = 260

    class Verstone(ActionBase):
        """
Deals earth damage with a potency of (source.job==35?(source.level>=84?330:(source.job==35?(source.level>=62?300:260):260)):(source.job==35?(source.level>=62?300:260):260)).
Additional Effect: Increases White Mana by 5
Can only be executed while Verstone Ready is active.
        """
        id = 7511
        name = {'Verstone', '赤飞石'}
        attack_type = magic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            if source and source.job == 35:
                if source.level >= 84:
                    self.damage_potency = 330
                elif source.level >= 62:
                    self.damage_potency = 300
                else:
                    self.damage_potency = 260
            else:
                self.damage_potency = 260

    class Zwerchhau(ActionBase):
        """
Delivers an attack with a potency of 100.
Combo Action: Riposte or Enchanted Riposte
Combo Potency: 150
Action upgraded to Enchanted Zwerchhau if both Black Mana and White Mana are at 15 or more.
        """
        id = 7512
        name = {'交击斩', 'Zwerchhau'}
        combo_action = 7504
        combo_damage_potency = 150
        attack_type = physic
        damage_potency = 100

    class EnchantedZwerchhau(ActionBase):
        """
Deals unaspected damage with a potency of 100.
Combo Action: Riposte or Enchanted Riposte
Combo Potency: 290
(source.job==35?(source.level>=68?Additional Effect: Grants a Mana Stack
:):)Balance Gauge Cost: 15 Black Mana
Balance Gauge Cost: 15 White Mana
※This action cannot be assigned to a hotbar.
        """
        id = 7528
        name = {'Enchanted Zwerchhau', '魔交击斩'}
        combo_action = 7504
        combo_damage_potency = 290
        attack_type = magic
        damage_potency = 100

    class Displacement(ActionBase):
        """
Delivers an attack with a potency of (source.job==35?(source.level>=72?180:130):130).
Additional Effect: 15-yalm backstep
Maximum Charges: 2
Cannot be executed while bound.
Shares a recast timer with Engagement.
>> 2013, Displacement, Next spell cast will deal increased damage.
        """
        id = 7515
        name = {'移转', 'Displacement'}
        attack_type = physic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 180 if source and source.job == 35 and source.level >= 72 else 130

    class Engagement(ActionBase):
        """
Delivers an attack with a potency of (source.job==35?(source.level>=72?180:130):130).
Maximum Charges: 2
Shares a recast timer with Displacement.
>> 2033, Engagement, A barrier is preventing damage.
        """
        id = 16527
        name = {'Engagement', '交剑'}
        attack_type = physic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 180 if source and source.job == 35 and source.level >= 72 else 130

    class Fleche(ActionBase):
        """
Delivers an attack with a potency of 460.
        """
        id = 7517
        name = {'Fleche', '飞刺'}
        attack_type = physic
        damage_potency = 460

    class Redoublement(ActionBase):
        """
Delivers an attack with a potency of 100.
Combo Action: Zwerchhau or Enchanted Zwerchhau
Combo Potency: 230
Action upgraded to Enchanted Redoublement if both Black Mana and White Mana are at 15 or more.
        """
        id = 7516
        name = {'Redoublement', '连攻'}
        combo_action = 7512
        combo_damage_potency = 230
        attack_type = physic
        damage_potency = 100

    class Acceleration(ActionBase):
        """
Ensures the next (source.job==35?(source.level>=82?Verthunder III, Veraero III:Verthunder, Veraero):Verthunder, Veraero), or (source.job==35?(source.level>=66?Impact:Scatter):Scatter) can be cast immediately.
Duration: 20s
Additional Effect: Increases the potency of (source.job==35?(source.level>=66?Impact:Scatter):Scatter) by 50
Additional Effect: Ensures (source.job==35?(source.level>=82?Verthunder III and Veraero III:Verthunder and Veraero):Verthunder and Veraero) trigger Verfire Ready or Verstone Ready respectively(source.job==35?(source.level>=88?
Maximum Charges: 2:):)
>> 1238, Acceleration, Next (source.job==35?(source.level>=82?Verthunder III, Veraero III:Verthunder, Veraero):Verthunder, Veraero), or (source.job==35?(source.level>=66?Impact:Scatter):Scatter) can be cast immediately.
Potency of (source.job==35?(source.level>=66?Impact:Scatter):Scatter) is increased, and (source.job==35?(source.level>=82?Verthunder III and Veraero III:Verthunder and Veraero):Verthunder and Veraero) trigger Verfire Ready or Verstone Ready respectively.
        """
        id = 7518
        name = {'Acceleration', '促进'}

    class EnchantedRedoublement(ActionBase):
        """
Deals unaspected damage with a potency of 100.
Combo Action: Enchanted Zwerchhau
Combo Potency: 470
(source.job==35?(source.level>=68?Additional Effect: Grants a Mana Stack
:):)Balance Gauge Cost: 15 Black Mana
Balance Gauge Cost: 15 White Mana
※This action cannot be assigned to a hotbar.
        """
        id = 7529
        name = {'Enchanted Redoublement', '魔连攻'}
        combo_action = 7512
        combo_damage_potency = 470
        attack_type = magic
        damage_potency = 100

    class Moulinet(ActionBase):
        """
Delivers an attack with a potency of 60 to all enemies in a cone before you.
Action upgraded to Enchanted Moulinet if both Black Mana and White Mana are at 20 or more.
        """
        id = 7513
        name = {'划圆斩', 'Moulinet'}
        attack_type = physic
        damage_potency = 60

    class EnchantedMoulinet(ActionBase):
        """
Deals unaspected damage with a potency of 130 to all enemies in a cone before you.
(source.job==35?(source.level>=68?Additional Effect: Grants a Mana Stack
:):)Balance Gauge Cost: 20 Black Mana
Balance Gauge Cost: 20 White Mana
※This action cannot be assigned to a hotbar.
        """
        id = 7530
        name = {'Enchanted Moulinet', '魔划圆斩'}
        attack_type = magic
        damage_potency = 130

    class Vercure(ActionBase):
        """
Restores target's HP.
Cure Potency: 350
        """
        id = 7514
        name = {'Vercure', '赤治疗'}
        cure_potency = 350

    class ContreSixte(ActionBase):
        """
Delivers an attack with a potency of 360 to target and all enemies nearby it.
        """
        id = 7519
        name = {'六分反击', 'Contre Sixte'}
        attack_type = physic
        damage_potency = 360

    class Embolden(ActionBase):
        """
Increases own magic damage dealt by 5% and damage dealt by nearby party members by 5%.
Duration: 20s
>> 1297, Embolden, Damage dealt is increased.
>> 1239, Embolden, Magic damage dealt is increased.
>> 2282, Embolden, Damage dealt is increased.
        """
        id = 7520
        name = {'Embolden', '鼓励'}

    class Manafication(ActionBase):
        """
Increases both Black Mana and White Mana by 50.
(source.job==35?(source.level>=78?Additional Effect: Grants (source.job==35?(source.level>=90?6:5):5) stacks of Manafication
Manafication Effect: Increases magic damage dealt by 5%
Duration: 15s
:):)All combos are canceled upon execution of Manafication.
Can only be executed while in combat.
>> 1971, Manafication, Magic damage dealt is increased.
        """
        id = 7521
        name = {'倍增', 'Manafication'}

    class JoltIi(ActionBase):
        """
Deals unaspected damage with a potency of (source.job==35?(source.level>=84?310:280):280).
Additional Effect: Increases both Black Mana and White Mana by 2
        """
        id = 7524
        name = {'震荡', 'Jolt II'}
        attack_type = magic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 310 if source and source.job == 35 and source.level >= 84 else 280

    class Verraise(ActionBase):
        """
Resurrects target to a weakened state.
        """
        id = 7523
        name = {'Verraise', '赤复活'}

    class Impact(ActionBase):
        """
Deals unaspected damage with a potency of (source.job==35?(source.level>=84?210:200):200) to target and all enemies nearby it.
Acceleration Potency: (source.job==35?(source.level>=84?260:250):250)
Additional Effect: Increases both Black Mana and White Mana by 3
        """
        id = 16526
        name = {'Impact', '冲击'}
        attack_type = magic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            if source and source.job == 35:
                if source.effects.has(Status.Acceleration.id):
                    self.damage_potency = 260 if source.level >= 84 else 250
                else:
                    self.damage_potency = 210 if source.level >= 84 else 200
            else:
                self.damage_potency = 200

    class Verflare(ActionBase):
        """
Deals fire damage to target and all enemies nearby it with a potency of 580 for the first enemy, and 60% less for all remaining enemies.
Additional Effect: Increases Black Mana by 11
Additional Effect: 20% chance of becoming Verfire Ready
Duration: 30s
Chance to become Verfire Ready increases to 100% if White Mana is higher than Black Mana at time of execution.
Mana Stack Cost: 3
※This action cannot be assigned to a hotbar.
        """
        id = 7525
        name = {'赤核爆', 'Verflare'}
        attack_type = magic
        damage_potency = 580
        aoe_scale = .4

    class Verholy(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 580 for the first enemy, and 60% less for all remaining enemies.
Additional Effect: Increases White Mana by 11
Additional Effect: 20% chance of becoming Verstone Ready
Duration: 30s
Chance to become Verstone Ready increases to 100% if Black Mana is higher than White Mana at time of execution.
Mana Stack Cost: 3
※This action cannot be assigned to a hotbar.
        """
        id = 7526
        name = {'Verholy', '赤神圣'}
        attack_type = magic
        damage_potency = 580
        aoe_scale = .4

    class EnchantedReprise(ActionBase):
        """
Deals unaspected damage with a potency of (source.job==35?(source.level>=84?330:290):290).
Balance Gauge Cost: 5 Black Mana
Balance Gauge Cost: 5 White Mana
※This action cannot be assigned to a hotbar.
        """
        id = 16528
        name = {'Enchanted Reprise', '魔续斩'}
        attack_type = magic

        def __init__(self, source: 'Actor|None', target: 'Actor|None'):
            super().__init__(source, target)
            self.damage_potency = 330 if source and source.job == 35 and source.level >= 84 else 290

    class Reprise(ActionBase):
        """
Delivers an attack with a potency of 100.
Action upgraded to Enchanted Reprise if both Black Mana and White Mana are at 5 or more.
        """
        id = 16529
        name = {'Reprise', '续斩'}
        attack_type = physic
        damage_potency = 100

    class Scorch(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 680 for the first enemy, and 60% less for all remaining enemies.
Combo Action: Verflare or Verholy
Additional Effect: Increases both Black Mana and White Mana by 4
Jolt II and Impact are changed to Scorch upon landing Verflare or Verholy as a combo action.
※This action cannot be assigned to a hotbar.
        """
        id = 16530
        name = {'焦热', 'Scorch'}
        combo_action = 7525
        attack_type = magic
        damage_potency = 680
        aoe_scale = .4

    class VerthunderIii(ActionBase):
        """
Deals lightning damage with a potency of 380.
Additional Effect: Increases Black Mana by 6
Additional Effect: 50% chance of becoming Verfire Ready
Duration: 30s
        """
        id = 25855
        name = {'Verthunder III'}
        attack_type = magic
        damage_potency = 380

    class VeraeroIii(ActionBase):
        """
Deals wind damage with a potency of 380.
Additional Effect: Increases White Mana by 6
Additional Effect: 50% chance of becoming Verstone Ready
Duration: 30s
        """
        id = 25856
        name = {'Veraero III'}
        attack_type = magic
        damage_potency = 380

    class MagickBarrier(ActionBase):
        """
Reduces magic damage taken by self and nearby party members by 10%, while increasing HP recovered by healing actions by 5%.
Duration: 10s
>> 2707, Magick Barrier, Magic damage taken is reduced and HP recovery via healing actions is increased.
        """
        id = 25857
        name = {'Magick Barrier'}

    class Resolution(ActionBase):
        """
Deals unaspected damage to all enemies in a straight line before you with a potency of 750 for the first enemy, and 60% less for all remaining enemies.
Combo Action: Scorch
Additional Effect: Increases both Black Mana and White Mana by 4
Scorch is changed to Resolution upon landing Scorch as a combo action.
※This action cannot be assigned to a hotbar.
        """
        id = 25858
        name = {'Resolution'}
        combo_action = 16530
        attack_type = magic
        damage_potency = 750
        aoe_scale = .4
