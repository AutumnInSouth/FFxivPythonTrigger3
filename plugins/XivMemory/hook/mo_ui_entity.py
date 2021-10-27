from ctypes import *
from . import ValueBindHook
from ..struct.actor import Actor


class MoUiEntityHook(ValueBindHook):
    argtypes = [c_int64, POINTER(Actor)]

    def get_value(self, a1, actor):
        return actor[0] if actor else None
