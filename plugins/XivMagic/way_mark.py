from ctypes import *
from typing import Union

from FFxivPythonTrigger.popular_struct import Vector3, Position

way_mark_interface = CFUNCTYPE(c_ubyte, c_int64, c_uint, c_void_p)
way_mark_clear_interface = CFUNCTYPE(c_ubyte, c_int64, c_uint)
way_mark_clear_all_interface = CFUNCTYPE(c_ubyte, c_int64)

way_mark_names = ['a', 'b', 'c', 'd', 'one', 'two', 'three', 'four']

way_marks = {way_mark_names[i]: i for i in range(len(way_mark_names))}


class WayMark(object):
    def __init__(self, way_mark_address: int, way_mark_clear_address: int, way_mark_clear_all_address: int,
                 marking_controller_address: int, action_manager_address: int):
        self._set = way_mark_interface(way_mark_address)
        self._clear = way_mark_clear_interface(way_mark_clear_address)
        self._clear_all = way_mark_clear_all_interface(way_mark_clear_all_address)
        self.marking_controller_address = marking_controller_address
        self.action_manager_address = action_manager_address

    def set(self, mark_type: Union[str, int], pos: Union[Vector3, Position, tuple[float, float, float]]):
        if isinstance(pos, tuple):
            pos = Vector3(x=pos[0], y=pos[1], z=pos[2])
        mark_id = mark_type if isinstance(mark_type, int) else way_marks[mark_type]
        return self._set(self.marking_controller_address, mark_id, byref(pos))

    def __call__(self, mark_type: Union[str, int], pos: Union[Vector3, Position, tuple[float, float, float]]):
        return self.set(mark_type, pos)

    def clear(self, mark_type: Union[str, int]):
        mark_id = mark_type if isinstance(mark_type, int) else way_marks[mark_type]
        return self._clear(self.action_manager_address, mark_id)

    def clear_all(self):
        return self._clear_all(self.marking_controller_address)
