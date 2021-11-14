from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.popular_struct import Vector3
from .actor import Actor

head_marking_names = ['attack1', 'attack2', 'attack3', 'attack4', 'attack5',
                      'bind1', 'bind2', 'bind3', 'stop1', 'stop2', 'square',
                      'circle', 'cross', 'triangle']
way_mark_names = ['a', 'b', 'c', 'd', 'one', 'two', 'three', 'four']


class WayMarkStruct(OffsetStruct({
    '_pos': (Vector3, 0x0),
    '_x': (c_int, 0x10),
    '_z': (c_int, 0x14),
    '_y': (c_int, 0x18),
    'is_active': (c_bool, 0x1c),
}, 0x20)):
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
        if isinstance(other, tuple):
            x, y, z = other
            self.x = x
            self.y = y
            self.z = z
        else:
            self.x = other.x
            self.y = other.y
            self.z = other.z

    def add(self, other):
        if isinstance(other, tuple):
            x, y, z = other
            self.x += x
            self.y += y
            self.z += z
        else:
            self.x += other.x
            self.y += other.y
            self.z += other.z


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


class HeadMarkStruct(OffsetStruct({
    '_actor_id': c_uint
}, 8)):
    @property
    def actor_id(self):
        return self._actor_id

    @actor_id.setter
    def actor_id(self, value):
        if not value:
            self._actor_id = 0xe0000000
        else:
            if isinstance(value, Actor):
                self._actor_id = value.id
            elif isinstance(value, int):
                self._actor_id = value
            else:
                raise ValueError(f"unsupported value type: {type(value)}")


class LocalHeadMarks(OffsetStruct({
    'attack1': HeadMarkStruct,
    'attack2': HeadMarkStruct,
    'attack3': HeadMarkStruct,
    'attack4': HeadMarkStruct,
    'attack5': HeadMarkStruct,
    'bind1': HeadMarkStruct,
    'bind2': HeadMarkStruct,
    'bind3': HeadMarkStruct,
    'stop1': HeadMarkStruct,
    'stop2': HeadMarkStruct,
    'square': HeadMarkStruct,
    'circle': HeadMarkStruct,
    'cross': HeadMarkStruct,
    'triangle': HeadMarkStruct,
})):
    attack1: HeadMarkStruct
    attack2: HeadMarkStruct
    attack3: HeadMarkStruct
    attack4: HeadMarkStruct
    attack5: HeadMarkStruct
    bind1: HeadMarkStruct
    bind2: HeadMarkStruct
    bind3: HeadMarkStruct
    stop1: HeadMarkStruct
    stop2: HeadMarkStruct
    square: HeadMarkStruct
    circle: HeadMarkStruct
    cross: HeadMarkStruct
    triangle: HeadMarkStruct


class Markings(OffsetStruct({
    'head_mark': (LocalHeadMarks, 0x10),
    'way_mark': (LocalWayMarks, 0x1b0),
})):
    head_mark: LocalHeadMarks
    way_mark: LocalWayMarks
