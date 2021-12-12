from FFxivPythonTrigger import *
from ctypes import *

behemoth_names = {'Behemoth'}
pythons_name = {'Python'}
quetzalcoatl_name = {'Quetzalcoatl'}
cnt = 0
for actor in plugins.XivMemory.actor_table:
    if actor.type != 'battle_npc': continue
    name = actor.name
    cnt += 1
    if name in behemoth_names:
        print('behemoth', hex(addressof(actor)))
    elif name in pythons_name:
        print('python', hex(addressof(actor)))
    elif name in quetzalcoatl_name:
        print('quetzalcoatl', hex(addressof(actor)))
    else:
        cnt -= 1
print('total', cnt)
