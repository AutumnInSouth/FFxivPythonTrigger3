from ..base import *


class Actions:

    class Slice(ActionBase):
        """
Delivers an attack with a potency of (source.job==39?(source.level>=60?300:260):260).(source.job==39?(source.level>=50?
Additional Effect: Increases Soul Gauge by 10:):)
        """
        id = 24373
        name = {'Slice'}

    class WaxingSlice(ActionBase):
        """
Delivers an attack with a potency of (source.job==39?(source.level>=60?140:100):100).
Combo Action: Slice
Combo Potency: (source.job==39?(source.level>=60?380:340):340)(source.job==39?(source.level>=50?
Combo Bonus: Increases Soul Gauge by 10:):)
        """
        id = 24374
        name = {'Waxing Slice'}
        combo_action = 24373

    class ShadowOfDeath(ActionBase):
        """
Delivers an attack with a potency of (source.job==39?(source.level>=60?300:240):240).
Additional Effect: Afflicts target with Death's Design, increasing damage you deal target by 10%
Duration: 30s
Extends duration of Death's Design by 30s to a maximum of 60s.(source.job==39?(source.level>=50?
Additional Effect: Increases Soul Gauge by 10 if target is KO'd before effect expires:):)
        """
        id = 24378
        name = {'Shadow of Death'}

    class Harpe(ActionBase):
        """
Deals unaspected damage with a potency of (source.job==39?(source.level>=60?300:200):200).
        """
        id = 24386
        name = {'Harpe'}

    class HellsIngress(ActionBase):
        """
Quickly dash 15 yalms forward.
Additional Effect: Allows next Harpe to be cast immediately
Duration: 15s
(source.job==39?(source.level>=74?Additional Effect: Leaves behind a Hellsgate at point of origin, and grants Threshold to self
Duration: 10s
:):)Cannot be executed while bound.
Shares a recast timer with Hell's Egress.
        """
        id = 24401
        name = {"Hell's Ingress"}

    class HellsEgress(ActionBase):
        """
Quickly dash 15 yalms backwards.
Additional Effect: Allows next Harpe to be cast immediately
Duration: 15s
(source.job==39?(source.level>=74?Additional Effect: Leaves behind a Hellsgate at point of origin, and grants Threshold to self
Duration: 10s
:):)Cannot be executed while bound.
Shares a recast timer with Hell's Ingress.
        """
        id = 24402
        name = {"Hell's Egress"}

    class SpinningScythe(ActionBase):
        """
Delivers an attack with a potency of (source.job==39?(source.level>=60?140:120):120) to all nearby enemies.(source.job==39?(source.level>=50?
Additional Effect: Increases Soul Gauge by 10:):)
        """
        id = 24376
        name = {'Spinning Scythe'}

    class InfernalSlice(ActionBase):
        """
Delivers an attack with a potency of (source.job==39?(source.level>=60?140:100):100).
Combo Action: Waxing Slice
Combo Potency: (source.job==39?(source.level>=60?460:420):420)(source.job==39?(source.level>=50?
Combo Bonus: Increases Soul Gauge by 10:):)
        """
        id = 24375
        name = {'Infernal Slice'}
        combo_action = 24374

    class WhorlOfDeath(ActionBase):
        """
Delivers an attack with a potency of (source.job==39?(source.level>=60?100:80):80) to all nearby enemies.
Additional Effect: Afflicts target with Death's Design, increasing damage you deal target by 10%
Duration: 30s
Extends duration of Death's Design by 30s to a maximum of 60s.(source.job==39?(source.level>=50?
Additional Effect: Increases Soul Gauge by 10 if target is KO'd before effect expires:):)
        """
        id = 24379
        name = {'Whorl of Death'}

    class ArcaneCrest(ActionBase):
        """
Grants Crest of Time Borrowed to self, creating a barrier that nullifies damage totaling up to 10% of maximum HP.
Duration: 5s(source.job==39?(source.level>=84?
Grants Crest of Time Returned to self and nearby party members within a radius of 15 yalms when barrier is completely absorbed.
Crest of Time Returned Effect: Gradually restores HP
Cure Potency: 100
Duration: 15s:):)
        """
        id = 24404
        name = {'Arcane Crest'}

    class NightmareScythe(ActionBase):
        """
Delivers an attack with a potency of (source.job==39?(source.level>=60?120:100):100) to all nearby enemies.
Combo Action: Spinning Scythe
Combo Potency: (source.job==39?(source.level>=60?180:160):160)(source.job==39?(source.level>=50?
Combo Bonus: Increases Soul Gauge by 10:):)
        """
        id = 24377
        name = {'Nightmare Scythe'}
        combo_action = 24376

    class BloodStalk(ActionBase):
        """
Summons your avatar to deliver an attack with a potency of 340.
(source.job==39?(source.level>=70?Additional Effect: Grants Soul Reaver
Duration: 30s
Stack count will be reduced to 1 when already under the effect of Soul Reaver.
:):)Soul Gauge Cost: 50
Shares a recast timer with all avatar attacks except Gluttony.(source.job==39?(source.level>=86?
※Action changes to Lemure's Slice while under the effect of Enshrouded.:):)
        """
        id = 24389
        name = {'Blood Stalk'}

    class GrimSwathe(ActionBase):
        """
Summons your avatar to deliver an attack with a potency of 140 to all enemies in a cone before you.
(source.job==39?(source.level>=70?Additional Effect: Grants Soul Reaver
Duration: 30s
Stack count will be reduced to 1 when already under the effect of Soul Reaver.
:):)Soul Gauge Cost: 50
Shares a recast timer with all avatar attacks except Gluttony.(source.job==39?(source.level>=86?
※Action changes to Lemure's Scythe while under the effect of Enshrouded.:):)
        """
        id = 24392
        name = {'Grim Swathe'}

    class SoulSlice(ActionBase):
        """
Delivers an attack with a potency of 460.
Additional Effect: Increases Soul Gauge by 50
(source.job==39?(source.level>=78?Maximum Charges: 2
:):)Shares a recast timer with Soul Scythe.
        """
        id = 24380
        name = {'Soul Slice'}

    class SoulScythe(ActionBase):
        """
Delivers an attack with a potency of 180 to all nearby enemies.
Additional Effect: Increases Soul Gauge by 50
(source.job==39?(source.level>=78?Maximum Charges: 2
:):)Shares a recast timer with Soul Slice.
        """
        id = 24381
        name = {'Soul Scythe'}

    class Gibbet(ActionBase):
        """
Delivers an attack with a potency of 400.
460 when executed from a target's flank.
Enhanced Gibbet Potency: 460
Flank Enhanced Potency: 520
Additional Effect: Grants Enhanced Gallows
Duration: 60s
The action Blood Stalk changes to Unveiled Gallows while under the effect of Enhanced Gallows.
(source.job==39?(source.level>=80?Additional Effect: Increases Shroud Gauge by 10
:):)Can only be executed while under the effect of Soul Reaver.(source.job==39?(source.level>=80?
※Action changes to Void Reaping while under the effect of Enshrouded.:):)
        """
        id = 24382
        name = {'Gibbet'}

    class Gallows(ActionBase):
        """
Delivers an attack with a potency of 400.
460 when executed from a target's rear.
Enhanced Gallows Potency: 460
Rear Enhanced Potency: 520
Additional Effect: Grants Enhanced Gibbet
Duration: 60s
The action Blood Stalk changes to Unveiled Gibbet while under the effect of Enhanced Gibbet.
(source.job==39?(source.level>=80?Additional Effect: Increases Shroud Gauge by 10
:):)Can only be executed while under the effect of Soul Reaver.(source.job==39?(source.level>=80?
※Action changes to Cross Reaping while under the effect of Enshrouded.:):)
        """
        id = 24383
        name = {'Gallows'}

    class Guillotine(ActionBase):
        """
Delivers an attack with a potency of 200 to all enemies in a cone before you.
(source.job==39?(source.level>=80?Additional Effect: Increases Shroud Gauge by 10
:):)Can only be executed while under the effect of Soul Reaver.(source.job==39?(source.level>=80?
※Action changes to Grim Reaping while under the effect of Enshrouded.:):)
        """
        id = 24384
        name = {'Guillotine'}

    class UnveiledGibbet(ActionBase):
        """
Summons your avatar to deliver an attack with a potency of 400.
Additional Effect: Grants Soul Reaver
Duration: 30s
Stack count will be reduced to 1 when already under the effect of Soul Reaver.
Soul Gauge Cost: 50
Can only be executed while under the effect of Enhanced Gibbet.
Shares a recast timer with all avatar attacks except Gluttony.
※This action cannot be assigned to a hotbar.
        """
        id = 24390
        name = {'Unveiled Gibbet'}

    class UnveiledGallows(ActionBase):
        """
Summons your avatar to deliver an attack with a potency of 400.
Additional Effect: Grants Soul Reaver
Duration: 30s
Stack count will be reduced to 1 when already under the effect of Soul Reaver.
Soul Gauge Cost: 50
Can only be executed while under the effect of Enhanced Gallows.
Shares a recast timer with all avatar attacks except Gluttony.
※This action cannot be assigned to a hotbar.
        """
        id = 24391
        name = {'Unveiled Gallows'}

    class ArcaneCircle(ActionBase):
        """
Increases damage dealt by self and nearby party members by 3%.
Duration: 20s(source.job==39?(source.level>=88?
Additional Effect: Grants Circle of Sacrifice to self and nearby party members
Duration: 5s
Additional Effect: Grants Bloodsown Circle to self
Duration: 6s
Circle of Sacrifice Effect: When you or party members under this effect successfully land a weaponskill or cast a spell, the reaper who applied it may be granted a stack of Immortal Sacrifice, up to a maximum of 8
Duration: 30s
Bloodsown Circle Effect: Allows you to accumulate stacks of Immortal Sacrifice from party members under the effect of your Circle of Sacrifice:):)
>> 2599, Arcane Circle, Damage dealt is increased.
        """
        id = 24405
        name = {'Arcane Circle'}

    class Regress(ActionBase):
        """
Move instantly to the Hellsgate left behind by you.
Can only be executed while under the effect of Threshold.
Cannot be executed while bound.
※This action cannot be assigned to a hotbar.
        """
        id = 24403
        name = {'Regress'}

    class Gluttony(ActionBase):
        """
Summons your avatar to deal unaspected damage to target and all enemies nearby it with a potency of 500 for the first enemy, and 25% less for all remaining enemies.
Additional Effect: Grants 2 stacks of Soul Reaver
Duration: 30s
Soul Gauge Cost: 50
        """
        id = 24393
        name = {'Gluttony'}

    class Enshroud(ActionBase):
        """
Offers your flesh as a vessel to your avatar, gaining maximum stacks of Lemure Shroud.
Duration: 30s
Certain actions cannot be executed while playing host to your avatar.
Shroud Gauge Cost: 50
        """
        id = 24394
        name = {'Enshroud'}

    class VoidReaping(ActionBase):
        """
Delivers an attack with a potency of 460.
Enhanced Void Reaping Potency: 520
Additional Effect: Grants Enhanced Cross Reaping
Duration: 30s
(source.job==39?(source.level>=86?Additional Effect: Grants Void Shroud
:):)Can only be executed while under the effect of Enshrouded.
Recast timer cannot be affected by status effects or gear attributes.
Lemure Shroud Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 24395
        name = {'Void Reaping'}

    class CrossReaping(ActionBase):
        """
