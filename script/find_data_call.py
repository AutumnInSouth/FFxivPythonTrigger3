from ctypes import *

from FFxivPythonTrigger.memory import BASE_ADDR, read_ushort, read_ubyte
from FFxivPythonTrigger.text_pattern import search_from_text
from FFxivPythonTrigger.saint_coinach import status_sheet


def col_offset(col_name: str):
    return status_sheet.header.get_column(status_sheet.header.sheet_definition.find_column(col_name)).offset


check = {row.key: row['PartyListPriority'] for row in status_sheet if row['PartyListPriority']}
col = status_sheet.header.find_column('LockMovement')
print(col.offset,col.type)
t_offset = col.offset
t_mask = col.type - 0x19


def test_offset(offset: int):
    call = CFUNCTYPE(c_int64, c_int64)(BASE_ADDR + offset)
    for row in status_sheet:
        b = call(row.key)
        if not b:
            # print(f'{offset:x} no return at {row.key}')
            return False
        flag = read_ubyte(b + t_offset)
        if flag & t_mask != row['LockMovement']:
            #print(f'{offset:x} wrong value at {row.key} ({flag:b})')
            return False
    print(f'{offset:x} is found')
    return True


sig = '48 83 EC ? 48 8B 05 ? ? ? ? 44 8B C1 BA ? ? ? ? 48 8B 88 ? ? ? ? E8 ? ? ? ? 48 85 C0 75 ? 48 83 C4 ? C3 48 8B 00 48 83 C4 ? C3'
for offset, _ in search_from_text(sig):
    if test_offset(offset):
        print(hex(offset))
