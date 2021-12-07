from ctypes import *
from FFxivPythonTrigger import *


def add():
    me = plugins.XivMemory.actor_table.me
    print(hex(addressof(me.effects)))
    t_effect = me.effects[-1]
    t_effect.buff_id = 1422
    t_effect.actor_id = me.id

def clear():
    me = plugins.XivMemory.actor_table.me
    t_effect = me.effects[-1]
    t_effect.buff_id = 0
    t_effect.actor_id = 0xe0000000

clear()
