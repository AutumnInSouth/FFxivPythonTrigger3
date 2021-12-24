from FFxivPythonTrigger.memory.struct_factory import *


class Vector3U16(OffsetStruct({
    'x': c_uint16,
    'z': c_uint16,
    'y': c_uint16
})):
    x: int
    y: int
    z: int