Delivers an attack with a potency of 460.
Enhanced Cross Reaping Potency: 520
Additional Effect: Grants Enhanced Void Reaping
Duration: 30s
(source.job==39?(source.level>=86?Additional Effect: Grants Void Shroud
:):)Can only be executed while under the effect of Lemure Shroud.
Recast timer cannot be affected by status effects or gear attributes.
Lemure Shroud Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 24396
        name = {'Cross Reaping'}

    class GrimReaping(ActionBase):
        """
Delivers an attack with a potency of 200 to all enemies in a cone before you.
(source.job==39?(source.level>=86?Additional Effect: Grants Void Shroud
:):)Can only be executed while under the effect of Enshrouded.
Recast timer cannot be affected by status effects or gear attributes.
Lemure Shroud Cost: 1
※This action cannot be assigned to a hotbar.
        """
        id = 24397
        name = {'Grim Reaping'}

    class Soulsow(ActionBase):
        """
Grants Soulsow to self, changing the action to Harvest Moon.
Cast time is instant when used outside of battle.
>> 2594, Soulsow, Able to execute Harvest Moon.
        """
        id = 24387
        name = {'Soulsow'}

    class HarvestMoon(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 600 for the first enemy, and 50% less for all remaining enemies.
Can only be executed while under the effect of Soulsow.
※This action cannot be assigned to a hotbar.
        """
        id = 24388
        name = {'Harvest Moon'}

    class LemuresSlice(ActionBase):
        """
Delivers an attack with a potency of 200.
Void Shroud Cost: 2
Shares a recast timer with Lemure's Scythe.
※This action cannot be assigned to a hotbar.
        """
        id = 24399
        name = {"Lemure's Slice"}

    class LemuresScythe(ActionBase):
        """
Delivers an attack with a potency of 100 to all enemies in a cone before you.
Void Shroud Cost: 2
Shares a recast timer with Lemure's Slice.
※This action cannot be assigned to a hotbar.
        """
        id = 24400
        name = {"Lemure's Scythe"}

    class PlentifulHarvest(ActionBase):
        """
Delivers an attack to all enemies in a straight line before you with a potency of 520 for the first enemy, and 60% less for all remaining enemies.
Immortal Sacrifice Cost: 1 stack
Potency increases up to 800 as stacks of Immortal Sacrifice exceed minimum cost.
Additional Effect: Increases Shroud Gauge by 50
Cannot be executed while under the effect of Bloodsown Circle.
Consumes all stacks of Immortal Sacrifice upon execution.
        """
        id = 24385
        name = {'Plentiful Harvest'}

    class Communio(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 1,000 for the first enemy, and 60% less for all remaining enemies.
Enshrouded effect expires upon execution.
Requires at least one stack of Lemure Shroud to execute.
        """
        id = 24398
        name = {'Communio'}
