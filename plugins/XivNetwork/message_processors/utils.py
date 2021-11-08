from typing import TYPE_CHECKING, Type
from threading import Lock

from FFxivPythonTrigger import EventBase
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct

if TYPE_CHECKING:
    from ..base_struct import BundleHeader, MessageHeader


class Controller(object):
    def __init__(self, event: '_NetworkEvent'):
        self.event = event
        self.inited = False
        self.init_lock = Lock()

    def init(self):
        if not self.inited:
            with self.init_lock:
                if not self.inited:
                    self.event.init()
                    self.inited = True


class _NetworkEvent(EventBase):
    is_server: bool
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
        self.controller = Controller(self)

    def init(self):
        pass

    def _text(self):
        return self.id

    def text(self):
        self.controller.init()
        return self._text()

    def _str_event(self):
        pass

    def str_event(self):
        self.controller.init()
        return self._str_event()


class _NetworkZoneEvent(_NetworkEvent):
    scope = "zone"
    id = _NetworkEvent.id + "zone/"


class NetworkZoneClientEvent(_NetworkZoneEvent):
    is_server = False
    id = _NetworkZoneEvent.id + "client/"


class NetworkZoneServerEvent(_NetworkZoneEvent):
    is_server = True
    id = _NetworkZoneEvent.id + "server/"


class _NetworkChatEvent(_NetworkEvent):
    scope = "chat"
    id = _NetworkEvent.id + "chat/"


class NetworkChatClientEvent(_NetworkChatEvent):
    is_server = False
    id = _NetworkChatEvent.id + "client/"


class NetworkChatServerEvent(_NetworkChatEvent):
    is_server = True
    id = _NetworkChatEvent.id + "server/"


class _NetworkLobbyEvent(_NetworkEvent):
    scope = "lobby"
    id = _NetworkEvent.id + "lobby/"


class NetworkLobbyClientEvent(_NetworkLobbyEvent):
    is_server = False
    id = _NetworkLobbyEvent.id + "client/"


class NetworkLobbyServerEvent(_NetworkLobbyEvent):
    is_server = True
    id = _NetworkLobbyEvent.id + "server/"


class BaseProcessors(object):
    opcode: str
    struct = OffsetStruct({}, 0)
    event: Type[_NetworkEvent]
