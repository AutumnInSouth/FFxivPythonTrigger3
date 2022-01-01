from ctypes import *
from functools import cache

from FFxivPythonTrigger import *
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import BASE_ADDR
from FFxivPythonTrigger.saint_coinach import action_sheet
from FFxivPythonTrigger.address_manager import AddressManager
from FFxivPythonTrigger.text_pattern import find_signature_point, find_signature_address


@cache
def is_area_action(action_id: int):
    return action_sheet[action_id]['TargetArea']


sigs = {
    "action_type_check": {
        'call': find_signature_address,
        'param': "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 48 8B 2D ? ? ? ? 49 8B D8",
        'add': BASE_ADDR,
    },
    "action_data_sig": {
        'call': find_signature_point,
        'param': "E8 * * * * 48 8B F0 48 85 C0 0F 84 ? ? ? ? BA ? ? ? ? 48 8B CB E8 ? ? ? ? 48 8B 0D ? ? ? ?",
        'add': BASE_ADDR,
    },
    "do_action": {
        'call': find_signature_point,
        'param': "E8 * * * * 89 9F ? ? ? ? EB ? C7 87 ? ? ? ? ? ? ? ?",
        'add': BASE_ADDR,
    },
}


class MoAction(PluginBase):
    name = "MoAction"

    def __init__(self):
        super().__init__()
        address = AddressManager(self.name, self.logger, ).load(sigs)
        self.on_do_action(self, address['do_action'])
        self.get_action_data = CFUNCTYPE(c_void_p, c_int64)(address['action_data_sig'])
        self.action_type_check = CFUNCTYPE(c_bool, c_int64, c_void_p, c_void_p)(address['action_type_check'])

    def check_action_target(self, action_id, target_entity):
        return self.action_type_check(action_id, self.get_action_data(action_id), byref(target_entity))

    @PluginHook.decorator(c_int64, [c_int64, c_uint, c_uint, c_int64, c_uint, c_uint, c_int, c_void_p],True)
    def on_do_action(self, hook, action_manager_address, action_type, action_id, target_id, unk1, unk2, unk3, unk4):
        self.logger.debug(f"type: {action_type} id: {action_id} target: {target_id}")

        if action_type == 1:
            if is_area_action(action_id):
                l = plugins.XivMemory.utils.mo_location
                if l is not None:
                    plugins.XivMemory.calls.do_action_location(1, action_id, *l, target_id)
                    return 1
            else:
                target = plugins.XivMemory.utils.mo_entity
                if target is not None and self.check_action_target(action_id, target):
                    return hook.original(action_manager_address, action_type, action_id, target.id, unk1, unk2, unk3, unk4)
        return hook.original(action_manager_address, action_type, action_id, target_id, unk1, unk2, unk3, unk4)
