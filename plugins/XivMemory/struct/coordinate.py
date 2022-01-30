from FFxivPythonTrigger.memory import read_memory
from FFxivPythonTrigger.memory.struct_factory import PointerStruct
from FFxivPythonTrigger.popular_struct import Position

from ..sigs import main_coordinate_shifts


class Coordinate(object):
    def __init__(self, address):
        self._coordinate_main = read_memory(
            PointerStruct(Position, *main_coordinate_shifts),
            address["coordinate_main_pointer"]
        )
        self.coordinate_fly = read_memory(
            Position, address["coordinate_fly"]
        )

    def __str__(self):
        return str(self.coordinate_main)

    @property
    def coordinate_main(self):
        return self._coordinate_main.value

    @property
    def x(self):
        return self.coordinate_main.x

    @x.setter
    def x(self, value):
        self.coordinate_main.x = value
        self.coordinate_fly.x = value

    @property
    def y(self):
        return self.coordinate_main.y

    @y.setter
    def y(self, value):
        self.coordinate_main.y = value
        self.coordinate_fly.y = value

    @property
    def z(self):
        return self.coordinate_main.z

    @z.setter
    def z(self, value):
        self.coordinate_main.z = value
        self.coordinate_fly.z = value

    @property
    def r(self):
        return self.coordinate_main.r

    @r.setter
    def r(self, value):
        self.coordinate_main.r = value
        self.coordinate_fly.r = value

    def from_obj(self, other):
        self.x = other.x
        self.y = other.y
        self.z = other.z

    def set(self, x=None, y=None, z=None):
        if x is not None: self.x = x
        if y is not None: self.y = y
        if z is not None: self.z = z
