import pysaintcoinach
from pathlib import Path

game_path_chs = r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game'
game_path_eng = r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game'

rp = Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3')
realm_chs = pysaintcoinach.ARealmReversed(game_path_chs, pysaintcoinach.Language.chinese_simplified, rp / 'DefinitionsExt3')  # 国服
realm_eng = pysaintcoinach.ARealmReversed(game_path_eng, pysaintcoinach.Language.english, rp / 'DefinitionsExt4')  # 国际服

sheets = []
for sheet in realm_chs._game_data.definition.sheet_definitions:
    _sheet = realm_chs.game_data.get_sheet(sheet.name)
    first_key = next(iter(_sheet)).key
    if first_key < 0x10000 or first_key & 0xffff:
        continue
    sheets.append((sheet.name, first_key))

sheets.sort(key=lambda x: x[1])
for sheet_name, start_key in sheets:
    print(sheet_name, hex(start_key))
