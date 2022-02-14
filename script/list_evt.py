import pysaintcoinach
from pathlib import Path

game_path_chs = r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game'
game_path_eng = r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game'

rp = Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3')
realm_chs = pysaintcoinach.ARealmReversed(game_path_chs, pysaintcoinach.Language.chinese_simplified, rp / 'DefinitionsExt3')  # 国服
realm_eng = pysaintcoinach.ARealmReversed(game_path_eng, pysaintcoinach.Language.english, rp / 'DefinitionsExt4')  # 国际服

da = []


def process_e_npc(e_npc):
    for i in range(32):
        d = e_npc[f"ENpcData[{i}]"]
        if d:  da.append((d.key, str(d), d.sheet.name))


def process_eobj(eobj):
    d = eobj['Data']
    if d:
        da.append((d.key, str(d), d.sheet.name))


def main(zone_id):
    for row in realm_eng.game_data.get_sheet('Level'):
        if getattr(row['Territory'], 'key', 0) != zone_id: continue
        match getattr(getattr(row['Object'], 'sheet', None), 'name', None):
            case 'EObj':
                process_eobj(row['Object'])
            case 'ENpcBase':
                process_e_npc(row['Object'])
            case None:
                pass
            case unk:
                print(f"unknown object sheet: {unk}")
    da.sort(key=lambda x: x[0])
    for k, v, s in da:
        print(f"{k:#X} {s} {v}")


main(611)
