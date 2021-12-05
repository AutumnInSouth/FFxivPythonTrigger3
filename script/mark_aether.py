from FFxivPythonTrigger import *

plugins.XivMemory.calls.do_action(1,26988)
cnt = 0
for actor in plugins.XivMemory.actor_table:
    if actor.name == 'Aether Current' and actor.type == 'event_obj' and actor.can_select:
        plugins.XivMemory.calls.way_mark(cnt, actor.pos)
        cnt += 1
print(f"{cnt} found")
