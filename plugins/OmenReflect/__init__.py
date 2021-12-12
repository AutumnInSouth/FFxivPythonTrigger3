from ctypes import *
from inspect import isclass
from typing import TYPE_CHECKING

from FFxivPythonTrigger import PluginBase, plugins, AddressManager, PluginNotFoundException, game_ext
from FFxivPythonTrigger.decorator import event
from FFxivPythonTrigger.saint_coinach import action_sheet, action_names, territory_type_names
from . import utils
from .reflect import reflect_data
from .extra_omens import ExtraOmens

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.actor_cast import ServerActorCastEvent


get_action_data_interface = CFUNCTYPE(POINTER(utils.action_struct), c_int64)

if game_ext == 4:
    add_omen_interface = CFUNCTYPE(
        c_void_p,  # rtn: pointer of the new omen
        c_void_p,  # pointer of the source actor
        POINTER(c_ushort),  # [web_x, web_z, web_y]
        c_float,  # facing
        POINTER(utils.action_struct),  # pointer of the omen
        c_float,  # unk
        c_uint  # unk
    )
else:
    add_omen_interface = CFUNCTYPE(
        c_void_p,  # rtn: pointer of the new omen
        c_void_p,  # pointer of the source actor
        POINTER(c_ushort),  # [web_x, web_z, web_y]
        c_float,  # facing
        POINTER(utils.action_struct),  # pointer of the omen
        c_float,  # unk
    )


class OmenReflect(PluginBase):
    name = "OmenReflect"

    def __init__(self):
        super().__init__()
        am = AddressManager(self.name, self.logger)
        self._get_action_data = get_action_data_interface(am.scan_point(
            'get_action_data', 'E8 * * * * 48 8B E8 48 85 C0 74 ? 45 84 E4'
        ))

        if game_ext == 4:
            self._add_omen_addr = am.scan_address('add_omen', '48 89 5C 24 ? 48 89 6C 24 ? F3 0F 11 54 24 ?')
        else:
            self._add_omen_addr = am.scan_address('add_omen_ext3', 'F3 0F 11 54 24 ? 53 56')

        self._add_omen_orig = add_omen_interface(self._add_omen_addr)
        self.log_record = set()
        self.register_makeup()

    def start(self):
        for row in action_sheet:
            self._get_action_data(row.key)[0].omen = reflect_data.get(row.key) or row['Omen'].key

    def onunload(self):
        for row in action_sheet:
            self._get_action_data(row.key)[0].omen = row['Omen'].key

    def _add_omen(self, actor_ptr, pos_ptr, facing, omen_ptr):
        if game_ext == 3:
            return self._add_omen_orig(actor_ptr, pos_ptr, facing, omen_ptr, 0.)
        else:
            return self._add_omen_orig(actor_ptr, pos_ptr, facing, omen_ptr, 0., 0)

    def add_omen(self, source_actor_ptr, target_pos, facing, omen_id, cast_type, effect_range, x_axis_modifier: int = 0):
        if isclass(target_pos):
            pos = (c_ushort * 3)(utils.raw_to_web(target_pos.x), utils.raw_to_web(target_pos.z), utils.raw_to_web(target_pos.y))
        else:
            x, y, z = target_pos
            pos = (c_ushort * 3)(utils.raw_to_web(x), utils.raw_to_web(z), utils.raw_to_web(y))

        omen_data = utils.action_struct(omen=omen_id, cast_type=cast_type, effect_range=effect_range, x_axis_modifier=x_axis_modifier)

        return self._add_omen(source_actor_ptr, pos, facing, byref(omen_data))

    @event("plugin_load:XivNetwork")
    def register_makeup(self, _=None):
        try:
            plugins.XivNetwork.register_packet_fixer(self, 'zone', True, 'ActorCast', self.make_up)
        except PluginNotFoundException:
            self.logger.warning("XivNetwork is not found")

    def make_up(self, bundle_header, message_header, raw_message, struct_message):
        #self.logger(message_header,struct_message)
        struct_message.display_delay = int(struct_message.display_delay / 6)
        return struct_message

    @event('network/zone/server/actor_cast')
    def on_cast(self, evt: 'ServerActorCastEvent'):
        if evt.source_actor.type.value != 'player':
            zone_id = plugins.XivMemory.zone_id
            msg = evt.struct_message
            key = (zone_id, evt.source_actor.name, evt.action_id, msg.display_action_id)
            if key not in self.log_record:
                self.log_record.add(key)
                try:
                    action = action_sheet[evt.action_id]
                except KeyError:
                    return
                self.logger.debug(
                    f"{territory_type_names.get(zone_id, 'unk')}|{evt.source_actor.name}|"
                    # f"{msg.display_action_id}|{action_names.get(msg.display_action_id, 'unk')}|"
                    f"{evt.action_id}|{action['Name']}|{evt.cast_time:.2f}s|{evt.struct_message.display_delay}|"
                    f"{action['Omen'].key}({action['CastType']}/{action['EffectRange']}/{action['XAxisModifier']})=>{reflect_data.get(evt.action_id)}|",
                    # '\n', msg
                )
