from ..base import *


class Status:
    class Swiftcast(StatusBase):
        id = 167
        name = {'即刻咏唱', 'Swiftcast'}

    class Raise(StatusBase):
        id = 148
        name = {'Raise', '复活'}


class Actions:
    class Return(ActionBase):
        """
Instantly return to your current home point.
>> 2452, Return, Aetherially entwined with the temporal manifold. You will be stunned and drawn back to your aetherial trace when this effect expires.
        """
        id = 6
        name = {'返回', 'Return'}

    class ShieldWall(ActionBase):
        """
Reduces damage taken by all party members by 20%.
Duration: 10s
>> 194, Shield Wall, Damage taken is reduced.
        """
        id = 197
        name = {'Shield Wall', '铜墙铁盾'}

    class Stronghold(ActionBase):
        """
Reduces damage taken by all party members by 40%.
Duration: 15s
>> 195, Stronghold, Damage taken is reduced.
        """
        id = 198
        name = {'Stronghold', '坚守要塞'}

    class LastBastion(ActionBase):
        """
Reduces damage taken by all party members by 80%.
Duration: 12s
>> 196, Last Bastion, Damage taken is reduced.
        """
        id = 199
        name = {'Last Bastion', '终极堡垒'}

    class Braver(ActionBase):
        """
Delivers an attack with a potency of 2,400.
        """
        id = 200
        name = {'勇猛烈斩', 'Braver'}

    class Bladedance(ActionBase):
        """
Delivers an attack with a potency of 5,250.
        """
        id = 201
        name = {'刀光剑舞', 'Bladedance'}

    class FinalHeaven(ActionBase):
        """
Delivers an attack with a potency of 9,000.
        """
        id = 202
        name = {'Final Heaven', '最终天堂'}

    class Skyshard(ActionBase):
        """
Deals unaspected damage with a potency of 1,650 to all enemies near point of impact.
        """
        id = 203
        name = {'苍穹破碎', 'Skyshard'}

    class Starstorm(ActionBase):
        """
Deals unaspected damage with a potency of 3,600 to all enemies near point of impact.
        """
        id = 204
        name = {'星体风暴', 'Starstorm'}

    class Meteor(ActionBase):
        """
Deals unaspected damage with a potency of 6,150 to all enemies near point of impact.
        """
        id = 205
        name = {'陨石流星', 'Meteor'}

    class HealingWind(ActionBase):
        """
Restores 25% of own HP and the HP of all nearby party members.
        """
        id = 206
        name = {'治愈微风', 'Healing Wind'}

    class BreathOfTheEarth(ActionBase):
        """
Restores 60% of own HP and the HP of all nearby party members.
        """
        id = 207
        name = {'大地气息', 'Breath of the Earth'}

    class PulseOfLife(ActionBase):
        """
Restores 100% of own HP and the HP of all nearby party members, including ones KO'd.
        """
        id = 208
        name = {'生命鼓动', 'Pulse of Life'}

    class MagitekCannon(ActionBase):
        """
Fires an explosive projectile at the designated area.
        """
        id = 1128
        name = {'魔导加农炮', 'Magitek Cannon'}

    class PhotonStream(ActionBase):
        """
Fires a short-range burst of energy in a straight line before you.
        """
        id = 1129
        name = {'魔导光子炮', 'Photon Stream'}

    class Cannonfire(ActionBase):
        """
Fires an explosive projectile at the designated area.
        """
        id = 1134
        name = {'Cannonfire', '炮击'}

    class Cannonfire(ActionBase):
        """
Fires an explosive projectile at the designated area.
        """
        id = 1437
        name = {'Cannonfire', '炮击'}

    class FieryBreath(ActionBase):
        """
Emits a stream of white-hot flames.
        """
        id = 1764
        name = {'Fiery Breath', '烈火吐息'}

    class BigSneeze(ActionBase):
        """
Discharges a shower of lukewarm spittle onto an unfortunate target.
        """
        id = 1765
        name = {'喷嚏', 'Big Sneeze'}

    class IronKiss(ActionBase):
        """
Fires an explosive projectile at the designated area.
        """
        id = 2237
        name = {'Iron Kiss', '炮击'}

    class SpindlyFinger(ActionBase):
        """
Fires a lightning-aspected projectile at the designated area.
Additional Effect: Stun
Duration: 1s
        """
        id = 2238
        name = {'Spindly Finger', '雷弹'}

    class FestalCant(ActionBase):
        """
Casts a minor spell upon the designated location.
        """
        id = 2360
        name = {'魔咒', 'Festal Cant'}

    class MagitekCannon(ActionBase):
        """
Fires an explosive projectile at the designated area.
※Has no effect in battle.
        """
        id = 2434
        name = {'魔导加农炮', 'Magitek Cannon'}

    class PhotonStream(ActionBase):
        """
Fires a short-range burst of energy in a straight line before you.
※Has no effect in battle.
        """
        id = 2435
        name = {'魔导光子炮', 'Photon Stream'}

    class FieryBreath(ActionBase):
        """
Emits a stream of white-hot flames.
※Has no effect in battle.
        """
        id = 2436
        name = {'Fiery Breath', '烈火吐息'}

    class Sneeze(ActionBase):
        """
Discharges a shower of lukewarm spittle onto an unfortunate target.
※Has no effect in battle.
        """
        id = 2437
        name = {'喷嚏', 'Sneeze'}

    class Saturate(ActionBase):
        """
Sprays tepid water over target.
        """
        id = 2620
        name = {'Saturate', '喷水'}

    class Cannonfire(ActionBase):
        """
Fires an explosive projectile at the designated area.
        """
        id = 2630
        name = {'Cannonfire', '炮击'}

    class ImpPunch(ActionBase):
        """
Delivers an impotent attack. In certain cases, may remove the Wet Plate status.
        """
        id = 3139
        name = {'Imp Punch', '河童拳'}

    class IronKiss(ActionBase):
        """
Fires an explosive projectile at the designated area.
        """
        id = 3377
        name = {'Iron Kiss', '炮击'}

    class SpindlyFinger(ActionBase):
        """
Fires a lightning-aspected projectile at the designated area.
Additional Effect: Stun
Duration: 1s
        """
        id = 3378
        name = {'Spindly Finger', '雷弹'}

    class PitchBomb(ActionBase):
        """
Coats the ground with a viscid sap, slowing the movement speed of any who enter.
        """
        id = 3379
        name = {'粘着弹', 'Pitch Bomb'}

    class Quickchant(ActionBase):
        """
Delivers a ranged attack.
        """
        id = 3504
        name = {'怒喊', 'Quickchant'}

    class LowVoltage(ActionBase):
        """
Emits a bright, harmless charge.
        """
        id = 3506
        name = {'Low Voltage', '低压电流'}

    class Heavydoom(ActionBase):
        """
Fires a pressurized round of ammunition. Has no effect against oversized targets.
        """
        id = 4062
        name = {'重压弹', 'Heavydoom'}

    class Cracklyplume(ActionBase):
        """
Fires a hypercharged round of ammunition capable of electrocuting living targets. Has no effect on machina.
        """
        id = 4063
        name = {'电压弹', 'Cracklyplume'}

    class Meltyspume(ActionBase):
        """
Fires a round of armor-piercing ammunition.
        """
        id = 4064
        name = {'强酸弹', 'Meltyspume'}

    class Stickyloom(ActionBase):
        """
Activates electromagnets capable of drawing in a target.
        """
        id = 4065
        name = {'Stickyloom', '电磁石'}

    class Recharge(ActionBase):
        """
Saps a target of its electrical charge.
>> 345, Recharge, Damage dealt is increased, while weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
        """
        id = 4067
        name = {'Recharge', '充电'}

    class Buffet(ActionBase):
        """
Commands your griffin to flap its wings.
        """
        id = 4583
        name = {'突风', 'Buffet'}

    class Buffet(ActionBase):
        """
Commands your griffin to flap its wings.
※Has no effect in battle.
        """
        id = 4584
        name = {'突风', 'Buffet'}

    class Trample(ActionBase):
        """
Commands your marid to stomp the earth.
        """
        id = 4585
        name = {'踩踏', 'Trample'}

    class Trample(ActionBase):
        """
Commands your marid to stomp the earth.
※Has no effect in battle.
        """
        id = 4586
        name = {'踩踏', 'Trample'}

    class SilencingCant(ActionBase):
        """
Casts a minor spell to prevent curses of transfiguration.
※Has no effect in battle.
        """
        id = 4592
        name = {'清扫魔咒', 'Silencing Cant'}

    class SelfDetonate(ActionBase):
        """
Initiate self-detonation.
        """
        id = 4800
        name = {'Self-detonate', '雾散爆发'}

    class Heavydoom(ActionBase):
        """
Fires a pressurized round of ammunition. Has no effect against oversized targets.
        """
        id = 4913
        name = {'重压弹', 'Heavydoom'}

    class Cracklyplume(ActionBase):
        """
Fires a hypercharged round of ammunition capable of electrocuting living targets. Has no effect on machina.
        """
        id = 4914
        name = {'电压弹', 'Cracklyplume'}

    class Meltyspume(ActionBase):
        """
Fires a round of armor-piercing ammunition.
        """
        id = 4915
        name = {'强酸弹', 'Meltyspume'}

    class Stickyloom(ActionBase):
        """
Activates electromagnets capable of drawing in a target.
        """
        id = 4916
        name = {'Stickyloom', '电磁石'}

    class Recharge(ActionBase):
        """
Saps a target of its electrical charge.
>> 345, Recharge, Damage dealt is increased, while weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
        """
        id = 4917
        name = {'Recharge', '充电'}

    class SilencingCant(ActionBase):
        """
Casts a minor spell to prevent curses of transfiguration.
        """
        id = 4930
        name = {'清扫魔咒', 'Silencing Cant'}

    class Buffet(ActionBase):
        """
Fills lungs with air then releases it in a single powerful gust.
        """
        id = 4931
        name = {'突风', 'Buffet'}

    class AirCombatManeuver(ActionBase):
        """
Do a barrel roll!
※Has no effect in battle.
        """
        id = 4976
        name = {'Air Combat Maneuver', '空战机动'}

    class Fumigate(ActionBase):
        """
Evenly distributes the Vath solution in a fine mist.
        """
        id = 5872
        name = {'Fumigate', '散播'}

    class Saturate(ActionBase):
        """
Sprays tepid water over target.
        """
        id = 6143
        name = {'Saturate', '喷水'}

    class Pummel(ActionBase):
        """
Deals damage to a target.
        """
        id = 6273
        name = {'Pummel', '殴打'}

    class VoidFireIi(ActionBase):
        """
Deals damage to nearby enemies while increasing vulnerability.
        """
        id = 6274
        name = {'虚空烈炎', 'Void Fire II'}

    class Roar(ActionBase):
        """
Emits a deafening roar charged with arcane dragon magicks.
        """
        id = 6293
        name = {'咆哮', 'Roar'}

    class Seed(ActionBase):
        """
Disperses countless moogle-soothing cloud mallow seeds into the air.
        """
        id = 6294
        name = {'Seed', '绒毛散播'}

    class Buffet(ActionBase):
        """
Fills lungs with air then releases it in a single powerful gust.
※Has no effect in battle.
        """
        id = 6295
        name = {'突风', 'Buffet'}

    class Fumigate(ActionBase):
        """
Evenly distributes Vath solution in a fine mist.
※Has no effect in battle.
        """
        id = 6296
        name = {'Fumigate', '散播'}

    class Seed(ActionBase):
        """
Disperses countless moogle-soothing cloud mallow seeds into the air.
※Has no effect in battle.
        """
        id = 6297
        name = {'Seed', '绒毛散播'}

    class MogatoryMogDance(ActionBase):
        """
Dance! Dance I say!
※Has no effect in battle.
        """
        id = 6324
        name = {'Mogatory Mog Dance', '莫古莫古回旋'}

    class HeavenlyJudge(ActionBase):
        """
Stuns and deals damage to all nearby targets. Damage increased for certain enemies.
        """
        id = 6871
        name = {'天罚', 'Heavenly Judge'}

    class Shockobo(ActionBase):
        """
Releases a shockingly cute chocobo chick.
        """
        id = 7599
        name = {'Shockobo', '陆行鸟玩偶'}

    class Shockobo(ActionBase):
        """
Releases a shockingly cute chocobo chick.
※Has no effect in battle.
        """
        id = 7600
        name = {'Shockobo', '陆行鸟玩偶'}

    class MagitekCannon(ActionBase):
        """
Fires an explosive projectile at the designated area.
        """
        id = 7619
        name = {'魔导加农炮', 'Magitek Cannon'}

    class PhotonStream(ActionBase):
        """
Fires a short-range burst of energy in a straight line before you.
        """
        id = 7620
        name = {'魔导光子炮', 'Photon Stream'}

    class DiffractiveMagitekCannon(ActionBase):
        """
Fires an explosive projectile at the designated area.
        """
        id = 7621
        name = {'魔导加农散弹炮', 'Diffractive Magitek Cannon'}

    class HighPoweredMagitekCannon(ActionBase):
        """
Fires a concentrated burst of energy in a straight line before you.
        """
        id = 7622
        name = {'High-powered Magitek Cannon', '高功率魔导加农炮'}

    class SmokeScreen(ActionBase):
        """
Throw an incendiary device that creates a blanket of smoke temporarily granting you the Stealth status.
>> 789, Smoke Screen, Enmity generation is reduced.
        """
        id = 7816
        name = {'烟雾弹', 'Smoke Screen'}

    class MagitekPulse(ActionBase):
        """
Fires an explosive projectile at the designated area.
Additional Effect: Binds magna roader
Duration: 4s
        """
        id = 7962
        name = {'Magitek Pulse', '魔导脉冲弹'}

    class Vril(ActionBase):
        """
Use the aetheric residue lingering on your body to temporarily disguise yourself as one of Lakshmi's loyal dreamers.
>> 1290, Vril, Damage taken by certain attacks is reduced or converted in to HP.
        """
        id = 8517
        name = {'元气', 'Vril'}

    class DoubleBubble(ActionBase):
        """
Sprays a jet of bubbly water.
        """
        id = 8623
        name = {'水泡', 'Double Bubble'}

    class MagitekPulse(ActionBase):
        """
Fires a magitek-powered burst of energy.
        """
        id = 8624
        name = {'Magitek Pulse', '魔导脉冲'}

    class MagitekThunder(ActionBase):
        """
Emits a bolt of magitek-powered lightning.
        """
        id = 8625
        name = {'Magitek Thunder', '魔导闪雷'}

    class ImpPunch(ActionBase):
        """
Delivers an impotent attack.
        """
        id = 9035
        name = {'Imp Punch', '河童拳'}

    class AntiGravityGimbal(ActionBase):
        """
Simulates the spell Levitate using Nero tol Scaeva's odd contraption.
        """
        id = 9066
        name = {'Anti-gravity Gimbal', '反重力装置'}

    class AethericSiphon(ActionBase):
        """
Activates the instrument.
        """
        id = 9102
        name = {'Aetheric Siphon', '以太干扰器'}

    class Vril(ActionBase):
        """
Use the aetheric residue lingering on your body to temporarily disguise yourself as one of Lakshmi's loyal dreamers.
>> 1290, Vril, Damage taken by certain attacks is reduced or converted in to HP.
        """
        id = 9345
        name = {'元气', 'Vril'}

    class AntiGravityGimbal(ActionBase):
        """
Simulates the spell Levitate using Nero tol Scaeva's odd contraption.
        """
        id = 9483
        name = {'Anti-gravity Gimbal', '反重力装置'}

    class Shatterstone(ActionBase):
        """
Sets an enchanted trap that triggers upon contact.
        """
        id = 9823
        name = {'爆炸岩', 'Shatterstone'}

    class Deflect(ActionBase):
        """
Scatters potentially harmful aether.
        """
        id = 10006
        name = {'偏折屏障', 'Deflect'}

    class Inhale(ActionBase):
        """
Orders the manta to draw water into its gaping maw.
        """
        id = 10013
        name = {'吸引', 'Inhale'}

    class Inhale(ActionBase):
        """
Orders the manta to draw water into its gaping maw.
※Has no effect in battle.
        """
        id = 10014
        name = {'吸引', 'Inhale'}

    class Starburst(ActionBase):
        """
Toss a Starburst into the air.
        """
        id = 10019
        name = {'礼花筒', 'Starburst'}

    class Starburst(ActionBase):
        """
Toss a Starburst into the air.
※Has no effect in battle.
        """
        id = 10020
        name = {'礼花筒', 'Starburst'}

    class Return(ActionBase):
        """
Returns your team to the starting area. Can be used while engaged in battle.
>> 2452, Return, Aetherially entwined with the temporal manifold. You will be stunned and drawn back to your aetherial trace when this effect expires.
        """
        id = 10061
        name = {'返回', 'Return'}

    class MegaPotion(ActionBase):
        """
Restores a moderate amount of health.
        """
        id = 10229
        name = {'Mega Potion', '回复药“大”'}

    class RedPaint(ActionBase):
        """
Red paint drips from the tip of this massive brush made from Alpha's feathers.
>> 1470, Red Paint, Carrying a pot of red paint.
        """
        id = 10262
        name = {'Red Paint', '红色陆行鸟之笔'}

    class YellowPaint(ActionBase):
        """
Yellow paint drips from the tip of this massive brush made from Alpha's feathers.
>> 1467, Yellow Paint, Carrying a pot of yellow paint.
        """
        id = 10263
        name = {'黄色陆行鸟之笔', 'Yellow Paint'}

    class BlackPaint(ActionBase):
        """
Black paint drips from the tip of this massive brush made from Alpha's feathers.
>> 1469, Black Paint, Carrying a pot of black paint.
        """
        id = 10264
        name = {'Black Paint', '黑色陆行鸟之笔'}

    class BluePaint(ActionBase):
        """
Blue paint drips from the tip of this massive brush made from Alpha's feathers.
>> 1468, Blue Paint, Carrying a pot of light blue paint.
        """
        id = 10265
        name = {'Blue Paint', '蓝色陆行鸟之笔'}

    class Snort(ActionBase):
        """
Emit a sinal blast precisely powerful enough to misdirect the wind itself.
        """
        id = 10270
        name = {'Snort', '鼻息'}

    class ChocoboBrush(ActionBase):
        """
A brush made from Alpha's feathers.
        """
        id = 10401
        name = {'陆行鸟之笔', 'Chocobo Brush'}

    class CheerJump(ActionBase):
        """
Might as well use a red light to cheer on your favorite performer.
        """
        id = 10713
        name = {'Cheer Jump', '声援小红'}

    class CheerWave(ActionBase):
        """
Use a yellow light to cheer on your favorite performer like you just don't care.
        """
        id = 10714
        name = {'Cheer Wave', '声援小黄'}

    class CheerOn(ActionBase):
        """
Use a pair of blue lights to clear your favorite performer for landing.
        """
        id = 10715
        name = {'Cheer On', '声援小蓝'}

    class CheerJump(ActionBase):
        """
Might as well use a red light to cheer on your favorite performer.
        """
        id = 10716
        name = {'Cheer Jump', '声援小红'}

    class CheerWave(ActionBase):
        """
Use a yellow light to cheer on your favorite performer like you just don't care.
        """
        id = 10717
        name = {'Cheer Wave', '声援小黄'}

    class CheerOn(ActionBase):
        """
Use a pair of blue lights to clear your favorite performer for landing.
        """
        id = 10718
        name = {'Cheer On', '声援小蓝'}

    class CurtainCall(ActionBase):
        """
Removes the “Face in the Crowd” status.
        """
        id = 11063
        name = {'离场', 'Curtain Call'}

    class RuinIii(ActionBase):
        """
Deals unaspected damage with a potency of 200.
        """
        id = 11191
        name = {'毁荡', 'Ruin III'}

    class Physick(ActionBase):
        """
Restores target's HP.
Cure Potency: 400
        """
        id = 11192
        name = {'Physick', '医术'}

    class Starstorm(ActionBase):
        """
Deals unaspected damage with a potency of 3,600 to all enemies near point of impact.
        """
        id = 11193
        name = {'星体风暴', 'Starstorm'}

    class TriShackle(ActionBase):
        """
Deals unaspected damage with a potency of 30 to target and all enemies nearby it.
Additional Effect: Bind
Duration: 20s
        """
        id = 11482
        name = {'Tri-shackle', '三重惩戒'}

    class Wasshoi(ActionBase):
        """
Lead the mikoshi bearers in a rousing display of civilization and enlightenment.
        """
        id = 11499
        name = {'喊口号', 'Wasshoi'}

    class Wasshoi(ActionBase):
        """
Lead the mikoshi bearers in a rousing display of civilization and enlightenment.
※Has no effect in battle.
        """
        id = 11500
        name = {'喊口号', 'Wasshoi'}

    class Cannonfire(ActionBase):
        """
Fires an explosive projectile at the designated area.
        """
        id = 12257
        name = {'Cannonfire', '炮击'}

    class MogHeaven(ActionBase):
        """
Fires a short-range burst of energy in a straight line before you.
Additional Effect: Increased damage taken
        """
        id = 12577
        name = {'Mog Heaven', '莫古力天堂'}

    class BringItPom(ActionBase):
        """
Restores HP and HP of all nearby party members, and grants healing over time as well as increased damage dealt.
        """
        id = 12578
        name = {'声援', 'Bring It Pom'}

    class OmegaJammer(ActionBase):
        """
Emits a pulse of concentrated electromagnetic energy.
        """
        id = 12911
        name = {'Omega Jammer', '欧米茄干扰器'}

    class WisdomOfTheAetherweaver(ActionBase):
        """
Increases magic damage dealt by 60%.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1631, Wisdom of the Aetherweaver, Magic damage is increased.
        """
        id = 12958
        name = {'术士的记忆', 'Wisdom of the Aetherweaver'}

    class WisdomOfTheMartialist(ActionBase):
        """
Increases damage dealt by 40%.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1632, Wisdom of the Martialist, Damage dealt is increased.
        """
        id = 12959
        name = {'斗士的记忆', 'Wisdom of the Martialist'}

    class WisdomOfThePlatebearer(ActionBase):
        """
Increases defense by 150% and maximum HP by 50%.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1633, Wisdom of the Platebearer, Maximum HP and defense are increased.
        """
        id = 12960
        name = {'Wisdom of the Platebearer', '重骑兵的记忆'}

    class WisdomOfTheGuardian(ActionBase):
        """
Increases defense by 50% and maximum HP by 10%.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1634, Wisdom of the Guardian, Maximum HP and defense are increased.
        """
        id = 12961
        name = {'Wisdom of the Guardian', '守护者的记忆'}

    class WisdomOfTheOrdained(ActionBase):
        """
Increases maximum MP by 50% and healing magic potency by 25%.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1635, Wisdom of the Ordained, Maximum MP and healing magic potency are increased.
        """
        id = 12962
        name = {'Wisdom of the Ordained', '祭司的记忆'}

    class WisdomOfTheSkirmisher(ActionBase):
        """
Increases damage dealt by 20%.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1636, Wisdom of the Skirmisher, Damage dealt is increased.
        """
        id = 12963
        name = {'Wisdom of the Skirmisher', '武人的记忆'}

    class WisdomOfTheWatcher(ActionBase):
        """
Increases evasion by 25% while reducing damage dealt by 5%.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1637, Wisdom of the Watcher, Evasion is enhanced, while damage dealt is reduced.
        """
        id = 12964
        name = {'Wisdom of the Watcher', '斥候的记忆'}

    class WisdomOfTheTemplar(ActionBase):
        """
Increases healing magic potency by 50% and maximum HP by 30%, while reducing damage dealt by 5%.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1638, Wisdom of the Templar, Maximum HP and healing magic potency are increased, while damage dealt is reduced.
        """
        id = 12965
        name = {'Wisdom of the Templar', '圣骑士的记忆'}

    class WisdomOfTheIrregular(ActionBase):
        """
Increases damage dealt by 30% while reducing magic defense by 60%.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1639, Wisdom of the Irregular, Damage dealt is increased, while magic defense is reduced.
        """
        id = 12966
        name = {'狂战士的记忆', 'Wisdom of the Irregular'}

    class WisdomOfTheBreathtaker(ActionBase):
        """
Increases poison resistance and movement speed, including mount speed, and increases evasion by 10%.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1640, Wisdom of the Breathtaker, Movement speed, evasion, and poison resistance are increased.
        """
        id = 12967
        name = {'Wisdom of the Breathtaker', '盗贼的记忆'}

    class SpiritOfTheRemembered(ActionBase):
        """
Increases maximum HP by 10% and accuracy by 30%.
Additional Effect: Grants a 70% chance of automatic revival upon KO
Duration: 180m
>> 1641, Spirit of the Remembered, Maximum HP and accuracy are increased. Chance of automatic revival upon KO.
        """
        id = 12968
        name = {'Spirit of the Remembered', '英杰的加护'}

    class ProtectL(ActionBase):
        """
Increases the physical defense of target by 1,000.
Duration: 30m
>> 1642, Protect L, Physical defense is increased.
        """
        id = 12969
        name = {'文理护盾', 'Protect L'}

    class ShellL(ActionBase):
        """
Increases the magic defense of target by 1,000.
Duration: 30m
>> 1643, Shell L, Magic defense is increased.
        """
        id = 12970
        name = {'Shell L', '文理魔盾'}

    class DeathL(ActionBase):
        """
KOs target. The less the target's HP, the greater the chance of success.
        """
        id = 12971
        name = {'文理即死', 'Death L'}

    class FocusL(ActionBase):
        """
Grants a stack of Boost, up to a maximum of 16.
Boost Bonus: Increases potency of next weaponskill by 30% per stack
Duration: 30s
Shares a recast timer with all weaponskills.
        """
        id = 12972
        name = {'Focus L', '文理蓄力'}

    class ParalyzeL(ActionBase):
        """
Afflicts target with Paralysis.
Duration: 60s
        """
        id = 12973
        name = {'文理麻痹', 'Paralyze L'}

    class ParalyzeLIii(ActionBase):
        """
Afflicts target and all neaby enemies with Paralysis.
Duration: 60s
        """
        id = 12974
        name = {'Paralyze L III', '文理强麻痹'}

    class SwiftL(ActionBase):
        """
Greatly increases movement speed.
Duration: 10s
>> 1644, Swift L, Movement speed is increased.
        """
        id = 12975
        name = {'文理敏捷', 'Swift L'}

    class FeatherfootL(ActionBase):
        """
Increases evasion by 15%.
Duration: 45s
        """
        id = 12976
        name = {'文理飘羽步', 'Featherfoot L'}

    class SpiritDartL(ActionBase):
        """
Delivers a ranged attack with a potency of 100.
Additional Effect: Afflicts target with Spirit Dart L, increasing damage taken by 8%
Duration: 60s
>> 1654, Spirit Dart L, Damage taken is increased.
        """
        id = 12977
        name = {'文理精神镖', 'Spirit Dart L'}

    class CatastropheL(ActionBase):
        """
Deals unaspected damage to all nearby enemies with a potency of 4,000, while dealing damage with a potency of 999,999 to self.
        """
        id = 12978
        name = {'文理天灾', 'Catastrophe L'}

    class DispelL(ActionBase):
        """
Removes one beneficial status from target.
        """
        id = 12979
        name = {'文理驱魔', 'Dispel L'}

    class FeintL(ActionBase):
        """
Delivers an attack with a potency of 100.
Additional Effect: Reduces target's evasion
Duration: 60s
        """
        id = 12980
        name = {'文理虚枪', 'Feint L'}

    class StealthL(ActionBase):
        """
Blend in with your surroundings, making it impossible for most enemies to detect you, but reducing movement speed by 50%. Has no effect on certain enemies with special sight.
Cannot be executed while in combat.
Effect ends upon use of any action other than Sprint, or upon reuse.
        """
        id = 12981
        name = {'Stealth L', '文理潜行'}

    class AetherialManipulationL(ActionBase):
        """
Rush to a target's side.
Unable to cast if bound.
        """
        id = 12982
        name = {'文理以太步', 'Aetherial Manipulation L'}

    class BackstepL(ActionBase):
        """
Jump 10 yalms back from current position. Cannot be executed while bound.
        """
        id = 12983
        name = {'文理后跳', 'Backstep L'}

    class TranquilizerL(ActionBase):
        """
Stuns target.
Duration: 8s
        """
        id = 12984
        name = {'文理镇定', 'Tranquilizer L'}

    class BloodbathL(ActionBase):
        """
Converts a portion of damage dealt into HP.
Duration: 45s
>> 1677, Bloodbath L, Attacks generate HP equal to a portion of damage dealt.
        """
        id = 12985
        name = {'Bloodbath L', '文理浴血'}

    class RejuvenateL(ActionBase):
        """
Instantly restores 50% of maximum HP and MP.
        """
        id = 12986
        name = {'文理充能', 'Rejuvenate L'}

    class HaymakerL(ActionBase):
        """
Delivers an attack with a potency of 300.
Can only be executed immediately after evading an attack.
Additional Effect: Slow +20%
Duration: 30s
        """
        id = 12987
        name = {'Haymaker L', '文理反攻'}

    class RapidRecastL(ActionBase):
        """
Shortens recast time for next ability used by 50%.
Duration: 15s
        """
        id = 12988
        name = {'文理高速复唱', 'Rapid Recast L'}

    class CureL(ActionBase):
        """
Restores target's HP.
Cure Potency: 9,000
        """
        id = 12989
        name = {'Cure L', '文理治疗'}

    class CureLIi(ActionBase):
        """
Restores target's HP.
Cure Potency: 12,000
        """
        id = 12990
        name = {'文理救疗', 'Cure L II'}

    class StoneskinL(ActionBase):
        """
Creates a barrier around target that absorbs damage totaling 10% of target's maximum HP.
Duration: 30s
        """
        id = 12991
        name = {'Stoneskin L', '文理石肤'}

    class CureLIii(ActionBase):
        """
Restores HP of target and all party members nearby target.
Cure Potency: 9,000
        """
        id = 12992
        name = {'文理愈疗', 'Cure L III'}

    class RegenL(ActionBase):
        """
Grants Regen to target.
Cure Potency: 2,500
Duration: 21s
        """
        id = 12993
        name = {'Regen L', '文理再生'}

    class EsunaL(ActionBase):
        """
Removes a single detrimental effect from target.
        """
        id = 12994
        name = {'Esuna L', '文理康复'}

    class IncenseL(ActionBase):
        """
Gesture threateningly, placing yourself at the top of a target's enmity list and increasing enmity generation.
Duration: 15s
>> 1657, Incense L, Enmity is increased.
        """
        id = 12995
        name = {'Incense L', '文理激怒'}

    class RaiseL(ActionBase):
        """
Resurrects target to a weakened state.
        """
        id = 12996
        name = {'Raise L', '文理复活'}

    class BraveryL(ActionBase):
        """
Increases target's damage dealt by 10%.
Duration: 300s
>> 1646, Bravery L, Damage dealt is increased.
        """
        id = 12997
        name = {'Bravery L', '文理勇气'}

    class SolidShieldL(ActionBase):
        """
Reduces physical damage taken by 99%.
Duration: 8s
        """
        id = 12998
        name = {'Solid Shield L', '文理物理盾'}

    class SpellShieldL(ActionBase):
        """
Reduces magic damage taken by 99%.
Duration: 8s
        """
        id = 12999
        name = {'Spell Shield L', '文理魔法盾'}

    class ReflectL(ActionBase):
        """
Creates a magic-reflecting barrier around self or party member.
Duration: 10s
>> 1649, Reflect L, Reflecting magic back on its caster.
        """
        id = 13000
        name = {'Reflect L', '文理反射'}

    class SmiteL(ActionBase):
        """
Delivers an attack with a potency of 1,000.
Can only be executed when your HP is below 50%.
Additional Effect: Restores an amount of own HP proportional to damage dealt
        """
        id = 13001
        name = {'文理猛击', 'Smite L'}

    class RefreshL(ActionBase):
        """
Increases the amount of magia aether regenerated over time by self and nearby party members.
Duration: 30s
>> 1651, Refresh L, Magia aether regeneration is increased.
        """
        id = 13002
        name = {'Refresh L', '文理醒神'}

    class BanishL(ActionBase):
        """
Deals unaspected damage with a potency of 200.
Additional Effect: Afflicts undead targets with Banish L, increasing damage taken by 25%
Duration: 60s
>> 1655, Banish L, Damage taken is increased.
        """
        id = 13003
        name = {'文理放逐', 'Banish L'}

    class BanishLIii(ActionBase):
        """
Deals unaspected damage with a potency of 150 to target and all enemies nearby it.
Additional Effect: Afflicts undead targets with Banish L, increasing damage taken by 25%
Duration: 60s
        """
        id = 13004
        name = {'Banish L III', '文理强放逐'}

    class MagicBurstL(ActionBase):
        """
Increases spell damage by 100% while increasing MP cost.
Duration: 20s
        """
        id = 13005
        name = {'文理魔法爆发', 'Magic Burst L'}

    class DoubleEdgeL(ActionBase):
        """
Increases physical damage dealt while dealing damage to self over time.
Stacks increase every 3 seconds, up to a maximum of 16. For each stack, physical damage dealt is increased by 15%, and potency of damage dealt to self increases by 360.
Duration: 48s
>> 1653, Double Edge L, Physical damage dealt is increasing, while you are sustaining damage over time.
        """
        id = 13006
        name = {'Double Edge L', '文理双刃剑'}

    class EagleEyeShotL(ActionBase):
        """
Delivers a ranged attack with a potency of 80. Potency increases up to 1,000% the lower the target's HP.
Generates significant enmity upon use.
        """
        id = 13007
        name = {'文理锐眼追击', 'Eagle Eye Shot L'}

    class TricksomeTreat(ActionBase):
        """
Casts a spell that alarms targets within the designated area.
        """
        id = 13265
        name = {'Tricksome Treat', '不给糖就捣蛋'}

    class Unveil(ActionBase):
        """
Removes the effects of transfiguration.
        """
        id = 13266
        name = {'Unveil', '解除变身'}

    class StoneIvOfTheSeventhDawn(ActionBase):
        """
Deals earth damage with a potency of 140.
        """
        id = 13423
        name = {'血盟崩石', 'Stone IV of the Seventh Dawn'}

    class AeroIiOfTheSeventhDawn(ActionBase):
        """
Deals wind damage with a potency of 50.
Additional Effect: Wind damage over time
Potency: 30
Duration: 18s
        """
        id = 13424
        name = {'Aero II of the Seventh Dawn', '血盟烈风'}

    class CureIiOfTheSeventhDawn(ActionBase):
        """
Restores target's HP.
Cure Potency: 700
        """
        id = 13425
        name = {'Cure II of the Seventh Dawn', '血盟救疗'}

    class Aetherwell(ActionBase):
        """
Restores MP.
        """
        id = 13426
        name = {'Aetherwell', '补魔'}

    class HeavenlySword(ActionBase):
        """
Wield the ethereal sword to strike forward.
        """
        id = 14414
        name = {'Heavenly Sword', '圣剑攻击'}

    class HeavenlyShield(ActionBase):
        """
Wield the ethereal shield to defend against frontal attacks.
>> 1735, Heavenly Shield, Protected by an ethereal shield. Damage taken from certain attacks is reduced.
        """
        id = 14415
        name = {'Heavenly Shield', '圣盾防御'}

    class PerceptionL(ActionBase):
        """
Reveals all traps within a 15-yalm radius. If no traps exist within 15 yalms, detects whether any traps are present within a 36-yalm radius.
Only effective within dungeons.
        """
        id = 14476
        name = {'Perception L', '文理探景'}

    class WisdomOfTheElder(ActionBase):
        """
Increases magic damage dealt by 35% and magic defense by 1,000, while decreasing spell MP cost.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1739, Wisdom of the Elder, Magic damage dealt and magic defense are increased. Spell MP cost is reduced.
        """
        id = 14477
        name = {'贤者的记忆', 'Wisdom of the Elder'}

    class WisdomOfTheDuelist(ActionBase):
        """
Increases physical damage dealt by 40% and maximum HP by 15%.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1740, Wisdom of the Duelist, Physical damage dealt and maximum HP are increased.
        """
        id = 14478
        name = {'剑豪的记忆', 'Wisdom of the Duelist'}

    class WisdomOfTheFiendhunter(ActionBase):
        """
Increases physical damage dealt by 25% and evasion by 25%.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1741, Wisdom of the Fiendhunter, Physical damage dealt and evasion are increased.
        """
        id = 14479
        name = {'Wisdom of the Fiendhunter', '弓圣的记忆'}

    class WisdomOfTheIndomitable(ActionBase):
        """
Increases defense by 2,000.
Grants one stack of HP Boost each time damage equal to or greater than half of maximum HP is taken from a single-target attack.
Cannot be used with other Wisdom abilities.
Effect ends upon reuse or upon replacement of duty action.
>> 1742, Wisdom of the Indomitable, Defense is increased. Maximum HP is boosted each time you take damage equivalent to at least 50% of your maximum HP from a single-target attack.
        """
        id = 14480
        name = {'豪杰的记忆', 'Wisdom of the Indomitable'}

    class SacrificeL(ActionBase):
        """
Restores all of a KO'd target's HP.
Cannot be executed if currently afflicted with Sacrifice.
Additional Effect: Inflicts Sacrifice on self
Sacrifice Effect: When effect expires, you will be KO'd
Duration: 10s
        """
        id = 14481
        name = {'文理献祭', 'Sacrifice L'}

    class WarpStrike(ActionBase):
        """
Move instantly to the target while delivering a physical attack. Potency increases with initial distance from target.
        """
        id = 14597
        name = {'Warp-strike', '位移破击'}

    class Kyokufu(ActionBase):
        """
Delivers an attack with a potency of 180.
        """
        id = 14840
        name = {'Kyokufu', '极风'}

    class Ajisai(ActionBase):
        """
Delivers an attack with a potency of 100.
Additional Effect: Damage over time
Potency: 30
Duration: 30s
>> 1779, Ajisai, Fine cuts are causing damage over time.
        """
        id = 14841
        name = {'Ajisai', '紫阳花'}

    class HissatsuGyoten(ActionBase):
        """
Rushes target and delivers an attack with a potency of 100.
        """
        id = 14842
        name = {'必杀剑·晓天', 'Hissatsu: Gyoten'}

    class SecondWind(ActionBase):
        """
Instantly restores own HP.
Cure Potency: 500
Cure potency varies with current attack power.
        """
        id = 15375
        name = {'内丹', 'Second Wind'}

    class Interject(ActionBase):
        """
Interrupts the use of a target's action.
        """
        id = 15537
        name = {'插言', 'Interject'}

    class Present(ActionBase):
        """
Present an eggsquisite gift.
        """
        id = 15553
        name = {'Present', '发礼物'}

    class FightOrFlight(ActionBase):
        """
Increases physical damage dealt by 25%.
Duration: 25s
>> 76, Fight or Flight, Physical damage dealt is increased.
        """
        id = 15870
        name = {'Fight or Flight', '战逃反应'}

    class SoothingPotion(ActionBase):
        """
Instantly restores own HP via the consumption of a curious Crystarium concoction.
        """
        id = 16436
        name = {'Soothing Potion', '镇痛恢复药'}

    class ShiningBlade(ActionBase):
        """
Harnesses the power of one of Minfilia's cartridges to lacerate the target with pure light.
        """
        id = 16437
        name = {'Shining Blade', '光明之刃'}

    class PerfectDeception(ActionBase):
        """
Completely conceals own presence by severely restricting the flow of life-sustaining aether.
Additional Effect: Fading Fast
>> 1906, Perfect Deception, Having severely restricted the flow of life-sustaining aether, your presence is concealed but you are subject to the effect of Fading Fast.
        """
        id = 16438
        name = {'Perfect Deception', '完美隐形'}

    class LeapOfFaith(ActionBase):
        """
Harnesses the mysterious power of Minfilia's experimental cartridge to deliver a powerful onslaught.
        """
        id = 16439
        name = {'Leap of Faith', '晶壤光斩'}

    class RonkanFireIii(ActionBase):
        """
Deals fire damage with a potency of 430.
        """
        id = 16574
        name = {'隆卡爆炎', 'Ronkan Fire III'}

    class RonkanBlizzardIii(ActionBase):
        """
Deals ice damage with a potency of 240.
Additional Effect: Restores MP
        """
        id = 16575
        name = {'Ronkan Blizzard III', '隆卡冰封'}

    class RonkanThunderIii(ActionBase):
        """
Deals lightning damage with a potency of 200.
Additional Effect: Lightning damage over time
Potency: 40
Duration: 24s
        """
        id = 16576
        name = {'隆卡暴雷', 'Ronkan Thunder III'}

    class RonkanFlare(ActionBase):
        """
Deals fire damage with a potency of 460 to target and all enemies nearby it.
        """
        id = 16577
        name = {'隆卡核爆', 'Ronkan Flare'}

    class FallingStar(ActionBase):
        """
Deals unaspected damage with a potency of 1,500 to all enemies near point of impact.
        """
        id = 16578
        name = {'坠星', 'Falling Star'}

    class RoughDivide(ActionBase):
        """
Delivers a jumping attack with a potency of 200.
Maximum Charges: 2
Cannot be executed while bound.
        """
        id = 16804
        name = {'粗分斩', 'Rough Divide'}

    class RonkanCureIi(ActionBase):
        """
Restores target's HP.
Cure Potency: 1300
        """
        id = 17000
        name = {'隆卡救疗', 'Ronkan Cure II'}

    class RonkanMedica(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 500
        """
        id = 17001
        name = {'隆卡医治', 'Ronkan Medica'}

    class RonkanEsuna(ActionBase):
        """
Removes a single detrimental effect from target.
        """
        id = 17002
        name = {'隆卡康复', 'Ronkan Esuna'}

    class RonkanStoneIi(ActionBase):
        """
Deals earth damage with a potency of 200.
        """
        id = 17003
        name = {'隆卡坚石', 'Ronkan Stone II'}

    class RonkanRenew(ActionBase):
        """
Restores all of a target's HP.
        """
        id = 17004
        name = {'隆卡痊愈', 'Ronkan Renew'}

    class AcidicBite(ActionBase):
        """
Delivers an attack with a potency of 300.
Additional Effect: Acidic Bite
Potency: 120
Duration: 30s
>> 2073, Acidic Bite, Toxins are causing damage over time.
        """
        id = 17122
        name = {'酸咬箭', 'Acidic Bite'}

    class HeavyShot(ActionBase):
        """
Delivers an attack with a potency of 550.
        """
        id = 17123
        name = {'强力射击', 'Heavy Shot'}

    class RadiantArrow(ActionBase):
        """
Delivers an attack with a potency of 1,100.
        """
        id = 17124
        name = {'Radiant Arrow', '星光箭'}

    class DullingArrow(ActionBase):
        """
Interrupts the use of a target's action.
        """
        id = 17125
        name = {'消声箭', 'Dulling Arrow'}

    class ChivalrousSpirit(ActionBase):
        """
Restores target's HP.
Cure Potency: 1200
Additional Effect: Restores to self 50% of HP restored to target if target is a party member
        """
        id = 17236
        name = {'骑士精神', 'Chivalrous Spirit'}

    class SouldeepInvisibility(ActionBase):
        """
Completely conceals own presence by temporarily severing the flow of life-sustaining aether.
Additional Effect: Fading Fast and Vital Sign
>> 1956, Souldeep Invisibility, Having severed the flow of life-sustaining aether, your presence is completely concealed but you are subject to the effects of Fading Fast and Vital Sign.
        """
        id = 17291
        name = {'Souldeep Invisibility', '绝脉隐形'}

    class SortOfDreadGaze(ActionBase):
        """
Fix your enemies with a gaze that won't quite strike fear into their hearts, but will certainly make them feel uncomfortable.
        """
        id = 17390
        name = {'Sort-of Dread Gaze', '恐怖视线？'}

    class SortOfDreadGaze(ActionBase):
        """
Fix your enemies with a gaze that won't quite strike fear into their hearts, but will certainly make them feel uncomfortable.
※Has no effect in battle.
        """
        id = 17391
        name = {'Sort-of Dread Gaze', '恐怖视线？'}

    class HuntersPrudence(ActionBase):
        """
Restores own HP.
Cure Potency: 1,000
Cure potency varies with current attack power.
        """
        id = 17596
        name = {'猎人的智慧', "Hunter's Prudence"}

    class Nebula(ActionBase):
        """
Reduces damage taken by 25%.
Duration: 10s
>> 1834, Nebula, Damage taken is reduced.
        """
        id = 17839
        name = {'星云', 'Nebula'}

    class Smackdown(ActionBase):
        """
Increases damage dealt by 10% and accuracy by 100%.
Duration: 10s
>> 2068, Smackdown, Accuracy and damage dealt are increased.
        """
        id = 17901
        name = {'折服', 'Smackdown'}

    class SiphonSnout(ActionBase):
        """
Sucks up any substance with a great huffing snort.
        """
        id = 18187
        name = {'Siphon Snout', '鼻吸'}

    class SiphonSnout(ActionBase):
        """
Sucks up any substance with a great huffing snort.
※Has no effect in battle.
        """
        id = 18188
        name = {'Siphon Snout', '鼻吸'}

    class SkydragonDive(ActionBase):
        """
Delivers a jumping fire-based attack with a potency of 800 to target and all enemies nearby it.
        """
        id = 18775
        name = {'苍天龙炎冲', 'Skydragon Dive'}

    class AlaMorn(ActionBase):
        """
Delivers an attack with a potency of 3,000.
Additional Effect: Absorbs a portion of damage dealt as HP
        """
        id = 18776
        name = {'绝灭', 'Ala Morn'}

    class Drachenlance(ActionBase):
        """
Delivers an attack with a potency of 500.
Additional Effect: Damage over time
Duration: 15s
        """
        id = 18777
        name = {'Drachenlance', '腾龙枪'}

    class HorridRoar(ActionBase):
        """
Delivers an attack with a potency of 600 to all nearby enemies, as well as enemies in proximity to those initially affected.
This action does not share a recast timer with any other actions.
        """
        id = 18778
        name = {'Horrid Roar', '恐惧咆哮'}

    class Stardiver(ActionBase):
        """
Delivers a jumping fire-based attack to target and all enemies nearby it with a potency of 1,500 for the first enemy, and 30% less for all remaining enemies.
        """
        id = 18780
        name = {'坠星冲', 'Stardiver'}

    class DragonshadowDive(ActionBase):
        """
Delivers an attack to target and all enemies nearby it.
        """
        id = 18781
        name = {'暗影龙炎冲', 'Dragonshadow Dive'}

    class SolicitSiphonSnout(ActionBase):
        """
Direct Ezel II to devour a dream.
        """
        id = 18813
        name = {'Solicit Siphon Snout', '鼻吸指示'}

    class Deflect(ActionBase):
        """
Scatters potentially harmful aether.
        """
        id = 18863
        name = {'偏折屏障', 'Deflect'}

    class AquaVitae(ActionBase):
        """
Restores own HP.
        """
        id = 19218
        name = {'Aqua Vitae', '生命水'}

    class CouldBeWorseBreath(ActionBase):
        """
Blows breath that is not so horrid as to stop one in their tracks, yet still unmistakably offensive, in a cone before you.
※Has no effect in battle.
        """
        id = 19275
        name = {'微微臭气', 'Could-be-worse Breath'}

    class RemoveCostume(ActionBase):
        """
Cease to wear this peculiar garb and return to wearing your usual peculiar garb.
        """
        id = 19731
        name = {'解除玩偶装', 'Remove Costume'}

    class StandFirm(ActionBase):
        """
Brace yourself to stand against even the most relentless onslaught.
        """
        id = 19994
        name = {'抵御冲击', 'Stand Firm'}

    class Seize(ActionBase):
        """
Snare a chicken in your net with a single swift motion.
        """
        id = 19997
        name = {'抓捕', 'Seize'}

    class Birdlime(ActionBase):
        """
Toss a glob of paste to stick overexcited chickens to the ground.
        """
        id = 19998
        name = {'粘鸟胶', 'Birdlime'}

    class PeculiarLight(ActionBase):
        """
Plumb the depths of the great serpent's power for no particular reason, unleashing an awe-inspiring ray of light. May or may not obliterate nonbelievers.
>> 1721, Peculiar Light, Magic damage taken is increased.
        """
        id = 20030
        name = {'Peculiar Light', '惊奇光'}

    class PeculiarLight(ActionBase):
        """
Plumb the depths of the great serpent's power for no particular reason, unleashing an awe-inspiring ray of light. May or may not obliterate nonbelievers.
※Has no effect in battle.
>> 1721, Peculiar Light, Magic damage taken is increased.
        """
        id = 20031
        name = {'Peculiar Light', '惊奇光'}

    class DazzlingDisplay(ActionBase):
        """
Commands your peacock to proudly display its plumage.
※Has no effect in battle.
        """
        id = 20064
        name = {'开屏', 'Dazzling Display'}

    class Cannonfire(ActionBase):
        """
Solves your problems with excessive explosive force.
        """
        id = 20121
        name = {'Cannonfire', '炮击'}

    class Cannonfire(ActionBase):
        """
Solves your problems with excessive explosive force.
※Has no effect in battle.
        """
        id = 20122
        name = {'Cannonfire', '炮击'}

    class BlackPaint(ActionBase):
        """
Black paint drips from the tip of this massive brush made from Alpha's feathers.
>> 1469, Black Paint, Carrying a pot of black paint.
        """
        id = 20304
        name = {'Black Paint', '黑色陆行鸟之笔'}

    class AetherCannon(ActionBase):
        """
Deals unaspected damage with a potency of 600.
        """
        id = 20489
        name = {'Aether Cannon', '以太加农炮'}

    class UltimaBuster(ActionBase):
        """
Deals unaspected damage with a potency of 1,200 to all enemies in a straight line before you.
Triggers the cooldown of weaponskills and spells upon execution.
        """
        id = 20493
        name = {'究极破坏炮', 'Ultima Buster'}

    class PyreticBooster(ActionBase):
        """
Reduces cast time and recast time of weaponskills by 25% and increases movement speed by 25%. HP is drained while in use.
Effect ends upon reuse.
>> 2294, Pyretic Booster, The G-Warrior's capabilities are enhanced, decreasing weaponskill cast and recast time and increasing movement speed. Use of this mode gradually drains HP.
        """
        id = 20494
        name = {'Pyretic Booster', '加速模式'}

    class AetherialAegis(ActionBase):
        """
Reduces damage taken by 50%. EP is drained while in use.
Effect ends upon reuse or when EP is depleted.
>> 2295, Aetherial Aegis, The G-Warrior is protected by an aetherial barrier, reducing damage taken. Use of this mode gradually drains EP.
        """
        id = 20495
        name = {'Aetherial Aegis', '以太屏障'}

    class AetherMine(ActionBase):
        """
Deals unaspected damage with a potency of 300 to target and all enemies nearby it.
Additional Effect: Increases target's damage taken by 20%
Duration: 60s
This action does not share a recast timer with any other actions.
        """
        id = 20496
        name = {'以太机雷', 'Aether Mine'}

    class CrimsonSavior(ActionBase):
        """
Deals unaspected damage with a potency of 200 to all nearby enemies.
        """
        id = 20533
        name = {'Crimson Savior', '深红救世'}

    class LostParalyzeIii(ActionBase):
        """
Afflicts target and all nearby enemies with Paralysis.
Duration: 60s
        """
        id = 20701
        name = {'失传强麻痹', 'Lost Paralyze III'}

    class LostBanishIii(ActionBase):
        """
Deals unaspected damage with a potency of 200 to target and all enemies nearby it.
Additional Effect: Increases damage undead enemies take by 25%
Duration: 60s
        """
        id = 20702
        name = {'失传强放逐', 'Lost Banish III'}

    class LostManawall(ActionBase):
        """
Temporarily applies Heavy to self, while reducing damage taken by 90% and nullifying most knockback and draw-in effects.
Duration: 6s
>> 2345, Lost Manawall, Damage taken is reduced and immune to most knockback and draw-in effects.
        """
        id = 20703
        name = {'失传坚壁', 'Lost Manawall'}

    class LostDispel(ActionBase):
        """
Removes one beneficial status from target.
Cancels auto-attack upon execution.
        """
        id = 20704
        name = {'Lost Dispel', '失传驱魔'}

    class LostStealth(ActionBase):
        """
Blend in with your surroundings, making it impossible for most enemies to detect you, but reducing movement speed by 25%. Has no effect on certain enemies with special sight.
Cannot be executed while in combat.
Effect ends upon use of any action other than Sprint, or upon reuse.
>> 2336, Lost Stealth, Unable to be detected. Movement speed is severely reduced.
        """
        id = 20705
        name = {'失传潜行', 'Lost Stealth'}

    class LostSpellforge(ActionBase):
        """
Grants the effect of Lost Spellforge to self or target ally.
Lost Spellforge Effect: All attacks deal magic damage. However, all bonuses to damage dealt are determined by the attack's base damage type.
Duration: 300s
Effect cannot be stacked with Lost Steelsting.
>> 2338, Lost Spellforge, All attacks deal magic damage.
        """
        id = 20706
        name = {'Lost Spellforge', '失传铸魔'}

    class LostSteelsting(ActionBase):
        """
Grants the effect of Lost Steelsting to self or target ally.
Lost Steelsting Effect: All attacks deal physical damage. However, all bonuses to damage dealt are determined by the attack's base damage type.
Duration: 300s
Effect cannot be stacked with Lost Spellforge.
>> 2339, Lost Steelsting, All attacks deal physical damage.
        """
        id = 20707
        name = {'Lost Steelsting', '失传钢刺'}

    class LostSwift(ActionBase):
        """
Greatly increases movement speed.
Effect cannot be stacked with other movement speed enhancing abilities.
Duration: 10s
Spirit of the Breathtaker Effect: Increases evasion by 30%
Duration: 60s
Spirit of the Watcher Effect: Grants Rapid Recast to self
Rapid Recast Effect: Shortens recast time for next ability used by 60%
Effect only applies to certain abilities.
Duration: 30s
>> 2335, Lost Swift, Movement speed is increased.
        """
        id = 20708
        name = {'失传敏捷', 'Lost Swift'}

    class LostProtect(ActionBase):
        """
Applies a barrier to self or target player reducing physical damage taken by 10%.
Duration: 30m
>> 2333, Lost Protect, Physical damage taken is reduced.
        """
        id = 20709
        name = {'Lost Protect', '失传护盾'}

    class LostShell(ActionBase):
        """
Applies a barrier to self or target player reducing magic damage taken by 10%.
Duration: 30m
>> 2334, Lost Shell, Magic damage taken is reduced.
        """
        id = 20710
        name = {'Lost Shell', '失传魔盾'}

    class LostReflect(ActionBase):
        """
Creates a barrier around self or party member that reflects most magic attacks.
Duration: 10s
Spirit of the Guardian Effect: Duration is increased to 30s
>> 2337, Lost Reflect, Reflecting magic back on its caster.
        """
        id = 20711
        name = {'Lost Reflect', '失传反射'}

    class LostStoneskin(ActionBase):
        """
Applies a barrier to self or target player that absorbs damage totaling 15% of target's maximum HP.
Duration: 60s
        """
        id = 20712
        name = {'Lost Stoneskin', '失传石肤'}

    class LostBravery(ActionBase):
        """
Increases damage dealt by an ally or self by 5%.
Duration: 600s
>> 2341, Lost Bravery, Damage dealt is increased.
        """
        id = 20713
        name = {'失传勇气', 'Lost Bravery'}

    class LostFocus(ActionBase):
        """
Grants a stack of Boost, up to a maximum of 16.
Boost Bonus: Increases potency of next weaponskill by 15% per stack
Duration: 30s
Effect ends upon using another lost action.
Shares a recast timer with all other weaponskills and spells.
        """
        id = 20714
        name = {'Lost Focus', '失传蓄力'}

    class LostFontOfMagic(ActionBase):
        """
Increases damage dealt by 70%, draining MP while in use.
Duration: 30s
Spirit of the Veteran Effect: Grants Spell Shield to self
Spell Shield Effect: Reduces magic damage taken by 50%
Duration: 15s
Can only be executed while in combat.
>> 2332, Lost Font of Magic, Increasing damage dealt while draining own MP.
        """
        id = 20715
        name = {'失传魔泉', 'Lost Font of Magic'}

    class LostFontOfSkill(ActionBase):
        """
Resets the recast timer for most actions and role actions.
        """
        id = 20716
        name = {'Lost Font of Skill', '失传技泉'}

    class LostFontOfPower(ActionBase):
        """
Increases damage dealt by 30% and critical hit rate by 40%.
Duration: 30s
Spirit of the Irregular Effect: Damage bonus effect is increased to 40%
Spirit of the Platebearer Effect: Grants Solid Shield to self
Solid Shield Effect: Reduces physical damage taken by 50%
Duration: 15s
Can only be executed while in combat.
>> 2346, Lost Font of Power, Damage dealt and critical hit rate are increased.
        """
        id = 20717
        name = {'Lost Font of Power', '失传力泉'}

    class LostSlash(ActionBase):
        """
Delivers an attack with a potency of 800 to all enemies in a cone before you. When critical damage is dealt, potency is tripled.
This action does not share a recast timer with any other actions. Furthermore, the recast timer cannot be affected by other actions.
        """
        id = 20718
        name = {'Lost Slash', '失传斩击'}

    class LostDeath(ActionBase):
        """
KOs target. The less the target's HP, the greater the chance of success.
Spirit of the Ordained Effect: Chance of success is increased
This action does not share a recast timer with any other actions. Furthermore, the recast timer cannot be affected by other actions.
        """
        id = 20719
        name = {'失传即死', 'Lost Death'}

    class BannerOfNobleEnds(ActionBase):
        """
Storm the field under the Banner of Noble Ends, increasing damage dealt by 50% while reducing own HP recovery via most healing actions by 100%.
Duration: 15s
Can only be executed while in combat.
Effect cannot be stacked with other Banner actions.
>> 2326, Banner of Noble Ends, HP recovered via most healing actions is nullified, but damage dealt is increased.
        """
        id = 20720
        name = {'Banner of Noble Ends', '背水境地'}

    class BannerOfHonoredSacrifice(ActionBase):
        """
Storm the field under the Banner of Honored Sacrifice, increasing damage dealt by 55% while draining your HP.
Duration: 15s
Can only be executed while in combat.
Effect cannot be stacked with other Banner actions.
>> 2327, Banner of Honored Sacrifice, Sustaining damage over time in exchange for dealing increased damage.
        """
        id = 20721
        name = {'Banner of Honored Sacrifice', '舍身境地'}

    class BannerOfTirelessConviction(ActionBase):
        """
Storm the field under the Banner of Tireless Conviction, gaining additional stacks each time damage is taken, up to a maximum of 5.
Banner of Tireless Conviction Effect: Increases damage taken by 15% per stack
Duration: 30s
At maximum stacks, take up the Banner of Unyielding Defense.
Banner of Unyielding Defense Effect: Reduces damage taken by 30%
Duration: 180s
Effect cannot be stacked with other Banner actions.
>> 2328, Banner of Tireless Conviction, Damage taken is increased, but your conviction is strengthened with each attack received. At maximum stacks, take up the Banner of Unyielding Defense.
Banner of Unyielding Defense Effect: Damage taken is reduced.
        """
        id = 20722
        name = {'忍耐境地', 'Banner of Tireless Conviction'}

    class BannerOfFirmResolve(ActionBase):
        """
Storm the field under the Banner of Firm Resolve, gaining additional stacks each time damage is taken, up to a maximum of 5.
Banner of Firm Resolve Effect: Reduces damage dealt by 15% per stack
Duration: 30s
At maximum stacks, take up the Banner of Unyielding Defense.
Banner of Unyielding Defense Effect: Reduces damage taken by 30%
Duration: 180s
Effect cannot be stacked with other Banner actions.
>> 2329, Banner of Firm Resolve, Damage dealt is reduced, but your resolve is strengthened with each attack received. At maximum stacks, take up the Banner of Unyielding Defense.
Banner of Unyielding Defense Effect: Damage taken is reduced.
        """
        id = 20723
        name = {'Banner of Firm Resolve', '坚守境地'}

    class BannerOfSolemnClarity(ActionBase):
        """
Storm the field under the Banner of Solemn Clarity, periodically gaining additional stacks, up to a maximum of 4.
Duration: 30s
Effect ends upon using another action or moving (including facing a different direction).
Cancels auto-attack upon execution.
At maximum stacks, take up the Banner of Limitless Grace.
Banner of Limitless Grace Effect: Increases healing potency by 50% while reducing MP cost
Duration: 120s
Can only be executed while in combat.
Effect cannot be stacked with other Banner actions.
>> 2330, Banner of Solemn Clarity, You take a moment to still your mind, gaining clarity as time passes. At maximum stacks, take up the Banner of Limitless Grace.
Banner of Limitless Grace Effect: Potency of HP restoration actions is increased while MP cost is reduced.
        """
        id = 20724
        name = {'冥想境地', 'Banner of Solemn Clarity'}

    class BannerOfHonedAcuity(ActionBase):
        """
Storm the field under the Banner of Honed Acuity, gaining additional stacks each time an attack is evaded, up to a maximum of 3.
Banner of Honed Acuity Effect: Increases damage taken by 10% per stack
Duration: 120s
At maximum stacks, take up the Banner of Transcendent Finesse.
Banner of Transcendent Finesse Effect: Increases critical hit rate by 30% and reduces weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay by 20%
Duration: 180s
Can only be executed while in combat.
Effect cannot be stacked with other Banner actions.
>> 2331, Banner of Honed Acuity, Damage taken is increased, but your senses sharpen with each attack evaded. At maximum stacks, take up the Banner of Transcendent Finesse.
Banner of Transcendent Finesse Effect: Critical hit rate is increased while weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
        """
        id = 20725
        name = {'Banner of Honed Acuity', '敏锐境地'}

    class LostCure(ActionBase):
        """
Restores target's HP.
Cure Potency: 15,000
        """
        id = 20726
        name = {'失传治疗', 'Lost Cure'}

    class LostCureIi(ActionBase):
        """
Restores target's HP.
Cure Potency: 21,700
Spirit of the Savior Effect: Regen
Cure Potency: 6,000
Duration: 21s
        """
        id = 20727
        name = {'失传救疗', 'Lost Cure II'}

    class LostCureIii(ActionBase):
        """
Restores HP of target and all party members nearby target.
Cure Potency: 15,000
        """
        id = 20728
        name = {'失传愈疗', 'Lost Cure III'}

    class LostCureIv(ActionBase):
        """
Restores HP of target and all party members nearby target.
Cure Potency: 21,700
Spirit of the Savior Effect: Regen
Cure Potency: 6,000
Duration: 21s
        """
        id = 20729
        name = {'Lost Cure IV', '失传圣疗'}

    class LostArise(ActionBase):
        """
Restores all of a KO'd target's HP.
If the target was weakened at the time of Raise, the weakness effect will be removed.
        """
        id = 20730
        name = {'Lost Arise', '失传完全复活'}

    class LostIncense(ActionBase):
        """
Gesture threateningly, placing yourself at the top of a target's enmity list.
Additional Effect: Enmity generation is increased and damage taken is reduced by 20%
Duration: 20s
>> 2356, Lost Incense, Enmity is increased and damage taken is reduced.
        """
        id = 20731
        name = {'Lost Incense', '失传激怒'}

    class LostFairTrade(ActionBase):
        """
Through sheer force of will, restore a random technique of the lost to physical form and throw it at a single target, dealing damage with a potency of 50.
Potency increases up to 1,000 based on the weight of the lost action.
The lost action thrown will be lost upon execution.
This action does not share a recast timer with any other actions. Furthermore, the recast timer cannot be affected by other actions.
        """
        id = 20732
        name = {'失传公平交易', 'Lost Fair Trade'}

    class Mimic(ActionBase):
        """
Study the lost techniques used by a targeted ally and make them your own.
Cannot be executed while in combat.
>> 1056, Mimic, Repeating any ability or item used by forerunning chocobos.
        """
        id = 20733
        name = {'模仿', 'Mimic'}

    class DynamisDice(ActionBase):
        """
Place your faith in the goddess Nymeia as she spins the wheel of fate.
Can only be executed while in combat.
Shares a recast timer with Resistance Potion and Resistance Elixir.
        """
        id = 20734
        name = {'命运骰子', 'Dynamis Dice'}

    class ResistancePhoenix(ActionBase):
        """
Resurrects target to a weakened state.
        """
        id = 20735
        name = {'Resistance Phoenix', '义军不死鸟之尾'}

    class ResistanceReraiser(ActionBase):
        """
Grants a 70% chance of automatic revival upon KO.
Duration: 180m
        """
        id = 20736
        name = {'义军复活药', 'Resistance Reraiser'}

    class ResistancePotionKit(ActionBase):
        """
Grants Auto-potion to self.
Auto-potion Effect: Restores HP automatically when HP falls below 50%
Duration: 600s
When triggered, there is a 50% chance the effect will end.
Spirit of the Breathtaker Effect: Chance for Auto-potion effect to end is reduced to 10%
Shares a recast timer with Resistance Ether Kit and Resistance Medikit.
        """
        id = 20737
        name = {'义军恢复药箱', 'Resistance Potion Kit'}

    class ResistanceEtherKit(ActionBase):
        """
Grants Auto-ether to self.
Auto-ether Effect: Restores MP automatically when MP falls below 20%
Duration: 600s
When triggered, there is a 50% chance the effect will end.
Spirit of the Breathtaker Effect: Chance for Auto-ether effect to end is reduced to 10%
Shares a recast timer with Resistance Potion Kit and Resistance Medikit.
        """
        id = 20738
        name = {'义军以太药箱', 'Resistance Ether Kit'}

    class ResistanceMedikit(ActionBase):
        """
Removes a single detrimental effect from self. When not suffering from detrimental effects, creates a barrier that protects against most status ailments. The barrier is removed after curing the next status ailment suffered.
Effect cannot be stacked with similar barrier actions.
Duration: 30m
Shares a recast timer with Resistance Potion Kit and Resistance Ether Kit.
        """
        id = 20739
        name = {'义军治愈箱', 'Resistance Medikit'}

    class ResistancePotion(ActionBase):
        """
Gradually restores HP.
Cure Potency: 5,000
Duration: 40s
Shares a recast timer with Dynamis Dice and Resistance Elixir.
        """
        id = 20740
        name = {'Resistance Potion', '义军恢复药'}

    class EssenceOfTheAetherweaver(ActionBase):
        """
Increases damage dealt by 80%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20741
        name = {'Essence of the Aetherweaver', '术士的秘药'}

    class EssenceOfTheMartialist(ActionBase):
        """
Increases damage dealt by 60%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20742
        name = {'Essence of the Martialist', '斗士的秘药'}

    class EssenceOfTheSavior(ActionBase):
        """
Increases healing potency by 60%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20743
        name = {'治愈者的秘药', 'Essence of the Savior'}

    class EssenceOfTheVeteran(ActionBase):
        """
Increases physical defense by 150%, magic defense by 45%, and maximum HP by 60%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20744
        name = {'魔战士的秘药', 'Essence of the Veteran'}

    class EssenceOfThePlatebearer(ActionBase):
        """
Increases defense by 80% and maximum HP by 45%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20745
        name = {'重骑兵的秘药', 'Essence of the Platebearer'}

    class EssenceOfTheGuardian(ActionBase):
        """
Increases defense by 30% and maximum HP by 10%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20746
        name = {'守护者的秘药', 'Essence of the Guardian'}

    class EssenceOfTheOrdained(ActionBase):
        """
Increases damage dealt by 20%, healing potency by 25%, and maximum MP by 50%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20747
        name = {'Essence of the Ordained', '祭司的秘药'}

    class EssenceOfTheSkirmisher(ActionBase):
        """
Increases damage dealt by 20% and critical hit rate by 15%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20748
        name = {'武人的秘药', 'Essence of the Skirmisher'}

    class EssenceOfTheWatcher(ActionBase):
        """
Reduces maximum HP by 5% while increasing evasion by 40%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20749
        name = {'Essence of the Watcher', '斥候的秘药'}

    class EssenceOfTheProfane(ActionBase):
        """
Reduces healing potency by 70% while increasing damage dealt by 100%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20750
        name = {'Essence of the Profane', '破戒僧的秘药'}

    class EssenceOfTheIrregular(ActionBase):
        """
Increases damage dealt by 90% and damage taken by 200% while reducing maximum HP by 30%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20751
        name = {'狂战士的秘药', 'Essence of the Irregular'}

    class EssenceOfTheBreathtaker(ActionBase):
        """
Increases poison resistance and movement speed, including mount speed, and increases evasion by 10%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20752
        name = {'Essence of the Breathtaker', '盗贼的秘药'}

    class EssenceOfTheBloodsucker(ActionBase):
        """
Increases damage dealt by 40%.
Additional Effect: Absorb a portion of damage dealt as HP
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20753
        name = {'Essence of the Bloodsucker', '吸血鬼的秘药'}

    class EssenceOfTheBeast(ActionBase):
        """
Increases defense by 50% and maximum HP by 45%.
Additional Effect: Absorb a portion of damage dealt as HP
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20754
        name = {'狼人的秘药', 'Essence of the Beast'}

    class EssenceOfTheTemplar(ActionBase):
        """
Increases defense by 50%, maximum HP by 45%, and damage dealt by 60%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20755
        name = {'Essence of the Templar', '圣骑士的秘药'}

    class DeepEssenceOfTheAetherweaver(ActionBase):
        """
Increases damage dealt by 96%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20756
        name = {'术士的灵药', 'Deep Essence of the Aetherweaver'}

    class DeepEssenceOfTheMartialist(ActionBase):
        """
Increases damage dealt by 72%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20757
        name = {'斗士的灵药', 'Deep Essence of the Martialist'}

    class DeepEssenceOfTheSavior(ActionBase):
        """
Increases healing potency by 72%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20758
        name = {'Deep Essence of the Savior', '治愈者的灵药'}

    class DeepEssenceOfTheVeteran(ActionBase):
        """
Increases physical defense by 180%, magic defense by 54%, and maximum HP by 72%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20759
        name = {'Deep Essence of the Veteran', '魔战士的灵药'}

    class DeepEssenceOfThePlatebearer(ActionBase):
        """
Increases defense by 96% and maximum HP by 54%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20760
        name = {'重骑兵的灵药', 'Deep Essence of the Platebearer'}

    class DeepEssenceOfTheGuardian(ActionBase):
        """
Increases defense by 36% and maximum HP by 12%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20761
        name = {'Deep Essence of the Guardian ', '守护者的灵药'}

    class DeepEssenceOfTheOrdained(ActionBase):
        """
Increases damage dealt by 24%, healing potency by 30%, and maximum MP by 60%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20762
        name = {'祭司的灵药', 'Deep Essence of the Ordained'}

    class DeepEssenceOfTheSkirmisher(ActionBase):
        """
Increases damage dealt by 24% and critical hit rate by 18%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20763
        name = {'武人的灵药', 'Deep Essence of the Skirmisher'}

    class DeepEssenceOfTheWatcher(ActionBase):
        """
Reduces maximum HP by 3% while increasing evasion by 48%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20764
        name = {'Deep Essence of the Watcher', '斥候的灵药'}

    class DeepEssenceOfTheProfane(ActionBase):
        """
Reduces healing potency by 70% while increasing damage dealt by 120%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20765
        name = {'破戒僧的灵药', 'Deep Essence of the Profane'}

    class DeepEssenceOfTheIrregular(ActionBase):
        """
Increases damage dealt by 108% and damage taken by 200% while reducing maximum HP by 30%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20766
        name = {'Deep Essence of the Irregular', '狂战士的灵药'}

    class DeepEssenceOfTheBreathtaker(ActionBase):
        """
Increases poison resistance and movement speed, including mount speed, and increases evasion by 20%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20767
        name = {'盗贼的灵药', 'Deep Essence of the Breathtaker'}

    class DeepEssenceOfTheBloodsucker(ActionBase):
        """
Increases damage dealt by 48%.
Additional Effect: Absorb a portion of damage dealt as HP
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20768
        name = {'Deep Essence of the Bloodsucker', '吸血鬼的灵药'}

    class DeepEssenceOfTheBeast(ActionBase):
        """
Increases defense by 60% and maximum HP by 54%.
Additional Effect: Absorb a portion of damage dealt as HP
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20769
        name = {'Deep Essence of the Beast', '狼人的灵药'}

    class DeepEssenceOfTheTemplar(ActionBase):
        """
Increases defense by 60%, maximum HP by 54%, and damage dealt by 72%.
Effect ends upon reuse.
Cannot be used with other Essence or Deep Essence actions.
        """
        id = 20770
        name = {'Deep Essence of the Templar', '圣骑士的灵药'}

    class AutoRestoration(ActionBase):
        """
Restores up to 40% of own HP and 30% of own EP.
        """
        id = 20940
        name = {'Auto Restoration', '自我修复'}

    class EnkindlingFlameDance(ActionBase):
        """
Sets a Bombard's heart ablaze. More ablaze than usual, that is.
        """
        id = 21324
        name = {'Enkindling Flame Dance', '火焰之舞：燃烧舞步'}

    class InvigoratingFlameDance(ActionBase):
        """
Fills a Bombard with vim and vigor.
        """
        id = 21325
        name = {'火焰之舞：青磷舞步', 'Invigorating Flame Dance'}

    class Fleche(ActionBase):
        """
Delivers an attack with a potency of 440.
        """
        id = 21494
        name = {'Fleche', '飞刺'}

    class ContreSixte(ActionBase):
        """
Delivers an attack with a potency of 400 to target and all enemies nearby it.
        """
        id = 21495
        name = {'Contre Sixte', '六分反击'}

    class Vercure(ActionBase):
        """
Restores target's HP.
Cure Potency: 350
        """
        id = 21497
        name = {'Vercure', '赤治疗'}

    class MaleficIii(ActionBase):
        """
Deals unaspected damage with a potency of 210.
        """
        id = 21498
        name = {'祸星', 'Malefic III'}

    class Benefic(ActionBase):
        """
Restores target's HP.
Cure Potency: 400
        """
        id = 21608
        name = {'吉星', 'Benefic'}

    class AspectedHelios(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 200
Additional Effect: Regen
Cure Potency: 100
Duration: 15s
>> 836, Aspected Helios, Regenerating HP over time.
        """
        id = 21609
        name = {'Aspected Helios', '阳星相位'}

    class FixedSign(ActionBase):
        """
Creates a fixed sign centered around the caster, reducing damage taken by 10% for self and any party members who enter.
Duration: 18s
Additional Effect: Healing over time
Cure Potency: 100
Duration: 15s
Effect ends upon using another action or moving (including facing a different direction).
Cancels auto-attack upon execution.
>> 2640, Fixed Sign, Damage taken is reduced.
>> 2641, Fixed Sign, Regenerating HP over time.
>> 2639, Fixed Sign, An area of land has been granted protection, reducing damage taken for all who enter.
        """
        id = 21611
        name = {'不动宫', 'Fixed Sign'}

    class AllaganBlizzardIv(ActionBase):
        """
Deals ice damage with a potency of 300.
Additional Effect: Restores up to 40% of MP
        """
        id = 21852
        name = {'Allagan Blizzard IV', '亚拉戈冰澈'}

    class ThunderIv(ActionBase):
        """
Deals lightning damage with a potency of 200 to target and all enemies nearby it.
Additional Effect: Lightning damage over time
Potency: 30
Duration: 18s

>> 1210, Thunder IV, Sustaining lightning damage over time.
        """
        id = 21884
        name = {'霹雷', 'Thunder IV'}

    class CureIi(ActionBase):
        """
Restores target's HP.
Cure Potency: 700
        """
        id = 21886
        name = {'Cure II', '救疗'}

    class MedicaIi(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 200
Additional Effect: Regen
Cure Potency: 100
Duration: 15s
>> 150, Medica II, Regenerating HP over time.
        """
        id = 21888
        name = {'医济', 'Medica II'}

    class Break(ActionBase):
        """
Prevents spellcasting, movement, and other activity of all nearby enemies.
>> 2573, Break, Activity is severely impeded.
        """
        id = 21921
        name = {'Break', '石化'}

    class LostPerception(ActionBase):
        """
Detect traps within a radius of 15 yalms.
If there are no traps within 15 yalms, alerts you to the presence of traps with a radius of 36 yalms.
※This action can only be used in Delubrum Reginae.
        """
        id = 22344
        name = {'Lost Perception', '失传探景'}

    class LostSacrifice(ActionBase):
        """
Restores all of a KO'd target's HP.
Cannot be executed if currently afflicted with Sacrifice.
Additional Effect: Inflicts Sacrifice on self
Sacrifice Effect: When effect expires, you will be KO'd
Duration: 10s
        """
        id = 22345
        name = {'Lost Sacrifice', '失传献祭'}

    class PureEssenceOfTheGambler(ActionBase):
        """
Increases evasion by 11%, critical hit rate by 77%, and direct hit rate by 77%.
Effect ends upon reuse.
Cannot be used with other Essence, Deep Essence, or Pure Essence actions.
It is said that Pure Essences may grant unexpected effects...
※This action can only be used in Delubrum Reginae.
        """
        id = 22346
        name = {'Pure Essence of the Gambler', '胜负师的仙药'}

    class PureEssenceOfTheElder(ActionBase):
        """
Increases defense by 25%, damage dealt by 50%, and maximum HP by 100%.
Effect ends upon reuse.
Cannot be used with other Essence, Deep Essence, or Pure Essence actions.
It is said that Pure Essences may grant unexpected effects...
※This action can only be used in Delubrum Reginae.
        """
        id = 22347
        name = {'Pure Essence of the Elder', '贤者的仙药'}

    class PureEssenceOfTheDuelist(ActionBase):
        """
Increases defense by 60%, damage dealt by 60%, and maximum HP by 81%.
Effect ends upon reuse.
Cannot be used with other Essence, Deep Essence, or Pure Essence actions.
It is said that Pure Essences may grant unexpected effects...
※This action can only be used in Delubrum Reginae.
        """
        id = 22348
        name = {'Pure Essence of the Duelist', '剑豪的仙药'}

    class PureEssenceOfTheFiendhunter(ActionBase):
        """
Increases defense by 60%, damage dealt by 50%, and maximum HP by 81%.
Effect ends upon reuse.
Cannot be used with other Essence, Deep Essence, or Pure Essence actions.
It is said that Pure Essences may grant unexpected effects...
※This action can only be used in Delubrum Reginae.
        """
        id = 22349
        name = {'Pure Essence of the Fiendhunter', '弓圣的仙药'}

    class PureEssenceOfTheIndomitable(ActionBase):
        """
Increases defense by 40%, damage dealt by 72%, and maximum HP by 50%.
Effect ends upon reuse.
Cannot be used with other Essence, Deep Essence, or Pure Essence actions.
It is said that Pure Essences may grant unexpected effects...
※This action can only be used in Delubrum Reginae.
        """
        id = 22350
        name = {'豪杰的仙药', 'Pure Essence of the Indomitable'}

    class PureEssenceOfTheDivine(ActionBase):
        """
Increases defense by 25%, damage dealt by 35%, and maximum HP by 100%.
Effect ends upon reuse.
Cannot be used with other Essence, Deep Essence, or Pure Essence actions.
It is said that Pure Essences may grant unexpected effects...
※This action can only be used in Delubrum Reginae.
        """
        id = 22351
        name = {'Pure Essence of the Divine', '圣人的仙药'}

    class LostFlareStar(ActionBase):
        """
Consumes MP to deal unaspected damage with a potency of 300 to all nearby enemies.
Additional Effect: Unaspected damage over time
Potency: 350
Duration: 60s
The damage over time effect of Lost Flare Star can only be applied once per target at any given time. This effect cannot be stacked by multiple players.
>> 2440, Lost Flare Star, Sustaining damage over time.
        """
        id = 22352
        name = {'失传耀星', 'Lost Flare Star'}

    class LostRendArmor(ActionBase):
        """
Delivers a jumping attack with a potency of 100.
Additional Effect: Increases target's damage taken by 10%.
Duration: 30s
Cannot be executed while bound.
>> 2441, Lost Rend Armor, Damage taken is increased.
        """
        id = 22353
        name = {'失传破甲', 'Lost Rend Armor'}

    class LostSeraphStrike(ActionBase):
        """
Consumes MP to deliver a jumping attack that deals unaspected damage with a potency of 500.
Additional Effect: Reduces target's accuracy by 10%.
Duration: 15s
Additional Effect: Grants Cleric Stance to self.
Cleric Stance Bonus: Reduces healing potency by 60% while increasing damage dealt by 60%.
Duration: 15s
Cannot be executed while bound.
        """
        id = 22354
        name = {'失传炽天强袭', 'Lost Seraph Strike'}

    class LostAethershield(ActionBase):
        """
Reduces damage taken by self and nearby party members by 30%.
Duration: 15s
>> 2443, Lost Aethershield, Damage taken is reduced.
        """
        id = 22355
        name = {'失传以太之盾', 'Lost Aethershield'}

    class LostDervish(ActionBase):
        """
Increases critical hit rate of self and nearby party members by 10%, increases damage dealt by 7%, and reduces weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay by 1%.
Duration: 60s
>> 2444, Lost Dervish, Critical hit rate and damage dealt are increased, while weaponskill cast time and recast time, spell cast time and recast time, and auto-attack delay are reduced.
        """
        id = 22356
        name = {'Lost Dervish', '失传速度之星'}

    class SemiEternalBreath(ActionBase):
        """
Unleash an Eternal Breath...sort-of.
※Has no effect in battle.
        """
        id = 23345
        name = {'亚永恒吐息', 'Semi-eternal Breath'}

    class Lodestone(ActionBase):
        """
Instantly return to the starting point of the area.
Cannot be executed while in combat.
Shares a recast timer with all other weaponskills and spells.
        """
        id = 23907
        name = {'返回磁石', 'Lodestone'}

    class LostStoneskinIi(ActionBase):
        """
Creates a barrier around self and all party members near you that absorbs damage totaling 10% of maximum HP.
Duration: 30s
        """
        id = 23908
        name = {'失传坚石肤', 'Lost Stoneskin II'}

    class LostBurst(ActionBase):
        """
Deals lightning damage with a potency of 300 to all nearby enemies.
Additional Effect: Interrupts all nearby enemies
Additional Effect: Increases damage taken by enemies with Magical Aversion by 10%
Duration: 60s
>> 2558, Lost Burst, Damage taken is increased.
        """
        id = 23909
        name = {'失传磁暴', 'Lost Burst'}

    class LostRampage(ActionBase):
        """
Delivers an attack with a potency of 300 to all nearby enemies.
Additional Effect: Interrupts all nearby enemies
Additional Effect: Increases damage taken by enemies with Physical Aversion by 10%
Duration: 60s
>> 2559, Lost Rampage, Damage taken is increased.
        """
        id = 23910
        name = {'Lost Rampage', '失传暴怒'}

    class LightCurtain(ActionBase):
        """
Grants the effect of Lost Reflect to self.
Lost Reflect Effect: Reflects most magic attacks
Duration: 10s
Shares a recast timer with all other weaponskills and spells.
        """
        id = 23911
        name = {'光之幕帘', 'Light Curtain'}

    class LostReraise(ActionBase):
        """
Grants the effect of Reraise to self or target player.
Reraise Effect: Grants an 80% chance of automatic revival upon KO
Duration: 180m
        """
        id = 23912
        name = {'Lost Reraise', '失传重生'}

    class LostChainspell(ActionBase):
        """
Temporarily eliminates cast time for all spells.
Duration: 30s
Additional Effect: Magic Burst
Magic Burst Effect: Increases spell damage by 45% while increasing MP cost
Duration: 30s
Spirit of the Ordained Effect: Raises Magic Burst spell damage increase to 100% and nullifies additional MP cost
Spirit of the Watcher Effect: Lost Chainspell duration is extended to 90s
Can only be executed while in combat.
>> 2560, Lost Chainspell, Spells require no time to cast.
        """
        id = 23913
        name = {'Lost Chainspell', '失传连锁咏唱'}

    class LostAssassination(ActionBase):
        """
Delivers a close-quarter attack with a potency of 350. Chance of instant KO when attacking from the rear, which increases the lower the target's HP.
Spirit of the Beast Effect: Grants the effect of Lost Font of Power to self
Lost Font of Power Effect: Increases damage dealt by 30% and critical hit rate by 40%
Duration: 18s
This action does not share a recast timer with any other actions. Furthermore, the recast timer cannot be affected by other actions.
        """
        id = 23914
        name = {'失传暗杀', 'Lost Assassination'}

    class LostProtectIi(ActionBase):
        """
Applies a barrier to self or target player reducing physical damage taken by 15%.
Duration: 30m
>> 2561, Lost Protect II, Physical damage taken is reduced.
        """
        id = 23915
        name = {'Lost Protect II', '失传护盾II'}

    class LostShellIi(ActionBase):
        """
Applies a barrier to self or target player reducing magic damage taken by 15%.
Duration: 30m
>> 2562, Lost Shell II, Magic damage taken is reduced.
        """
        id = 23916
        name = {'失传魔盾II', 'Lost Shell II'}

    class LostBubble(ActionBase):
        """
Increases maximum HP of self or target player by 30%.
Duration: 600s
>> 2563, Lost Bubble, Maximum HP is increased.
        """
        id = 23917
        name = {'失传生机', 'Lost Bubble'}

    class LostImpetus(ActionBase):
        """
Quickly dash 10 yalms forward.
Additional Effect: Applies Lost Swift to self and nearby party members
Lost Swift Effect: Greatly increases movement speed
Effect cannot be stacked with other movement speed enhancing abilities.
Duration: 10s
Spirit of the Breathtaker Effect: Increases evasion of self and nearby party members by 15%
Duration: 60s
Spirit of the Watcher Effect: Grants Rapid Recast to self and nearby party members
Rapid Recast Effect: Shortens recast time for next ability used by 25%
Effect only applies to certain abilities.
Duration: 15s
Cannot be executed while bound.
        """
        id = 23918
        name = {'失传推进', 'Lost Impetus'}

    class LostExcellence(ActionBase):
        """
Instantly cures Weakness and temporarily nullifies most attacks, while increasing damage dealt by 65%. Memorable will be applied when effect ends.
Duration: 10s
Memorable Effect: Increases damage dealt by 65% while decreasing damage taken by 10%
Duration: 50s
Can only be executed while in combat.
>> 2564, Lost Excellence, Impervious to most attacks. Damage dealt is increased.
        """
        id = 23919
        name = {'失传卓异', 'Lost Excellence'}

    class LostFullCure(ActionBase):
        """
Fully restores HP and MP while granting Auto-potion and Auto-ether to self and nearby party members.
Auto-potion Effect: Restores HP automatically when HP falls below 50%
Duration: 600s
When triggered, there is a 50% chance the effect will end.
Auto-ether Effect: Restores MP automatically when MP falls below 20%
Duration: 600s
When triggered, there is a 50% chance the effect will end.
Spirit of the Breathtaker Effect: Chance for Auto-potion and Auto-ether effect to end is reduced to 10%
        """
        id = 23920
        name = {'失传痊愈', 'Lost Full Cure'}

    class LostBloodRage(ActionBase):
        """
Increases damage dealt by 15% and reduces damage taken by 5% per stack. Stacks increase with each use of a dash attack while effect is active, to a maximum of 4.
Duration: 18s
Maximum stacks grant the effect of Blood Rush.
Blood Rush Effect: Increases damage dealt by 60%, shortens recast times by 75%, and gradually restores HP and MP. Recast time reduction does not apply to charged actions.
Duration: 30s
Can only be executed while in combat.
>> 2566, Lost Blood Rage, Damage dealt is increased, while damage taken is decreased.
        """
        id = 23921
        name = {'失传血怒', 'Lost Blood Rage'}

    class ResistanceElixir(ActionBase):
        """
Restores own HP and MP to maximum.
Shares a recast timer with Resistance Potion and Dynamis Dice.
        """
        id = 23922
        name = {'义军圣灵药', 'Resistance Elixir'}

    class CrystalIce(ActionBase):
        """
Create a shower of delicate frozen crystals.
※Has no effect in battle.
        """
        id = 24276
        name = {'冰花', 'Crystal Ice'}

    class MightyMaximizer(ActionBase):
        """
Do as the Mighty Moogle and show the fine specimen that you are to all present.
        """
        id = 24277
        name = {'Mighty Maximizer', '肌肉肌肉'}

    class ChirpyChecker(ActionBase):
        """
Do as the Chirpy Chocobo and point and acknowledge─because safety is paramount.
        """
        id = 24278
        name = {'Chirpy Checker', '蓬松蓬松'}

    class PerkyPeeler(ActionBase):
        """
Do as the Perky Piggy and keep your eyes peeled for hidden treasure.
        """
        id = 24279
        name = {'转圈转圈', 'Perky Peeler'}

    class LiminalFire(ActionBase):
        """
Unleash a digital barrage that damages black walls and pylons.
        """
        id = 24619
        name = {'Liminal Fire', '射击'}

    class LiminalFire(ActionBase):
        """
Unleash a digital barrage that damages white walls and pylons.
        """
        id = 24620
        name = {'Liminal Fire', '射击'}

    class F0Switch(ActionBase):
        """
Swap your color.
        """
        id = 24621
        name = {'色相反转', 'F-0 Switch'}

    class F0Switch(ActionBase):
        """
Swap your color.
        """
        id = 24622
        name = {'色相反转', 'F-0 Switch'}

    class Diagnosis(ActionBase):
        """
Restores target's HP.
Cure Potency: 400
        """
        id = 26224
        name = {'Diagnosis'}

    class Embolden(ActionBase):
        """
Increases own magic damage dealt by 5% and damage dealt by nearby party members by 5%.
Duration: 20s
>> 1297, Embolden, Damage dealt is increased.
>> 2282, Embolden, Damage dealt is increased.
>> 1239, Embolden, Magic damage dealt is increased.
        """
        id = 26225
        name = {'Embolden'}

    class MagitekCannon(ActionBase):
        """
Fires cannon at the designated area.
        """
        id = 26231
        name = {'Magitek Cannon'}

    class DiffractiveMagitekCannon(ActionBase):
        """
Fires diffractive cannon at the designated area.
        """
        id = 26232
        name = {'Diffractive Magitek Cannon'}

    class HighPoweredMagitekCannon(ActionBase):
        """
Fires a concentrated burst of energy in a forward direction.
        """
        id = 26233
        name = {'High-powered Magitek Cannon'}

    class FightOrFlight(ActionBase):
        """
Increases physical damage dealt by 25%.
Duration: 25s
>> 76, Fight or Flight, Physical damage dealt is increased.
        """
        id = 26252
        name = {'Fight or Flight'}

    class Rampart(ActionBase):
        """
Reduces damage taken by 10%.
Duration: 20s
>> 1191, Rampart, Damage taken is reduced.
>> 1978, Rampart, Damage taken is reduced.
>> 71, Rampart, Damage taken is reduced.
        """
        id = 26253
        name = {'Rampart'}

    class FiendishLantern(ActionBase):
        """
Emits a wavelength of light that voidsent absolutely detest.
        """
        id = 26890
        name = {'Fiendish Lantern'}

    class HealingHolyWater(ActionBase):
        """
Frees captured souls.
        """
        id = 26891
        name = {'Healing Holy Water'}

    class TheAetherCompass(ActionBase):
        """
Examine your aether compass to deduce the proximate location of nearby aether currents.
        """
        id = 26988
        name = {'the Aether Compass'}

    class LeveilleurDiagnosis(ActionBase):
        """
Restores target's HP.
Cure Potency: 300
Additional Effect: Erects a magicked barrier which nullifies damage equaling 125% of the amount of HP restored
Duration: 30s

        """
        id = 27042
        name = {'Leveilleur Diagnosis'}

    class Prognosis(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 300

        """
        id = 27043
        name = {'Prognosis'}

    class LeveilleurDruochole(ActionBase):
        """
Restores target's HP.
Cure Potency: 600
        """
        id = 27044
        name = {'Leveilleur Druochole'}

    class DosisIii(ActionBase):
        """
Deals unaspected damage with a potency of 300.
        """
        id = 27045
        name = {'Dosis III'}

    class ルヴェユール_トキシコンii(ActionBase):
        """
対象とその周囲の敵に無属性範囲魔法攻撃。
威力：300
        """
        id = 27046
        name = {'ルヴェユール・トキシコンII'}

    class LeveilleurToxikon(ActionBase):
        """
Deals unaspected damage with a potency of 260 to target and all enemies nearby it.
        """
        id = 27047
        name = {'Leveilleur Toxikon'}

    class CrimsonSavior(ActionBase):
        """
Deals unaspected damage with a potency of 200 to all nearby enemies.
        """
        id = 27053
        name = {'Crimson Savior'}

    class ContreSixte(ActionBase):
        """
Delivers an attack with a potency of 400 to target and all enemies nearby it.
        """
        id = 27060
        name = {'Contre Sixte'}

    class Vercure(ActionBase):
        """
Restores target's HP.
Cure Potency: 350
        """
        id = 27061
        name = {'Vercure'}

    class VermilionPledge(ActionBase):
        """
Deals unaspected damage to all enemies in a straight line before you.
        """
        id = 27062
        name = {'Vermilion Pledge'}

    class MedicalKit(ActionBase):
        """
Restores 35% of maximum HP.
        """
        id = 27315
        name = {'Medical Kit'}

    class Nebula(ActionBase):
        """
Reduces damage taken by 30%.
Duration: 15s
>> 1834, Nebula, Damage taken is reduced.
        """
        id = 27430
        name = {'Nebula'}

    class SwiftDeception(ActionBase):
        """
Masks your presence, making it impossible for most enemies to detect you, and increases movement speed. Cannot be cast while in combat.
Duration: 10s
>> 2957, Swift Deception, Unable to be detected by sight, and movement speed is increased.
        """
        id = 27432
        name = {'Swift Deception'}

    class SilentTakedown(ActionBase):
        """
While hidden, delivers an attack that neutralizes imperial soldiers. When the target is magitek weaponry or a guard dog, delivers an attack with a potency of 100.
Can only be executed while under the effect of Swift Deception.
        """
        id = 27433
        name = {'Silent Takedown'}

    class BewildermentBomb(ActionBase):
        """
Throws a bomb that confuses the senses of guard dogs, neutralizing them. Has no effect on imperial soldiers or magitek weaponry.
        """
        id = 27434
        name = {'Bewilderment Bomb'}

    class FamilyOuting(ActionBase):
        """
Temporarily summons your paissa's eight brats (and counting).
※Has no effect in battle.
        """
        id = 28302
        name = {'Family Outing'}

    class LeveilleurDosisIii(ActionBase):
        """
Deals unaspected damage over time.
Potency: 70
Duration: 30s
>> 2650, Leveilleur Dosis III, Sustaining damage over time.
        """
        id = 28439
        name = {'Leveilleur Dosis III'}

    class LegGraze(ActionBase):
        """
Afflicts target with Heavy +40%.
Duration: 10s
        """
        id = 7554
        name = {'伤腿', 'Leg Graze'}

    class Rampart(ActionBase):
        """
Reduces damage taken by 20%.
Duration: 20s
>> 71, Rampart, Damage taken is reduced.
>> 1191, Rampart, Damage taken is reduced.
>> 1978, Rampart, Damage taken is reduced.
        """
        id = 7531
        name = {'Rampart', '铁壁'}

    class SecondWind(ActionBase):
        """
Instantly restores own HP.
Cure Potency: 500
        """
        id = 7541
        name = {'内丹', 'Second Wind'}

    class Addle(ActionBase):
        """
Lowers target's physical damage dealt by 5% and magic damage dealt by 10%.
Duration: 10s
>> 1203, Addle, Physical and magic damage are reduced.
>> 1988, Addle, Damage dealt is reduced.
        """
        id = 7560
        name = {'昏乱', 'Addle'}

    class Repose(ActionBase):
        """
Afflicts target with Sleep.
Duration: 30s
Cancels auto-attack upon execution.
        """
        id = 16560
        name = {'沉静', 'Repose'}

    class FootGraze(ActionBase):
        """
Binds target.
Duration: 10s
Cancels auto-attack upon execution.
Target unbound if damage taken.
        """
        id = 7553
        name = {'Foot Graze', '伤足'}

    class Esuna(ActionBase):
        """
Removes a single detrimental effect from target.
        """
        id = 7568
        name = {'康复', 'Esuna'}

    class LegSweep(ActionBase):
        """
Stuns target.
Duration: 3s
        """
        id = 7863
        name = {'扫腿', 'Leg Sweep'}

    class Sleep(ActionBase):
        """
Puts target and all nearby enemies to sleep.
Duration: 30s
Cancels auto-attack upon execution.
>> 3, Sleep, Overwhelming drowsiness is preventing the execution of actions.
>> 1348, Sleep, Overwhelming drowsiness is preventing the execution of actions.
>> 1363, Sleep, Overwhelming drowsiness is preventing the execution of actions.
>> 1510, Sleep, Overwhelming drowsiness is preventing the execution of actions.
>> 1947, Sleep, Overwhelming drowsiness is preventing the execution of actions.
>> 1596, Sleep, Overwhelming drowsiness is preventing the execution of actions.
>> 926, Sleep, Overwhelming drowsiness is preventing the execution of actions.
        """
        id = 25880
        name = {'Sleep'}

    class Resurrection(ActionBase):
        """
Resurrects target to a weakened state.
        """
        id = 173
        name = {'复生', 'Resurrection'}

    class LowBlow(ActionBase):
        """
Stuns target.
Duration: 5s
        """
        id = 7540
        name = {'Low Blow', '下踢'}

    class Bloodbath(ActionBase):
        """
Converts a portion of physical damage dealt into HP.
Duration: 20s
>> 84, Bloodbath, Physical attacks generate HP equal to a portion of damage dealt.
>> 1982, Bloodbath, Attacks generate HP equal to the amount of physical damage dealt.
        """
        id = 7542
        name = {'浴血', 'Bloodbath'}

    class Provoke(ActionBase):
        """
Gesture threateningly, placing yourself at the top of a target's enmity list while gaining additional enmity.
        """
        id = 7533
        name = {'挑衅', 'Provoke'}

    class Interject(ActionBase):
        """
Interrupts the use of a target's action.
        """
        id = 7538
        name = {'插言', 'Interject'}

    class Swiftcast(ActionBase):
        """
Next spell is cast immediately.
Duration: 10s
>> 1987, Swiftcast, The next spell will be cast immediately.
>> 167, Swiftcast, Next spell will require no time to cast.
>> 1325, Swiftcast, Next spell will require no time to cast.
        """
        id = 7561
        name = {'即刻咏唱', 'Swiftcast'}

    class Peloton(ActionBase):
        """
Increases movement speed of self and nearby party members.
Duration: 30s
Effect ends when enmity is generated. Has no effect in battle.
>> 1985, Peloton, Movement speed is increased.
>> 1199, Peloton, Movement speed is increased. Effect ends upon entering battle.
        """
        id = 7557
        name = {'Peloton', '速行'}

    class Reprisal(ActionBase):
        """
Reduces damage dealt by nearby enemies by 10%.
Duration: 10s
>> 753, Reprisal, Damage dealt is reduced.
>> 2101, Reprisal, Damage dealt is reduced.
>> 1193, Reprisal, Damage dealt is reduced.
        """
        id = 7535
        name = {'Reprisal', '雪仇'}

    class Feint(ActionBase):
        """
Lowers target's physical damage dealt by 10% and magic damage dealt by 5%.
Duration: 10s
>> 2185, Feint, Sustaining increased damage from target who executed Feint.
>> 1195, Feint, Physical and magic damage are reduced.
        """
        id = 7549
        name = {'牵制', 'Feint'}

    class HeadGraze(ActionBase):
        """
Interrupts the use of a target's action.
        """
        id = 7551
        name = {'Head Graze', '伤头'}

    class LucidDreaming(ActionBase):
        """
Gradually restores own MP.
Potency: 55
Duration: 21s
>> 1204, Lucid Dreaming, Restoring MP over time.
        """
        id = 7562
        name = {'醒梦', 'Lucid Dreaming'}

    class ArmsLength(ActionBase):
        """
Creates a barrier nullifying most knockback and draw-in effects.
Duration: 6s
Additional Effect: Slow +20% when barrier is struck
Duration: 15s
>> 1984, Arm's Length, Damage taken is reduced. Impervious to the next stun, sleep, bind, heavy, silence, knockback, or draw-in effect.
>> 2181, Arm's Length, Damage dealt is reduced.
>> 1209, Arm's Length, Slowing enemies when attacked. Immune to most knockback and draw-in effects.
>> 2172, Arm's Length, Weakening enemies when attacked. Damage taken is reduced.
        """
        id = 7548
        name = {"Arm's Length", '亲疏自行'}

    class Surecast(ActionBase):
        """
Spells can be cast without interruption.
Additional Effect: Nullifies most knockback and draw-in effects
Duration: 6s
>> 160, Surecast, Spells cannot be interrupted by taking damage.
        """
        id = 7559
        name = {'沉稳咏唱', 'Surecast'}

    class Shirk(ActionBase):
        """
Diverts 25% of enmity to target party member.
        """
        id = 7537
        name = {'Shirk', '退避'}

    class Rescue(ActionBase):
        """
Instantly draws target party member to your side. Cannot be used outside of combat or when target is suffering from certain enfeeblements.
        """
        id = 7571
        name = {'营救', 'Rescue'}

    class TrueNorth(ActionBase):
        """
Nullifies all action direction requirements.
Duration: 10s
Maximum Charges: 2
>> 1250, True North, All action direction requirements are nullified.
        """
        id = 7546
        name = {'真北', 'True North'}
