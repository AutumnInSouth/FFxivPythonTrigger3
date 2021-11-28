import math
from FFxivPythonTrigger import *
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.saint_coinach import action_names
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.utils import err_catch
from XivMemory import se_string


class TestHook(PluginBase):
    name = "test_hook"

    def __init__(self):
        super().__init__()
        self.cnt = 0
        self.test(3596)
        self.action_check(self, BASE_ADDR + 0x8047D0).install_and_enable()
        self.test(3596)



    def test(self, test_action):
        sub_14080B1F0 = CFUNCTYPE(c_int64, c_int64, c_uint, c_uint, c_uint, c_ubyte, c_ubyte)(BASE_ADDR + 0x80B1F0)
        self.logger(sub_14080B1F0(BASE_ADDR + 0x1d60580, 1, test_action, 0xe0000000, 1, 1))

    """bool __fastcall sub_1408047D0(unsigned int a1, unsigned int a2)"""
    @PluginHook.decorator(c_ubyte, [c_uint, c_uint])
    def action_check(self, hook, a1, a2):
        self.cnt += 1
        if self.cnt > 10: PluginHook.uninstall(hook)
        ans = hook.original(a1, a2)
        self.logger(f"{ans:x} {a1} {a2}")
        return ans

        #     self.cast_hook2(self, BASE_ADDR + 0x6E8CA0)
    #
    # """_QWORD *__fastcall sub_1406E8CA0(__int64 a1, unsigned int a2, unsigned int a3, __int64 a4, int a5, int a6)"""
    #
    # @PluginHook.decorator(c_int64, [c_int64, c_uint, c_uint, POINTER(c_ushort), c_float, c_int], True)
    # def cast_hook2(self, hook, source_actor_ptr, skill_type, action_id, pos, facing, a6):
    #     return hook.original(source_actor_ptr, skill_type, 23511, pos, facing, a6)
