from functools import cache
from pathlib import Path

import pysaintcoinach
import generate_data

realm = pysaintcoinach.ARealmReversed(
    r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game',
    pysaintcoinach.Language.english,
    Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3\DefinitionsExt4')
)
action_sheet = realm.game_data.get_sheet('Action')
action_sheet_chs = pysaintcoinach.ARealmReversed(
    r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game',
    pysaintcoinach.Language.chinese_simplified,
    Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3\DefinitionsExt3')
).game_data.get_sheet('Action')

action_time_line_black_list = {row.key for row in realm.game_data.get_sheet('ActionTimeline') if '[SKL_ID]' in row['Key']}


def name(action_id):
    name = action_sheet[action_id]['Name']
    if not name: return '? '
    try:
        chs_name = action_sheet_chs[action_id]['Name']
    except:
        return name + ' '
    if chs_name == name: return name + ' '
    return f'{name} / {chs_name} '


@cache
def end_type_omen_map():
    _map = {}
    for action in action_sheet:
        omen = getattr(action['Omen'], 'key', 0)
        if not omen: continue
        omen = generate_data.white_list.get(action.key, omen)
        key = getattr(action['Animation{End}'], 'key', 0), action['CastType']
        if key[0] == 0 or key[0] in action_time_line_black_list or key[1] < 2: continue
        _map.setdefault(key, set()).add(omen)
    return {k: generate_data.get_translate(min(v)) for k, v in _map.items()}


@cache
def name_end_type_omen_map():
    _map = {}
    for action in action_sheet:
        omen = getattr(action['Omen'], 'key', 0)
        if not omen: continue
        omen = generate_data.white_list.get(action.key, omen)
        key = action['Name'], getattr(action['Animation{End}'], 'key', 0), action['CastType']
        if key[1] == 0 or key[2] < 2: continue
        _map.setdefault(key, set()).add(omen)
    return {k: min(v) for k, v in _map.items()}


def find_omen(action_id):
    if not action_id % 1000: print(action_id)
    if action_id in generate_data.white_list:
        return generate_data.white_list[action_id]
    action = action_sheet[action_id]
    if action['Omen'].key or action['CastType'] < 2 or not action['Cast<100ms>']: return
    cast_type = action['CastType']
    ani_end = getattr(action['Animation{End}'], 'key', 0)
    return (name_end_type_omen_map().get((action['Name'], ani_end, cast_type)) or
            end_type_omen_map().get((ani_end, cast_type)) or
            generate_data.cast_type_omen_default.get(cast_type))


d = {a1: a2 for a1, a2 in {action.key: find_omen(action.key) for action in action_sheet}.items() if a2}
with open('reflect.py', 'w', encoding='utf-8') as f:
    f.write("reflect_data = {\n")
    for k, v in d.items():
        f.write(f"    {k}: {v},  # {name(k)}\n")
    f.write("}\n")
