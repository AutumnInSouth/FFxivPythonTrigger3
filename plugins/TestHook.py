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
        self.action(self,BASE_ADDR+0x7ea2d0)

    """char __fastcall sub_1407EA2D0(__int64 a1, unsigned int a2, unsigned int a3, __int64 a4, int a5, int a6, int a7, _BYTE *a8)"""

    @PluginHook.decorator(c_ubyte, [c_int64, c_uint, c_uint, c_int64, c_uint, c_uint, c_int, c_void_p],True)
    def action(self, hook, *args):
        ans = hook.original(*args)
        self.logger(f"{ans:x} {args} ")
        return ans

        #     self.cast_hook2(self, BASE_ADDR + 0x6E8CA0)
    #
    # """_QWORD *__fastcall sub_1406E8CA0(__int64 a1, unsigned int a2, unsigned int a3, __int64 a4, int a5, int a6)"""
    #
    # @PluginHook.decorator(c_int64, [c_int64, c_uint, c_uint, POINTER(c_ushort), c_float, c_int], True)
    # def cast_hook2(self, hook, source_actor_ptr, skill_type, action_id, pos, facing, a6):
    #     return hook.original(source_actor_ptr, skill_type, 23511, pos, facing, a6)
