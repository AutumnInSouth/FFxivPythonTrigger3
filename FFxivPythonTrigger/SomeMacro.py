import re
from ctypes import *
from re import compile

from FFxivPythonTrigger import plugins, PluginBase
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import read_string, read_memory

target_re = re.compile(r'^<t\.(id:(?P<id>[0-9a-fA-F]+);)?(name:(?P<name>[^;]+);)?>'.encode('utf8'))


def search_target(t_id=None, t_name=None):
    if t_id:
        target = plugins.XivMemory.actor_table.get_actor_by_id(int(t_id,16))
        if target: return addressof(target)
    if t_name:
        target = list(plugins.XivMemory.actor_table.get_actors_by_name(t_name.decode('utf8', 'ignore')))
        if target: return addressof(target[0])


class SomeMacro(PluginBase):
    name = "SomeMacro"

    @PluginHook.decorator(c_int64, [c_int64, POINTER(c_void_p)], True)
    def macro_parse_hook(self, hook, a1, a2):
        cmd = read_memory(c_char * 100, a2[0].value).value
        t_re = target_re.match(cmd)
        if t_re:
            target = search_target(t_re.group('id'), t_re.group('name'))
            if target:
                a2[0].value += t_re.end()
                return target
        return hook.original(a1, a2)
