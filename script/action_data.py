from pandas.core.ops import invalid

from FFxivPythonTrigger.text_pattern import find_signature_point
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.saint_coinach import action_sheet
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct

windll.kernel32.ReadProcessMemory.argtypes = [c_void_p, c_void_p, c_void_p, c_size_t, POINTER(c_size_t)]


def col_offset(col_name):
    return action_sheet.header.find_column(col_name).offset


def read_ubyte(address: int):
    buffer = c_ubyte()
    if windll.kernel32.ReadProcessMemory(-1, address, byref(buffer), 1, None):
        return buffer.value
    else:
        err_code = windll.kernel32.GetLastError()
        windll.kernel32.SetLastError(0)
        raise Exception("ReadProcessMemory failed with error code %d" % err_code)


class action_struct(OffsetStruct({
    'omen': (c_ushort, col_offset('Omen')),
    'cast_type': (c_ubyte, col_offset('CastType')),
    'effect_range': (c_ubyte, col_offset('EffectRange')),
    'x_axis_modifier': (c_ubyte, col_offset('XAxisModifier')),
    'cast_100ms': (c_ushort, col_offset('Cast<100ms>')),
    '_name': (c_char * 10, 60)
}, 0x70)):
    @property
    def name(self):
        return self._name.decode('utf-8', errors='ignore')

    @name.setter
    def name(self, value):
        self._name = value.encode('utf-8')


action_data_call = CFUNCTYPE(c_int64, c_int64)(
    find_signature_point('E8 * * * * 48 8B E8 48 85 C0 74 ? 45 84 E4') + BASE_ADDR)

for row in action_sheet:
    start = action_data_call(row.key) + 60
    cnt = 0
    try:
        while read_ubyte(start + cnt): cnt += 1
        while not read_ubyte(start + cnt): cnt += 1
    except Exception:
        pass
    name: bytes = row["Name"].encode('utf-8')
    # new_len = len(name) + 6
    # if new_len > cnt: name = name[:cnt - 6]
    # name += f'|{row.key:0>4X}'.encode('utf-8')
    write_ubytes(start, bytearray(name.ljust(cnt, b'\0')))
