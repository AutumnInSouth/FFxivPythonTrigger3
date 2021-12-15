from ctypes import byref

from FFxivPythonTrigger import plugins


def add_omen(source_actor, target_pos, facing, omen_id, cast_type, effect_range, x_axis_modifier: int = 0):
    return plugins.OmenReflect.add_omen(byref(source_actor), target_pos, facing, omen_id, cast_type, effect_range, x_axis_modifier)

def remove_omen(source_actor):
    return plugins.OmenReflect.remove_omen(byref(source_actor))
