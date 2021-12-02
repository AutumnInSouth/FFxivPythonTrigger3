from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Stone(ActionBase):
        """
        Deals earth damage with a potency of 140.
        """
        id = 119
        name = {"Stone", "飞石"}

    class Cure(ActionBase):
        """
        Restores target's HP. Cure Potency: 450(source.level>=32?(source.job==6? Additional Effect: 15% chance next Cure II will cost no MP Duration: 15s:(source.job==24? Additional Effect: 15% chance next Cure II will cost no MP Duration: 15s:)):)
        """
        id = 120
        name = {"Cure", "治疗"}

    class Aero(ActionBase):
        """
        Deals wind damage with a potency of 50. Additional Effect: Wind damage over time Potency: 30 Duration: 18s
        143, Aero, Aero, Sustaining wind damage over time.
        """
        id = 121
        name = {"Aero", "疾风"}

    class Medica(ActionBase):
        """
        Restores own HP and the HP of all nearby party members. Cure Potency: 300
        """
        id = 124
        name = {"Medica", "医治"}

    class Raise(ActionBase):
        """
        Resurrects target to a weakened state.
        148, Raise, Raise, Teetering on the brink of consciousness.
        1140, Raise, Raise, Teetering on the brink of consciousness.
        """
        id = 125
        name = {"Raise", "复活"}

    class StoneIi(ActionBase):
        """
        Deals earth damage with a potency of 200.
        """
        id = 127
        name = {"Stone II", "坚石"}

    class CureIii(ActionBase):
        """
        Restores HP of target and all party members nearby target. Cure Potency: 550
        """
        id = 131
        name = {"Cure III", "愈疗"}

    class AeroIi(ActionBase):
        """
        Deals wind damage with a potency of 60. Additional Effect: Wind damage over time Potency: 60 Duration: 18s
        144, Aero II, Aero II, Sustaining wind damage over time.
        """
        id = 132
        name = {"Aero II", "烈风"}

    class MedicaIi(ActionBase):
        """
        Restores own HP and the HP of all nearby party members. Cure Potency: 200 Additional Effect: Regen Cure Potency: 100 Duration: 15s
        150, Medica II, Medica II, Regenerating HP over time.
        """
        id = 133
        name = {"Medica II", "医济"}

    class FluidAura(ActionBase):
        """
        Binds target. Duration: 6s
        """
        id = 134
        name = {"Fluid Aura", "水流环"}

    class CureIi(ActionBase):
        """
        Restores target's HP. Cure Potency: 700
        """
        id = 135
        name = {"Cure II", "救疗"}

    class PresenceOfMind(ActionBase):
        """
        Reduces spell cast time and recast time, and auto-attack delay by 20%. Duration: 15s
        157, Presence of Mind, Presence of Mind, Spell cast times, recast times, and auto-attack delay are reduced.
        """
        id = 136
        name = {"Presence of Mind", "神速咏唱"}

    class Regen(ActionBase):
        """
        Grants healing over time effect to target. Cure Potency: 200 Duration: 18s
        158, Regen, Regen, Regenerating HP over time.
        897, Regen, Regen, Regenerating HP over time.
        1330, Regen, Regen, Regenerating HP over time.
        """
        id = 137
        name = {"Regen", "再生"}

    class Holy(ActionBase):
        """
        Deals unaspected damage with a potency of 140 to all nearby enemies. Additional Effect: Stun Duration: 4s
        """
        id = 139
        name = {"Holy", "神圣"}

    class Benediction(ActionBase):
        """
        Restores all of a target's HP.
        """
        id = 140
        name = {"Benediction", "天赐祝福"}

    class StoneIii(ActionBase):
        """
        Deals earth damage with a potency of 240.
        """
        id = 3568
        name = {"Stone III", "垒石"}

    class Asylum(ActionBase):
        """
        Envelops a designated area in a veil of succor, granting healing over time to self and any party members who enter. Cure Potency: 100 Duration: 24s (source.job==24?(source.level>=78? Additional Effect: Increases HP recovery via healing actions on party members in the designated area by 10%:):)
        739, Asylum, Asylum, A veil of succor is healing party members in the area.
        1911, Asylum, Asylum, A veil of succor is healing party members in the area.
        1912, Asylum, Asylum, HP recovery via healing actions is increased.
        """
        id = 3569
        name = {"Asylum", "庇护所"}

    class Tetragrammaton(ActionBase):
        """
        Restores target's HP. Cure Potency: 700
        """
        id = 3570
        name = {"Tetragrammaton", "神名"}

    class Assize(ActionBase):
        """
        Deals unaspected damage with a potency of 400 to all nearby enemies. Additional Effect: Restores own HP and the HP of nearby party members Cure Potency: 400 Additional Effect: Restores 5% of maximum MP
        """
        id = 3571
        name = {"Assize", "法令"}

    class ThinAir(ActionBase):
        """
        Reduces MP cost of all actions by 100%. Duration: 12s
        1217, Thin Air, Thin Air, Spells consume no MP.
        """
        id = 7430
        name = {"Thin Air", "无中生有"}

    class StoneIv(ActionBase):
        """
        Deals earth damage with a potency of 280.
        """
        id = 7431
        name = {"Stone IV", "崩石"}

    class DivineBenison(ActionBase):
        """
        Creates a barrier around self or target party member that absorbs damage equivalent to a heal of 500 potency. Duration: 15s
        1218, Divine Benison, Divine Benison, A holy blessing from the gods is nullifying damage.
        1404, Divine Benison, Divine Benison, A holy blessing from the gods is nullifying damage.
        """
        id = 7432
        name = {"Divine Benison", "神祝祷"}

    class PlenaryIndulgence(ActionBase):
        """
        Grants Confession to self and nearby party members. Upon receiving HP recovery via Medica, Medica II, Cure III, or Afflatus Rapture cast by self, Confession triggers an additional healing effect. Cure Potency: 200 Duration: 10s
        """
        id = 7433
        name = {"Plenary Indulgence", "全大赦"}

    class AfflatusSolace(ActionBase):
        """
        Restores target's HP. Cure Potency: 700(source.job==24?(source.level>=74? Additional Effect: Nourishes the Blood Lily:):) Healing Gauge Cost: 1 Lily
        2036, Afflatus Solace, Afflatus Solace, Regenerating HP over time.
        """
        id = 16531
        name = {"Afflatus Solace", "安慰之心"}

    class Dia(ActionBase):
        """
        Deals unaspected damage with a potency of 120. Additional Effect: Unaspected damage over time Potency: 60 Duration: 30s
        1871, Dia, Dia, Sustaining damage over time.
        2035, Dia, Dia, Damage taken is increased.
        """
        id = 16532
        name = {"Dia", "天辉"}

    class Glare(ActionBase):
        """
        Deals unaspected damage with a potency of 300.
        """
        id = 16533
        name = {"Glare", "闪耀"}

    class AfflatusRapture(ActionBase):
        """
        Restores own HP and the HP of all nearby party members. Cure Potency: 300 Additional Effect: Nourishes the Blood Lily Healing Gauge Cost: 1 Lily
        """
        id = 16534
        name = {"Afflatus Rapture", "狂喜之心"}

    class AfflatusMisery(ActionBase):
        """
        Deals unaspected damage to target and all enemies nearby it with a potency of 900 for the first enemy, and 25% less for all remaining enemies. Can only be executed when the Blood Lily is in full bloom.
        """
        id = 16535
        name = {"Afflatus Misery", "苦难之心"}

    class Temperance(ActionBase):
        """
        Increases healing magic potency by 20%, while reducing damage taken by self and all party members within a radius of 30 yalms by 10%. Duration: 20s
        1872, Temperance, Temperance, Healing magic potency is increased while damage taken by nearby party members is reduced.
        1873, Temperance, Temperance, Damage taken is reduced.
        2037, Temperance, Temperance, Damage dealt and potency of all HP restoration actions are increased while damage taken by nearby party members is reduced.
        2038, Temperance, Temperance, Damage taken is reduced.
        """
        id = 16536
        name = {"Temperance", "节制"}
