from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct


class Position(OffsetStruct({
    'x': c_float,
    'z': c_float,
    'y': c_float,
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
