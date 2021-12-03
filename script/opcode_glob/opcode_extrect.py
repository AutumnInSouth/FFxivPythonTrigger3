from pathlib import Path

import requests

url = r"https://raw.githubusercontent.com/karashiiro/FFXIVOpcodes/master/opcodes.json"
idx = {
    "5.58": "2021.11.28.0000.0000",
}
outputs = {
    'ServerZoneIpc': 'zone_server.opcodes',
    'ClientZoneIpc': 'zone_client.opcodes',
    'ServerChatIpc': 'chat_server.opcodes',
    'ClientChatIpc': 'chat_client.opcodes',
    'ServerLobbyIpc': 'lobby_server.opcodes',
    'ClientLobbyIpc': 'lobby_client.opcodes',
}
for data in requests.get(url).json():
    if data['version'] in idx and data['region'] == 'Global':
        version, version_key = data['version'], idx[data['version']]
        path = Path(f"opcode_{version_key}")
        path.mkdir(exist_ok=True)
        c_data = dict()
        for ot, data2 in data['lists'].items():
            _data = c_data.setdefault(ot.strip().strip('Type'), dict())
            for data3 in data2:_data[data3['name']] = data3['opcode']
        print(c_data)
        for scope, file_name in outputs.items():
            s_data = c_data.get(scope)
            if s_data:
                with open(path / file_name, "w+") as f:
                    for key, opcode in sorted(s_data.items()):
                        f.write(f"{key}|{opcode:X}\n")
                print(f"export {version_key} / {file_name}")
