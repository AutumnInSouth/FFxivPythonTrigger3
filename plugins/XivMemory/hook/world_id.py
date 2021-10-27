from ctypes import *

from FFxivPythonTrigger.memory import read_ushort
from . import ValueBindHook


class WorldIdHook(ValueBindHook):
    argtypes = [c_int64, c_int64]
    restype = c_int64

    def get_value(self, a1, a2):
        return read_ushort(a2 + 4)
