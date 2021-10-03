from ctypes import *

from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import plugin_hook
from FFxivPythonTrigger.memory import BASE_ADDR, read_int, read_ulonglong


class TestHook(PluginBase):
    name = "test_hook"

    def __init__(self):
        super().__init__()
        self.cnt = 0
        self.recv(self, BASE_ADDR + 0x1F0090)

    """void (__fastcall **)(_QWORD, _QWORD, __int64))"""
    """__int64 __fastcall sub_1401F0090(__int64 a1)"""

    @plugin_hook(_argtypes=[c_int64, c_int64, c_int64], _auto_install=True)
    def recv(self, hook, a1, a2, a3):
        self.logger(f"{a1:x} {a2:x} {a3:x} ")
        hook.original(a1, a2, a3)
        self.cnt += 1
        if self.cnt > 10:
            hook.uninstall()
