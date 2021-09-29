from ctypes import *
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from .enum import Jobs


class Attributes(OffsetStruct({
    'strength': (c_uint, 0x4),
    'dexterity': (c_uint, 0x8),
    'vitality': (c_uint, 0xc),
    'intelligence': (c_uint, 0x10),
    'mind': (c_uint, 0x14),
    'piety': (c_uint, 0x18),
    'tenacity': (c_uint, 0x4c),
    'attack': (c_uint, 0x50),
    'direct_hit': (c_uint, 0x58),
    'critical_hit ': (c_uint, 0x6c),
    'attack_magic_potency': (c_uint, 0x84),
    'heal_magic_potency': (c_uint, 0x88),
    'determination': (c_uint, 0xb0),
    'skill_speed': (c_uint, 0xb4),
    'spell_speed': (c_uint, 0xb8),
    'craft': (c_uint, 0x118),
    'control': (c_uint, 0x11c),
})):
    strength: int
    dexterity: int
    vitality: int
    intelligence: int
    mind: int
    piety: int
    tenacity: int
    attack: int
    direct_hit: int
    attack_magic_potency: int
    heal_magic_potency: int
    determination: int
    skill_speed: int
    spell_speed: int
    craft: int
    control: int


class Player(OffsetStruct({  # cn5.5
    'id': (c_uint, 0x54),
    'job': (Jobs, 0x6a),
    'jobs_level': (c_ushort * 29, 0x7a),
    'attr': (Attributes, 0x16c),
})):
    id: int
    job: Jobs
    jobs_level: list[int]
    attr: Attributes
