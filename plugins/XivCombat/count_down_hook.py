from ctypes import *
from time import perf_counter
from FFxivPythonTrigger.hook import PluginHook


class CountDownHook(PluginHook):
    restype = c_int64
    argtypes = [POINTER(c_float)]
    auto_install = True

    def __init__(self, plugin, func_address: int):
        super().__init__(plugin, func_address)
        self._last_count_down = None
        self._last_count_down_time = -1

    @property
    def is_working(self):
        return perf_counter() - self._last_count_down_time < .5

    @property
    def last_count_down(self):
        return self._last_count_down if self.is_working else None

    def hook_function(self, a1):
        res = self.original(a1)
        self._last_count_down = a1[10]
        self._last_count_down_time = perf_counter()
        return res
