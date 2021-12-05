from ctypes import *

from FFxivPythonTrigger import frame_inject
from FFxivPythonTrigger.popular_struct import Vector3


do_action_interface = CFUNCTYPE(c_int64, c_int64, c_uint, c_uint, c_int64, c_uint, c_uint, c_int, c_void_p)
do_action_location_interface = CFUNCTYPE(c_ubyte, c_int64, c_uint, c_uint, c_int64, POINTER(Vector3), c_uint)


class DoAction(object):
    def __init__(self, func_address: int, action_manager_address: int):
        self._original = do_action_interface(func_address)
        self.action_manager_address = action_manager_address

    def original(self, action_type: int, action_id: int, target_id=0xE0000000, unk1=0, unk2=0, unk3=0) -> int:
        return self._original(self.action_manager_address, action_type, action_id, target_id, unk1, unk2, unk3, 0)

    def __call__(self, action_type: int, action_id: int, target_id=0xE0000000, unk1=0, unk2=0, unk3=0):
        frame_inject.register_once_call(self.original, action_type, action_id, target_id, unk1, unk2, unk3)

    def use_action(self, action_id: int, target_id=0xE0000000):
        self(1, action_id, target_id)

    def use_item(self, item_id, target_id=0xE0000000, block_id=65535):
        self(2, item_id, target_id, block_id)

    def ride_mount(self, mount_id):
        self(13, mount_id)

    def call_minion(self, minion_id):
        self(8, minion_id)

    def fashion_item(self, item_id):
        self(20, item_id)

    def common_action(self, action_id, target_id=0xE0000000):
        self(5, action_id, target_id)

    def craft_action(self, action_id):
        self(9, action_id)


class DoActionLocation(object):
    def __init__(self, func_address: int, action_manager_address: int):
        self._original = do_action_location_interface(func_address)
        self.action_manager_address = action_manager_address

    def original(self, action_type, action_id, x: float, y: float, z: float, target_id=0xE0000000):
        return self._original(self.action_manager_address,
                              action_type, action_id, target_id,
                              byref(Vector3(x=x, y=y, z=z)), 0)

    def __call__(self, action_type, action_id, x: float, y: float, z: float, target_id=0xE0000000):
        frame_inject.register_once_call(self.original, action_type, action_id, x, y, z, target_id)
