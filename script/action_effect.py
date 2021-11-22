"""
v17 = sub_140A88C50();
v18 = sub_140A94860(v17, (unsigned int)v16);
"""
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger import plugins


def main():
    sub_140742B70 = CFUNCTYPE(c_int64, c_int64, c_int64)(BASE_ADDR + 0x0742B70)
    sub_1406CB800 = CFUNCTYPE(c_int64, c_int64)(BASE_ADDR + 0x06CB800)
    sub_14081E3D0 = CFUNCTYPE(c_int64, c_int64)(BASE_ADDR + 0x081E3D0)

    # qword_141DD62C0 = read_ulonglong(BASE_ADDR + 0x1DD62C0)
    # v9 = sub_140742B70(qword_141DD62C0, 0)
    # print(f"v9:{v9:x}")
    #v9 = addressof(plugins.XivMemory.actor_table.me)
    v9 = addressof(plugins.XivMemory.targets.current)
    v10 = sub_1406CB800(v9)
    print(f"v10:{v10:x}")
    v12 = CFUNCTYPE(c_int64, c_int64)(read_ulonglong(read_ulonglong(v10) + 664))(v10)
    print(f"v12:{v12:x}")
    v13 = sub_14081E3D0(v12)
    print(hex(v13))
