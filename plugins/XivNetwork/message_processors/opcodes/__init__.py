from pathlib import Path
from typing import Dict, List
from csv import DictReader

from FFxivPythonTrigger import game_version
from FFxivPythonTrigger.storage import get_module_storage

scope_name = ["chat", "lobby", "zone"]
csv_names = [
    'ChatClientIpc',
    'ChatServerIpc',
    'LobbyClientIpc',
    'LobbyServerIpc',
    'ZoneClientIpc',
    'ZoneServerIpc',
]


def load_opcodes(path) -> List[Dict[str, int]]:
    data = []
    for i in range(6):
        add = {}
        _path = path / f"{csv_names[i]}.csv"
        if _path.exists():
            with open(_path, 'r', encoding='utf-8') as f:
                for row in DictReader(f):
                    if not row['key'].startswith('_') and row.get(game_version):
                        add[row['key']] = eval(row.get(game_version))
        data.append(add)
    return data


user_path = get_module_storage("XivNetworkOpcodes").path
user_path.mkdir(exist_ok=True)
source_data = load_opcodes(Path(__file__).parent)
user_data = load_opcodes(user_path / game_version)
# key_to_code = [{} for i in range(6)]
key_to_code = [source_data[i] | user_data[i] for i in range(6)]
code_to_key = [{v: k for k, v in opcodes.items()} for opcodes in key_to_code]
