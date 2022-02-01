from typing import Type
from common_define import *


class LgbEntryType:
    BgParts = 1
    Light = 3
    Vfx = 4
    PositionMarker = 5
    Gimmick = 6
    SharedGroup6 = 6  # secondary variable is set to 2
    Sound = 7
    EventNpc = 8
    BattleNpc = 9
    Aetheryte = 12
    EnvSpace = 13
    Gathering = 14
    SharedGroup15 = 15  # secondary variable is set to 13
    Treasure = 16
    Weapon = 39
    PopRange = 40
    ExitRange = 41
    MapRange = 43
    NaviMeshRange = 44
    EventObject = 45
    EnvLocation = 47
    EventRange = 49
    QuestMarker = 51
    CollisionBox = 57
    DoorRange = 58
    LineVfx = 59
    ClientPath = 65
    ServerPath = 66
    GimmickRange = 67
    TargetMarker = 68
    ChairMarker = 69
    ClickableRange = 70
    PrefetchRange = 71
    FateRange = 72
    SphereCastRange = 75


_instance_object: Type[Structure] = type('instance_object', (Structure,), {'_fields_': [
    ('type', c_uint),
    ('unknown', c_uint),
    ('name_offset', c_uint),
    ('translation', Vec3),
    ('rotation', Vec3),
    ('scale', Vec3),
]})
_bg_parts_data: Type[Structure] = type('bg_parts_data', (Structure,), {'_fields_': [
    *_instance_object._fields_,
    ('model_file_offset', c_uint),
    ('collision_file_offset', c_uint),
    ('unknown4', c_uint),
    ('unknown5', c_uint),
    ('unknown6', c_uint),
    ('unknown7', c_uint),
    ('unknown8', c_uint),
    ('unknown9', c_uint),
]})
_gimmick_data: Type[Structure] = type('gimmick_data', (Structure,), {'_fields_': [
    *_instance_object._fields_,
    ('gimmick_file_offset', c_uint),
    ('unk_bytes', c_ubyte * 100)
]})
_e_npc_data: Type[Structure] = type('e_npc_data', (Structure,), {'_fields_': [
    *_instance_object._fields_,
    ('e_npc_id', c_uint),
    ('unk_bytes', c_ubyte * 0x24)
]})
_e_obj_data: Type[Structure] = type('e_obj_data', (Structure,), {'_fields_': [
    *_instance_object._fields_,
    ('e_obj_id', c_uint),
    ('level_hierachy_id', c_uint),
    ('unk_bytes', c_ubyte * 0xC),
]})
_map_range_data: Type[Structure] = type('map_range_data', (Structure,), {'_fields_': [
    *_instance_object._fields_,
    ('map_type', c_uint),
    ('unknown2', c_ushort),
    ('unknown3', c_ushort),
    ('unknown4', c_ubyte * 0x10),
]})
_collision_box_header: Type[Structure] = type('collisiion_box_data', (Structure,), {'_fields_': [
    *_instance_object._fields_,
    ('unk_bytes', c_ubyte * 100)
]})


class LgbEntry:
    entry = _instance_object
    header: Structure

    def __init__(self, buf: bytearray, offset: int):
        self.buf = buf
        self.offset = offset
        self._init_header()
        self.name = get_string(buf, self.header.name_offset + offset)

    def _init_header(self):
        self.header = self.entry.from_buffer(self.buf, self.offset)

    def entry_type(self):
        return self.header.type


class BgPartsData(LgbEntry):
    entry = _bg_parts_data

    def __init__(self, buf: bytearray, offset: int):
        super().__init__(buf, offset)
        self.model_file_name = get_string(buf, self.header.model_file_offset + offset)
        self.collision_file_name = get_string(buf, self.header.collision_file_offset + offset)


class GimmickData(LgbEntry):
    entry = _gimmick_data

    def __init__(self, buf: bytearray, offset: int):
        super().__init__(buf, offset)
        self.gimmick_file_name = get_string(buf, self.header.gimmick_file_offset + offset)


class ENpcData(LgbEntry):
    entry = _e_npc_data


class EObjData(LgbEntry):
    entry = _e_obj_data


class MapRangeData(LgbEntry):
    entry = _map_range_data


class CollisionBoxData(LgbEntry):
    entry = _collision_box_header


lgb_class = {
    LgbEntryType.BgParts: BgPartsData,
    LgbEntryType.Gimmick: GimmickData,
    LgbEntryType.EventObject: EObjData,
    LgbEntryType.CollisionBox: CollisionBoxData,
}

_lgb_group_header: Type[Structure] = type('lgb_group_header', (Structure,), {'_fields_': [
    ('unknown', c_uint32),
    ('group_name_offset', c_int32),
    ('entries_offset', c_int32),
    ('entry_count', c_int32),
    ('unknown2', c_uint32),
    ('unknown3', c_uint32),
    ('unknown4', c_uint32),
    ('unknown5', c_uint32),
    ('unknown6', c_uint32),
    ('unknown7', c_uint32),
    ('unknown8', c_uint32),
    ('unknown9', c_uint32),
    ('unknown10', c_uint32),
]})


class LgbGroup:
    def __init__(self, buf: bytearray, offset: int):
        self.buf = buf
        self.offset = offset
        self.header = _lgb_group_header.from_buffer(buf, offset)
        self.name = get_string(buf, self.header.group_name_offset + offset)
        entries_offset = self.header.entries_offset + offset
        entry_offsets = (c_uint * self.header.entry_count).from_buffer(buf, entries_offset)
        self.entries: list[BgPartsData | GimmickData | EObjData | CollisionBoxData] = []
        for i in range(self.header.entry_count):
            entry_offset = entries_offset + entry_offsets[i]
            entry_type = c_uint.from_buffer(buf, entry_offset).value
            if entry_type in lgb_class:
                self.entries.append(lgb_class[entry_type](buf, entry_offset))


_lgb_header: Type[Structure] = type('lgb_header', (Structure,), {'_fields_': [
    ('magic', c_char * 4),
    ('file_size', c_uint32),
    ('unknown', c_uint32),
    ('magic2', c_char * 4),
    ('unknown2', c_uint32),
    ('unknown3', c_uint32),
    ('unknown4', c_uint32),
    ('unknown5', c_uint32),
    ('group_count', c_int32),
]})
lgb_header_size = sizeof(_lgb_header)


class LgbFile:
    def __init__(self, buf: bytearray):
        self.buf = buf
        self.header = _lgb_header.from_buffer(buf, 0)
        if self.header.magic != b'LGB1' or self.header.magic2 != b'LGP1':
            raise Exception('Invalid LGb file')
        self.groups: list[LgbGroup] = []
        group_offsets = (c_uint * self.header.group_count).from_buffer(buf, lgb_header_size)
        for i in range(self.header.group_count):
            group_offset = lgb_header_size + group_offsets[i]
            self.groups.append(LgbGroup(buf, group_offset))
