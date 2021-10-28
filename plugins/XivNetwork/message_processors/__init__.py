from typing import List, Dict, TYPE_CHECKING, Type

from .chat_client import len_processors as chat_client_len_processors, opcode_processors as _chat_client_opcode_processors
from .chat_server import len_processors as chat_server_len_processors, opcode_processors as _chat_server_opcode_processors
from .lobby_client import len_processors as lobby_client_len_processors, opcode_processors as _lobby_client_opcode_processors
from .lobby_server import len_processors as lobby_server_len_processors, opcode_processors as _lobby_server_opcode_processors
from .opcodes import key_to_code, code_to_key
from .zone_client import len_processors as zone_client_len_processors, opcode_processors as _zone_client_opcode_processors
from .zone_server import len_processors as zone_server_len_processors, opcode_processors as _zone_server_opcode_processors

if TYPE_CHECKING:
    from .utils import BaseProcessors

len_processors = [
    chat_client_len_processors,
    chat_server_len_processors,
    lobby_client_len_processors,
    lobby_server_len_processors,
    zone_client_len_processors,
    zone_server_len_processors
]

_opcode_processors = [
    _chat_client_opcode_processors,
    _chat_server_opcode_processors,
    _lobby_client_opcode_processors,
    _lobby_server_opcode_processors,
    _zone_client_opcode_processors,
    _zone_server_opcode_processors
]

opcode_processors: List[Dict[int, Type['BaseProcessors']]] = [{
    key_to_code[i][key]: processor
    for key, processor in key_processors.items()
    if key in key_to_code[i]
} for i, key_processors in enumerate(_opcode_processors)]
