from ..base import *


class Actions:

    class Riposte(ActionBase):
        """
Delivers an attack with a potency of 130.(source.level>=2?(source.job==35?
Action upgraded to Enchanted Riposte if both Black Mana and White Mana are at 20 or more.:):)
        """
        id = 7504
        name = {'回刺', 'Riposte'}

    class EnchantedRiposte(ActionBase):
        """
Deals unaspected damage with a potency of 220.
(source.job==35?(source.level>=68?Additional Effect: Grants a Mana Stack
:):)Balance Gauge Cost: 20 Black Mana
Balance Gauge Cost: 20 White Mana
※This action cannot be assigned to a hotbar.
        """
        id = 7527
        name = {'魔回刺', 'Enchanted Riposte'}

    class Jolt(ActionBase):
        """
Deals unaspected damage with a potency of 170.
Additional Effect: Increases both Black Mana and White Mana by 2
        """
        id = 7503
        name = {'Jolt', '摇荡'}

    class Verthunder(ActionBase):
        """
Deals lightning damage with a potency of (source.job==35?(source.level>=62?360:300):300).
Additional Effect: Increases Black Mana by 6(source.level>=26?(source.job==35?
Additional Effect: 50% chance of becoming Verfire Ready
Duration: 30s:):)
        """
        id = 7505
        name = {'赤闪雷', 'Verthunder'}

    class CorpsACorps(ActionBase):
        """
Rushes target and delivers an attack with a potency of 130.
Maximum Charges: 2
Cannot be executed while bound.
    2012, Corps-a-corps, A barrier is preventing damage.
        """
        id = 7506
        name = {'短兵相接', 'Corps-a-corps'}

    class Veraero(ActionBase):
        """
Deals wind damage with a potency of (source.job==35?(source.level>=62?360:300):300).
Additional Effect: Increases White Mana by 6(source.level>=30?(source.job==35?
Additional Effect: 50% chance of becoming Verstone Ready
Duration: 30s:):)
        """
        id = 7507
        name = {'赤疾风', 'Veraero'}

    class Scatter(ActionBase):
        """
Deals unaspected damage with a potency of 120 to target and all enemies nearby it.
(source.job==35?(source.level>=50?Acceleration Potency: 170:):)
Additional Effect: Increases both Black Mana and White Mana by 3
        """
        id = 7509
        name = {'散碎', 'Scatter'}

    class VerthunderIi(ActionBase):
        """
Deals lightning damage with a potency of (source.job==35?(source.level>=84?140:(source.job==35?(source.level>=74?120:100):100)):(source.job==35?(source.level>=74?120:100):100)) to target and all enemies nearby it.
Additional Effect: Increases Black Mana by 7
        """
        id = 16524
        name = {'Verthunder II', '赤震雷'}

    class VeraeroIi(ActionBase):
        """
Deals wind damage with a potency of (source.job==35?(source.level>=84?140:(source.job==35?(source.level>=74?120:100):100)):(source.job==35?(source.level>=74?120:100):100)) to target and all enemies nearby it.
Additional Effect: Increases White Mana by 7
        """
        id = 16525
        name = {'赤烈风', 'Veraero II'}

    class Verfire(ActionBase):
        """
Deals fire damage with a potency of (source.job==35?(source.level>=84?330:(source.job==35?(source.level>=62?300:260):260)):(source.job==35?(source.level>=62?300:260):260)).
Additional Effect: Increases Black Mana by 5
Can only be executed while Verfire Ready is active.
        """
        id = 7510
        name = {'赤火炎', 'Verfire'}

    class Verstone(ActionBase):
        """
Deals earth damage with a potency of (source.job==35?(source.level>=84?330:(source.job==35?(source.level>=62?300:260):260)):(source.job==35?(source.level>=62?300:260):260)).
Additional Effect: Increases White Mana by 5
Can only be executed while Verstone Ready is active.
        """
        id = 7511
        name = {'赤飞石', 'Verstone'}

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

    class Displacement(ActionBase):
        """
Delivers an attack with a potency of (source.job==35?(source.level>=72?180:130):130).
Additional Effect: 15-yalm backstep
Maximum Charges: 2
Cannot be executed while bound.
Shares a recast timer with Engagement.
    2013, Displacement, Next spell cast will deal increased damage.
        """
        id = 7515
        name = {'Displacement', '移转'}

    class Fleche(ActionBase):
        """
Delivers an attack with a potency of 460.
        """
        id = 7517
        name = {'飞刺', 'Fleche'}

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

    class Acceleration(ActionBase):
        """
Ensures the next (source.job==35?(source.level>=82?Verthunder III, Veraero III:Verthunder, Veraero):Verthunder, Veraero), or (source.job==35?(source.level>=66?Impact:Scatter):Scatter) can be cast immediately.
Duration: 20s
Additional Effect: Increases the potency of (source.job==35?(source.level>=66?Impact:Scatter):Scatter) by 50
Additional Effect: Ensures (source.job==35?(source.level>=82?Verthunder III and Veraero III:Verthunder and Veraero):Verthunder and Veraero) trigger Verfire Ready or Verstone Ready respectively(source.job==35?(source.level>=88?
Maximum Charges: 2:):)
    1238, Acceleration, Next <If(Equal(PlayerParameter(68),35))><If(GreaterThanOrEqualTo(PlayerParameter(72),82))><UIForeground(500)><UIGlow(501)>Verthunder III</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Veraero III</UIGlow></UIForeground><Else/><UIForeground(500)><UIGlow(501)>Verthunder</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Veraero</UIGlow></UIForeground></If><Else/><UIForeground(500)><UIGlow(501)>Verthunder</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Veraero</UIGlow></UIForeground></If>, or <If(Equal(PlayerParameter(68),35))><If(GreaterThanOrEqualTo(PlayerParameter(72),66))><UIForeground(500)><UIGlow(501)>Impact</UIGlow></UIForeground><Else/><UIForeground(500)><UIGlow(501)>Scatter</UIGlow></UIForeground></If><Else/><UIForeground(500)><UIGlow(501)>Scatter</UIGlow></UIForeground></If> can be cast immediately. Potency of <If(Equal(PlayerParameter(68),35))><If(GreaterThanOrEqualTo(PlayerParameter(72),66))><UIForeground(500)><UIGlow(501)>Impact</UIGlow></UIForeground><Else/><UIForeground(500)><UIGlow(501)>Scatter</UIGlow></UIForeground></If><Else/><UIForeground(500)><UIGlow(501)>Scatter</UIGlow></UIForeground></If> is increased, and <If(Equal(PlayerParameter(68),35))><If(GreaterThanOrEqualTo(PlayerParameter(72),82))><UIForeground(500)><UIGlow(501)>Verthunder III</UIGlow></UIForeground> and <UIForeground(500)><UIGlow(501)>Veraero III</UIGlow></UIForeground><Else/><UIForeground(500)><UIGlow(501)>Verthunder</UIGlow></UIForeground> and <UIForeground(500)><UIGlow(501)>Veraero</UIGlow></UIForeground></If><Else/><UIForeground(500)><UIGlow(501)>Verthunder</UIGlow></UIForeground> and <UIForeground(500)><UIGlow(501)>Veraero</UIGlow></UIForeground></If> trigger <UIForeground(506)><UIGlow(507)>Verfire Ready</UIGlow></UIForeground> or <UIForeground(506)><UIGlow(507)>Verstone Ready</UIGlow></UIForeground> respectively.
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
        name = {'魔连攻', 'Enchanted Redoublement'}
        combo_action = 7512

    class Moulinet(ActionBase):
        """
