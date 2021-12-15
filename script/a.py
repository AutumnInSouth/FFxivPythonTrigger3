from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *


def main():
    # _QWORD *__fastcall sub_1407DE990(int a1, __int64 a2, __int64 a3, __int64 a4)
    sub_1407DE990 = CFUNCTYPE(c_int, c_int, c_int64, c_int64, c_int64)(BASE_ADDR + 0x7DE990)
    print(sub_1407DE990(1, 16145, CFUNCTYPE(c_int64, c_int64)(BASE_ADDR + 6858064)(16145), 0x0))


main()
