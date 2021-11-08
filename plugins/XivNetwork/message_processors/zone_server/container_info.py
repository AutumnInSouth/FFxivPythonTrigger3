from ctypes import *

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from ..utils import NetworkZoneServerEvent, BaseProcessors


class ServerContainerInfo(OffsetStruct({
    'container_sequence': c_uint,
    'item_count': c_uint,
    'container_id': c_uint,
    'unk': c_uint,
}, 16)):
    container_sequence: int
    item_count: int
    container_id: int
    unk: int


class ServerContainerInfoEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'container_info'
    struct_message: ServerContainerInfo

    def __str__(self):
        return f"container:{self.struct_message.container_id} - item count:{self.struct_message.item_count}"


class ContainerInfo(BaseProcessors):
    opcode = "ContainerInfo"
    struct = ServerContainerInfo
    event = ServerContainerInfoEvent
