from FFxivPythonTrigger.memory import *

# a1 = 0x176a32ce3e0
#
# _a1 = read_ulonglong(a1 + 8)
#
# print(hex(read_ulonglong(read_ulonglong(_a1) + 64) - BASE_ADDR))
#
# v4 = _a1 + 0xb8e80
#
# print(hex(read_ulonglong(read_ulonglong(v4) + 72) - BASE_ADDR))
# print(hex(read_ulonglong(read_ulonglong(_a1) + 272) - BASE_ADDR))
# v5=_a1+0xc8828
# res = read_ulonglong(v5+32+8*4)
# print(hex(res))

a1 = 0x176a32cd9c0
print(hex(read_ulonglong(a1 + 2480)))
