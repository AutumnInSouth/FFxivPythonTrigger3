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
        #self.omen_create(self, BASE_ADDR + 0x6FF1C0)
        self.action_recast(self, BASE_ADDR + 0x07DE990)

    # """_QWORD *__fastcall sub_1406F9730(__int64 a1, unsigned int a2, unsigned int a3, __int64 a4, int a5, int a6)"""
    #
    # @PluginHook.decorator(c_int64, [c_int64, c_uint, c_uint, POINTER(c_ushort), c_float, c_int], True)
    # def omen_create(self, hook, source_actor_ptr, skill_type, action_id, pos, facing, a6):
    #     true_pos = [web_to_true(pos[0]), web_to_true(pos[1]), web_to_true(pos[2])]
    #     self.logger(f"{read_string(source_actor_ptr + 0x30)} {skill_type} {action_id} {true_pos} {facing} {a6}")
    #     #self.create_mission(self.recall, 5, [source_actor_ptr, skill_type, action_id, pos, facing, a6])
    #     return hook.original(source_actor_ptr, skill_type, action_id, pos, facing, a6)
    #
    # def recall(self, after, argus):
    #     sleep(after)
    #     self.omen_create_hook.original(*argus)

    """__int64 __fastcall sub_1406FF1C0(__int64 source_actor_ptr, unsigned __int16 *web_pos, float a3, __int64 action_data, float a5, unsigned int a6)"""

    @PluginHook.decorator(c_int64, [c_int64, POINTER(c_ushort), c_float, POINTER(action_struct), c_float, c_uint], True)
    def omen_create(self, hook, source_actor_ptr, web_pos, facing, action_data, a5, a6):
        if read_uint(source_actor_ptr + 0x74) > 0x20000000 and action_data[0].omen:
            self.logger(f"c1 {read_string(source_actor_ptr + 0x30)} {source_actor_ptr:x}"
                        f" ({web_to_raw(web_pos[0]):.2f},{web_to_raw(web_pos[2]):.2f},{web_to_raw(web_pos[1]):.2f})"
                        f" {facing:.2f} {action_data[0]}")
        return hook.original(source_actor_ptr, web_pos, facing, action_data, a5, a6)

    #_QWORD *__fastcall sub_1407DE990(int a1, __int64 a2, __int64 a3, __int64 a4)
    @PluginHook.decorator(c_int, [c_int, c_int64, c_int64, c_int64], True)
    def action_recast(self, hook, a1, a2, a3, a4):
        self.cnt+=1
        if self.cnt>=10:
            hook.uninstall()
        ans = hook.original(a1, a2, a3, a4)
        self.logger(f"{ans} {a1} {a2:x} {a3:x} {a4:x}")
        return ans
