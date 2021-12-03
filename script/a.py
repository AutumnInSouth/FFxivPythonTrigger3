from FFxivPythonTrigger.saint_coinach import action_sheet
from FFxivPythonTrigger.memory import *


def main():
    # _QWORD *__fastcall sub_14068A550(unsigned int a1)
    sub_14068A550 = CFUNCTYPE(POINTER(c_ubyte), c_uint)(BASE_ADDR + 0x68A550)
    sm: set | None = None
    for row in action_sheet:
        o = row['Omen'].key
        s = set()
        ptr = sub_14068A550(row.key)
        for i in range(200):
            if ptr[i] == o: s.add(i)
        if sm is not None:
            sm = sm.intersection(s)
        else:
            sm = s
        if len(sm) <2:
            break
    print(sm)
