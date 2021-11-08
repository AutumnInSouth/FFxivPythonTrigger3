from inspect import isclass
from typing import List, Dict, Type, Set

from . import chat_client, chat_server, lobby_client, lobby_server, zone_client, zone_server
from .opcodes import key_to_code, code_to_key, scope_name
from .utils import BaseProcessors, _NetworkEvent

len_processors: List[Dict[int, Set[Type[BaseProcessors]]]] = []
_opcode_processors: List[Dict[str, Type[BaseProcessors]]] = []

for module in chat_client, chat_server, lobby_client, lobby_server, zone_client, zone_server:
    len_dict = {}
    opcode_dict = {}
    for key in dir(module):
        attr = getattr(module, key)
        if isclass(attr) and issubclass(attr, BaseProcessors):
            len_dict.setdefault(attr.struct.struct_size, set()).add(attr)
            opcode_dict[attr.opcode] = attr
    len_processors.append(len_dict)
    _opcode_processors.append(opcode_dict)

opcode_processors: List[Dict[int, Type[BaseProcessors]]] = [{
    key_to_code[i][key]: processor
    for key, processor in key_processors.items()
    if key in key_to_code[i]
} for i, key_processors in enumerate(_opcode_processors)]

for scope, data in enumerate(key_to_code):
    for key, code in data.items():
        if code not in opcode_processors[scope]:
            _scope_name = scope_name[scope // 2]
            is_send = not bool(scope % 2)


            class UndefinedProcessor(BaseProcessors):
                class event(_NetworkEvent):
                    id = f"{_NetworkEvent.id}undefined/{_scope_name}/{'client' if is_send else 'server'}/{key}"
                    scope = _scope_name
                    is_server = is_send

                opcode = key


            opcode_processors[scope][code] = UndefinedProcessor
