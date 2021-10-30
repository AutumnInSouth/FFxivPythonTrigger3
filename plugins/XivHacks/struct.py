from ctypes import *

from FFxivPythonTrigger.memory import write_float
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct


class MinMax(OffsetStruct({'min': c_float, 'max': c_float})):
    def set_min(self, num: float):
        write_float(addressof(self), float(num))

    def set_max(self, num: float):
        write_float(addressof(self) + 4, float(num))

    def set(self, data: dict):
        self.set_min(data['min'])
        self.set_max(data['max'])


class ActionParam(OffsetStruct({
    'action_id': (c_ushort, 28),
    'action_id_2': (c_uint, 8),
    'time': (c_float, 16),
    'target_cnt': (c_ubyte, 33),
})):
    action_id: int
    action_id_2: int
    time: float
    target_cnt: int


class ActionEffectEntry(OffsetStruct({
    'type': c_ubyte,
    'param1': c_ubyte,
    'param2': c_ubyte,
    'param3': c_ubyte,
    'param4': c_ubyte,
    'param5': c_ubyte,
    'main_param': c_ushort,
})):
    type: int
    param1: int
    param2: int
    param3: int
    param4: int
    param5: int
    main_param: int
