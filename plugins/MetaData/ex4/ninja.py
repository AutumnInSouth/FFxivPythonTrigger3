from ..base import *


class Actions:

    class SpinningEdge(ActionBase):
        """
Delivers an attack with a potency of (source.job==30?(source.level>=84?200:180):180).(source.job==30?(source.level>=62?
Additional Effect: Increases Ninki Gauge by 5:):)
        """
        id = 2240
        name = {'双刃旋', 'Spinning Edge'}

    class ShadeShift(ActionBase):
        """
Create shadows that nullify damage up to 20% of maximum HP.
Duration: 20s
    488, Shade Shift, Shadows are nullifying damage.
    2011, Shade Shift, Shadows are nullifying damage.
        """
        id = 2241
        name = {'残影', 'Shade Shift'}

    class GustSlash(ActionBase):
        """
Delivers an attack with a potency of (source.job==30?(source.level>=84?140:100):100).
Combo Action: Spinning Edge
Combo Potency: (source.job==30?(source.level>=84?300:260):260)(source.job==30?(source.level>=62?
Combo Bonus: Increases Ninki Gauge by 5:):)
        """
        id = 2242
        name = {'绝风', 'Gust Slash'}
        combo_action = 2240

    class Hide(ActionBase):
        """
Blend in with your surroundings, making it impossible for most enemies to detect you, but reducing movement speed by 50%. Has no effect on enemies 10 levels higher than your own, or certain enemies with special sight.
(source.level>=30?(source.job==30?Additional Effect: Restores 2 charges to all mudra
:):)Cannot be executed while in combat.
Effect ends upon use of any action other than Sprint, or upon reuse of Hide.
    1952, Hide, Unable to be detected. Movement speed is severely reduced.
    1316, Hidden, Unable to be detected.
    614, Hidden, Unable to be detected. Movement speed is severely reduced.
    615, Hidden, Unable to be detected. Movement speed is severely reduced.
    1705, Hidden, Unable to be detected. Movement speed is severely reduced.
    1108, Hidden, Unable to be detected. Movement speed is severely reduced.
        """
        id = 2245
        name = {'隐遁', 'Hide'}

    class ThrowingDagger(ActionBase):
        """
Delivers a ranged attack with a potency of 120.(source.job==30?(source.level>=62?
Additional Effect: Increases Ninki Gauge by 5:):)
        """
        id = 2247
        name = {'Throwing Dagger', '飞刀'}

    class Mug(ActionBase):
        """
Delivers an attack with a potency of 150.
Additional Effect: Increases the chance of additional items being dropped by target if Mug is dealt before, or as, the finishing blow(source.level>=66?(source.job==30?
Additional Effect: Increases Ninki Gauge by 40:):)
        """
        id = 2248
        name = {'夺取', 'Mug'}

    class TrickAttack(ActionBase):
        """
Delivers an attack with a potency of 300.
400 when executed from a target's rear.
Additional Effect: Increases target's damage taken by 5%
Duration: 15s
Can only be executed while under the effect of Hidden.
    2014, Trick Attack, Damage taken is increased.
        """
        id = 2258
        name = {'Trick Attack', '攻其不备'}

    class AeolianEdge(ActionBase):
        """
Delivers an attack with a potency of (source.job==30?(source.level>=84?120:100):100).
(source.job==30?(source.level>=84?180:160):160) when executed from a target's rear.
Combo Action: Gust Slash
Combo Potency: (source.job==30?(source.level>=84?340:320):320)
Rear Combo Potency: (source.job==30?(source.level>=84?400:380):380)(source.job==30?(source.level>=62?
Combo Bonus: Increases Ninki Gauge by (source.job==30?(source.level>=84?15:(source.job==30?(source.level>=78?10:5):5)):(source.job==30?(source.level>=78?10:5):5)):):)
        """
        id = 2255
        name = {'旋风刃', 'Aeolian Edge'}
        combo_action = 2242

    class ShadowFang(ActionBase):
        """
Delivers an attack with a potency of 200.
Additional Effect: Damage over time
Potency: 90
Duration: 30s
(source.job==30?(source.level>=62?Additional Effect: Increases Ninki Gauge by (source.job==30?(source.level>=78?10:5):5)
:):)This weaponskill does not share a recast timer with any other actions.
    1313, Shadow Fang, Sustaining damage over time, as well as increased damage from target who executed <UIForeground(500)><UIGlow(501)>Shadow Fang</UIGlow></UIForeground>.
    508, Shadow Fang, Wounds are bleeding, causing damage over time.
        """
        id = 2257
        name = {'Shadow Fang', '影牙'}

    class Ten(ActionBase):
        """
Make the ritual mudra hand gesture for “heaven.”
Duration: 6s
Maximum Charges: 2
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
Conversely, execution of weaponskills triggers the cooldown of this action.
        """
        id = 2259
        name = {'Ten', '天之印'}

    class Ninjutsu(ActionBase):
        """
Executes a specific ninjutsu action coinciding with the combination of mudra made immediately beforehand.
If any other action is used before the mudra are combined and the ninjutsu executed, Ninjutsu will fail.
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
Conversely, execution of weaponskills triggers the cooldown of this action.
        """
        id = 2260
        name = {'忍术', 'Ninjutsu'}

    class FumaShuriken(ActionBase):
        """
Delivers a ranged ninjutsu attack with a potency of 450.
Mudra Combination: Any one of the Ten, Chi, or Jin mudra
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
        """
        id = 2265
        name = {'风魔手里剑', 'Fuma Shuriken'}

    class RabbitMedium(ActionBase):
        """
Thumpity thump thump, thumpity thump thump...
        """
        id = 2272
        name = {'通灵之术', 'Rabbit Medium'}

    class Ten(ActionBase):
        """
Make the ritual mudra hand gesture for “heaven.”
Duration: 6s
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
Conversely, execution of weaponskills triggers the cooldown of this action.
        """
        id = 18805
        name = {'Ten', '天之印'}

    class FumaShuriken(ActionBase):
        """
Delivers a ranged ninjutsu attack with a potency of 450.
Mudra Combination: Any one of the Ten, Chi, or Jin mudra
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
        """
        id = 18873
        name = {'风魔手里剑', 'Fuma Shuriken'}

    class FumaShuriken(ActionBase):
        """
Delivers a ranged ninjutsu attack with a potency of 450.
Mudra Combination: Any one of the Ten, Chi, or Jin mudra
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
        """
        id = 18874
        name = {'风魔手里剑', 'Fuma Shuriken'}

    class FumaShuriken(ActionBase):
        """
Delivers a ranged ninjutsu attack with a potency of 450.
Mudra Combination: Any one of the Ten, Chi, or Jin mudra
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
        """
        id = 18875
        name = {'风魔手里剑', 'Fuma Shuriken'}

    class Chi(ActionBase):
        """
Make the ritual mudra hand gesture for “earth.”
Duration: 6s
Maximum Charges: 2
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
Conversely, execution of weaponskills triggers the cooldown of this action.
        """
        id = 2261
        name = {'地之印', 'Chi'}

    class Katon(ActionBase):
        """
Deals fire damage with a potency of 350 to target and all enemies nearby it.
Mudra Combination: Chi→Ten or Jin→Ten
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
        """
        id = 2266
        name = {'火遁之术', 'Katon'}

    class Raiton(ActionBase):
        """
Deals lightning damage with a potency of 650.
(source.job==30?(source.level>=90?Additional Effect: Grants a stack of Forked Raiju Ready
Duration: 15s
Maximum Stacks: 3
:):)Mudra Combination: Ten→Chi or Jin→Chi
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
        """
        id = 2267
        name = {'Raiton', '雷遁之术'}

    class Chi(ActionBase):
        """
Make the ritual mudra hand gesture for “earth.”
Duration: 6s
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
Conversely, execution of weaponskills triggers the cooldown of this action.
        """
        id = 18806
        name = {'地之印', 'Chi'}

    class Katon(ActionBase):
        """
Delivers fire damage with a potency of 350 to target and all enemies nearby it.
Mudra Combination: Chi→Ten or Jin→Ten
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
        """
        id = 18876
        name = {'火遁之术', 'Katon'}

    class Raiton(ActionBase):
        """
Deals lightning damage with a potency of 650.
(source.job==30?(source.level>=90?Additional Effect: Grants a stack of Forked Raiju Ready
Duration: 15s
Maximum Stacks: 3
:):)Mudra Combination: Ten→Chi or Jin→Chi
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
        """
        id = 18877
        name = {'Raiton', '雷遁之术'}

    class DeathBlossom(ActionBase):
        """
Delivers an attack with a potency of 100 to all nearby enemies.(source.job==30?(source.level>=62?
Additional Effect: Increases Ninki Gauge by 5:):)
        """
        id = 2254
        name = {'血雨飞花', 'Death Blossom'}

    class Shukuchi(ActionBase):
        """
Move quickly to the specified location.
(source.job==30?(source.level>=74?Maximum Charges: 2
:):)Cannot be executed while bound.
        """
        id = 2262
        name = {'缩地', 'Shukuchi'}

    class Jin(ActionBase):
        """
Make the ritual mudra hand gesture for “man.”
Duration: 6s
Maximum Charges: 2
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
Conversely, execution of weaponskills triggers the cooldown of this action.
        """
        id = 2263
        name = {'人之印', 'Jin'}

    class Hyoton(ActionBase):
        """
Deals ice damage with a potency of 350.
Additional Effect: Bind
Duration: 15s
Mudra Combination: Ten→Jin or Chi→Jin
Cancels auto-attack upon execution.
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
        """
        id = 2268
        name = {'Hyoton', '冰遁之术'}

    class Huton(ActionBase):
        """
Reduces weaponskill recast time and auto-attack delay by 15%.
Duration: 60s
Mudra Combination: Jin→Chi→Ten or Chi→Jin→Ten
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
    500, Huton, Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
        """
        id = 2269
        name = {'风遁之术', 'Huton'}

    class Doton(ActionBase):
        """
Creates a patch of corrupted earth, dealing damage with a potency of 70 to any enemies who enter.
Duration: 24s
Additional Effect: Heavy +40%
Mudra Combination: Ten→Jin→Chi or Jin→Ten→Chi
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
    501, Doton, Foul magicks corrupt the ground, dealing earth damage to any who tread upon it.
        """
        id = 2270
        name = {'土遁之术', 'Doton'}

    class Suiton(ActionBase):
        """
Deals water damage with a potency of 500.
Additional Effect: Grants Suiton
Duration: 20s
Suiton Effect: Allows execution of actions which require the effect of Hidden, without being under that effect
Mudra Combination: Ten→Chi→Jin or Chi→Ten→Jin
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
    507, Suiton, Body is enveloped in a light-bending veil of water, allowing use of actions normally requiring the <UIForeground(506)><UIGlow(507)>Hidden</UIGlow></UIForeground> status.
        """
        id = 2271
        name = {'Suiton', '水遁之术'}

    class Jin(ActionBase):
        """
Make the ritual mudra hand gesture for “man.”
Duration: 6s
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
Conversely, execution of weaponskills triggers the cooldown of this action.
        """
        id = 18807
        name = {'人之印', 'Jin'}

    class Hyoton(ActionBase):
        """
Delivers ice damage with a potency of 350.
Additional Effect: Bind
Duration: 15s
Mudra Combination: Ten→Jin or Chi→Jin
Cancels auto-attack upon execution.
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
        """
        id = 18878
        name = {'Hyoton', '冰遁之术'}

    class Huton(ActionBase):
        """
Reduces weaponskill recast time and auto-attack delay by 15%.
Duration: 60s
Mudra Combination: Jin→Chi→Ten or Chi→Jin→Ten
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
    500, Huton, Weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
        """
        id = 18879
        name = {'风遁之术', 'Huton'}

    class Doton(ActionBase):
        """
Creates a patch of corrupted earth, dealing damage with a potency of 70 to any enemies who enter.
Duration: 24s
Additional Effect: Heavy +40%
Mudra Combination: Ten→Jin→Chi or Jin→Ten→Chi
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
    501, Doton, Foul magicks corrupt the ground, dealing earth damage to any who tread upon it.
        """
        id = 18880
        name = {'土遁之术', 'Doton'}

    class Suiton(ActionBase):
        """
Deals water damage with a potency of 500.
Additional Effect: Grants Suiton
Duration: 20s
Suiton Effect: Allows execution of actions which require the effect of Hidden, without being under that effect
Mudra Combination: Ten→Chi→Jin or Chi→Ten→Jin
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
    507, Suiton, Body is enveloped in a light-bending veil of water, allowing use of actions normally requiring the <UIForeground(506)><UIGlow(507)>Hidden</UIGlow></UIForeground> status.
        """
        id = 18881
        name = {'Suiton', '水遁之术'}

    class Kassatsu(ActionBase):
        """
Allows the execution of a single ninjutsu without consumption of mudra charges.
Additional Effect: Increases damage for the next ninjutsu action by 30%
Duration: 15s
Recast timer of mudra is not affected by the execution of this action.
    497, Kassatsu, Able to execute a ninjutsu with increased potency.
        """
        id = 2264
        name = {'Kassatsu', '生杀予夺'}

    class HakkeMujinsatsu(ActionBase):
        """
Delivers an attack with a potency of 100 to all nearby enemies.
Combo Action: Death Blossom
Combo Potency: 120
Combo Bonus: Extends Huton duration by 10s to a maximum of 60s(source.job==30?(source.level>=62?
Combo Bonus: Increases Ninki Gauge by 5:):)
        """
        id = 16488
        name = {'八卦无刃杀', 'Hakke Mujinsatsu'}
        combo_action = 2254

    class ArmorCrush(ActionBase):
        """
Delivers an attack with a potency of (source.job==30?(source.level>=84?120:100):100).
(source.job==30?(source.level>=84?180:160):160) when executed from a target's flank.
Combo Action: Gust Slash
Combo Potency: (source.job==30?(source.level>=84?320:300):300)
Flank Combo Potency: (source.job==30?(source.level>=84?380:360):360)
Combo Bonus: Extends Huton duration by 30s to a maximum of 60s(source.job==30?(source.level>=62?
Combo Bonus: Increases Ninki Gauge by (source.job==30?(source.level>=84?15:(source.job==30?(source.level>=78?10:5):5)):(source.job==30?(source.level>=78?10:5):5)):):)
        """
        id = 3563
        name = {'Armor Crush', '强甲破点突'}
        combo_action = 2242

    class DreamWithinADream(ActionBase):
        """
Delivers a threefold attack, each hit with a potency of 150.
        """
        id = 3566
        name = {'Dream Within a Dream', '梦幻三段'}

    class Assassinate(ActionBase):
        """
Delivers an attack with a potency of 200.
    1314, Assassinated, Sustaining damage over time, as well as increased damage.
        """
        id = 2246
        name = {'Assassinate', '断绝'}

    class HellfrogMedium(ActionBase):
        """
Deals fire damage with a potency of 160 to target and all enemies nearby it.
Ninki Gauge Cost: 50
Shares a recast timer with Bhavacakra.
        """
        id = 7401
        name = {'通灵之术·大虾蟆', 'Hellfrog Medium'}

    class Bhavacakra(ActionBase):
        """
Deals unaspected damage with a potency of 400.
(source.job==30?(source.level>=88?Meisui Bonus: Potency is increased to 500 when under the effect of Meisui
:):)Ninki Gauge Cost: 50
Shares a recast timer with Hellfrog Medium.
        """
        id = 7402
        name = {'Bhavacakra', '六道轮回'}

    class TenChiJin(ActionBase):
        """
Temporarily converts each of the three mudra into a ninjutsu action. Executing one of these actions will convert the remaining mudra into different ninjutsu actions until all three have been executed or the Ten Chi Jin effect expires.
Duration: 6s
Only ninjutsu available while active. The same ninjutsu cannot be executed twice.
Cannot be executed while under the effect of Kassatsu. Effect ends upon moving.
    1186, Ten Chi Jin, Able to execute ninjutsu in succession.
        """
        id = 7403
        name = {'Ten Chi Jin', '天地人'}

    class Meisui(ActionBase):
        """
Dispels Suiton, increasing the Ninki Gauge by 50.
(source.job==30?(source.level>=88?Additional Effect: Increases the potency of Bhavacakra to 500
Duration: 30s
:):)Can only be executed while in combat.
        """
        id = 16489
        name = {'Meisui', '命水'}

    class GokaMekkyaku(ActionBase):
        """
Deals fire damage with a potency of 600 to target and all enemies nearby it.
Mudra Combination: Chi→Ten or Jin→Ten
Can only be executed while under the effect of Kassatsu.
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
        """
        id = 16491
        name = {'Goka Mekkyaku', '劫火灭却之术'}

    class HyoshoRanryu(ActionBase):
        """
Deals ice damage with a potency of 1,200.
Mudra Combination: Chi→Jin or Ten→Jin
Can only be executed while under the effect of Kassatsu.
Triggers the cooldown of weaponskills, mudra, and Ninjutsu upon execution.
※This action cannot be assigned to a hotbar.
        """
        id = 16492
        name = {'Hyosho Ranryu', '冰晶乱流之术'}

    class Bunshin(ActionBase):
        """
Grants 5 stacks of Bunshin, each stack allowing your shadow to attack enemies each time you execute a weaponskill. Shadow attack potency varies based on the attack executed, but is not affected by combo bonuses.
Melee Attack Potency: 160
Ranged Attack Potency: 160
Area Attack Potency: 80
Ninki Gauge increases by 5 each time your shadow lands an attack.
Duration: 30s
(source.job==30?(source.level>=82?Additional Effect: Grants Phantom Kamaitachi Ready
:):)Ninki Gauge Cost: 50
    2010, Bunshin, Your corporeal shadow is performing an attack each time you execute a weaponskill.
    1954, Bunshin, Your corporeal shadow is performing an attack each time you execute a weaponskill.
        """
        id = 16493
        name = {'Bunshin', '分身之术'}
