from ctypes import *

from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import plugin_hook
from FFxivPythonTrigger.memory import BASE_ADDR, read_int, read_ulonglong, read_ubyte


class TestHook(PluginBase):
    name = "test_hook"

    def __init__(self):
        super().__init__()
        self.cnt = 0
        # self.h2(self, BASE_ADDR + 0x1284270)
        # self.h2(self, BASE_ADDR + 0x05C7890)
        self.h3(self, BASE_ADDR + 0x11697F0)
        self.h4(self, BASE_ADDR + 0xA63080)

    """char __fastcall sub_1408944C0(__int64 a1, __int64 a2)"""

    @plugin_hook(_restype=c_ubyte, _argtypes=[c_int64, c_int64], _auto_install=True)
    def h(self, hook, a1, a2):
        ans = hook.original(a1, a2)
        self.logger(f"{a1:x} {a2:x} {ans:x}")
        return ans

    """__int64 __fastcall sub_141284270(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)"""

    @plugin_hook(_restype=c_int64, _argtypes=[c_int64, c_int64, c_int64, c_int64, c_int64], _auto_install=True)
    def h2(self, hook, a1, a2, a3, a4, a5):
        ans = hook.original(a1, a2, a3, a4, a5)
        self.logger(f"{a1:x} {a2:x} {a3:x} {a4:x} {a5:x} {ans:x}")
        return ans

    """void __fastcall sub_1411697F0(__int64 a1)"""

    @plugin_hook(_restype=c_int64, _argtypes=[c_int64], _auto_install=True)
    def h3(self, hook, a1):
        self.logger('h3', f"{a1:x} {read_ulonglong(a1 + 48):x} {read_ubyte(a1 + 17)&1}")
        addr1=read_ulonglong(BASE_ADDR+0x1DFC080)
        self.logger('', f"{read_ubyte(a1 + 316)} {addr1:x} {read_ubyte(addr1)&0x10}")
        self.logger('','', f"{read_ubyte(a1 + 317)}")
        return hook.original(a1)

    """__int64 __fastcall sub_140A63080(__int64 a1)"""
    @plugin_hook(_restype=c_int64, _argtypes=[c_int64], _auto_install=True)
    def h4(self, hook, a1):
        self.logger('h4', f"{a1:x}")
        ans = hook.original(a1)
        self.logger('h4-a', f"{ans:x}")
        return ans
