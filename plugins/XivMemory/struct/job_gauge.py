from FFxivPythonTrigger.memory.struct_factory import OffsetStruct, EnumStruct
from ctypes import *


def byte_get_bit(byte: int, start: int, length: int):
    return (1 << length) - 1 & byte >> start


class RedMageGauge(OffsetStruct({
    'white_mana': (c_ubyte, 0),
    'black_mana': (c_ubyte, 1),
}, 16)):
    white_mana: int
    black_mana: int


class WarriorGauge(OffsetStruct({
    'beast': (c_ubyte, 0)
}, 16)):
    beast: int


class GunbreakerGauge(OffsetStruct({
    'cartridges': (c_ubyte, 0),
    'continuation_milliseconds': (c_ushort, 2),  # Is 15000 if and only if continuation_state is not zero.
    'continuation_state': (c_ubyte, 4)
}, 16)):
    cartridges: int
    continuation_milliseconds: int
    continuation_state: int


class DarkKnightGauge(OffsetStruct({
    'blood': (c_ubyte, 0),
    'darkside_timer': (c_ushort, 2),
    'dark_art': (c_ubyte, 4),
    'shadow_timer': (c_ushort, 6),
}, 16)):
    blood: int
    darkside_timer: int
    dark_art: int
    shadow_timer: int


class PaladinGauge(OffsetStruct({
    'oath': (c_ubyte, 0),
}, 16)):
    oath: int


BardSong = EnumStruct(c_ubyte, {
    0: '',
    5: 'ballad',
    10: 'paeon',
    15: 'minuet',
}, default='', name="BardSong")


class BardGauge(OffsetStruct({
    'song_milliseconds': (c_ushort, 0),
    'song_procs': (c_ubyte, 2),
    'soul_gauge': (c_ubyte, 3),
    'song_type': (BardSong, 4)
}, 16)):
    song_milliseconds: int
    song_procs: int
    soul_gauge: int
    song_type: BardSong


DancerStep = EnumStruct(c_ubyte, {
    0: '',
    1: 'emboite',  # red
    2: 'entrechat',  # blue
    3: 'jete',  # green
    4: 'pirouette',  # yellow
}, name="DancerStep")


class DancerGauge(OffsetStruct({
    'feathers': (c_ubyte, 0),
    'esprit': (c_ubyte, 1),
    'step': (DancerStep * 4, 2),
    'current_step': (c_ubyte, 6)
}, 16)):
    feathers: int
    esprit: int
    step: list[DancerStep]
    current_step: int


class DragoonGauge(OffsetStruct({
    'blood_or_life_ms': (c_ushort, 0),
    'stance': (c_ubyte, 2),  # 0 = None, 1 = Blood, 2 = Life
    'eyes_amount': (c_ubyte, 3),
}, 16)):
    blood_or_life_ms: int
    stance: int
    eyes_amount: int

    @property
    def blood_ms(self):
        return self.blood_or_life_ms if self.stance == 1 else 0

    @property
    def life_ms(self):
        return self.blood_or_life_ms if self.stance == 2 else 0


class NinjaGauge(OffsetStruct({
    'huton_ms': (c_uint, 0),
    'ninki_amount': (c_ubyte, 4),
    'huton_count': (c_ubyte, 5),
}, 16)):
    huton_ms: int
    ninki_amount: int
    huton_count: int


class ThaumaturgeGauge(OffsetStruct({
    'umbral_ms': (c_ushort, 2),  # Number of ms left in umbral fire/ice.
    'umbral_stacks': (c_byte, 4),  # Positive = Umbral Fire Stacks, Negative = Umbral Ice Stacks.
}, 16)):
    umbral_ms: int
    umbral_stacks: int


class BlackMageGauge(OffsetStruct({
    'next_polyglot_ms': (c_ushort, 0),
    'umbral_ms': (c_ushort, 2),
    'umbral_stacks': (c_byte, 4),
    'umbral_hearts': (c_ubyte, 5),
    'foul_count': (c_ubyte, 6),
    'enochain_state': (c_ubyte, 7),
}, 16)):
    next_polyglot_ms: int
    umbral_ms: int
    umbral_stacks: int
    umbral_hearts: int
    foul_count: int
    enochain_state: int

    @property
    def enochain_active(self):
        return byte_get_bit(self.enochain_state, 0, 1)

    @property
    def polygot_active(self):
        return byte_get_bit(self.enochain_state, 1, 1)


class WhiteMageGauge(OffsetStruct({
    'lily_ms': (c_ushort, 2),
    'lily_stacks': (c_ubyte, 4),
    'blood_lily_stacks': (c_ubyte, 5),
}, 16)):
    lily_ms: int
    lily_stacks: int
    blood_lily_stacks: int


