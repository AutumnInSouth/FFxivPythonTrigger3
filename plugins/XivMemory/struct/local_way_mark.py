from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.popular_struct import Vector3, Position


class WayMarkStruct(OffsetStruct({
    '_pos': (Vector3, 0x0),
    '_x': (c_int, 0x10),
    '_z': (c_int, 0x14),
    '_y': (c_int, 0x18),
    'is_active': (c_bool, 0x1c),
})):
    is_active: bool

    @property
    def x(self):
        return self._pos.x

    @x.setter
    def x(self, value: float):
        self._pos.x = value
        self._x = int(value * 1000)

    @property
    def y(self):
        return self._pos.y

    @y.setter
    def y(self, value: float):
        self._pos.y = value
        self._y = int(value * 1000)

    @property
    def z(self):
        return self._pos.z

    @z.setter
    def z(self, value: float):
        self._pos.z = value
        self._z = int(value * 1000)

    def set(self, other):
        if isinstance(other, (Vector3, Position)):
            self.x = other.x
            self.y = other.y
            self.z = other.z
        elif isinstance(other, tuple):
            x, y, z = other
            self.x = x
            self.y = y
            self.z = z
        else:
            raise ValueError("Only allow Vector3, Position or tuple of float")

    def add(self, other):
        if isinstance(other, (Vector3, Position)):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        elif isinstance(other, tuple):
            x, y, z = other
            self.x += x
            self.y += y
            self.z += z
        else:
            raise ValueError("Only allow Vector3, Position or tuple of float")


class LocalWayMarks(OffsetStruct({
    'a': (WayMarkStruct, 0x0),
    'b': (WayMarkStruct, 0x20),
    'c': (WayMarkStruct, 0x40),
    'd': (WayMarkStruct, 0x60),
    'one': (WayMarkStruct, 0x80),
    'two': (WayMarkStruct, 0xA0),
    'three': (WayMarkStruct, 0xC0),
    'four': (WayMarkStruct, 0xE0),
})):
    a: WayMarkStruct
    b: WayMarkStruct
    c: WayMarkStruct
    d: WayMarkStruct
    one: WayMarkStruct
    two: WayMarkStruct
    three: WayMarkStruct
    four: WayMarkStruct
