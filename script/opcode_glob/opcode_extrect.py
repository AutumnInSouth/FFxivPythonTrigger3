from pathlib import Path

import requests

url = r"https://raw.githubusercontent.com/karashiiro/FFXIVOpcodes/master/opcodes.json"
idx = {
    "6.05": "2022.01.25.0000.0000",
}
outputs = {
    'ServerZoneIpc': 'zone_server.opcodes',
    'ClientZoneIpc': 'zone_client.opcodes',
    'ServerChatIpc': 'chat_server.opcodes',
    'ClientChatIpc': 'chat_client.opcodes',
    'ServerLobbyIpc': 'lobby_server.opcodes',
    'ClientLobbyIpc': 'lobby_client.opcodes',
}
translate = {

    "ActionEffect32": "AoeEffect32",
    "ActionEffect24": "AoeEffect24",
    "ActionEffect16": "AoeEffect16",
    "ActionEffect8": "AoeEffect8",
    "ActionEffect": "Effect",
}
for data in requests.get(url).json():
    if data['version'] in idx and data['region'] == 'Global':
        version, version_key = data['version'], idx[data['version']]
        path = Path(f"opcode_{version_key}")
        path.mkdir(exist_ok=True)
        c_data = dict()
        for ot, data2 in data['lists'].items():
            _data = c_data.setdefault(ot.strip().strip('Type'), dict())
            for data3 in data2: _data[data3['name']] = data3['opcode']
        print(c_data)
        for scope, file_name in outputs.items():
            s_data = c_data.get(scope)
            if s_data:
                with open(path / file_name, "w+") as f:
                    for key, opcode in sorted(s_data.items()):
                        f.write(f"{translate.get(key, key)}|{opcode:X}\n")
                print(f"export {version_key} / {file_name}")
