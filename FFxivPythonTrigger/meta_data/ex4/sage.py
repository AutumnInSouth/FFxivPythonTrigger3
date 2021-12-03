from ..base import *


class Actions:

    class Dosis(ActionBase):
        """
Deals unaspected damage with a potency of (source.job==40?(source.level>=64?300:(source.job==40?(source.level>=54?250:180):180)):(source.job==40?(source.level>=54?250:180):180)).
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
        """
        id = 24283
        name = {'Dosis'}

    class Diagnosis(ActionBase):
        """
Restores target's HP.
Cure Potency: (source.job==40?(source.level>=85?450:400):400)
        """
        id = 24284
        name = {'Diagnosis'}

    class Kardia(ActionBase):
        """
Grants self the effect of Kardia and a selected party member or self the effect of Kardion, restoring HP after casting certain magic attacks.
>> 2604, Kardia, Triggers a healing effect on a player under the effect of Kardion granted by you when casting attack magic.
>> 2871, Kardia, Triggers a healing effect on a player under the effect of Kardion granted by you when casting attack magic.
        """
        id = 24285
        name = {'Kardia'}

    class Prognosis(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 300
        """
        id = 24286
        name = {'Prognosis'}

    class Egeiro(ActionBase):
        """
Resurrects target to a weakened state.
        """
        id = 24287
        name = {'Egeiro'}

    class Physis(ActionBase):
        """
Gradually restores own HP and the HP of all nearby party members.
Cure Potency: 100
Duration: 15s
>> 2617, Physis, Regenerating HP over time.
        """
        id = 24288
        name = {'Physis'}

    class Phlegma(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of (source.job==40?(source.level>=64?400:(source.job==40?(source.level>=54?330:230):230)):(source.job==40?(source.level>=54?330:230):230)) for the first enemy, and 30% less for all remaining enemies.
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
Maximum Charges: 2
This action does not share a recast timer with any other actions.
        """
        id = 24289
        name = {'Phlegma'}

    class Eukrasia(ActionBase):
        """
Augments certain offensive and healing magic actions.
(source.job==40?(source.level>=82?Dosis III is upgraded to Eukrasian Dosis III:(source.job==40?(source.level>=72?Dosis II is upgraded to Eukrasian Dosis II:Dosis is upgraded to Eukrasian Dosis):Dosis is upgraded to Eukrasian Dosis)):(source.job==40?(source.level>=72?Dosis II is upgraded to Eukrasian Dosis II:Dosis is upgraded to Eukrasian Dosis):Dosis is upgraded to Eukrasian Dosis)).
Diagnosis is upgraded to Eukrasian Diagnosis.
Prognosis is upgraded to Eukrasian Prognosis.
>> 2867, Eukrasia, Certain actions are being augmented.
>> 2606, Eukrasia, Certain actions are being augmented.
        """
        id = 24290
        name = {'Eukrasia'}

    class EukrasianDiagnosis(ActionBase):
        """
Restores target's HP.
Cure Potency: 300
Additional Effect: Erects a magicked barrier which nullifies damage equaling (source.job==40?(source.level>=85?180:125):125)％ of the amount of HP restored. When critical HP is restored, also grants Differential Diagnosis, nullifying damage equaling (source.job==40?(source.level>=85?180:125):125)% the amount of HP restored.
Duration: 30s
Effect cannot be stacked with Eukrasian Prognosis or scholar's Galvanize.
※This action cannot be assigned to a hotbar.
>> 2865, Eukrasian Diagnosis, A magicked barrier is nullifying damage.
>> 2607, Eukrasian Diagnosis, A magicked barrier is nullifying damage.
        """
        id = 24291
        name = {'Eukrasian Diagnosis'}

    class EukrasianPrognosis(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 100
Additional Effect: Erects a magicked barrier which nullifies damage equaling (source.job==40?(source.level>=85?320:230):230)% of the amount of HP restored
Duration: 30s
Effect cannot be stacked with those of Eukrasian Diagnosis or scholar's Galvanize.
※This action cannot be assigned to a hotbar.
>> 2609, Eukrasian Prognosis, A magicked barrier is nullifying damage.
>> 2866, Eukrasian Prognosis, A magicked barrier is nullifying damage.
        """
        id = 24292
        name = {'Eukrasian Prognosis'}

    class EukrasianDosis(ActionBase):
        """
Deals unaspected damage over time.
Potency: (source.job==40?(source.level>=64?40:(source.job==40?(source.level>=54?35:30):30)):(source.job==40?(source.level>=54?35:30):30))
Duration: 30s
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
※This action cannot be assigned to a hotbar.
>> 2614, Eukrasian Dosis, Sustaining unaspected damage over time.
        """
        id = 24293
        name = {'Eukrasian Dosis'}

    class Soteria(ActionBase):
        """
Increases the cure potency of Kardion effects granted by you by 50%.
Duration: 15s
>> 2610, Soteria, The healing potency of Kardia is increased.
        """
        id = 24294
        name = {'Soteria'}

    class Icarus(ActionBase):
        """
Rush to a targeted enemy's or party member's location.
Unable to cast if bound.
        """
        id = 24295
        name = {'Icarus'}

    class Druochole(ActionBase):
        """
Restores target's HP.
Cure Potency: 600
Additional Effect: Restores 7% of maximum MP
Addersgall Cost: 1
        """
        id = 24296
        name = {'Druochole'}

    class Dyskrasia(ActionBase):
        """
Deals unaspected damage with a potency of 160 to all nearby enemies.
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
        """
        id = 24297
        name = {'Dyskrasia'}

    class Kerachole(ActionBase):
        """
Reduces damage taken by self and nearby party members by 10%.
Duration: 15s
Effect cannot be stacked with Taurochole.
(source.job==40?(source.level>=78?Additional Effect: Regen
Cure Potency: 100
Duration: 15s
:):)Additional Effect: Restores 7% of maximum MP
Addersgall Cost: 1
>> 2618, Kerachole, Damage taken is reduced.
        """
        id = 24298
        name = {'Kerachole'}

    class Ixochole(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 400
Additional Effect: Restores 7% of maximum MP
Addersgall Cost: 1
        """
        id = 24299
        name = {'Ixochole'}

    class Zoe(ActionBase):
        """
Increases healing magic potency of your next healing spell by 50%.
Duration: 30s
>> 2611, Zoe, Healing magic potency of next spell cast is increased.
        """
        id = 24300
        name = {'Zoe'}

    class Pepsis(ActionBase):
        """
Restores own HP and the HP of nearby party members by removing Eukrasian Diagnosis and Eukrasian Prognosis effects granted by you.
Eukrasian Diagnosis Cure Potency: 450
Eukrasian Prognosis Cure Potency: 350
Targets not under the effect of Eukrasian Diagnosis or Eukrasian Prognosis will not be healed.
        """
        id = 24301
        name = {'Pepsis'}

    class PhysisIi(ActionBase):
        """
Gradually restores own HP and the HP of all nearby party members.
Cure Potency: 130
Duration: 15s
Additional Effect: Increases HP recovered by healing actions by 10%
Duration: 10s
>> 2620, Physis II, Regenerating HP over time.
        """
        id = 24302
        name = {'Physis II'}

    class Taurochole(ActionBase):
        """
Restores own or target party member's HP.
Cure Potency: 700
Additional Effect: Reduces target's damage taken by 10%
Duration: 15s
Effect cannot be stacked with Kerachole.
Additional Effect: Restores 7% of maximum MP
Addersgall Cost: 1
>> 2619, Taurochole, Damage taken is reduced.
        """
        id = 24303
        name = {'Taurochole'}

    class Toxikon(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of (source.job==40?(source.level>=72?300:240):240) for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
Addersting Cost: 1
        """
        id = 24304
        name = {'Toxikon'}

    class Haima(ActionBase):
        """
Erects a magicked barrier around self or target party member that absorbs damage equivalent to a heal of 300 potency.
Additional Effect: Grants 5 stacks of Haimatinon
Duration: 15s
When the barrier is completely absorbed, a stack of Haimatinon is consumed and a new barrier is applied.
When the effect duration expires, a healing effect is then applied.
Cure Potency: 150 per remaining stack of Haimatinon
>> 2612, Haima, A magicked barrier is nullifying damage.
>> 2869, Haima, A magicked barrier is nullifying damage.
        """
        id = 24305
        name = {'Haima'}

    class DosisIi(ActionBase):
        """
Deals unaspected damage with a potency of 320.
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
        """
        id = 24306
        name = {'Dosis II'}

    class PhlegmaIi(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 490 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
Maximum Charges: 2
This action does not share a recast timer with any other actions.
        """
        id = 24307
        name = {'Phlegma II'}

    class EukrasianDosisIi(ActionBase):
        """
Deals unaspected damage over time.
Potency: 60
Duration: 30s
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
※This action cannot be assigned to a hotbar.
>> 2615, Eukrasian Dosis II, Sustaining unaspected damage over time.
        """
        id = 24308
        name = {'Eukrasian Dosis II'}

    class Rhizomata(ActionBase):
        """
Grants 1 stack of Addersgall.
        """
        id = 24309
        name = {'Rhizomata'}

    class Holos(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 300
Additional Effect: Reduces damage taken by self and nearby party members by 10%
Duration: 20s
>> 3003, Holos, Damage taken is reduced.
        """
        id = 24310
        name = {'Holos'}

    class Panhaima(ActionBase):
        """
Erects a magicked barrier around self and all party members near you that absorbs damage equivalent to a heal of 200 potency.
Additional Effect: Grants 5 stacks of Panhaimatinon
Duration: 15s
When the barrier is completely absorbed, a stack of Panhaimatinon is consumed and a new barrier is applied.
When the effect duration expires, a healing effect is then applied.
Cure Potency: 100 per remaining stack of Panhaimatinon
>> 2613, Panhaima, A magicked barrier is nullifying damage.
        """
        id = 24311
        name = {'Panhaima'}

    class DosisIii(ActionBase):
        """
Deals unaspected damage with a potency of 330.
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
        """
        id = 24312
        name = {'Dosis III'}

    class PhlegmaIii(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 510 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
Maximum Charges: 2
This action does not share a recast timer with any other actions.
        """
        id = 24313
        name = {'Phlegma III'}

    class EukrasianDosisIii(ActionBase):
        """
Deals unaspected damage over time.
Potency: 70
Duration: 30s
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
※This action cannot be assigned to a hotbar.
>> 2616, Eukrasian Dosis III, Sustaining unaspected damage over time.
>> 2864, Eukrasian Dosis III, Weaponskill and spell cast time and recast time are increased.
        """
        id = 24314
        name = {'Eukrasian Dosis III'}

    class DyskrasiaIi(ActionBase):
        """
Deals unaspected damage with a potency of 170 to all nearby enemies.
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
        """
        id = 24315
        name = {'Dyskrasia II'}

    class ToxikonIi(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 330 for the first enemy, and 50% less for all remaining enemies.
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
Addersting Cost: 1
        """
        id = 24316
        name = {'Toxikon II'}

    class Krasis(ActionBase):
        """
Increases HP recovery via healing actions for a party member or self by 20%.
Duration: 10s
>> 2622, Krasis, HP recovery via healing actions is increased.
        """
        id = 24317
        name = {'Krasis'}

    class Pneuma(ActionBase):
        """
Deals unaspected damage to all enemies in a straight line before you with a potency of 330 for the first enemy, and 40% less for all remaining enemies.
Additional Effect: Restores own HP and the HP of all party members within a radius of 20 yalms
Cure Potency: 600
Additional Effect: Restores HP to targets under the effect of Kardion granted by you
Cure Potency: (source.job==40?(source.level>=85?170:130):130)
This action does not share a recast timer with any other actions.
>> 2868, Pneuma, Damage taken is reduced.
>> 2623, Pneuma, Damage taken is reduced.
        """
        id = 24318
        name = {'Pneuma'}
