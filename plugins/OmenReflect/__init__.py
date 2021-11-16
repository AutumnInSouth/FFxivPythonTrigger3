from ctypes import *
from FFxivPythonTrigger import PluginBase
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import BASE_ADDR, read_uint
from .reflect2 import reflect_data


class OmenReflect(PluginBase):
    name = "OmenReflect"

    def __init__(self):
        super().__init__()
        self.omen_hook(self, BASE_ADDR + 0x6E8CA0)

    @PluginHook.decorator(c_int64, [c_int64, c_uint, c_uint, POINTER(c_ushort), c_float, c_int], True)
    def omen_hook(self, hook, source_actor_ptr, skill_type, action_id, pos, facing, a6):
        if read_uint(source_actor_ptr + 0x74) > 0x20000000:
            return hook.original(source_actor_ptr, skill_type, reflect_data.get(action_id, action_id), pos, facing, a6)
