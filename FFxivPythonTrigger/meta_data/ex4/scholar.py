from ..base import *


class Actions:

    class Embrace(ActionBase):
        """
Restores target's HP.
Cure Potency: (source.job==28?(source.level>=85?180:150):150)
※This action cannot be assigned to a hotbar.
        """
        id = 802
        name = {'Embrace', '仙光的拥抱'}

    class Ruin(ActionBase):
        """
Deals unaspected damage with a potency of 150.
        """
        id = 17869
        name = {'Ruin', '毁灭'}

    class Bio(ActionBase):
        """
Deals unaspected damage over time.
Potency: 20
Duration: 30s
>> 179, Bio, Contagions are spreading, causing damage over time.
        """
        id = 17864
        name = {'毒菌', 'Bio'}

    class Physick(ActionBase):
        """
Restores target's HP.
Cure Potency: (source.job==28?(source.level>=85?450:400):400)
        """
        id = 190
        name = {'医术', 'Physick'}

    class SummonEos(ActionBase):
        """
Summons the faerie Eos to fight at your side. When set to guard, automatically casts Embrace on party members who suffer damage.
        """
        id = 17215
        name = {'Summon Eos', '朝日召唤'}

    class SummonSelene(ActionBase):
        """
Summons the faerie Selene to fight at your side. When set to guard, automatically casts Embrace on party members who suffer damage.
        """
        id = 17216
        name = {'Summon Selene', '夕月召唤'}

    class WhisperingDawn(ActionBase):
        """
Gradually restores the HP of all nearby party members.
Cure Potency: 80
Duration: 21s
※This action cannot be assigned to a hotbar.
>> 315, Whispering Dawn, Regenerating HP over time.
        """
        id = 803
        name = {'仙光的低语', 'Whispering Dawn'}

    class WhisperingDawn(ActionBase):
        """
Orders faerie to execute Whispering Dawn.(source.job==28?(source.level>=80? If Seraph is summoned, orders her to execute Angel's Whisper.:):)
Whispering Dawn(source.job==28?(source.level>=80?/Angel's Whisper:):) Effect: Gradually restores the HP of all nearby party members
Cure Potency: 80
Duration: 21s
>> 315, Whispering Dawn, Regenerating HP over time.
        """
        id = 16537
        name = {'仙光的低语', 'Whispering Dawn'}

    class BioIi(ActionBase):
        """
Deals unaspected damage over time.
Potency: 40
Duration: 30s
>> 189, Bio II, Lungs are failing, causing damage over time.
        """
        id = 17865
        name = {'猛毒菌', 'Bio II'}

    class Adloquium(ActionBase):
        """
Restores target's HP.
Cure Potency: 300
Additional Effect: Grants Galvanize to target, nullifying damage equaling (source.job==28?(source.level>=85?180:125):125)% of the amount of HP restored. When critical HP is restored, also grants Catalyze, nullifying damage equaling (source.job==28?(source.level>=85?180:125):125)% the amount of HP restored.
Duration: 30s
Effect cannot be stacked with certain sage barrier effects.
        """
        id = 185
        name = {'鼓舞激励之策', 'Adloquium'}

    class Succor(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 200
Additional Effect: Erects a magicked barrier which nullifies damage equaling (source.job==28?(source.level>=85?160:115):115)% of the amount of HP restored
Duration: 30s
Effect cannot be stacked with certain sage barrier effects.
>> 166, Succor, Next Succor will cost no MP.
        """
        id = 186
        name = {'士气高扬之策', 'Succor'}

    class RuinIi(ActionBase):
        """
Deals unaspected damage with a potency of (source.job==28?(source.level>=82?220:(source.job==28?(source.level>=72?200:(source.job==28?(source.level>=64?180:(source.job==28?(source.level>=54?160:140):140)):(source.job==28?(source.level>=54?160:140):140))):(source.job==28?(source.level>=64?180:(source.job==28?(source.level>=54?160:140):140)):(source.job==28?(source.level>=54?160:140):140)))):(source.job==28?(source.level>=72?200:(source.job==28?(source.level>=64?180:(source.job==28?(source.level>=54?160:140):140)):(source.job==28?(source.level>=54?160:140):140))):(source.job==28?(source.level>=64?180:(source.job==28?(source.level>=54?160:140):140)):(source.job==28?(source.level>=54?160:140):140)))).
        """
        id = 17870
        name = {'毁坏', 'Ruin II'}

    class FeyIllumination(ActionBase):
        """
Increases healing magic potency of all nearby party members by 10%, while reducing magic damage taken by all nearby party members by 5%.
Duration: 20s
Effect cannot be stacked with Seraphic Illumination.
※This action cannot be assigned to a hotbar.
>> 317, Fey Illumination, Magic defense and healing magic potency are increased.
        """
        id = 805
        name = {'Fey Illumination', '异想的幻光'}

    class FeyIllumination(ActionBase):
        """
Orders faerie to execute Fey Illumination.(source.job==28?(source.level>=80? If Seraph is summoned, orders her to execute Seraphic Illumination.:):)
Fey Illumination(source.job==28?(source.level>=80?/Seraphic Illumination:):) Effect: Increases healing magic potency of all nearby party members by 10%, while reducing magic damage taken by all nearby party members by 5%
Duration: 20s(source.job==28?(source.level>=80?
Effect cannot be stacked with Seraphic Illumination.:):)
>> 317, Fey Illumination, Magic defense and healing magic potency are increased.
        """
        id = 16538
        name = {'Fey Illumination', '异想的幻光'}

    class Aetherflow(ActionBase):
        """
Restores 20% of maximum MP.
Additional Effect: Aetherflow III
Can only be executed while in combat.
>> 304, Aetherflow, Aether is gathering in the body.
        """
        id = 166
        name = {'Aetherflow', '以太超流'}

    class EnergyDrain(ActionBase):
        """
Deals unaspected damage with a potency of 100.
Additional Effect: Absorbs a portion of damage dealt as HP
(source.level>=70?(source.job==28?Additional Effect: Increases Faerie Gauge by 10
:):)Aetherflow Gauge Cost: 1
        """
        id = 167
        name = {'Energy Drain', '能量吸收'}

    class Lustrate(ActionBase):
        """
Restores target's HP.
Cure Potency: 600
(source.level>=70?(source.job==28?Additional Effect: Increases Faerie Gauge by 10
:):)Aetherflow Gauge Cost: 1
        """
        id = 189
        name = {'Lustrate', '生命活性法'}

    class ArtOfWar(ActionBase):
        """
Deals unaspected damage with a potency of (source.job==28?(source.level>=54?165:150):150) to all nearby enemies.
        """
        id = 16539
        name = {'破阵法', 'Art of War'}

    class SacredSoil(ActionBase):
        """
Creates a designated area in which party members will only suffer 90% of all damage inflicted.
Duration: 15s
(source.job==28?(source.level>=78?Additional Effect: Regen
Cure Potency: 100
:):)(source.level>=70?(source.job==28?Additional Effect: Increases Faerie Gauge by 10
:):)Aetherflow Gauge Cost: 1
>> 298, Sacred Soil, An area of land has been sanctified, reducing damage taken for all who enter.
>> 299, Sacred Soil, Damage taken is reduced.
>> 2637, Sacred Soil, A circle of sanctified earth is healing party members and reducing damage taken within its bounds.
>> 2638, Sacred Soil, Damage taken is reduced.
>> 1944, Sacred Soil, A circle of sanctified earth is healing party members and reducing damage taken within its bounds.
        """
        id = 188
        name = {'Sacred Soil', '野战治疗阵'}

    class Indomitability(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: 400
(source.level>=70?(source.job==28?Additional Effect: Increases Faerie Gauge by 10
:):)Aetherflow Gauge Cost: 1
        """
        id = 3583
        name = {'Indomitability', '不屈不挠之策'}

    class Broil(ActionBase):
        """
Deals unaspected damage with a potency of 220.
        """
        id = 3584
        name = {'Broil', '气炎法'}

    class DeploymentTactics(ActionBase):
        """
Extends Galvanize effect cast on self or target to nearby party members.
Duration: Time remaining on original effect
No effect when target is not under the effect of Galvanize.
        """
        id = 3585
        name = {'展开战术', 'Deployment Tactics'}

    class EmergencyTactics(ActionBase):
        """
Transforms the next Galvanize and Catalyze statuses into HP recovery equaling the amount of damage reduction intended for the barrier.
Duration: 15s
>> 792, Emergency Tactics, The next Galvanize and Catalyze statuses are transformed into HP recovery equaling the amount of damage reduction intended for their barriers.
        """
        id = 3586
        name = {'应急战术', 'Emergency Tactics'}

    class Dissipation(ActionBase):
        """
Orders your faerie away while granting you a full Aetherflow stack. Also increases healing magic potency by 20%.
Duration: 30s
Current faerie will return once the effect expires.
Summon Eos or Summon Selene cannot be executed while under the effect of Dissipation.
Can only be executed while in combat.
>> 2069, Dissipation, Damage dealt and potency of all HP restoration actions are increased.
>> 791, Dissipation, Healing magic potency is increased.
        """
        id = 3587
        name = {'Dissipation', '转化'}

    class Excogitation(ActionBase):
        """
Grants self or target party member the effect of Excogitation, restoring HP when member's HP falls below 50% or upon effect duration expiration.
Cure Potency: 800
Duration: 45s
(source.level>=70?(source.job==28?Additional Effect: Increases Faerie Gauge by 10
:):)Aetherflow Gauge Cost: 1
>> 1220, Excogitation, HP will be restored automatically upon falling below a certain level or expiration of effect duration.
>> 2182, Excogitation, HP will be restored automatically upon falling below a certain level or expiration of effect duration.
        """
        id = 7434
        name = {'Excogitation', '深谋远虑之策'}

    class BroilIi(ActionBase):
        """
Deals unaspected damage with a potency of 240.
        """
        id = 7435
        name = {'Broil II', '魔炎法'}

    class ChainStratagem(ActionBase):
        """
Increases rate at which target takes critical hits by 10%.
Duration: 15s
>> 1221, Chain Stratagem, Rate at which critical hits are taken is increased.
>> 1406, Chain Stratagem, Damage taken is increased.
        """
        id = 7436
        name = {'Chain Stratagem', '连环计'}

    class Aetherpact(ActionBase):
        """
Orders faerie to execute Fey Union with target party member. Effect ends upon reuse.
Faerie Gauge Cost: 10
The Faerie Gauge increases when (source.job==28?(source.level>=80?a faerie or Seraph:a faerie):a faerie) is summoned and an Aetherflow action is successfully executed while in combat.
        """
        id = 7437
        name = {'Aetherpact', '以太契约'}

    class FeyUnion(ActionBase):
        """
Gradually restores HP of party member with which faerie has a Fey Union.
Cure Potency: 300
Faerie Gauge is depleted while HP is restored. Fey Union effect fades upon execution of other faerie actions. Party member must be within 15 yalms.
※This action cannot be assigned to a hotbar.
>> 1222, Fey Union, Allowing regeneration of HP over time.
>> 1223, Fey Union, Regenerating HP over time.
        """
        id = 7438
        name = {'Fey Union', '异想的融光'}

    class DissolveUnion(ActionBase):
        """
Dissolves current Fey Union.
        """
        id = 7869
        name = {'Dissolve Union', '融光解除'}

    class Biolysis(ActionBase):
        """
Deals unaspected damage over time.
Potency: 70
Duration: 30s
>> 2039, Biolysis, Rapid decomposition of the flesh is reducing HP recovery.
>> 1895, Biolysis, Sustaining damage over time.
        """
        id = 16540
        name = {'蛊毒法', 'Biolysis'}

    class BroilIii(ActionBase):
        """
Deals unaspected damage with a potency of 255.
        """
        id = 16541
        name = {'死炎法', 'Broil III'}

    class Recitation(ActionBase):
        """
Allows the execution of Adloquium, Succor, Indomitability, or Excogitation without consuming resources while also ensuring critical HP is restored.
Duration: 15s
>> 1896, Recitation, The next Adloquium, Succor, Indomitability, or Excogitation executed will cost no MP or Aetherflow stacks and will restore critical HP.
        """
        id = 16542
        name = {'秘策', 'Recitation'}

    class FeyBlessing(ActionBase):
        """
Orders faerie to execute Fey Blessing.
Fey Blessing Effect: Restores the HP of all nearby party members
Cure Potency: 320
        """
        id = 16543
        name = {'异想的祥光', 'Fey Blessing'}

    class FeyBlessing(ActionBase):
        """
Restores the HP of all nearby party members.
Cure Potency: 320
※This action cannot be assigned to a hotbar.
        """
        id = 16544
        name = {'异想的祥光', 'Fey Blessing'}

    class SummonSeraph(ActionBase):
        """
Summons Seraph to fight at your side. When set to guard, automatically casts Seraphic Veil on party members who suffer damage.
Cannot summon Seraph unless a pet is already summoned. Current pet will leave the battlefield while Seraph is present, and return once gone.
Duration: 22s
※Action changes to Consolation upon execution.
        """
        id = 16545
        name = {'Summon Seraph', '炽天召唤'}

    class Consolation(ActionBase):
        """
Orders Seraph to execute Consolation.
Consolation Effect: Restores the HP of all nearby party members
Cure Potency: 250
Additional Effect: Erects a magicked barrier which nullifies damage equaling the amount of HP restored
Duration: 30s
Maximum Charges: 2
        """
        id = 16546
        name = {'慰藉', 'Consolation'}

    class Consolation(ActionBase):
        """
Restores the HP of all nearby party members.
Cure Potency: 250
Additional Effect: Erects a magicked barrier which nullifies damage equaling the amount of HP restored
Duration: 30s
※This action cannot be assigned to a hotbar.
        """
        id = 16547
        name = {'慰藉', 'Consolation'}

    class SeraphicVeil(ActionBase):
        """
Restores target's HP.
Cure Potency: (source.job==28?(source.level>=85?180:150):150)
Additional Effect: Erects a magicked barrier which nullifies damage equaling the amount of HP restored
Duration: 30s
※This action cannot be assigned to a hotbar.
>> 2040, Seraphic Veil, An aetherial barrier is preventing damage.
>> 1917, Seraphic Veil, A holy barrier is nullifying damage.
        """
        id = 16548
        name = {'Seraphic Veil', '炽天的幕帘'}

    class AngelsWhisper(ActionBase):
        """
Gradually restores the HP of all nearby party members.
Cure Potency: 80
Duration: 21s
※This action cannot be assigned to a hotbar.
>> 1874, Angel's Whisper, Regenerating HP over time.
        """
        id = 16550
        name = {"Angel's Whisper", '天使的低语'}

    class SeraphicIllumination(ActionBase):
        """
Increases healing magic potency of nearby party members by 10%, while reducing magic damage taken by nearby party members by 5%.
Duration: 20s
Effect cannot be stacked with Fey Illumination.
※This action cannot be assigned to a hotbar.
>> 1875, Seraphic Illumination, Magic defense and healing magic potency are increased.
        """
        id = 16551
        name = {'炽天的幻光', 'Seraphic Illumination'}

    class BroilIv(ActionBase):
        """
Deals unaspected damage with a potency of 295.
        """
        id = 25865
        name = {'Broil IV'}

    class ArtOfWarIi(ActionBase):
        """
Deals unaspected damage with a potency of 180 to all nearby enemies.
        """
        id = 25866
        name = {'Art of War II'}

    class Protraction(ActionBase):
        """
Increases maximum HP of a party member or self by 10% and restores the amount increased.
Additional Effect: Increases HP recovery via healing actions by 10%
Duration: 10s
>> 2710, Protraction, Maximum HP is increased and HP recovery via healing actions is increased.
        """
        id = 25867
        name = {'Protraction'}

    class Expedient(ActionBase):
        """
Grants Expedience and Desperate Measures to all nearby party members.
Expedience Effect: Increases movement speed
Desperate Measures Effect: Reduces damage taken by 10%
Duration: 20s
        """
        id = 25868
        name = {'Expedient'}