Delivers an attack with a potency of 60 to all enemies in a cone before you.
Action upgraded to Enchanted Moulinet if both Black Mana and White Mana are at 20 or more.
        """
        id = 7513
        name = {'Moulinet', '划圆斩'}

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

    class Vercure(ActionBase):
        """
Restores target's HP.
Cure Potency: 350
        """
        id = 7514
        name = {'Vercure', '赤治疗'}

    class ContreSixte(ActionBase):
        """
Delivers an attack with a potency of 360 to target and all enemies nearby it.
        """
        id = 7519
        name = {'六分反击', 'Contre Sixte'}

    class Embolden(ActionBase):
        """
Increases own magic damage dealt by 5% and damage dealt by nearby party members by 5%.
Duration: 20s
    1297, Embolden, Damage dealt is increased.
    1239, Embolden, Magic damage dealt is increased.
    2282, Embolden, Damage dealt is increased.
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
    1971, Manafication, Magic damage dealt is increased.
        """
        id = 7521
        name = {'Manafication', '倍增'}

    class JoltIi(ActionBase):
        """
Deals unaspected damage with a potency of (source.job==35?(source.level>=84?310:280):280).
Additional Effect: Increases both Black Mana and White Mana by 2
    1498, Shocked, Experiencing periodic immobility while bleeding HP over time.
        """
        id = 7524
        name = {'震荡', 'Jolt II'}

    class Verraise(ActionBase):
        """
Resurrects target to a weakened state.
        """
        id = 7523
        name = {'赤复活', 'Verraise'}

    class Impact(ActionBase):
        """
Deals unaspected damage with a potency of (source.job==35?(source.level>=84?210:200):200) to target and all enemies nearby it.
Acceleration Potency: (source.job==35?(source.level>=84?260:250):250)
Additional Effect: Increases both Black Mana and White Mana by 3
    995, Headache, Suffering mild head trauma. Damage dealt is reduced. Increased trauma results in a Concussion.
        """
        id = 16526
        name = {'冲击', 'Impact'}

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
        combo_action = 7529

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
        combo_action = 7529

    class Engagement(ActionBase):
        """
Delivers an attack with a potency of (source.job==35?(source.level>=72?180:130):130).
Maximum Charges: 2
Shares a recast timer with Displacement.
    2033, Engagement, A barrier is preventing damage.
        """
        id = 16527
        name = {'交剑', 'Engagement'}

    class EnchantedReprise(ActionBase):
        """
Deals unaspected damage with a potency of (source.job==35?(source.level>=84?330:290):290).
Balance Gauge Cost: 5 Black Mana
Balance Gauge Cost: 5 White Mana
※This action cannot be assigned to a hotbar.
        """
        id = 16528
        name = {'Enchanted Reprise', '魔续斩'}

    class Reprise(ActionBase):
        """
Delivers an attack with a potency of 100.
Action upgraded to Enchanted Reprise if both Black Mana and White Mana are at 5 or more.
        """
        id = 16529
        name = {'Reprise', '续斩'}

    class Scorch(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 680 for the first enemy, and 60% less for all remaining enemies.
Combo Action: Verflare or Verholy
Additional Effect: Increases both Black Mana and White Mana by 4
Jolt II and Impact are changed to Scorch upon landing Verflare or Verholy as a combo action.
※This action cannot be assigned to a hotbar.
        """
        id = 16530
        name = {'Scorch', '焦热'}
        combo_action = 7525
