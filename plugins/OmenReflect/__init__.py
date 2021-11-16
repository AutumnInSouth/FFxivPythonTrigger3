from ctypes import *
from FFxivPythonTrigger import PluginBase
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import BASE_ADDR, read_uint
from .reflect import reflect_data


class OmenReflect(PluginBase):
    name = "OmenReflect"

    def __init__(self):
        super().__init__()
        self.omen_data_hook(self, BASE_ADDR + 0x6764B0)

    @PluginHook.decorator(c_int64, [c_int64], True)
    def omen_data_hook(self, hook, action_id):
        ans = hook.original(action_id)
        if action_id in reflect_data:
            cast(ans, POINTER(c_ubyte))[24] = reflect_data[action_id]
        return ans
