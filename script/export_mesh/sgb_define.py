from typing import Type
from common_define import *


class SgbDataType:
    Unknown0008 = 0x0008
    Group = 0x0100


class SgbGroupEntryType:
    Model = 0x01
    Gimmick = 0x06


_sgb_group_header: Type[Structure] = type('sgb_group_header', (Structure,), {'_fields_': [
    ('type', c_uint32),
    ('name_offset', c_int32),
    ('unknown08', c_uint32),
    ('unknown0C', c_uint32),
    ('unknown10', c_uint32),
    ('unknown14', c_uint32),
    ('unknown18', c_uint32),
    ('unknown1C', c_uint32),
    ('entry_count', c_int32),
    ('unknown24', c_uint32),
    ('unknown28', c_uint32),
    ('unknown2C', c_uint32),
    ('unknown30', c_uint32),
    ('unknown34', c_uint32),
    ('unknown38', c_uint32),
    ('unknown3C', c_uint32),
    ('unknown40', c_uint32),
    ('unknown44', c_uint32),
]})

_sgb_group_1c_header: Type[Structure] = type('sgb_group_1c_header', (Structure,), {'_fields_': [
    ('type', c_uint32),
    ('name_offset', c_int32),
    ('unknown08', c_uint32),
    ('entry_count', c_int32),
    ('unknown14', c_uint32),
    ('model_file_offset', c_int32),
    ('unknown_float3', Vec3),
    ('unknown_float3_2', Vec3),
    ('state_offset', c_int32),
    ('model_file_offset_2', c_int32),
    ('unknown_3', c_uint32),
    ('unknown_4', c_float),
    ('name_offset_2', c_int32),
    ('unknown_float3_3', Vec3),
]})

_sgb_group_1c_entry: Type[Structure] = type('sgb_group_1c_entry', (Structure,), {'_fields_': [
    ('unk', c_uint32),
    ('unk2', c_uint32),
    ('name_offset', c_int32),
    ('index', c_uint32),
    ('unk3', c_uint32),
    ('model_file_offset', c_int32),
]})

_sgb_entry_header: Type[Structure] = type('sgb_entry_header', (Structure,), {'_fields_': [
    ('type', c_uint32),
    ('unknown2', c_uint32),
    ('name_offset', c_int32),
    ('translation', Vec3),
    ('rotation', Vec3),
    ('scale', Vec3),
]})

_sgb_model_header: Type[Structure] = type('sgb_model_header', (Structure,), {'_fields_': [
    *_sgb_entry_header._fields_,
    ('model_file_offset', c_int32),
    ('collision_file_offset', c_int32),
]})

_sgb_header: Type[Structure] = type('sgb_header', (Structure,), {'_fields_': [
    ('magic', c_char * 4),
    ('file_size', c_uint32),
    ('unknown1', c_uint32),
    ('magic2', c_char * 4),
    ('unknown10', c_uint32),
    ('shared_offset', c_int32),
    ('unknown18', c_uint32),
    ('offset_1c', c_int32),
    ('unknown20', c_uint32),
    ('unknown24', c_uint32),
    ('unknown28', c_uint32),
    ('unknown2c', c_uint32),
    ('unknown30', c_uint32),
    ('unknown34', c_uint32),
    ('unknown38', c_uint32),
    ('unknown3c', c_uint32),
    ('unknown40', c_uint32),
    ('unknown44', c_uint32),
    ('unknown48', c_uint32),
    ('unknown4c', c_uint32),
    ('unknown50', c_uint32),
    ('unknown54', c_uint32),
]})

sgb_group_1c_header_size = sizeof(_sgb_group_1c_header)
sgb_group_header_size = sizeof(_sgb_group_header)


class SgbModelEntry:
    def __init__(self, buf: bytearray, offset: int, model_entry_type: int):
        self.buf = buf
        self.offset = offset
        self.model_entry_type = model_entry_type
        self.header = _sgb_model_header.from_buffer(buf, offset)
        self.name = get_string(buf, offset + self.header.name_offset)
        self.model_file_name = get_string(buf, offset + self.header.model_file_offset)
        self.collision_file_name = get_string(buf, offset + self.header.collision_file_offset)


class SgbGroup:
    def __init__(
            self,
            buf: bytearray,
            file: 'SgbFile',
            offset1c_objects: set[str],
            file_size: int,
            offset: int,
            is_offset1C: bool = False
    ):
        self.parent = file
        self.buf = buf
        self.entries = []
        if is_offset1C:
            header_1c = _sgb_group_1c_header.from_buffer(buf, offset)
            entries_offset = offset + sgb_group_1c_header_size
            for i in range(header_1c.entry_count):
                entry_offset = entries_offset + i * 24
                entry_model_file = get_string(
                    buf, entry_offset + _sgb_group_1c_entry.from_buffer(
                        buf, entry_offset
                    ).model_file_offset + 9
                )
                if '.sgb' in entry_model_file:
                    offset1c_objects.add(entry_model_file)
        else:
            header = _sgb_group_header.from_buffer(buf, offset)
            entries_offset = offset + sgb_group_header_size
            entry_offsets = (c_uint * header.entry_count).from_buffer(buf, entries_offset)
            self.name = get_string(buf, offset + header.name_offset)
            for i in range(header.entry_count):
                entry_offset = entries_offset + entry_offsets[i]
                if entry_offset > file_size:
                    raise Exception('SGB entry offset is out of bounds')
                group_entry_type = c_uint.from_buffer(buf, entry_offset).value
                if group_entry_type == SgbGroupEntryType.Model or group_entry_type == SgbGroupEntryType.Gimmick:
                    self.entries.append(SgbModelEntry(buf, entry_offset, group_entry_type))


_sgb_file_base_offset = 0x14


class SgbFile:
    def __init__(self, buf: bytearray):
        self.buf = buf
        self.header = _sgb_header.from_buffer(buf)
        if self.header.magic != b'SGB1' or self.header.magic2 != b'SCN1':
            raise Exception('Invalid SGB file')
        self.entries = []
        self.state_entries = set()
        self.entries.append(SgbGroup(buf, self, self.state_entries, self.header.file_size, _sgb_file_base_offset + self.header.shared_offset))
        self.entries.append(SgbGroup(buf, self, self.state_entries, self.header.file_size, _sgb_file_base_offset + self.header.offset_1c, True))

    def iter_group_entries(self):
        for group in self.entries:
            for entry in group.entries:
                yield entry
