import base64
from ctypes import *
from pathlib import Path
from typing import TYPE_CHECKING

import math

from FFxivPythonTrigger import PluginBase, plugins, AddressManager, PluginNotFoundException, game_version
from FFxivPythonTrigger.decorator import BindValue, event
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import read_memory, write_float, read_int, read_ubytes, write_ubytes, write_ubyte
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct, PointerStruct
from . import afix
from .sigs import sigs
from .struct import MinMax, ActionParam, ActionEffectEntry

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_client.update_position_handler import ClientUpdatePositionHandlerEvent
    from XivNetwork.message_processors.zone_client.update_position_instance import ClientUpdatePositionInstanceEvent
    from XivNetwork.message_processors.zone_client.action_send import ClientActionSend
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent

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


hack_zoom = True
hack_swing_reduce = True
hack_ninja_stiff = True
hack_speed = True
hack_afix = True
hack_move_swing = True
hack_knock_ani_lock = True
hack_hit_box = True


class XivHacks(PluginBase):
    name = "XivHacks"
    layout = str(Path(__file__).parent / 'layout.js')

    def __init__(self):
        super().__init__()
        am = AddressManager(self.name, self.logger)
        self.version_data = self.storage.data.setdefault(game_version, {})
        self._address = am.load(sigs)

        # zoom
        if hack_zoom:
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

        # swing reduce
        if hack_swing_reduce:
            self.SwingReadHook(self, self._address["swing_read"])
            self.SwingSyncHook(self, self._address["swing_sync"])

        if hack_knock_ani_lock:
            self.ActionHook(self, self._address["action_hook"])  # anti knock & skill animation lock

        # ninja_stiff
        if hack_ninja_stiff:
            if 'ninja_stiff_orig' not in self.version_data:
                self.version_data['ninja_stiff_orig'] = base64.b64encode(
                    read_ubytes(self._address["ninj_stiff"], 6)
                ).decode('ascii')
            self._ninja_stiff_orig = base64.b64decode(self.version_data['ninja_stiff_orig'].encode('ascii'))

        # speed
        if hack_speed:
            self.SpeedMainHook(self, self._address['speed_main'])
            self.SpeedFlyHook(self, self._address['speed_fly'])

        if hack_hit_box:
            self.ActorHitBixHook(self, self._address['actor_hit_box_get'])  # hit box adjust

        # afix
        if hack_afix:
            self.afix_adjust_mode = True
            self.afix_adjust_sig = 0
            self.afix_set_sig = 0x93
            self.afix_work = False
            self.register_afix()

        # moving swing
        if hack_move_swing:
            self.register_moving_swing()

        self.storage.save()

    def onunload(self):
        self.zoom_set(self.version_data['zoom_defaults'])
        self.zoom_cam_distance_reset_set(False)
        self.zoom_cam_no_collision_set(False)
        self.ninja_stiff_set(False)

    # zoom
    if hack_zoom:
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

        @BindValue.decorator(init_set=True, auto_save=True)
        def zoom_property(self, new_val, old_val):
            self.zoom_set(new_val)
            return True

        @BindValue.decorator(default=False, init_set=True, auto_save=True)
        def zoom_cam_distance_reset(self, new_val, old_val):
            self.zoom_cam_distance_reset_set(new_val)
            return True

        @BindValue.decorator(default=False, init_set=True, auto_save=True)
        def zoom_cam_no_collision(self, new_val, old_val):
            self.zoom_cam_no_collision_set(new_val)
            return True

    # swing reduce
    if hack_swing_reduce:
        swing_reduce = BindValue(default=0., auto_save=True)

        @PluginHook.decorator(c_int, [c_uint, c_int64, c_uint, c_int64], True)
        def SwingReadHook(self, hook, *args):
            return int(max(hook.original(*args) - self.swing_reduce * 1000, 0))

        @PluginHook.decorator(c_float, [c_float], True)
        def SwingSyncHook(self, hook, a1):
            return max(hook.original(a1) - self.swing_reduce, 0)

    # anti knock & skill animation lock
    if hack_knock_ani_lock:
        anti_knock = BindValue(default=False, auto_save=True)

        def set_local_ani_lock(self, new_val=None):
            address = self._address["skill_animation_lock_local"]
            if new_val is None:
                write_float(address + 4, DEFAULT_SALOCK_FIX1)
                write_float(address + 14, DEFAULT_SALOCK_FIX2)
            else:
                write_float(address + 4, min(new_val, DEFAULT_SALOCK_FIX1))
                write_float(address + 14, min(new_val, DEFAULT_SALOCK_FIX2))

        @BindValue.decorator(default=True, auto_save=True)
        def skill_animation_lock_local(self, new_val, old_val):
            self.set_local_ani_lock(self.skill_animation_lock_time if new_val else None)
            return True

        @BindValue.decorator(default=.5, init_set=True, auto_save=True)
        def skill_animation_lock_time(self, new_val, old_val):
            if self.skill_animation_lock_local: self.set_local_ani_lock(new_val)
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
    if hack_ninja_stiff:
        def ninja_stiff_set(self, mode):
            write_ubytes(self._address['ninj_stiff'], bytearray(b'\x90' * 6 if mode else self._ninja_stiff_orig))

        @BindValue.decorator(default=False, init_set=True, auto_save=True)
        def ninja_stiff(self, new_val, old_val):
            self.ninja_stiff_set(new_val)
            return True

    # speed
    if hack_speed:
        speed_percent = BindValue(default=1, auto_save=True)

        @PluginHook.decorator(c_float, [c_int64, c_byte, c_int], True)
        def SpeedMainHook(self, hook, *args):
            return hook.original(*args) * self.speed_percent

        @PluginHook.decorator(c_float, [c_void_p], True)
        def SpeedFlyHook(self, hook, *args):
            return hook.original(*args) * self.speed_percent

    # hit box adjust
    if hack_hit_box:
        hit_box_adjust = BindValue(default=0, auto_save=True)

        @PluginHook.decorator(c_float, [c_int64, c_ubyte], True)
        def ActorHitBixHook(self, hook, *args):
            return max(hook.original(*args) + self.hit_box_adjust, 0)

    # cutscene_skip
    if 1:
        def set_cutscene_skip(self, mode):
            write_ubyte(self._address['cutscene_skip'], 0x2e if mode else 4)

        @BindValue.decorator(default=False, init_set=True, auto_save=True)
        def cutscene_skip(self, new_val, old_val):
            self.set_cutscene_skip(new_val)
            return True

    # afix
    if hack_afix:
        afix_enable = BindValue(default=False, auto_save=True)
        afix_distance = BindValue(default=5, auto_save=True)

        @event('network/zone/client/update_position_instance')
        def deal_adjust(self, evt: 'ClientUpdatePositionInstanceEvent'):
            self.afix_adjust_mode = True
            self.afix_adjust_sig = evt.struct_message.unk1 & 0xf

        @event('network/zone/client/update_position_handler')
        def deal_set(self, evt: 'ClientUpdatePositionHandlerEvent'):
            self.afix_adjust_mode = False
            if not (evt.struct_message.unk0 or evt.struct_message.unk1) and 0x10000 > evt.struct_message.unk2 > 0:
                self.afix_set_sig = evt.struct_message.unk2

        def goto(self, new_x=None, new_y=None, new_r=None, stop=False):
            c = plugins.XivMemory.coordinate
            if new_r is None: new_r = c.r
            target = {
                'x': new_x if new_x is not None else c.x,
                'y': new_y if new_y is not None else c.y,
                'z': c.z
            }
            if self.afix_adjust_mode:
                msg = {
                    'old_r': c.r,
                    'new_r': new_r,
                    'old_pos': target,
                    'new_pos': target,
                    'unk0': (0x4000 if stop else 0),
                    'unk1': (0x40 if stop else 0) | self.afix_adjust_sig
                }
                code = "UpdatePositionInstance"
            else:
                msg = {'r': new_r, 'pos': target, 'unk2': self.afix_set_sig if stop else 0}
                code = "UpdatePositionHandler"
            self.logger.debug(f'goto x:{target["x"]:.2f} y:{target["y"]:.2f} z:{target["z"]:.2f} r:{new_r:.2f}')
            plugins.XivNetwork.send_messages('zone', (code, msg))

        @event('network/zone/server/action_effect')
        def coor_return(self, evt: 'ActionEffectEvent'):
            if not self.afix_work or evt.source_id != plugins.XivMemory.player_info.id or evt.action_type != 'action':
                return
            self.goto(stop=True)

        @event("plugin_load:XivNetwork")
        def register_afix(self, _=None):
            try:
                plugins.XivNetwork.register_packet_fixer(self, 'zone', False, 'ActionSend', self.makeup_action_send)
            except PluginNotFoundException:
                self.logger.warning("XivNetwork is not found")

        def makeup_action_send(self, bundle_header, message_header, raw_message, struct_message: 'ClientActionSend'):
            me = plugins.XivMemory.actor_table.me
            me_effects = me.effects.get_dict()
            msg = struct_message
            if self.afix_enable and msg.action_id in afix.afix_skills and 1250 not in me_effects and 1179 not in me_effects:
                t = plugins.XivMemory.actor_table.get_actor_by_id(msg.target_id)
                if t is not None and t.is_positional:
                    if isinstance(afix.afix_skills[msg.action_id], int):
                        pos, statement = afix.afix_skills[msg.action_id], lambda x: True
                    else:
                        pos, statement = afix.afix_skills[msg.action_id]
                    if statement(msg.action_id):
                        c = plugins.XivMemory.coordinate
                        xy = afix.get_nearest(c, t, pos)
                        if xy is not None:
                            dis = afix.distance(xy, (c.x, c.y))
                            if dis >= self.afix_distance:
                                self.logger.debug(f"too far to fix: {dis}")
                            else:
                                new_r = c.r
                                new_r = new_r + (-math.pi if new_r > 0 else math.pi)
                                self.afix_work = True
                                self.goto(*xy, new_r)
            return struct_message

    # moving swing
    if hack_move_swing:
        moving_swing_enable = BindValue(default=False, auto_save=True)
        moving_swing_time = BindValue(default=1.5, auto_save=True)

        @event("plugin_load:XivNetwork")
        def register_moving_swing(self, _=None):
            try:
                plugins.XivNetwork.register_packet_fixer(self, 'zone', False, 'UpdatePositionInstance', self.makeup_moving)
                plugins.XivNetwork.register_packet_fixer(self, 'zone', False, 'UpdatePositionHandler', self.makeup_moving)
            except PluginNotFoundException:
                self.logger.warning("XivNetwork is not found")

        def makeup_moving(self, bundle_header, message_header, raw_message, struct_message):
            if self.moving_swing_enable:
                me = plugins.XivMemory.actor_table.me
                if me and self.moving_swing_time > me.casting_time - me.casting_progress > 0.3:  # TODO: flag check
                    return None
            return raw_message
