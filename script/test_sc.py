from ctypes import *

from FFxivPythonTrigger import plugins


def add_omen(source_actor, target_pos, facing, omen_id, cast_type, effect_range, x_axis_modifier: int = 0):
    return plugins.OmenReflect.add_omen(byref(source_actor), target_pos, facing, omen_id, cast_type, effect_range, x_axis_modifier)


me = plugins.XivMemory.actor_table.me
pos = me.pos
add_omen(me, (pos.x, pos.y, pos.z), pos.r, 188, 11, 40, 10)
