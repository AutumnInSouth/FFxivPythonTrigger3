from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Hakaze(ActionBase):
        """
        Delivers an attack with a potency of 200.(source.level>=62?(source.job==34? Additional Effect: Increases Kenki Gauge by 5:):)
        """
        id = 7477
        name = {"Hakaze", "刃风"}

    class Jinpu(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Hakaze Combo Potency: 320 Combo Bonus: Increases damage dealt by (source.job==34?(source.level>=78?13:10):10)% Duration: 40s(source.level>=62?(source.job==34? Combo Bonus: Increases Kenki Gauge by 5:):)
        1298, Jinpu, Jinpu, Damage dealt is increased.
        """
        id = 7478
        name = {"Jinpu", "阵风"}
        combo_action = 7477

    class Shifu(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Hakaze Combo Potency: 320 Combo Bonus: Reduces weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay by (source.job==34?(source.level>=78?13:10):10)% Duration: 40s(source.level>=62?(source.job==34? Combo Bonus: Increases Kenki Gauge by 5:):)
        1299, Shifu, Shifu, Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
        """
        id = 7479
        name = {"Shifu", "士风"}
        combo_action = 7477

    class Yukikaze(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Hakaze Combo Potency: 360(source.level>=52?(source.job==34? Combo Bonus: Increases Kenki Gauge by (source.level>=62?(source.job==34?15:10):10) Combo Bonus: Grants Setsu: Combo Bonus: Grants Setsu): Combo Bonus: Grants Setsu)
        1227, Yukikaze, Yukikaze, Slashing resistance is reduced.
        1318, Yukikaze, Yukikaze, Sustaining increased damage from target who executed <UIForeground(500)><UIGlow(501)>Yukikaze</UIGlow></UIForeground>.
        """
        id = 7480
        name = {"Yukikaze", "雪风"}
        combo_action = 7477

    class Gekko(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Jinpu Combo Potency: 480(source.level>=52?(source.job==34? Rear Combo Bonus: Increases Kenki Gauge by 5:):)(source.level>=62?(source.job==34? Combo Bonus: Increases Kenki Gauge by 5 Combo Bonus: Grants Getsu: Combo Bonus: Grants Getsu): Combo Bonus: Grants Getsu)
        """
        id = 7481
        name = {"Gekko", "月光"}
        combo_action = 7478

    class Kasha(ActionBase):
        """
        Delivers an attack with a potency of 100. Combo Action: Shifu Combo Potency: 480(source.level>=52?(source.job==34? Flank Combo Bonus: Increases Kenki Gauge by 5:):)(source.level>=62?(source.job==34? Combo Bonus: Increases Kenki Gauge by 5 Combo Bonus: Grants Ka: Combo Bonus: Grants Ka): Combo Bonus: Grants Ka)
        """
        id = 7482
        name = {"Kasha", "花车"}
        combo_action = 7479

    class Fuga(ActionBase):
        """
        Delivers an attack with a potency of 100 to all enemies in a cone before you.(source.level>=62?(source.job==34? Additional Effect: Increases Kenki Gauge by 5:):)
        """
        id = 7483
        name = {"Fuga", "风雅"}

    class Mangetsu(ActionBase):
        """
        Delivers an attack with a potency of 100 to all nearby enemies. Combo Action: Fuga Combo Potency: 160 Combo Bonus: Extends Jinpu duration by 15s to a maximum of 40s(source.level>=52?(source.job==34? Combo Bonus: Increases Kenki Gauge by (source.level>=62?(source.job==34?10:5):5) Combo Bonus: Grants Getsu: Combo Bonus: Grants Getsu): Combo Bonus: Grants Getsu)
        """
        id = 7484
        name = {"Mangetsu", "满月"}
        combo_action = 7483

    class Oka(ActionBase):
        """
        Delivers an attack with a potency of 100 to all nearby enemies. Combo Action: Fuga Combo Potency: 160 Combo Bonus: Extends Shifu duration by 15s to a maximum of 40s(source.level>=52?(source.job==34? Combo Bonus: Increases Kenki Gauge by (source.level>=62?(source.job==34?10:5):5) Combo Bonus: Grants Ka: Combo Bonus: Grants Ka): Combo Bonus: Grants Ka)
        """
        id = 7485
        name = {"Oka", "樱花"}
        combo_action = 7483

    class Enpi(ActionBase):
        """
        Delivers a ranged attack with a potency of 100.(source.level>=56?(source.job==34? Enhanced Enpi Bonus Potency: 320:):)(source.level>=52?(source.job==34? Additional Effect: Increases Kenki Gauge by (source.level>=62?(source.job==34?10:5):5):):)
        """
        id = 7486
        name = {"Enpi", "燕飞"}

    class MidareSetsugekka(ActionBase):
        """
        Delivers an attack with a potency of 800. (source.job==34?(source.level>=80?Additional Effect: Grants a stack of Meditation, up to a maximum of 3 :):) ※This action cannot be assigned to a hotbar.
        """
        id = 7487
        name = {"Midare Setsugekka", "纷乱雪月花"}

    class TenkaGoken(ActionBase):
        """
        Delivers an attack with a potency of 360 to all enemies in a cone before you. (source.job==34?(source.level>=80?Additional Effect: Grants a stack of Meditation, up to a maximum of 3 :):) ※This action cannot be assigned to a hotbar.
        """
        id = 7488
        name = {"Tenka Goken", "天下五剑"}

    class Higanbana(ActionBase):
        """
        Delivers an attack with a potency of 250. Additional Effect: Damage over time Potency: 40 Duration: 60s (source.job==34?(source.level>=80?Additional Effect: Grants a stack of Meditation, up to a maximum of 3 :):) ※This action cannot be assigned to a hotbar.
        1228, Higanbana, Higanbana, Open wounds are bleeding, causing damage over time.
        1319, Higanbana, Higanbana, Open wounds are bleeding, causing damage over time. HP recovery is reduced.
        """
        id = 7489
        name = {"Higanbana", "彼岸花"}

    class HissatsuShinten(ActionBase):
        """
        Delivers an attack with a potency of 320. Kenki Gauge Cost: 25
        """
        id = 7490
        name = {"Hissatsu: Shinten", "必杀剑·震天"}

    class HissatsuKyuten(ActionBase):
        """
        Delivers an attack with a potency of 150 to all nearby enemies. Kenki Gauge Cost: 25
        """
        id = 7491
        name = {"Hissatsu: Kyuten", "必杀剑·九天"}

    class HissatsuGyoten(ActionBase):
        """
        Rushes target and delivers an attack with a potency of 100. Kenki Gauge Cost: 10 Cannot be executed while bound.
        """
        id = 7492
        name = {"Hissatsu: Gyoten", "必杀剑·晓天"}

    class HissatsuYaten(ActionBase):
        """
        Delivers an attack with a potency of 100. Additional Effect: 10-yalm backstep Additional Effect: Grants Enhanced Enpi Duration: 15s Kenki Gauge Cost: 10 Cannot be executed while bound.
        """
        id = 7493
        name = {"Hissatsu: Yaten", "必杀剑·夜天"}

    class HissatsuKaiten(ActionBase):
        """
        Increases potency of next weaponskill by 50%. Duration: 10s Kenki Gauge Cost: 20
        """
        id = 7494
        name = {"Hissatsu: Kaiten", "必杀剑·回天"}

    class Hagakure(ActionBase):
        """
        Converts Setsu, Getsu, and Ka into Kenki. Each Sen converted increases your Kenki Gauge by 10. Can only be executed if under the effect of at least one of the three statuses.
        """
        id = 7495
        name = {"Hagakure", "叶隐"}

    class HissatsuGuren(ActionBase):
        """
        Delivers an attack with a potency of 850 to all enemies in a straight line before you. Kenki Gauge Cost: 50(source.job==34?(source.level>=72? Shares a recast timer with Hissatsu: Senei.:):)
        """
        id = 7496
        name = {"Hissatsu: Guren", "必杀剑·红莲"}

    class Meditate(ActionBase):
        """
        Gradually increases your Kenki Gauge. Duration: 15s (source.job==34?(source.level>=80?Additional Effect: Grants stacks of Meditation when used in combat, up to a maximum of 3 :):)Kenki Gauge not affected when used outside battle. Effect ends upon using another action or moving (including facing a different direction). Cancels auto-attack upon execution. Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.
        1231, Meditate, Meditate, Storing <UIForeground(500)><UIGlow(501)>Kenki</UIGlow></UIForeground>.
        """
        id = 7497
        name = {"Meditate", "默想"}

    class ThirdEye(ActionBase):
        """
        Reduces the amount of damage taken by the next attack by 10%. Duration: 3s(source.level>=58?(source.job==34? Additional Effect: Grants Eyes Open when hit Duration: 15s:):)
        1232, Third Eye, Third Eye, Next damage taken is reduced.
        """
        id = 7498
        name = {"Third Eye", "心眼"}

    class MeikyoShisui(ActionBase):
        """
        Execute up to 3 weaponskill combos without meeting combo prerequisites. Does not affect Iaijutsu. Duration: 15s
        1233, Meikyo Shisui, Meikyo Shisui, Combo prerequisites are met.
        1320, Meikyo Shisui, Meikyo Shisui, Final combo prerequisite is met.
        """
        id = 7499
        name = {"Meikyo Shisui", "明镜止水"}

    class HissatsuSeigan(ActionBase):
        """
        Delivers an attack with a potency of 220. Kenki Gauge Cost: 15 Can only be executed while under the effect of Eyes Open. Shares a recast timer with Merciful Eyes.
        """
        id = 7501
        name = {"Hissatsu: Seigan", "必杀剑·星眼"}

    class MercifulEyes(ActionBase):
        """
        Instantly restores own HP. Cure Potency: 200 Can only be executed while under the effect of Eyes Open. Shares a recast timer with Hissatsu: Seigan.
        """
        id = 7502
        name = {"Merciful Eyes", "慈眼"}

    class Iaijutsu(ActionBase):
        """
        Executes a weaponskill depending on current number of Sen stored in Sen Gauge. 1 Sen: Higanbana 2 Sen: Tenka Goken 3 Sen: Midare Setsugekka
        """
        id = 7867
        name = {"Iaijutsu", "居合术"}

    class HissatsuSenei(ActionBase):
        """
        Delivers an attack with a potency of 1,100. Kenki Gauge Cost: 50 Shares a recast timer with Hissatsu: Guren.
        """
        id = 16481
        name = {"Hissatsu: Senei", "必杀剑·闪影"}

    class Ikishoten(ActionBase):
        """
        Increases Kenki Gauge by 50. Can only be executed while in combat.
        """
        id = 16482
        name = {"Ikishoten", "意气冲天"}

    class TsubameGaeshi(ActionBase):
        """
        Repeats the previously executed iaijutsu with increased potency. Can only be executed immediately following Iaijutsu. Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.
        """
        id = 16483
        name = {"Tsubame-gaeshi", "燕回返"}

    class KaeshiHiganbana(ActionBase):
        """
        Delivers an attack with a potency of 375. Additional Effect: Damage over time Potency: 60 Duration: 60s (source.job==34?(source.level>=80?Additional Effect: Grants a stack of Meditation, up to a maximum of 3 :):)Effect cannot be stacked with Higanbana. Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills. ※This action cannot be assigned to a hotbar.
        """
        id = 16484
        name = {"Kaeshi: Higanbana", "回返彼岸花"}

    class KaeshiGoken(ActionBase):
        """
        Delivers an attack with a potency of 540 to all enemies in a cone before you. (source.job==34?(source.level>=80?Additional Effect: Grants a stack of Meditation, up to a maximum of 3 :):)Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills. ※This action cannot be assigned to a hotbar.
        """
        id = 16485
        name = {"Kaeshi: Goken", "回返五剑"}

    class KaeshiSetsugekka(ActionBase):
        """
        Delivers an attack with a potency of 1,200. (source.job==34?(source.level>=80?Additional Effect: Grants a stack of Meditation, up to a maximum of 3 :):)Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills. ※This action cannot be assigned to a hotbar.
        """
        id = 16486
        name = {"Kaeshi: Setsugekka", "回返雪月花"}

    class Shoha(ActionBase):
        """
        Delivers an attack with a potency of 400. Can only be executed after accumulating three stacks of Meditation by executing Iaijutsu, Tsubame-gaeshi, or Meditate while in combat. Meditation effect fades upon execution.
        """
        id = 16487
        name = {"Shoha", "照破"}
