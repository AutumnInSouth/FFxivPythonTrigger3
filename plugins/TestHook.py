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
        self.cast_hook2(self, BASE_ADDR + 0x6E8CA0)
        # self.omen_hook1(self, BASE_ADDR + 0x6EDF70)
        # self.omen_hook1(self, BASE_ADDR + 0x6EDF79)
        # self.omen_hook2(self, BASE_ADDR + 0x6EE2B0)
        #self.omen_data_hook(self, BASE_ADDR + 0x6764B0)
        self.cast_omen_reflect = {}

    @PluginHook.decorator(c_int64, [c_uint, c_int64], True)
    def cast_hook1(self, hook, target, data):
        ans = hook.original(target, data)
        self.logger(hex(ans), '<-', hex(target), hex(data))
        return ans

    """_QWORD *__fastcall sub_1406E8CA0(__int64 a1, unsigned int a2, unsigned int a3, __int64 a4, int a5, int a6)"""

    @PluginHook.decorator(c_int64, [c_int64, c_uint, c_uint, POINTER(c_ushort), c_float, c_int], True)
    def cast_hook2(self, hook, source_actor_ptr, skill_type, action_id, pos, facing, a6):
        return hook.original(source_actor_ptr, skill_type, 22474, pos, facing, a6)

    """void __fastcall sub_1406EDF70(__int64 *source_actor, unsigned __int16 *pos_ptr, __int64 action_omen, float a4)"""

    @PluginHook.decorator(c_int64, [c_int64, c_int64, c_int64, c_float], True)
    def omen_hook1(self, hook, source_actor_ptr, pos_ptr, action_omen, a4):
        ans = hook.original(source_actor_ptr, pos_ptr, action_omen, a4)
        self.logger('omen_hook1', hex(ans), '<-', hex(source_actor_ptr), hex(pos_ptr), hex(action_omen), a4)
        return ans

    """void __fastcall sub_1406EE2B0(__int64 source_actor, unsigned __int16 *pos_ptr, float a3, __int64 action_omen, float a5)"""

    @PluginHook.decorator(c_int64, [c_int64, c_int64, c_float, c_int64, c_float], True)
    def omen_hook2(self, hook, source_actor_ptr, pos_ptr, a3, action_omen, a5):
        ans = hook.original(source_actor_ptr, pos_ptr, a3, action_omen, a5)
        self.logger('omen_hook2', hex(ans), '<-', hex(source_actor_ptr), hex(pos_ptr), a3, hex(action_omen), a5)
        return ans

    """_QWORD *__fastcall sub_1406764B0(unsigned int a1)"""

    @PluginHook.decorator(c_int64, [c_int64], True)
    @err_catch
    def omen_data_hook(self, hook, action_id):
        ans=hook.original(action_id)
        data = cast(ans, POINTER(c_ubyte))
        match data[35]:
            case t if 0 < t < 8:
                data[24] = c_ubyte(1)
        return ans
