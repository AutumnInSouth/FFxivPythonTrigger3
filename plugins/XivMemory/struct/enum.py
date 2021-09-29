from ctypes import c_ubyte
from functools import cache

from FFxivPythonTrigger.saint_coinach import realm
from FFxivPythonTrigger.memory.struct_factory import EnumStruct


class ActorType(EnumStruct(c_ubyte, {
    0: 'null',
    1: 'player',
    2: 'battle_npc',
    3: 'event_npc',
    4: 'treasure',
    5: 'aetheryte',
    6: 'gathering_point',
    7: 'event_obj',
    8: 'mount_type',
    9: 'companion',  # minion
    10: 'retainer',
    11: 'area',
    12: 'housing',
    13: 'cutscene',
    14: 'card_stand',
})):
    pass


job_sheet = realm.game_data.get_sheet('ClassJob')
job_category_sheet = realm.game_data.get_sheet('ClassJobCategory')


@cache
def is_job_in_category(category_id, job_id) -> bool:
    n = job_short_name(job_id)
    if n:
        return job_category_sheet[category_id][n]
    return False


@cache
def job_name(job_id):
    return job_sheet[job_id]['Name']


@cache
def job_short_name(job_id):
    try:
        return job_sheet[job_id]['Abbreviation']
    except:
        return ""


_job_name_key = {row.key: row['Name'] for row in job_sheet} | {
    5: 'Archer',  # 弓箭手 Arc
    19: 'Paladin',  # 骑士PLD
    20: 'Monk',  # 武僧MNK
    21: 'Warrior',  # 战士WAR
    22: 'Dragoon',  # 龙骑士DRG
    23: 'Bard',  # 吟游诗人BRD
    24: 'WhiteMage',  # 白魔法师WHM
    25: 'BlackMage',  # 黑魔法师BLM
    26: 'Arcanist',  # 秘术师ACN
    27: 'Summoner',  # 召唤师SMN
    28: 'Scholar',  # 学者SCH
    30: 'Ninja',  # 忍者NIN
    31: 'Machinist',  # 机工士MCH
    32: 'DarkKnight',  # 暗黑骑士DRK
    33: 'Astrologian',  # 占星术士AST
    34: 'Samurai',  # 武士SAM
    35: 'RedMage',  # 赤魔法师RDM
    36: 'BlueMage',  # 青魔BLM
    37: 'Gunbreaker',  # 绝枪战士GNB
    38: 'Dancer',  # 舞者DNC
}


class Jobs(EnumStruct(c_ubyte, _job_name_key)):
    @property
    def name(self):
        return job_name(self.raw_value)

    @property
    def short_name(self):
        return job_short_name(self.raw_value)

    @property
    def is_melee(self):
        return is_job_in_category(86, self.raw_value)

    @property
    def is_range(self):
        return is_job_in_category(87, self.raw_value)

    @property
    def is_tank(self):
        return is_job_in_category(156, self.raw_value)

    @property
    def is_healer(self):
        return is_job_in_category(157, self.raw_value)

    @property
    def is_dps(self):
        return is_job_in_category(131, self.raw_value)

    @property
    def is_physic_dps(self):
        return is_job_in_category(158, self.raw_value)

    @property
    def is_magic_dps(self):
        return is_job_in_category(159, self.raw_value)


class ChatType(object):
    none = 0
    debug = 1
    urgent = 2
    notice = 3
    say = 10
    shout = 11
    tell_outgoing = 12
    tell_incoming = 13
    party = 14
    alliance = 15
    link_shell_1 = 16
    link_shell_2 = 17
    link_shell_3 = 18
    link_shell_4 = 19
    link_shell_5 = 20
    link_shell_6 = 21
    link_shell_7 = 22
    link_shell_8 = 23
    free_company = 24
    novice_network = 27
    custom_emote = 28
    standard_emote = 29
    yell = 30
    cross_party = 32
    pvp_team = 36
    cross_link_shell1 = 37
    echo = 56
    system_error = 58
    system_message = 57
    gathering_system_message = 59
    error_message = 60
    retainer_sale = 71
    cross_link_shell_2 = 101
    cross_link_shell_3 = 102
    cross_link_shell_4 = 103
    cross_link_shell_5 = 104
    cross_link_shell_6 = 105
    cross_link_shell_7 = 106
    cross_link_shell_8 = 107


INVENTORY_CONTAINERS = {
    "backpack": {0, 1, 2, 3},
    "equipment": {1000},
    "currency": {2000},
    "crystal": {2001},
    "mission_props": {2004},
    "main_hand": {3500},
    "off_hand": {3200},
    "head": {3201},
    "body": {3202},
    "gloves": {3203},
    "belt": {3204},
    "leggings": {3205},
    "feets": {3206},
    "earring": {3207},
    "necklace": {3208},
    "bracelet": {3209},
    "ring": {3300},
    "soul_crystal": {3400},
    "chocobo_backpack": {4000, 4001},
    "employee_backpack": {10000, 10001, 10002, 10003, 10004, 10005},
    "employee_equipment": {11000},
    "employee_currency": {12000},
    "employee_crystal": {12001},
    "employee_selling": {12002},
}
