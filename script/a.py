import pysaintcoinach
from pathlib import Path

game_path_chs = r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game'
rp = Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3\DefinitionsExt3')
realm_chs = pysaintcoinach.ARealmReversed(game_path_chs, pysaintcoinach.Language.chinese_simplified, rp)

for row in realm_chs.game_data.get_sheet('Action'):
    if row['ClassJobCategory']['BLM'] and row['IsPvP']:
        print(f"'{row}': {row.key},")
