import pysaintcoinach
import re
from pathlib import Path

game_path_chs = r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game'  # 自行替换
game_path_eng = r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game'  # 自行替换
line_break = re.compile(r'[\r\n\u3000]+')
ui_foreground = re.compile(r"</?UIForeground(\(\d+\))?>")
ui_glow = re.compile(r"</?UIGlow(\(\d+\))?>")
if_job = re.compile(r"<If\(Equal\(PlayerParameter\(68\),(?P<job_id>\d+)\)\)>(?P<true_statement>[^<]*)<Else/>(?P<false_statement>[^<]*)</If>")
if_lv = re.compile(r"<If\(GreaterThanOrEqualTo\(PlayerParameter\(72\),(?P<min_lv>\d+)\)\)>"
                   r"(?P<true_statement>[^<]*)<Else/>(?P<false_statement>[^<]*)</If>")

rp = Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3')
realm_chs = pysaintcoinach.ARealmReversed(game_path_chs, pysaintcoinach.Language.chinese_simplified, rp / 'DefinitionsExt3')  # 国服
realm_eng = pysaintcoinach.ARealmReversed(game_path_eng, pysaintcoinach.Language.english, rp / 'DefinitionsExt4')  # 国际服
data_realm = realm_eng
translate_realm = realm_eng
action_sheet = data_realm.game_data.get_sheet('Action')
eng_action_sheet = realm_eng.game_data.get_sheet('Action')
status_sheet = data_realm.game_data.get_sheet('Status')
status_sheet_eng = realm_eng.game_data.get_sheet('Status')
action_sheet_chs = realm_chs.game_data.get_sheet('Action')
action_transient_sheet = data_realm.game_data.get_sheet('ActionTransient')
action_transient_translate_sheet = translate_realm.game_data.get_sheet('ActionTransient')
eng_cj_sheet = realm_eng.game_data.get_sheet('ClassJob')
fight_abbrev = [class_job['Abbreviation']
                for class_job in data_realm.game_data.get_sheet('ClassJob')
                if class_job['Abbreviation'] and class_job['ClassJobCategory'].key in {30, 31}]
fight_category = []
common_category = []
for class_job_category in data_realm.game_data.get_sheet('ClassJobCategory'):
    if sum(class_job_category[class_job] for class_job in fight_abbrev) ==0:continue
    (fight_category if sum(class_job_category[class_job] for class_job in fight_abbrev) < 3 else common_category).append(class_job_category.key)

status_by_name = {}
for status in realm_chs.game_data.get_sheet('Status'):
    status_by_name.setdefault(status['Name'], []).append(status)
for status in realm_eng.game_data.get_sheet('Status'):
    status_by_name.setdefault(status['Name'].lower(), []).append(status)


def to_under_line(s):
    return re.sub(r'([A-Z]|[_ -][a-z])', lambda m: '_' + m.group(0)[-1].lower(), s).replace(' ', '')


def to_hump(s):
    return re.sub(r'[_ -]([a-zA-Z])', lambda m: m.group(1).upper(), s.capitalize()).replace(' ', '').replace("'", '').replace(':', '')


def desc_process(desc: str):
    rtn = ui_glow.sub('', ui_foreground.sub('', line_break.sub('\n', desc)))
    while if_job.search(rtn) or if_lv.search(rtn):
        rtn = if_job.sub(r"(source.job==\1?\2:\3)", rtn)
        rtn = if_lv.sub(r"(source.level>=\1?\2:\3)", rtn)
    return rtn


w_mode = True
# for class_job in data_realm.game_data.get_sheet('ClassJob'):
#      if class_job.key and class_job['Abbreviation'] and class_job['ClassJobCategory'].key in {30, 31} and not class_job['StartingTown'].key:
#     #if class_job['Abbreviation']=="AST":
#         if class_job['Abbreviation'] in {'PLD','DRK','BRD'}:continue
#         print(class_job['Name'])
#         with open('tmp', 'w+') if not w_mode else open(f'{to_under_line(eng_cj_sheet[class_job.key]["Name"])}.py', 'w+', encoding='utf-8') as f:
#             (f.write if w_mode else print)("""from ..base import *
#
#
# class Actions:
# """)
#             to_print_action = [action for action in action_sheet if (
#                     action['Name'] and not action['IsPvP'] and action['ClassJobCategory'] and
#                     action['ClassJobCategory'][class_job['Abbreviation']] and
#                     action['ClassJobCategory'].key in fight_category and
#                     action_transient_sheet[action.key]['Description']
#             )]
#             to_print_action.sort(key=lambda action: action['ClassJobLevel'])
#             for action in to_print_action:
#                 names = {eng_action_sheet[action.key]['Name']}
#                 try:
#                     if action_sheet_chs[action.key]['Name']:
#                         names.add(action_sheet_chs[action.key]['Name'])
#                 except:
#                     pass
#                 (f.write if w_mode else print)(f"""
#     class {to_hump(eng_action_sheet[action.key]['Name'])}(ActionBase):
#         \"""
# {desc_process(action_transient_translate_sheet[action.key]['Description'])}""")
#                 status = set()
#                 for name in names: status|=set(s.key for s in status_by_name.get(action['Name'].lower(), []))
#                 for status in status:
#                     status = status_sheet_eng[status]
#                     (f.write if w_mode else print)(
#                         f"\n>> {status.key}, {status['Name']}, {desc_process(status['Description'])}")
#                 (f.write if w_mode else print)(f"""
#         \"""
#         id = {action.key}
#         name = {names}
# """)
#                 if action['Action{Combo}'].key:
#                     (f.write if w_mode else print)(f"        combo_action = {action['Action{Combo}'].key}\n")

with open('tmp', 'w+') if not w_mode else open(f'common.py', 'w+', encoding='utf-8') as f:
    (f.write if w_mode else print)("""from ..base import *


class Status:
    pass


class Actions:
""")
    to_print_action = [action for action in action_sheet if (
            action['Name'] and not action['IsPvP'] and action['ClassJobCategory'] and
            action['ClassJobCategory'].key in common_category and
            action_transient_sheet[action.key]['Description']
    )]
    to_print_action.sort(key=lambda action: action['ClassJobLevel'])
    for action in to_print_action:
        names = {eng_action_sheet[action.key]['Name']}
        try:
            if action_sheet_chs[action.key]['Name']:
                names.add(action_sheet_chs[action.key]['Name'])
        except:
            pass
        (f.write if w_mode else print)(f"""
    class {to_hump(eng_action_sheet[action.key]['Name'])}(ActionBase):
        \"""
{desc_process(action_transient_translate_sheet[action.key]['Description'])}""")
        status = set()
        for name in names: status |= set(s.key for s in status_by_name.get(action['Name'].lower(), []))
        for status in status:
            status = status_sheet_eng[status]
            (f.write if w_mode else print)(
                f"\n>> {status.key}, {status['Name']}, {desc_process(status['Description'])}")
        (f.write if w_mode else print)(f"""
        \"""
        id = {action.key}
        name = {names}
    """)
        if action['Action{Combo}'].key:
            (f.write if w_mode else print)(f"        combo_action = {action['Action{Combo}'].key}\n")
