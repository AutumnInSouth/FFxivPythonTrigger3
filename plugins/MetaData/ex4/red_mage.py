from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Jolt(ActionBase):
        """
        Deals unaspected damage with a potency of 180. Additional Effect: Increases both Black Mana and White Mana by 3
        """
        id = 7503
        name = {"Jolt", "摇荡"}

    class Riposte(ActionBase):
        """
        Delivers an attack with a potency of 130.(source.level>=2?(source.job==35? Action upgraded to Enchanted Riposte if both Black Mana and White Mana are at 30 or more.:):)
        """
        id = 7504
        name = {"Riposte", "回刺"}

    class Verthunder(ActionBase):
        """
        Deals lightning damage with a potency of (source.job==35?(source.level>=62?370:310):310). Additional Effect: Increases Black Mana by 11(source.level>=26?(source.job==35? Additional Effect: 50% chance of becoming Verfire Ready Duration: 30s:):)
        """
        id = 7505
        name = {"Verthunder", "赤闪雷"}

    class CorpsACorps(ActionBase):
        """
        Rushes target and delivers an attack with a potency of 130. Cannot be executed while bound.
        2012, Corps-a-corps, Corps-a-corps, A barrier is preventing damage.
        """
        id = 7506
        name = {"Corps-a-corps", "短兵相接"}

    class Veraero(ActionBase):
        """
        Deals wind damage with a potency of (source.job==35?(source.level>=62?370:310):310). Additional Effect: Increases White Mana by 11(source.level>=30?(source.job==35? Additional Effect: 50% chance of becoming Verstone Ready Duration: 30s:):)
        """
        id = 7507
        name = {"Veraero", "赤疾风"}

    class Scatter(ActionBase):
        """
        Deals unaspected damage with a potency of 120 to target and all enemies nearby it. Additional Effect: Increases both Black Mana and White Mana by 3
        """
        id = 7509
        name = {"Scatter", "散碎"}

    class Verfire(ActionBase):
        """
        Deals fire damage with a potency of (source.job==35?(source.level>=62?310:270):270). Additional Effect: Increases Black Mana by 9 Can only be executed while Verfire Ready is active.
        """
        id = 7510
        name = {"Verfire", "赤火炎"}

    class Verstone(ActionBase):
        """
        Deals earth damage with a potency of (source.job==35?(source.level>=62?310:270):270). Additional Effect: Increases White Mana by 9 Can only be executed while Verstone Ready is active.
        """
        id = 7511
        name = {"Verstone", "赤飞石"}

    class Zwerchhau(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Riposte or Enchanted Riposte Combo Potency: 150 Action upgraded to Enchanted Zwerchhau if both Black Mana and White Mana are at 25 or more.
        """
        id = 7512
        name = {"Zwerchhau", "交击斩"}
        combo_action = 7504

    class Moulinet(ActionBase):
        """
        Delivers an attack with a potency of 60 to all enemies in a cone before you. Action upgraded to Enchanted Moulinet if both Black Mana and White Mana are at 20 or more.
        """
        id = 7513
        name = {"Moulinet", "划圆斩"}

    class Vercure(ActionBase):
        """
        Restores target's HP. Cure Potency: 350
        """
        id = 7514
        name = {"Vercure", "赤治疗"}

    class Displacement(ActionBase):
        """
        Delivers an attack with a potency of (source.job==35?(source.level>=72?200:130):130). Additional Effect: 15-yalm backstep Cannot be executed while bound.(source.job==35?(source.level>=72? Shares a recast timer with Engagement.:):)
        2013, Displacement, Displacement, Next spell cast will deal increased damage.
        """
        id = 7515
        name = {"Displacement", "移转"}

    class Redoublement(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Zwerchhau or Enchanted Zwerchhau Combo Potency: 230 Action upgraded to Enchanted Redoublement if both Black Mana and White Mana are at 25 or more.
        """
        id = 7516
        name = {"Redoublement", "连攻"}
        combo_action = 7512

    class Fleche(ActionBase):
        """
        Delivers an attack with a potency of 440.
        """
        id = 7517
        name = {"Fleche", "飞刺"}

    class Acceleration(ActionBase):
        """
        Ensures the next three casts of Verthunder/Verflare or Veraero/Verholy will, for their first hits, trigger Verfire Ready or Verstone Ready respectively. Duration: 20s
        1238, Acceleration, Acceleration, Additional effects of <UIForeground(500)><UIGlow(501)>Verthunder</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Verflare</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Veraero</UIGlow></UIForeground>, or <UIForeground(500)><UIGlow(501)>Verholy</UIGlow></UIForeground> will trigger.
        """
        id = 7518
        name = {"Acceleration", "促进"}

    class ContreSixte(ActionBase):
        """
        Delivers an attack with a potency of 400 to target and all enemies nearby it.
        """
        id = 7519
        name = {"Contre Sixte", "六分反击"}

    class Embolden(ActionBase):
        """
        Increases own magic damage dealt by 10% and physical damage dealt by nearby party members by 10%. Both effects are reduced by 20% every 4s. Duration: 20s
        1239, Embolden, Embolden, Magic damage dealt is increased.
        1297, Embolden, Embolden, Physical damage dealt is increased.
        2282, Embolden, Embolden, Damage dealt is increased.
        """
        id = 7520
        name = {"Embolden", "鼓励"}

    class Manafication(ActionBase):
        """
        Doubles current Black Mana and White Mana levels. Additional Effect: Resets (source.job==35?(source.level>=72?Corps-a-corps, Displacement, and Engagement:Corps-a-corps and Displacement):Corps-a-corps and Displacement) recast timers(source.job==35?(source.level>=74? Additional Effect: Increases magic damage dealt by 5% Duration: 10s:):) All combos are canceled upon execution of Manafication.
        1971, Manafication, Manafication, Magic damage dealt is increased.
        """
        id = 7521
        name = {"Manafication", "倍增"}

    class Verraise(ActionBase):
        """
        Resurrects target to a weakened state.
        """
        id = 7523
        name = {"Verraise", "赤复活"}

    class JoltIi(ActionBase):
        """
        Deals unaspected damage with a potency of 290. Additional Effect: Increases both Black Mana and White Mana by 3
        """
        id = 7524
        name = {"Jolt II", "震荡"}

    class Verflare(ActionBase):
        """
        Deals fire damage with a potency of 600. Combo Action: Enchanted Redoublement Additional Effect: Increases Black Mana by 21 Additional Effect: 20% chance of becoming Verfire Ready Duration: 30s Chance to become Verfire Ready increases to 100% if White Mana is higher than Black Mana at time of execution. Verthunder is changed to Verflare upon landing Enchanted Redoublement as a combo action. ※This action cannot be assigned to a hotbar.
        """
        id = 7525
        name = {"Verflare", "赤核爆"}
        combo_action = 7529

    class Verholy(ActionBase):
        """
        Deals unaspected damage with a potency of 600. Combo Action: Enchanted Redoublement Additional Effect: Increases White Mana by 21 Additional Effect: 20% chance of becoming Verstone Ready Duration: 30s Chance to become Verstone Ready increases to 100% if Black Mana is higher than White Mana at time of execution. Veraero is changed to Verholy upon landing Enchanted Redoublement as a combo action. ※This action cannot be assigned to a hotbar.
        """
        id = 7526
        name = {"Verholy", "赤神圣"}
        combo_action = 7529

    class EnchantedRiposte(ActionBase):
        """
        Deals unaspected damage with a potency of 220. Balance Gauge Cost: 30 Black Mana Balance Gauge Cost: 30 White Mana ※This action cannot be assigned to a hotbar.
        """
        id = 7527
        name = {"Enchanted Riposte", "魔回刺"}

    class EnchantedZwerchhau(ActionBase):
        """
        Deals unaspected damage with a potency of 100. Combo Action: Riposte or Enchanted Riposte Combo Potency: 290 Balance Gauge Cost: 25 Black Mana Balance Gauge Cost: 25 White Mana ※This action cannot be assigned to a hotbar.
        """
        id = 7528
        name = {"Enchanted Zwerchhau", "魔交击斩"}
        combo_action = 7504

    class EnchantedRedoublement(ActionBase):
        """
        Deals unaspected damage with a potency of 100. Combo Action: Enchanted Zwerchhau Combo Potency: 470 Balance Gauge Cost: 25 Black Mana Balance Gauge Cost: 25 White Mana ※This action cannot be assigned to a hotbar.
        """
        id = 7529
        name = {"Enchanted Redoublement", "魔连攻"}
        combo_action = 7512

    class EnchantedMoulinet(ActionBase):
        """
        Deals unaspected damage with a potency of 200 to all enemies in a cone before you. Balance Gauge Cost: 20 Black Mana Balance Gauge Cost: 20 White Mana ※This action cannot be assigned to a hotbar.
        """
        id = 7530
        name = {"Enchanted Moulinet", "魔划圆斩"}

    class VerthunderIi(ActionBase):
        """
        Deals lightning damage with a potency of (source.job==35?(source.level>=78?120:100):100) to target and all enemies nearby it. Additional Effect: Increases Black Mana by 7
        """
        id = 16524
        name = {"Verthunder II", "赤震雷"}

    class VeraeroIi(ActionBase):
        """
        Deals wind damage with a potency of (source.job==35?(source.level>=78?120:100):100) to target and all enemies nearby it. Additional Effect: Increases White Mana by 7
        """
        id = 16525
        name = {"Veraero II", "赤烈风"}

    class Impact(ActionBase):
        """
        Deals unaspected damage with a potency of 220 to target and all enemies nearby it. Additional Effect: Increases both Black Mana and White Mana by 3
        """
        id = 16526
        name = {"Impact", "冲击"}

    class Engagement(ActionBase):
        """
        Delivers an attack with a potency of 150. Shares a recast timer with Displacement.
        2033, Engagement, Engagement, A barrier is preventing damage.
        """
        id = 16527
        name = {"Engagement", "交剑"}

    class EnchantedReprise(ActionBase):
        """
        Deals unaspected damage with a potency of 300. Balance Gauge Cost: 5 Black Mana Balance Gauge Cost: 5 White Mana ※This action cannot be assigned to a hotbar.
        """
        id = 16528
        name = {"Enchanted Reprise", "魔续斩"}

    class Reprise(ActionBase):
        """
        Delivers an attack with a potency of 100. Action upgraded to Enchanted Reprise if both Black Mana and White Mana are at 5 or more.
        """
        id = 16529
        name = {"Reprise", "续斩"}

    class Scorch(ActionBase):
        """
        Deals unaspected damage with a potency of 700. Combo Action: Verflare or Verholy Additional Effect: Increases both Black Mana and White Mana by 7 Jolt II is changed to Scorch upon landing Verflare or Verholy as a combo action. ※This action cannot be assigned to a hotbar.
        """
        id = 16530
        name = {"Scorch", "焦热"}
        combo_action = 7525
