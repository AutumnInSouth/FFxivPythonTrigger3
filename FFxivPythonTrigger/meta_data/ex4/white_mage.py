from ..base import *


class Actions:

    class Stone(ActionBase):
        """
Deals earth damage with a potency of 140.
        """
        id = 119
        name = {'飞石', 'Stone'}

    class Cure(ActionBase):
        """
Restores target's HP.
Cure Potency: (source.job==24?(source.level>=85?500:450):450)(source.level>=32?(source.job==6?
Additional Effect: 15% chance next Cure II will cost no MP
Duration: 15s:(source.job==24?
Additional Effect: 15% chance next Cure II will cost no MP
Duration: 15s:)):)
        """
        id = 120
        name = {'Cure', '治疗'}

    class Aero(ActionBase):
        """
Deals wind damage with a potency of 50.
Additional Effect: Wind damage over time
Potency: 30
Duration: 18s
>> 143, Aero, Sustaining wind damage over time.
        """
        id = 121
        name = {'疾风', 'Aero'}

    class Medica(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: (source.job==24?(source.level>=85?400:300):300)
        """
        id = 124
        name = {'Medica', '医治'}

    class Raise(ActionBase):
        """
Resurrects target to a weakened state.
>> 1140, Raise, Teetering on the brink of consciousness.
>> 148, Raise, Teetering on the brink of consciousness.
        """
        id = 125
        name = {'复活', 'Raise'}

    class StoneIi(ActionBase):
        """
Deals earth damage with a potency of 190.
        """
        id = 127
        name = {'Stone II', '坚石'}

    class CureIi(ActionBase):
        """
Restores target's HP.
Cure Potency: (source.job==24?(source.level>=85?800:700):700)
        """
        id = 135
        name = {'Cure II', '救疗'}

    class PresenceOfMind(ActionBase):
        """
Reduces spell cast time and recast time, and auto-attack delay by 20%.
Duration: 15s
>> 157, Presence of Mind, Spell cast times, recast times, and auto-attack delay are reduced.
        """
        id = 136
        name = {'Presence of Mind', '神速咏唱'}

    class Regen(ActionBase):
        """
Grants healing over time effect to target.
Cure Potency: (source.job==24?(source.level>=85?250:200):200)
Duration: 18s
>> 897, Regen, Regenerating HP over time.
>> 1330, Regen, Regenerating HP over time.
>> 158, Regen, Regenerating HP over time.
        """
        id = 137
        name = {'再生', 'Regen'}

    class CureIii(ActionBase):
        """
Restores HP of target and all party members nearby target.
Cure Potency: (source.job==24?(source.level>=85?600:550):550)
        """
        id = 131
        name = {'Cure III', '愈疗'}

    class Holy(ActionBase):
        """
Deals unaspected damage with a potency of 140 to all nearby enemies.
Additional Effect: Stun
Duration: 4s
        """
        id = 139
        name = {'神圣', 'Holy'}

    class AeroIi(ActionBase):
        """
Deals wind damage with a potency of 60.
Additional Effect: Wind damage over time
Potency: 60
Duration: 18s
>> 144, Aero II, Sustaining wind damage over time.
        """
        id = 132
        name = {'烈风', 'Aero II'}

    class MedicaIi(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: (source.job==24?(source.level>=85?250:200):200)
Additional Effect: Regen
Cure Potency: (source.job==24?(source.level>=85?150:100):100)
Duration: 15s
>> 150, Medica II, Regenerating HP over time.
        """
        id = 133
        name = {'医济', 'Medica II'}

    class Benediction(ActionBase):
        """
Restores all of a target's HP.
        """
        id = 140
        name = {'天赐祝福', 'Benediction'}

    class Asylum(ActionBase):
        """
Envelops a designated area in a veil of succor, granting healing over time to self and any party members who enter.
Cure Potency: 100
Duration: 24s (source.job==24?(source.level>=78?
Additional Effect: Increases HP recovery via healing actions on party members in the designated area by 10%:):)
>> 739, Asylum, A veil of succor is healing party members in the area.
>> 1911, Asylum, A veil of succor is healing party members in the area.
>> 1912, Asylum, HP recovery via healing actions is increased.
        """
        id = 3569
        name = {'Asylum', '庇护所'}

    class AfflatusSolace(ActionBase):
        """
Restores target's HP.
Cure Potency: (source.job==24?(source.level>=85?800:700):700)(source.job==24?(source.level>=74?
Additional Effect: Nourishes the Blood Lily:):)
Healing Gauge Cost: 1 Lily
>> 2036, Afflatus Solace, Regenerating HP over time.
        """
        id = 16531
        name = {'安慰之心', 'Afflatus Solace'}

    class StoneIii(ActionBase):
        """
Deals earth damage with a potency of 230.
        """
        id = 3568
        name = {'垒石', 'Stone III'}

    class Assize(ActionBase):
        """
Deals unaspected damage with a potency of 400 to all nearby enemies.
Additional Effect: Restores own HP and the HP of nearby party members
Cure Potency: 400
Additional Effect: Restores 5% of maximum MP
        """
        id = 3571
        name = {'法令', 'Assize'}

    class ThinAir(ActionBase):
        """
Next action is executed without MP cost.
Duration: 12s
Maximum Charges: 2
>> 1217, Thin Air, Next spell cast consumes no MP.
        """
        id = 7430
        name = {'Thin Air', '无中生有'}

    class Tetragrammaton(ActionBase):
        """
Restores target's HP.
Cure Potency: 700
        """
        id = 3570
        name = {'神名', 'Tetragrammaton'}

    class StoneIv(ActionBase):
        """
Deals earth damage with a potency of 270.
        """
        id = 7431
        name = {'崩石', 'Stone IV'}

    class DivineBenison(ActionBase):
        """
Creates a barrier around self or target party member that absorbs damage equivalent to a heal of 500 potency.
Duration: 15s(source.job==24?(source.level>=88?
Maximum Charges: 2:):)
>> 1218, Divine Benison, A holy blessing from the gods is nullifying damage.
>> 1404, Divine Benison, A holy blessing from the gods is nullifying damage.
        """
        id = 7432
        name = {'Divine Benison', '神祝祷'}

    class PlenaryIndulgence(ActionBase):
        """
Grants Confession to self and nearby party members.
Upon receiving HP recovery via Medica, Medica II, Cure III, or Afflatus Rapture cast by self, Confession triggers an additional healing effect.
Cure Potency: 200
Duration: 10s
        """
        id = 7433
        name = {'Plenary Indulgence', '全大赦'}

    class Dia(ActionBase):
        """
Deals unaspected damage with a potency of 60.
Additional Effect: Unaspected damage over time
Potency: 60
Duration: 30s
>> 2035, Dia, Damage taken is increased.
>> 1871, Dia, Sustaining damage over time.
        """
        id = 16532
        name = {'天辉', 'Dia'}

    class Glare(ActionBase):
        """
Deals unaspected damage with a potency of 290.
        """
        id = 16533
        name = {'Glare', '闪耀'}

    class AfflatusMisery(ActionBase):
        """
Deals unaspected damage to target and all enemies nearby it with a potency of 900 for the first enemy, and 25% less for all remaining enemies.
Can only be executed when the Blood Lily is in full bloom.
        """
        id = 16535
        name = {'Afflatus Misery', '苦难之心'}

    class AfflatusRapture(ActionBase):
        """
Restores own HP and the HP of all nearby party members.
Cure Potency: (source.job==24?(source.level>=85?400:300):300)
Additional Effect: Nourishes the Blood Lily
Healing Gauge Cost: 1 Lily
        """
        id = 16534
        name = {'Afflatus Rapture', '狂喜之心'}

    class Temperance(ActionBase):
        """
Increases healing magic potency by 20%, while reducing damage taken by self and all party members within a radius of 30 yalms by 10%.
Duration: 20s
>> 1872, Temperance, Healing magic potency is increased while damage taken by nearby party members is reduced.
>> 1873, Temperance, Damage taken is reduced.
>> 2037, Temperance, Damage dealt and potency of all HP restoration actions are increased while damage taken by nearby party members is reduced.
>> 2038, Temperance, Damage taken is reduced.
        """
        id = 16536
        name = {'节制', 'Temperance'}

    class GlareIii(ActionBase):
        """
Deals unaspected damage with a potency of 310.
        """
        id = 25859
        name = {'Glare III'}

    class HolyIii(ActionBase):
        """
Deals unaspected damage with a potency of 150 to all nearby enemies.
Additional Effect: Stun
Duration: 4s
        """
        id = 25860
        name = {'Holy III'}

    class Aquaveil(ActionBase):
        """
Reduces damage taken by a party member or self by 15%.
Duration: 8s
>> 2708, Aquaveil, Damage taken is reduced.
        """
        id = 25861
        name = {'Aquaveil'}

    class LiturgyOfTheBell(ActionBase):
        """
Places a healing blossom at the designated location and grants 5 stacks of Liturgy of the Bell to self.
Duration: 15s
Taking damage will expend 1 stack of Liturgy of the Bell to heal self and all party members within a radius of 20 yalms.
Cure Potency: 400
The effect of this action can only be triggered once per second.
The healing blossom dissipates when all stacks are expended or the effect expires.
Any remaining stacks of Liturgy of the Bell when effect expires will trigger an additional healing effect.
Cure Potency: 200 for every remaining stack of Liturgy of the Bell
This action does not share a recast timer with any other actions.
>> 2709, Liturgy of the Bell, Triggers a healing effect upon taking damage or when duration expires.
        """
        id = 25862
        name = {'Liturgy of the Bell'}
