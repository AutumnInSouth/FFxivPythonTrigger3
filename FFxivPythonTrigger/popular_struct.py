from ctypes import *
from typing import TypeVar, Type

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct


class Position(OffsetStruct({
    'x': c_float,
    'z': c_float,
    'y': c_float,
    'unk': c_float,
    'r': c_float
})):
    x: float
    y: float
    z: float
    r: float


class Vector3(OffsetStruct({
    'x': c_float,
    'z': c_float,
    'y': c_float,
})):
    x: float
    y: float
    z: float


T = TypeVar('T')


def StdVector(_T: Type[T]):
    t_size = sizeof(_T)

    class StdVectorClass(OffsetStruct({
        'first': c_void_p,
        'last': c_void_p,
        'end': c_void_p,
    })):

        def __len__(self):
            if not self.first or not self.last: return 0
            return (self.last - self.first) // t_size

        def __getitem__(self, index) -> T:
            if index > len(self): raise IndexError(f"Index out of range, max: {len(self)} got: {index}")
            return cast(self.first, POINTER(_T))[index]

    return StdVectorClass
