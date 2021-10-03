from ctypes import *

from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import plugin_hook
from FFxivPythonTrigger.memory import BASE_ADDR, read_ushort
from FFxivPythonTrigger.popular_struct import Vector3


class TestHook(PluginBase):
    name = "test_hook"

    """char __fastcall sub_1407AEE00(__int64 a1)"""

    def __init__(self):
        super().__init__()
        self.cnt = 0
        self.test_hook = self.TestHook(self, BASE_ADDR + 0x7AEE00)

    @plugin_hook(_restype=c_ubyte,
                 _argtypes=[c_int64],
                 _auto_install=True)
    def TestHook(self, hook, action_manager_address):
        ans = hook.original(action_manager_address)
        self.logger(ans, hex(action_manager_address),)
        return ans
