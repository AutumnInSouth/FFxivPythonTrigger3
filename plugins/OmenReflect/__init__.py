from ctypes import *
from functools import cache
from inspect import isclass
from pathlib import Path
from typing import TYPE_CHECKING

from FFxivPythonTrigger import PluginBase, plugins, AddressManager, game_ext
from FFxivPythonTrigger.decorator import event, BindValue
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.saint_coinach import action_sheet, territory_type_names, realm
from . import utils
from .reflect import reflect_data, delay_percent
from .extra_omens import ExtraOmens

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.actor_cast import ServerActorCastEvent

get_action_data_interface = CFUNCTYPE(POINTER(utils.action_struct), c_int64)
remove_omen_interface = CFUNCTYPE(c_void_p, c_void_p)
omen_sheet = realm.game_data.get_sheet('Omen')


@cache
def omen_name(omen_id: int):
    return omen_sheet[omen_id]['Path']


@cache
def action_data(action_id: int):
    action = action_sheet[action_id]
    return {
        'name': action['Name'],
        'cast_type': utils.cast_type_name.get(action['CastType']) or f"Unknown ({action['CastType']})",
        'effect_range': action['EffectRange'],
        'x_axis_modifier': action['XAxisModifier'],
        'omen': action['Omen']['Path'],
        'new_omen': omen_name(reflect_data.get(action.key, 0)),
    }


class OmenReflect(PluginBase):
    name = "OmenReflect"
    layout = str(Path(__file__).parent / "layout.js")

    def __init__(self):
        super().__init__()
        am = AddressManager(self.name, self.logger)
        self._get_action_data = get_action_data_interface(am.scan_point(
            'get_action_data', 'E8 * * * * 48 8B E8 48 85 C0 74 ? 45 84 E4'
        ))
        self.remove_omen = remove_omen_interface(am.scan_address(
            'remove_omen', '48 89 5C 24 ? 57 48 83 EC ? 48 8B D9 33 FF 48 8B 89 ? ? ? ? 48 85 C9 74 ? E8 ? ? ? ? 48 8B 8B ? ? ? ?'
        ))
        self.add_action_omen_hook(self, am.scan_point(
            'add_action_omen', 'E8 * * * * 41 80 7E ? ? 0F 85 ? ? ? ? F3 0F 10 1D ? ? ? ?'
        ))

        if game_ext == 3:
            self._add_omen = CFUNCTYPE(
                c_void_p,  # rtn: pointer of the new omen
                c_void_p,  # pointer of the source actor
                POINTER(c_ushort),  # [web_x, web_z, web_y]
                c_float,  # facing
                POINTER(utils.action_struct),  # pointer of the omen
                c_float,  # display_delay
            )(am.scan_address(
                'add_omen', 'F3 0F 11 54 24 ? 53 56'
            ))
        else:
            self._add_omen = CFUNCTYPE(
                c_void_p,  # rtn: pointer of the new omen
                c_void_p,  # pointer of the source actor
                POINTER(c_ushort),  # [web_x, web_z, web_y]
                c_float,  # facing
                POINTER(utils.action_struct),  # pointer of the omen
                c_float,  # display_delay
                c_uint  # unk
            )(am.scan_address(
                'add_omen', '48 89 5C 24 ? 48 89 6C 24 ? F3 0F 11 54 24 ?'
            ))

        self.log_record = set()

    def start(self):
        for row in action_sheet: self._get_action_data(row.key)[0].omen = reflect_data.get(row.key) or row['Omen'].key

    def onunload(self):
        for row in action_sheet: self._get_action_data(row.key)[0].omen = row['Omen'].key

    if game_ext == 3:
        def add_omen(self, source_actor_ptr, target_pos, facing, omen_id, cast_type, effect_range, x_axis_modifier: int = 0):
            if isclass(target_pos):
                pos = (c_ushort * 3)(utils.raw_to_web(target_pos.x), utils.raw_to_web(target_pos.z), utils.raw_to_web(target_pos.y))
            else:
                x, y, z = target_pos
                pos = (c_ushort * 3)(utils.raw_to_web(x), utils.raw_to_web(z), utils.raw_to_web(y))
            omen_data = utils.action_struct(omen=omen_id, cast_type=cast_type, effect_range=effect_range, x_axis_modifier=x_axis_modifier)
            return self._add_omen(source_actor_ptr, pos, facing, byref(omen_data), 0.)
    else:
        def add_omen(self, source_actor_ptr, target_pos, facing, omen_id, cast_type, effect_range, x_axis_modifier: int = 0):
            if isclass(target_pos):
                pos = (c_ushort * 3)(utils.raw_to_web(target_pos.x), utils.raw_to_web(target_pos.z), utils.raw_to_web(target_pos.y))
            else:
                x, y, z = target_pos
                pos = (c_ushort * 3)(utils.raw_to_web(x), utils.raw_to_web(z), utils.raw_to_web(y))
            omen_data = utils.action_struct(omen=omen_id, cast_type=cast_type, effect_range=effect_range, x_axis_modifier=x_axis_modifier)
            return self._add_omen(source_actor_ptr, pos, facing, byref(omen_data), 0., 0)

    @PluginHook.decorator(c_void_p, [c_void_p, c_uint, c_uint, c_void_p, c_float, c_float], True)
    def add_action_omen_hook(self, hook, source_actor_ptr, skill_type, action_id, pos_ptr, facing_float, display_delay):
        if display_delay:
            delay_p = delay_percent.get(action_id, 6)
            self.logger.debug(f'lower delay of {action_id} - {display_delay:.2f} by /{delay_p}')
            display_delay = display_delay / delay_p
        return hook.original(source_actor_ptr, skill_type, action_id, pos_ptr, facing_float, display_delay)

    enable_record = BindValue(default=False,auto_save=True)

    @event('network/zone/server/actor_cast')
    def on_cast(self, evt: 'ServerActorCastEvent'):
        if self.enable_record and evt.source_actor.type.value != 'player' and evt.struct_message.skill_type == 1:
            self.client_event('actor_cast', {
                'epoch': evt.bundle_header.epoch,
                'zone': territory_type_names.get(plugins.XivMemory.zone_id, 'unk'),
                'source': {'id': evt.source_id, 'name': evt.source_name},
                'target': {'id': evt.target_id, 'name': evt.target_name},
                'cast': {
                    'action': evt.action_id,
                    'duration': evt.cast_time,
                    'delay': evt.struct_message.display_delay,
                    'position': {
                        'x': utils.web_to_raw(evt.struct_message.x),
                        'y': utils.web_to_raw(evt.struct_message.y),
                        'z': utils.web_to_raw(evt.struct_message.z),
                        'r': evt.struct_message.rotation
                    },
                },
            })

    def layout_get_action_data(self, action_id):
        return action_data(action_id)
