import base64
from ctypes import *
from importlib import import_module
from pathlib import Path
from traceback import format_exc

from FFxivPythonTrigger import PluginBase, AddressManager, plugins, game_version
from FFxivPythonTrigger.decorator import BindValue
from FFxivPythonTrigger.memory import read_memory, write_float, read_int, read_ubytes, write_ubytes, write_ubyte
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct, PointerStruct
from FFxivPythonTrigger.hook import PluginHook

from .sigs import sigs
from .struct import MinMax, ActionParam, ActionEffectEntry

action_hook_args_type = [c_int, c_int64, c_int64, POINTER(ActionParam), POINTER(ActionEffectEntry * 8), POINTER(c_ulonglong)]
DEFAULT_SALOCK_FIX1 = 0.35
DEFAULT_SALOCK_FIX2 = 0.5


def in_out_log(func):
    def wrapper(plugin, *args):
        res = func(plugin, *args)
        plugin.logger.debug(func.__name__, res, args)
        return res

    wrapper.__name__ = func.__name__
    return wrapper


class XivHacks(PluginBase):
    name = "XivHacks"
    layout = str(Path(__file__).parent / 'layout.js')

    def __init__(self):
        super().__init__()
        am = AddressManager(self.name, self.logger)
        self.version_data = self.storage.data.setdefault(game_version, {})
        self._address = am.load(sigs)

        self._zoom_cam = read_memory(PointerStruct(OffsetStruct({
            'zoom': (MinMax, read_int(self._address['zoom_zoom_offset']) + 4),
            'fov': (MinMax, read_int(self._address['zoom_fov_offset']) + 4),
            'angle': (MinMax, read_int(self._address['zoom_angle_offset'])),
        }), 0), self._address['zoom_cam_ptr'])
        if 'zoom_defaults' not in self.version_data:
            self.version_data['zoom_defaults'] = self.zoom_cam.get_data()
        if self.zoom_property is None:
            self.controller.bind_values['zoom_property'] = self.version_data['zoom_defaults']
        if 'zoom_cam_distance_reset_orig' not in self.version_data:
            self.version_data['zoom_cam_distance_reset_orig'] = base64.b64encode(
                read_ubytes(self._address["zoom_cam_distance_reset"], 8)).decode('ascii')
        self._zoom_cam_distance_reset_orig = base64.b64decode(self.version_data['zoom_cam_distance_reset_orig'].encode('ascii'))

        self.SwingReadHook(self, self._address["swing_read"])
        self.SwingSyncHook(self, self._address["swing_sync"])

        self.ActionHook(self, self._address["action_hook"])

        if 'ninja_stiff_orig' not in self.version_data:
            self.version_data['ninja_stiff_orig'] = base64.b64encode(
                read_ubytes(self._address["ninj_stiff"], 6)
            ).decode('ascii')
        self._ninja_stiff_orig = base64.b64decode(self.version_data['ninja_stiff_orig'].encode('ascii'))

        self.SpeedMainHook(self, self._address['speed_main'])
        self.SpeedFlyHook(self, self._address['speed_fly'])

        self.ActorHitBixHook(self, self._address['actor_hit_box_get'])

        self.storage.save()

    def onunload(self):
        self.zoom_set(self.version_data['zoom_defaults'])
        self.zoom_cam_distance_reset_set(False)
        self.zoom_cam_no_collision_set(False)
        self.ninja_stiff_set(False)

    # zoom

    @property
    def zoom_cam(self):
        return self._zoom_cam.value

    def zoom_set(self, data):
        for k in ['zoom', 'fov', 'angle']:
            if k in data:
                getattr(self.zoom_cam, k).set(data[k])

    def zoom_cam_distance_reset_set(self, mode):
        data = bytearray(b'\x90' * 8 if mode else self._zoom_cam_distance_reset_orig)
        write_ubytes(self._address["zoom_cam_distance_reset"], data)

    def zoom_cam_no_collision_set(self, mode):
        write_ubytes(self._address['zoom_cam_collision_jmp'], bytearray(b'\x90\xe9' if mode else b'\x0F\x84'))

    def apply_zoom(self):
        self.zoom_set(self.zoom_property)
        return True

    @BindValue.decorator(init_set=True,auto_save=True)
    def zoom_property(self, new_val, old_val):
        self.zoom_set(new_val)
        return True

    @BindValue.decorator(default=False, init_set=True,auto_save=True)
    def zoom_cam_distance_reset(self, new_val, old_val):
        self.zoom_cam_distance_reset_set(new_val)
        return True

    @BindValue.decorator(default=False, init_set=True,auto_save=True)
    def zoom_cam_no_collision(self, new_val, old_val):
        self.zoom_cam_no_collision_set(new_val)
        return True

    # swing reduce

    swing_reduce = BindValue(default=0.,auto_save=True)

    @PluginHook.decorator(c_int, [c_uint, c_int64, c_uint, c_int64], True)
    def SwingReadHook(self, hook, *args):
        return int(max(hook.original(*args) - self.swing_reduce * 1000, 0))

    @PluginHook.decorator(c_float, [c_float], True)
    def SwingSyncHook(self, hook, a1):
        return max(hook.original(a1) - self.swing_reduce, 0)

    # anti knock & skill animation lock

    anti_knock = BindValue(default=False,auto_save=True)

    @BindValue.decorator(default=.5, init_set=True,auto_save=True)
    def skill_animation_lock_time(self, new_val, old_val):
        address = self._address["skill_animation_lock_local"]
        write_float(address + 4, min(new_val, DEFAULT_SALOCK_FIX1))
        write_float(address + 14, min(new_val, DEFAULT_SALOCK_FIX2))
        return True

    @PluginHook.decorator(c_int64, action_hook_args_type, True)
    def ActionHook(self, hook, a1, a2, a3, action_param_ptr, effects, target_ids):
        data = action_param_ptr[0]
        if data.time > self.skill_animation_lock_time:
            data.time = self.skill_animation_lock_time
        if self.anti_knock:
            for i in range(data.target_cnt):
                if target_ids[i] != plugins.XivMemory.player_info.id: continue
                for j, e in enumerate(effects[i]):
                    if not e.type:
                        break
                    elif e.type == 0x20 or e.type == 0x21:
                        s = addressof(e)
                        d = read_ubytes(s + ActionEffectEntry.struct_size, (7 - j) * ActionEffectEntry.struct_size)
                        write_ubytes(s, d)
        return hook.original(a1, a2, a3, action_param_ptr, effects, target_ids)

    # ninja_stiff

    def ninja_stiff_set(self, mode):
        write_ubytes(self._address['ninj_stiff'], bytearray(b'\x90' * 6 if mode else self._ninja_stiff_orig))

    @BindValue.decorator(default=False, init_set=True,auto_save=True)
    def ninja_stiff(self, new_val, old_val):
        self.ninja_stiff_set(new_val)
        return True

    # speed
    speed_percent = BindValue(default=1,auto_save=True)

    @PluginHook.decorator(c_float, [c_int64, c_byte, c_int], True)
    def SpeedMainHook(self, hook, *args):
        return hook.original(*args) * self.speed_percent

    @PluginHook.decorator(c_float, [c_void_p], True)
    def SpeedFlyHook(self, hook, *args):
        return hook.original(*args) * self.speed_percent

    # hit box adjust
    hit_box_adjust = BindValue(default=0,auto_save=True)

    @PluginHook.decorator(c_float, [c_int64, c_ubyte], True)
    def ActorHitBixHook(self, hook, *args):
        return max(hook.original(*args) + self.hit_box_adjust, 0)

    # cutscene_skip
    def set_cutscene_skip(self, mode):
        write_ubyte(self._address['cutscene_skip'], 0x2e if mode else 4)

    @BindValue.decorator(default=False, init_set=True,auto_save=True)
    def cutscene_skip(self, new_val, old_val):
        self.set_cutscene_skip(new_val)
        return True
