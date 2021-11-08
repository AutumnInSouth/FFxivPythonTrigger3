from ctypes import *

from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneClientEvent, BaseProcessors


class ClientActionSend(OffsetStruct({
    'action_type': (c_uint, 0x0),
    'action_id': (c_uint, 0x4),
    'cnt': (c_ushort, 0x8),
    'unk1': (c_ushort, 0xa),
    'unk2': (c_ushort, 0xc),
    'unk3': (c_ushort, 0xe),
    'target_id': (c_uint, 0x10),
}, 32)):
    action_type: int
    action_id: int
    cnt: int
    unk1: int
    unk2: int
    unk3: int
    target_id: int


class ClientActionSendEvent(NetworkZoneClientEvent):
    id = NetworkZoneClientEvent.id + 'action_send'
    struct_message: ClientActionSend
    target_actor: any

    def __init__(self, bundle_header, message_header, raw_message, struct_message):
        super().__init__(bundle_header, message_header, raw_message, struct_message)
        self.target_name = hex(self.struct_message.target_id)

    def init(self):
        self.target_actor = plugins.XivMemory.actor_table.get_actor_by_id(self.struct_message.target_id)
        if self.target_actor is not None: self.target_name = self.target_actor.name

    def _text(self):
        return f"using {self.struct_message.action_type}-{self.struct_message.action_id} on {self.target_name}({self.struct_message.target_id:x})"


class ActionSend(BaseProcessors):
    opcode = "ActionSend"
    struct = ClientActionSend
    event = ClientActionSendEvent
