from ctypes import *

from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerUpdateHpMpTp(OffsetStruct({
    'current_hp': c_uint,
    'current_mp': c_ushort,
    'current_tp': c_ushort,
})):
    current_hp: int
    current_mp: int
    current_tp: int


class ServerUpdateHpMpTpEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'actor_update_hp_mp_tp'
    struct_message: ServerUpdateHpMpTp

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.target_id = message_header.actor_id
        self.target_name = hex(self.target_id)
        self.target_actor = None

    def init(self):
        self.target_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.target_id)
        if self.target_actor is not None: self.target_name = self.target_actor.name

    def _text(self):
        return f"{self.target_name} - {self.struct_message.current_hp},{self.struct_message.current_mp}"

    def _str_event(self):
        return f"network_actor_update_hp_mp_tp|{self.target_name}|{self.struct_message.current_hp}|{self.struct_message.current_mp}|{self.struct_message.current_tp}"


class ActorUpdateHpMpTp(BaseProcessors):
    opcode = "UpdateHpMpTp"
    struct = ServerUpdateHpMpTp
    event = ServerUpdateHpMpTpEvent
