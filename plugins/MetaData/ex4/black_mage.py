from ..base import *


class Actions:

    class Blizzard(ActionBase):
        """
Deals ice damage with a potency of 180.
Additional Effect: Grants Umbral Ice or removes Astral Fire
Duration: 15s
        """
        id = 142
        name = {'冰结', 'Blizzard'}

    class Fire(ActionBase):
        """
Deals fire damage with a potency of 180.
Additional Effect: Grants Astral Fire or removes Umbral Ice
Duration: 15s(source.level>=42?(source.job==7?
Additional Effect: 40% chance next Fire III will cost no MP and have no cast time
Duration: 30s:(source.job==25?
Additional Effect: 40% chance next Fire III will cost no MP and have no cast time
Duration: 30s:)):)
        """
        id = 141
        name = {'Fire', '火炎'}

    class Transpose(ActionBase):
        """
Swaps Astral Fire with a single Umbral Ice, or Umbral Ice with a single Astral Fire.
        """
        id = 149
        name = {'Transpose', '星灵移位'}

    class Thunder(ActionBase):
        """
Deals lightning damage with a potency of 30.
Additional Effect: Lightning damage over time
Potency: 35
Duration: 21s(source.level>=28?(source.job==7?
Additional Effect: 10% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
Duration: 40s
:(source.job==25?
Additional Effect: 10% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
Duration: 40s
:
)):
)Only one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target.
    161, Thunder, Sustaining lightning damage over time.
    1324, Thunder, Sustaining lightning damage over time.
        """
        id = 144
        name = {'Thunder', '闪雷'}

    class Sleep(ActionBase):
        """
Puts target and all nearby enemies to sleep.
Duration: 30s
Cancels auto-attack upon execution.
        """
        id = 145
        name = {'催眠', 'Sleep'}

    class BlizzardIi(ActionBase):
        """
Deals ice damage with a potency of 50 to all nearby enemies.
Additional Effect: Grants Umbral Ice or removes Astral Fire
Duration: 15s
        """
        id = 146
        name = {'冰冻', 'Blizzard II'}

    class Scathe(ActionBase):
        """
Deals unaspected damage with a potency of 100.
Additional Effect: 20% chance potency will double
        """
        id = 156
        name = {'崩溃', 'Scathe'}

    class FireIi(ActionBase):
        """
Deals fire damage with a potency of 100 to target and all enemies nearby it.
Additional Effect: (source.level>=35?(source.job==7?Grants Astral Fire III:(source.job==25?Grants Astral Fire III:Grants Astral Fire)):Grants Astral Fire) or removes Umbral Ice
Duration: 15s(source.job==25?(source.level>=56?
Astral Fire Bonus: Grants Enhanced Flare
Effect is canceled if Astral Fire ends.:):)    
        """
        id = 147
        name = {'Fire II', '烈炎'}

    class ThunderIi(ActionBase):
        """
Deals lightning damage with a potency of 50 to target and all enemies nearby it.
Additional Effect: Lightning damage over time
Potency: 15
Duration: 18s(source.level>=28?(source.job==7?
Additional Effect: 3% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
Duration: 40s
:(source.job==25?
Additional Effect: 3% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
Duration: 40s
:
)):
)Only one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target.
    162, Thunder II, Sustaining lightning damage over time.
    2075, Thunder II, Sustaining lightning damage over time.
        """
        id = 7447
        name = {'震雷', 'Thunder II'}

    class Manaward(ActionBase):
        """
Creates a barrier that nullifies damage totaling up to 30% of maximum HP.
Duration: 20s
    168, Manaward, An aetherial barrier is preventing damage.
    1989, Manaward, An aetherial barrier is preventing damage.
        """
        id = 157
        name = {'Manaward', '魔罩'}

    class Manafont(ActionBase):
        """
Restores 30% of maximum MP.
        """
        id = 158
        name = {'魔泉', 'Manafont'}

    class FireIii(ActionBase):
        """
Deals fire damage with a potency of 240.
Additional Effect: Grants Astral Fire III and removes Umbral Ice
Duration: 15s
        """
        id = 152
        name = {'爆炎', 'Fire III'}

    class Freeze(ActionBase):
        """
Deals ice damage with a potency of 120 to target and all enemies nearby it.
(source.job==25?(source.level>=58?Additional Effect: Grants 3 Umbral Hearts
Umbral Heart Bonus: Nullifies Astral Fire's MP cost increase for Fire spells and reduces MP cost for Flare by one-third
:):)Can only be executed while under the effect of Umbral Ice.
        """
        id = 159
        name = {'Freeze', '玄冰'}

    class BlizzardIii(ActionBase):
        """
Deals ice damage with a potency of 240.
Additional Effect: Grants Umbral Ice III and removes Astral Fire
Duration: 15s
        """
        id = 154
        name = {'Blizzard III', '冰封'}

    class ThunderIii(ActionBase):
        """
Deals lightning damage with a potency of 50.
Additional Effect: Lightning damage over time
Potency: 35
Duration: 30s(source.level>=28?(source.job==7?
Additional Effect: 10% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
Duration: 40s
:(source.job==25?
Additional Effect: 10% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
Duration: 40s
:
)):
)Only one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target.
    163, Thunder III, Sustaining lightning damage over time.
        """
        id = 153
        name = {'Thunder III', '暴雷'}

    class AetherialManipulation(ActionBase):
        """
Rush to a target party member's side.
Unable to cast if bound.
        """
        id = 155
        name = {'Aetherial Manipulation', '以太步'}

    class Flare(ActionBase):
        """
Deals fire damage to target and all enemies nearby it with a potency of 220 for the first enemy, and 40% less for all remaining enemies.
(source.job==25?(source.level>=56?Enhanced Flare Potency: 280
:):)Additional Effect: Grants Astral Fire III
Duration: 15s
Can only be executed while under the effect of Astral Fire.
        """
        id = 162
        name = {'Flare', '核爆'}

    class LeyLines(ActionBase):
        """
Connects naturally occurring ley lines to create a circle of power which, while standing within it, reduces spell cast time and recast time, and auto-attack delay by 15%.
Duration: 30s
    737, Ley Lines, Naturally occurring ley lines have been connected into a circle of power.
        """
        id = 3573
        name = {'Ley Lines', '黑魔纹'}

    class Sharpcast(ActionBase):
        """
Ensures the next Scathe, Fire, (source.job==25?(source.level>=90?Paradox, :):)or Thunder spell cast will, for the first hit, trigger Scathe's additional effect, Firestarter, or Thundercloud.
Duration: 30s(source.job==25?(source.level>=88?
Maximum Charges: 2:):)
    867, Sharpcast, Next <UIForeground(500)><UIGlow(501)>Scathe</UIGlow></UIForeground>, <UIForeground(500)><UIGlow(501)>Fire</UIGlow></UIForeground>, or <UIForeground(500)><UIGlow(501)>Thunder</UIGlow></UIForeground> spell cast will trigger enhanced status.
        """
        id = 3574
        name = {'Sharpcast', '激情咏唱'}

    class Enochian(ActionBase):
        """
Increases magic damage dealt by (source.job==25?(source.level>=78?15:(source.level>=70?(source.job==25?10:5):5)):(source.level>=70?(source.job==25?10:5):5))%.(source.job==25?(source.level>=58?(source.level>=60?(source.job==25?(source.level>=76? Also allows the casting of Blizzard IV, Fire IV, Despair, and Umbral Soul.: (source.job==25?(source.level>=72? Also allows the casting of Blizzard IV,  Fire IV, and Despair.: Also allows the casting of Blizzard IV and Fire IV.): Also allows the casting of Blizzard IV and Fire IV.)): (source.job==25?(source.level>=72? Also allows the casting of Blizzard IV,  Fire IV, and Despair.: Also allows the casting of Blizzard IV and Fire IV.): Also allows the casting of Blizzard IV and Fire IV.)): Also allows the casting of Blizzard IV.):):)
(source.level>=70?(source.job==25?Additional Effect: Grants Polyglot if Enochian is maintained for 30s
(source.job==25?(source.level>=80?Maximum Stacks: 2
:):):):)Can only be executed while under the effect of Astral Fire or Umbral Ice. Effect is canceled if Astral Fire or Umbral Ice ends.
    868, Enochian, Magic damage dealt is increased.
        """
        id = 3575
        name = {'Enochian', '天语'}

    class BlizzardIv(ActionBase):
        """
Deals ice damage with a potency of 300.
Additional Effect: Grants 3 Umbral Hearts
Umbral Heart Bonus: Nullifies Astral Fire's MP cost increase for Fire spells and reduces MP cost for Flare by one-third
Can only be executed while under the effect of Umbral Ice.
        """
        id = 3576
        name = {'Blizzard IV', '冰澈'}

    class FireIv(ActionBase):
        """
Deals fire damage with a potency of 300.
Can only be executed while under the effect of Astral Fire.
        """
        id = 3577
        name = {'炽炎', 'Fire IV'}

    class BetweenTheLines(ActionBase):
        """
Move instantly to Ley Lines drawn by you.
Cannot be executed while bound.
        """
        id = 7419
        name = {'Between the Lines', '魔纹步'}

    class ThunderIv(ActionBase):
        """
Deals lightning damage with a potency of 50 to target and all enemies nearby it.
Additional Effect: Lightning damage over time
Potency: 20
Duration: 18s
Additional Effect: 3% chance after each tick that the next Thunder spell of any grade will add its full damage over time amount to its initial damage, have no cast time, and cost no MP
Duration: 40s
Only one Thunder spell-induced damage over time effect per caster can be inflicted upon a single target.
    1210, Thunder IV, Sustaining lightning damage over time.
        """
        id = 7420
        name = {'Thunder IV', '霹雷'}

    class Triplecast(ActionBase):
        """
The next three spells will require no cast time.
Duration: 15s
Maximum Charges: 2
    1211, Triplecast, Spells require no time to cast.
        """
        id = 7421
        name = {'Triplecast', '三连咏唱'}

    class Foul(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 560 for the first enemy, and 60% less for all remaining enemies.
Polyglot Cost: 1
        """
        id = 7422
        name = {'Foul', '秽浊'}

    class Despair(ActionBase):
        """
Deals fire damage with a potency of 340.
Additional Effect: Grants Astral Fire III
Duration: 15s
Can only be executed while under the effect of Astral Fire.
        """
        id = 16505
        name = {'Despair', '绝望'}

    class UmbralSoul(ActionBase):
        """
Grants Umbral Ice and 1 Umbral Heart.
Umbral Heart Bonus: Nullifies Astral Fire's MP cost increase for Fire spells and reduces MP cost for Flare by one-third
Can only be executed while under the effect of Umbral Ice.
        """
        id = 16506
        name = {'灵极魂', 'Umbral Soul'}

    class Xenoglossy(ActionBase):
        """
Deals unaspected damage with a potency of 660.
Polyglot Cost: 1
        """
        id = 16507
        name = {'Xenoglossy', '异言'}
