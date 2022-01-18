from time import sleep
from FFxivPythonTrigger import plugins
from random import choice

keys = ['attack2', 'bind2', 'stop2', ]

t_a = plugins.XivMemory.targets.current
t_id = t_a.id
while t_a and t_a.id == t_id:
    need_set = {}
    is_set = False
    for key in keys:
        _t_id = getattr(plugins.XivMemory.markings.head_mark, key).actor_id
        if _t_id == t_id:
            is_set = True
        elif _t_id != 0xe0000000:
            need_set[key] = 0xe0000000
    if not is_set:
        need_set[choice(keys)] = t_id
    for key, value in need_set.items():
        plugins.XivMemory.calls.head_mark(key, value)
    plugins.XivMemory.calls.way_mark('b', t_a.pos)
    sleep(0.05)
