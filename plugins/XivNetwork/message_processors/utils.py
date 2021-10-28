from typing import TYPE_CHECKING, Type

from FFxivPythonTrigger import EventBase
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct

if TYPE_CHECKING:
    from ..base_struct import BundleHeader, MessageHeader


class _NetworkEvent(EventBase):
    is_send: bool
    scope: str
    id = "network/"

    def __init__(self,
                 bundle_header: 'BundleHeader',
                 message_header: 'MessageHeader',
                 raw_message: bytearray,
                 struct_message=None):
        self.bundle_header = bundle_header
        self.message_header = message_header
        self.raw_message = raw_message
        self.struct_message = struct_message


class _NetworkZoneEvent(_NetworkEvent):
    scope = "zone"
    id = _NetworkEvent.id + "zone/"


class NetworkZoneClientEvent(_NetworkZoneEvent):
    is_send = True
    id = _NetworkZoneEvent.id + "client/"


class NetworkZoneServerEvent(_NetworkZoneEvent):
    is_send = False
    id = _NetworkZoneEvent.id + "server/"


class _NetworkChatEvent(_NetworkEvent):
    scope = "chat"
    id = _NetworkEvent.id + "chat/"


class NetworkChatClientEvent(_NetworkChatEvent):
    is_send = True
    id = _NetworkChatEvent.id + "client/"


class NetworkChatServerEvent(_NetworkChatEvent):
    is_send = False
    id = _NetworkChatEvent.id + "server/"


class _NetworkLobbyEvent(_NetworkEvent):
    scope = "lobby"
    id = _NetworkEvent.id + "lobby/"


class NetworkLobbyClientEvent(_NetworkLobbyEvent):
    is_send = True
    id = _NetworkLobbyEvent.id + "client/"


class NetworkLobbyServerEvent(_NetworkLobbyEvent):
    is_send = False
    id = _NetworkLobbyEvent.id + "server/"


class BaseProcessors(object):
    opcode: str
    struct = OffsetStruct({}, 0)
    Event: Type[_NetworkEvent]
