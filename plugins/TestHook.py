import math
from FFxivPythonTrigger import *
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.saint_coinach import action_names, realm
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.utils import err_catch
from XivMemory import se_string
from OmenReflect.utils import action_struct

map_sheet = realm.game_data.get_sheet('Map')


def web_to_map(pos):
    c = map_sheet[plugins.XivMemory.map_id]['SizeFactor'] / 100
    return (41.0 / c * ((pos * c / 1000 + 1024.0) / 2048.0)) + 1.0


def web_to_raw(pos):
    return pos * 0.0305 - 1000


def raw_to_web(pos):
    return (pos + 1000) / 0.0305


def map_to_web(pos):
    c = map_sheet[plugins.XivMemory.map_id]['SizeFactor'] / 100
    return int(((pos - 1) * c / 41 * 2048 - 1024) / c)


class TestHook(PluginBase):
    name = "test_hook"

    def __init__(self):
        super().__init__()
        self.cnt = 0
        # self.omen_create(self, BASE_ADDR + 0x6FF1C0)
        # self.action_recast(self, BASE_ADDR + 0x07DE990)
        # self.sub_1416014C0(self, BASE_ADDR + 0x16014C0)
        # self.sub_140A41260(self, BASE_ADDR + 0xA41260)
        # self.set_omen_create(self, BASE_ADDR + 0x6F9C60)

    @PluginHook.decorator(c_int64, [c_int64, c_uint, c_uint, POINTER(c_ushort), c_float, c_int], True)
    def set_omen_create(self, hook, source_actor_ptr, skill_type, action_id, pos, facing, a6):
        """E8 ? ? ? ? 41 80 7E ? ? 0F 85 ? ? ? ? F3 0F 10 1D ? ? ? ?"""
        self.logger(f"{source_actor_ptr:x} {skill_type} {action_id} {pos} {facing} {a6}")
        return hook.original(source_actor_ptr, skill_type, action_id, pos, facing, a6)

    """__int64 __fastcall sub_1406FF1C0(__int64 source_actor_ptr, unsigned __int16 *web_pos, float a3, __int64 action_data, float a5, unsigned int a6)"""

    @PluginHook.decorator(c_int64, [c_int64, POINTER(c_ushort), c_float, POINTER(action_struct), c_float, c_uint], True)
    def omen_create(self, hook, source_actor_ptr, web_pos, facing, action_data, a5, a6):
        if read_uint(source_actor_ptr + 0x74) > 0x20000000 and action_data[0].omen:
            self.logger(f"c1 {read_string(source_actor_ptr + 0x30)} {source_actor_ptr:x}"
                        f" ({web_to_raw(web_pos[0]):.2f},{web_to_raw(web_pos[2]):.2f},{web_to_raw(web_pos[1]):.2f})"
                        f" {facing:.2f} {action_data[0]}")
        return hook.original(source_actor_ptr, web_pos, facing, action_data, a5, a6)

    # _QWORD *__fastcall sub_1407DE990(int a1, __int64 a2, __int64 a3, __int64 a4)
    @PluginHook.decorator(c_int, [c_int, c_int64, c_int64, c_int64], True)
    def action_recast(self, hook, a1, a2, a3, a4):
        self.cnt += 1
        if self.cnt >= 10:
            hook.uninstall()
        ans = hook.original(a1, a2, a3, a4)
        self.logger(f"{ans} {a1} {a2:x} {a3:x} {a4:x}")
        return ans

    """_BYTE *__fastcall sub_1416014C0(_QWORD *a1,unsigned int a2)"""

    @PluginHook.decorator(c_int64, [c_int64, c_uint], True)
    def sub_1416014C0(self, hook, a1, a2):
        self.cnt += 1
        if self.cnt >= 1000:
            hook.uninstall()
        ans = hook.original(a1, a2)
        str = read_string(ans)
        if str == "金刚极意":
            self.logger(f"{ans:x} {a1:x} {a2} {str}")
            hook.uninstall()
        return ans

    """__int64 __fastcall sub_140A41260(int a1, int a2, int a3, int a4, int a5, __int64 a6, __int64 a7, __int64 a8)"""

    @PluginHook.decorator(c_int64, [c_int, c_int, c_int, c_int, c_int, c_int64, c_int64, c_int64], True)
    @err_catch
    def sub_140A41260(self, hook, *args):
        self.logger(f"{args}")
        res = hook.original(*args)
        self.logger(f"{res}")
        return res
