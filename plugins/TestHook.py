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
        self.knock_back(self, BASE_ADDR + 0x81DF40)

    """_int64 __fastcall sub_14081DF40(__int64 a1, __int64 a2, __int64 a3, unsigned int a4)"""

    @PluginHook.decorator(c_int64, [c_int64, c_int64, c_int64, c_uint], True)
    def knock_back(self, hook, a1, a2, a3, a4):
        return 1
        ans = hook.original(a1, a2, a3, a4)
        self.logger(f"{ans:x} {a1:x} {a2:x} {a3:x} {a4:x}")
        return ans

        #     self.cast_hook2(self, BASE_ADDR + 0x6E8CA0)
    #
    # """_QWORD *__fastcall sub_1406E8CA0(__int64 a1, unsigned int a2, unsigned int a3, __int64 a4, int a5, int a6)"""
    #
    # @PluginHook.decorator(c_int64, [c_int64, c_uint, c_uint, POINTER(c_ushort), c_float, c_int], True)
    # def cast_hook2(self, hook, source_actor_ptr, skill_type, action_id, pos, facing, a6):
    #     return hook.original(source_actor_ptr, skill_type, 23511, pos, facing, a6)