class ArcanistGauge(OffsetStruct({
    'aether_flow_stacks': (c_ubyte, 4),
}, 16)):
    aether_flow_stacks: int


class SummonerGauge(OffsetStruct({
    'stance_ms': (c_ushort, 0),
    'return_summon': (c_ubyte, 2),
    'return_summon_glam': (c_ubyte, 3),
    'stacks': (c_ubyte, 4),
}, 16)):
    stance_ms: int
    return_summon: int
    return_summon_glam: int
    stacks: int

    @property
    def aether_flow_stacks(self):
        return byte_get_bit(self.stacks, 0, 2)

    @property
    def bahamut_ready(self):
        return self.stacks & 0b1000 > 0

    @property
    def phoenix_ready(self):
        return self.stacks & 0b10000 > 0


class ScholarGauge(OffsetStruct({
    'aether_flow_stacks': (c_ubyte, 2),
    'fairy_gauge': (c_ubyte, 3),
    'fairy_ms': (c_ushort, 4),  # Seraph time left ms.
    'fairy_status': (c_ubyte, 6)
    # Varies depending on which fairy was summoned, during Seraph/Dissipation: 6 - Eos, 7 - Selene, else 0.
}, 16)):
    aether_flow_stacks: int
    fairy_gauge: int
    fairy_ms: int
    fairy_status: int


class PuglistGauge(OffsetStruct({
    'lightning_ms': (c_ushort, 0),
    'lightning_stacks': (c_ubyte, 2),
}, 16)):
    lightning_ms: int
    lightning_stacks: int


class MonkGauge(OffsetStruct({
    'chakra_stacks': (c_ushort, 0),
}, 16)):
    chakra_stacks: int


class MachinistGauge(OffsetStruct({
    'overheat_ms': (c_ushort, 0),
    'battery_ms': (c_ushort, 2),
    'heat': (c_ubyte, 4),
    'battery': (c_ubyte, 5)
}, 16)):
    overheat_ms: int
    battery_ms: int
    heat: int
    battery: int


AstCard = EnumStruct(c_ubyte, {
    0: '',
    1: 'balance',
    2: 'bole',
    3: 'arrow',
    4: 'spear',
    5: 'ewer',
    6: 'spire',
}, name="AstCard")

AstArcanum = EnumStruct(c_ubyte, {
    0: '',
    1: 'solar',
    2: 'lunar',
    3: 'celestial',
}, name="AstArcanum")


class AstrologianGauge(OffsetStruct({
    'held_card': (AstCard, 4),
    'arcanums': (AstArcanum * 3, 5),
}, 16)):
    held_card: AstCard
    arcanums: list[AstArcanum]


class SamuraiGauge(OffsetStruct({
    'prev_kaeshi_time': (c_ushort, 0),
    'prev_kaeshi_lv': (c_ubyte, 2),
    'kenki': (c_ubyte, 3),
    'meditation': (c_ubyte, 4),
    'sen_bits': (c_ubyte, 5)
}, 16)):
    prev_kaeshi_time: int
    prev_kaeshi_lv: int
    kenki: int
    meditation: int
    sen_bits: int

    @property
    def snow(self):
        return bool(self.sen_bits & 1)

    @property
    def moon(self):
        return bool(self.sen_bits & 2)

    @property
    def flower(self):
        return bool(self.sen_bits & 4)


gauges = {
    'Paladin': PaladinGauge,  # 骑士PLD
    'Monk': MonkGauge,  # 武僧MNK
    'Warrior': WarriorGauge,  # 战士WAR
    'Dragoon': DragoonGauge,  # 龙骑士DRG
    'Bard': BardGauge,  # 吟游诗人BRD
    'WhiteMage': WhiteMageGauge,  # 白魔法师WHM
    'BlackMage': BlackMageGauge,  # 黑魔法师BLM
    'Arcanist': ArcanistGauge,  # 秘术师ACN
    'Summoner': SummonerGauge,  # 召唤师SMN
    'Scholar': ScholarGauge,  # 学者SCH
    'Ninja': NinjaGauge,  # 忍者NIN
    'Machinist': MachinistGauge,  # 机工士MCH
    'DarkKnight': DarkKnightGauge,  # 暗黑骑士DRK
    'Astrologian': AstrologianGauge,  # 占星术士AST
    'Samurai': SamuraiGauge,  # 武士SAM
    'RedMage': RedMageGauge,  # 赤魔法师RDM
    'Gunbreaker': GunbreakerGauge,  # 绝枪战士GNB
    'Dancer': DancerGauge,  # 舞者DNC
}
