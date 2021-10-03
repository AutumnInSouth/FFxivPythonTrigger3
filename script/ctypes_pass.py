from ctypes import *


def _a(num):
    print(num)


a = CFUNCTYPE(c_void_p, c_int64)(_a)


def _b(obj):
    a(obj)


CFUNCTYPE(c_void_p, c_void_p)(_b)(byref(c_uint(1)))
