from time import sleep
from FFxivPythonTrigger import plugins


def dis(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5


# m = ['one', 'two', 'three', 'four', 'a', 'b', 'c', 'd']
m = ['three', 'c']

i = -1
last_pos = None
while True:
    t_id = plugins.XivMemory.markings.head_mark.circle.actor_id
    t_a = plugins.XivMemory.actor_table.get_actor_by_id(t_id)
    if t_a and (last_pos is None or dis(last_pos[0], last_pos[1], last_pos[2], t_a.pos.x, t_a.pos.y, t_a.pos.z) > 5):
        i += 1
        plugins.XivMemory.calls.way_mark(m[i % len(m)], t_a.pos)
        last_pos = (t_a.pos.x, t_a.pos.y, t_a.pos.z)
    sleep(0.1)
