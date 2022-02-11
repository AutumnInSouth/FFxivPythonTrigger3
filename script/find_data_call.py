from ctypes import *

from FFxivPythonTrigger.memory import BASE_ADDR, read_ushort, read_ubyte
from FFxivPythonTrigger.text_pattern import search_from_text
from FFxivPythonTrigger.saint_coinach import status_sheet, realm


def col_offset(col_name: str):
    return status_sheet.header.get_column(status_sheet.header.sheet_definition.find_column(col_name)).offset


def test_status_offset(offset: int):
    call = CFUNCTYPE(c_int64, c_int64)(BASE_ADDR + offset)
    col = status_sheet.header.find_column('LockMovement')
    for row in status_sheet:
        b = call(row.key)
        if not b: return False
        flag = read_ubyte(b + col.offset)
        if flag & (col.type - 0x19) != row['LockMovement']: return False
    print(f'{offset:x} is found')
    return True


text_command_sheet = realm.game_data.get_sheet('TextCommand')


def test_tc(offset: int):
    t = CFUNCTYPE(POINTER(c_ubyte), c_int64)(BASE_ADDR + offset)(237)
    if t:print(f"{offset:x} {t}")
    if t and text_command_sheet[237]['ShortCommand'].encode('utf-8') in bytes(t[:300]):
        print(f'{offset:x} is found')
        return True
    return False


sig = '48 83 EC ? 48 8B 05 ? ? ? ? 44 8B C1 BA ? ? ? ? 48 8B 88 ? ? ? ? E8 ? ? ? ? 48 85 C0 75 ? 48 83 C4 ? C3 48 8B 00 48 83 C4 ? C3'
for offset, _ in search_from_text(sig):
    if test_tc(offset):
        print(hex(offset))
