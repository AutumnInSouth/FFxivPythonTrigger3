from pathlib import Path
import pandas as pd

idx = {
    "5.55": "2021.09.17.0000.0000",
    "5.57": "2021.10.26.0000.0000",
}
outputs = {
    'ServerZoneIpc': 'zone_server.opcodes',
    'ClientZoneIpc': 'zone_client.opcodes',
    'ServerChatIpc': 'chat_server.opcodes',
    'ClientChatIpc': 'chat_client.opcodes',
    'ServerLobbyIpc': 'lobby_server.opcodes',
    'ClientLobbyIpc': 'lobby_client.opcodes',
}
data = pd.read_csv('cn_opcodes.csv').fillna('')
for version, version_key in idx.items():
    path = Path(f"opcode_{version_key}")
    path.mkdir(exist_ok=True)
    c_data = dict()
    for i, row in data.iterrows():
        if not row[version]: continue
        c_data.setdefault(row['Scope'].strip(), dict())[(row['ACT'] or row['Name']).strip()] = eval(row[version]), row['Length']
    for scope, file_name in outputs.items():
        s_data = c_data.get(scope)
        if s_data:
            with open(path / file_name, "w+") as f:
                for key, r_data in sorted(s_data.items()):
                    opcode, length = r_data
                    length = length if length else -1
                    f.write(f"{key}|{opcode:X}\n")
            print(f"export {version_key} / {file_name}")
