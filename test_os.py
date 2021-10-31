from ctypes import *
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct, EnumStruct

print(
    OffsetStruct({
        'a_id': c_uint,
        'type': EnumStruct(c_ubyte, {
            1: 'a',
            2: 'b',
            3: 'c'
        }),
        'pos': OffsetStruct({
            'x': c_float,
            'y': c_float,
            'z': c_float,
        })
    }).from_dict({
        'a_id': 1,
        'type':'c',
        'pos': {
            'x': 1.1,
            'y': 2.2,
            'z': 3.3,
        }
    }).get_data()
)
