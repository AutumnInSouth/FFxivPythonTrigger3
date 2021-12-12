from ctypes import *
import time
from FFxivPythonTrigger import plugins

s = []
for actor in plugins.XivMemory.actor_table:
    if actor.type == 'player' or actor.can_select: continue
    pos=actor.pos
    try:
        plugins.OmenReflect.add_omen(byref(actor), (pos.x, pos.y, pos.z), pos.r, 1, 2, 3)
    except:
        pass
    else:
        print(actor)
        s.append(actor)
time.sleep(3)

for actor in s:
    plugins.OmenReflect.remove_omen(byref(actor))
