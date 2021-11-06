import re
import traceback
from ctypes import *

from FFxivPythonTrigger import plugins, PluginBase, Counter
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import read_memory, BASE_ADDR, read_string, read_ulonglong

target_re = re.compile(r'^<t\.(id:(?P<id>[0-9a-fA-F]+);)?(name:(?P<name>[^;]+);)?>'.encode('utf8'))
item_re = re.compile(r'^<item\.(?P<id>[0-9a-fA-F]+)>'.encode('utf8'))


def search_target(t_id=None, t_name=None):
    if t_id:
        target = plugins.XivMemory.actor_table.get_actor_by_id(int(t_id, 16))
        if target: return addressof(target)
    if t_name:
        target = list(plugins.XivMemory.actor_table.get_actors_by_name(t_name.decode('utf8', 'ignore')))
        if target: return addressof(target[0])
    return 0


class SomeMacro(PluginBase):
    name = "SomeMacro"

    def __init__(self):
        super().__init__()
        self.counter = Counter()
        self.counter.current = 0x900000
        self.returns = {}
        self.macro_parse_hook(self, BASE_ADDR + 0x6319B0)
        self.actor_fallback_hook(self, BASE_ADDR + 0x631D50)

    def store(self, val):
        vid = self.counter.get()
        self.returns[vid] = val
        return vid

    @PluginHook.decorator(c_int64, [c_int64, POINTER(c_int64)], True)
    def macro_parse_hook(self, hook, a1, a2):
        try:
            cmd = read_memory(c_char * 50, a2[0]).value
            t_re = target_re.match(cmd)
            if t_re:
                a2[0] += t_re.end()
                return self.store(search_target(t_re.group('id'), t_re.group('name')))
        except:
            self.logger.error(traceback.format_exc())
        return hook.original(a1, a2)

    @PluginHook.decorator(c_int64, [c_int64, c_uint], True)
    def actor_fallback_hook(self, hook, a1, a2):
        try:
            if a2 > 10000:
                return self.returns[a2]
        except:
            self.logger.error(traceback.format_exc())
        return hook.original(a1, a2)
