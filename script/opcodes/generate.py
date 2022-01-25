from pathlib import Path
from csv import DictWriter,DictReader

outputs = {
    'ZoneServerIpc': 'zone_server.opcodes',
    'ZoneClientIpc': 'zone_client.opcodes',
    'ChatServerIpc': 'chat_server.opcodes',
    'ChatClientIpc': 'chat_client.opcodes',
    'LobbyServerIpc': 'lobby_server.opcodes',
    'LobbyClientIpc': 'lobby_client.opcodes',
}

versions = {
    '2021.09.17.0000.0000': 'cn_5.55',
    '2021.10.26.0000.0000': 'cn_5.57',
    '2021.11.28.0000.0000': 'in_6.00',
    '2021.12.16.0000.0000': 'in_6.01',
    '2021.12.24.0000.0000': 'in_6.05',
    '2022.01.06.0000.0000': 'cn_5.58',
    '2022.01.25.0000.0000': 'in_6.08',
}

p = Path()

data = {}

for ipc_key, file_name in outputs.items():
    path=p / f'{ipc_key}.csv'
    if path.exists():
        ipc_data = data.setdefault(ipc_key, {})
        with open(path, 'r') as f:
            reader = DictReader(f)
            for row in reader:
                if not row['key'].startswith('_'):
                    for pg_ver,val in row.items():
                        if pg_ver != 'key':
                            ipc_data.setdefault(row['key'], {})[pg_ver] = val

headers = ['key']
game_versions = {'key': '_game_ver'}

for pg_ver, game_ver in versions.items():
    headers.append(pg_ver)
    game_versions[pg_ver] = game_ver
    ver_dir = p / ('opcode_' + pg_ver)
    if not ver_dir.exists() or not ver_dir.is_dir(): continue
    for ipc_key, file_name in outputs.items():
        file_path = ver_dir / file_name
        if not file_path.exists() or not file_path.is_file(): continue
        ipc_data = data.setdefault(ipc_key, {})
        with open(file_path, 'r') as f:
            for line in f.readlines():
                if line.startswith("#"): continue
                try:
                    name, code = line.strip().split('|')
                except ValueError:
                    pass
                else:
                    ipc_data.setdefault(name, {})[pg_ver] = f"0x{int(code, 16):04X}"

for ipc_key, file_name in outputs.items():
    if ipc_key not in data: continue
    with open(p / f'{ipc_key}.csv', 'w+') as f:
        writer = DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerow(game_versions)
        for name, codes in sorted(data[ipc_key].items(),key=lambda x: x[0]):
            writer.writerow({'key': name, **codes})

