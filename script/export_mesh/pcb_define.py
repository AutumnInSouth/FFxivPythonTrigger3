from typing import Type
from common_define import *

_pcb_header: Type[Structure] = type('pcb_header', (Structure,), {'_fields_': [
    ('unknown_1', c_uint32),
    ('unknown_2', c_uint32),
    ('num_entries', c_uint32),  # count starts at 0
    ('total_indices', c_uint32),
    ('padding', c_uint64)
]})

_pcb_block_header: Type[Structure] = type('pcb_block_header', (Structure,), {'_fields_': [
    ('type', c_uint32),  # 0 for entry, 0x30 for group
    ('group_size', c_uint32),  # when group size in bytes for the group block
    # bounding box
    ('v1', Vec3),
    ('v2', Vec3),
    # number of vertices packed into 16 bit
    ('num_v16', c_uint16),
    # number of indices
    ('num_indices', c_uint16),
    # number of normal floar vertices
    ('num_vertices', c_uint32),
]})

_pcb_index_data: Type[Structure] = type('pcb_index_data', (Structure,), {'_fields_': [
    ('index', c_uint8 * 3),
    ('unknown', c_uint8 * 3),
    ('unknown1', c_uint8 * 6),
]})

_pcb_vec3_i16: Type[Structure] = type('pcb_vec3_i16', (Structure,), {'_fields_': [
    ('x', c_uint16),
    ('y', c_uint16),
    ('z', c_uint16),
]})

pcb_header_size = sizeof(_pcb_header)
pcb_block_header_size = sizeof(_pcb_block_header)
pcb_vec3_i16_size = sizeof(_pcb_vec3_i16)


class PcbData(Structure):
    vertices: list[Vec3]
    vertices_i16: list[pcb_vec3_i16_size]
    indices: list[_pcb_index_data]


class PcbBlock:
    def __init__(self, header: _pcb_header, data: 'PcbData'):
        self.header = header
        self.data = data


class PcbFile:
    def __init__(self, buf: bytearray):
        self.buf = buf
        self.header = _pcb_header.from_buffer(buf)
        self.entries: list[PcbBlock] = []
        offset = pcb_header_size
        is_group = True
        while is_group:
            block_header = _pcb_block_header.from_buffer(buf, offset)
            is_group = block_header.type == 0x30
            if is_group:
                self._parse_entry(offset + 0x30)
                offset += block_header.group_size
            else:
                self._parse_entry(offset)

    def _parse_entry(self, buf_offset: int):
        is_group = True
        while is_group:
            block_header = _pcb_block_header.from_buffer(self.buf, buf_offset)
            is_group = block_header.type == 0x30
            if is_group:
                self._parse_entry(buf_offset + 0x30)
                buf_offset += block_header.group_size
            else:
                self.entries.append(PcbBlock(block_header, type('pcb_block_data', (Structure,), {'_fields_': [
                    ('vertices', Vec3 * block_header.num_vertices),
                    ('vertices_i16', _pcb_vec3_i16 * block_header.num_v16),
                    ('indices', _pcb_index_data * block_header.num_indices),
                ]}).from_buffer(self.buf, buf_offset + pcb_block_header_size)))
