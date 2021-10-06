from pathlib import Path

from FFxivPythonTrigger import game_version
from FFxivPythonTrigger.storage import get_module_storage

socket_type_name = ["lobby", "zone", "chat"]


def load_opcodes():
    user_path = get_module_storage("XivNetworkOpcodes").path
    user_path.mkdir(exist_ok=True)
    source_data = _load_opcodes(Path(__file__).parent / f'opcode_{game_version}')
    user_data = _load_opcodes(user_path / game_version)
    key_to_code = [source_data[i] | user_data[i] for i in range(6)]
    code_to_key = [{v: k for k, v in opcodes.items()} for opcodes in key_to_code]
    return key_to_code, code_to_key


def _load_opcodes(path):
    data = []
    for i in range(6):
        add = {}
        _path = path / f"{socket_type_name[i // 2]}_{'server' if i % 2 else 'client'}.opcodes"
        if _path.exists():
            with open(_path) as f:
                for line in f.readlines():
                    try:
                        name, code = line.strip().split('|')
                    except ValueError:
                        pass
                    else:
                        add[name] = int(code, 16)
        data.append(add)
    return data
