import pysaintcoinach
import re


game_path = r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game'  # 自行替换
game_path_eng = r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game'  # 自行替换
line_break = re.compile(r'[\r\n\u3000]+')
ui_foreground = re.compile(r"</?UIForeground(\(\d+\))?>")
ui_glow = re.compile(r"</?UIGlow(\(\d+\))?>")
if_job = re.compile(r"<If\(Equal\(PlayerParameter\(68\),(?P<job_id>\d+)\)\)>(?P<true_statement>[^<]*)<Else/>(?P<false_statement>[^<]*)</If>")
if_lv = re.compile(r"<If\(GreaterThanOrEqualTo\(PlayerParameter\(72\),(?P<min_lv>\d+)\)\)>"
                   r"(?P<true_statement>[^<]*)<Else/>(?P<false_statement>[^<]*)</If>")

realm = pysaintcoinach.ARealmReversed(game_path, pysaintcoinach.Language.chinese_simplified)  # 国服
realm_eng = pysaintcoinach.ARealmReversed(game_path_eng, pysaintcoinach.Language.english)  # 国际服
action_sheet = realm.game_data.get_sheet('Action')
status_sheet = realm.game_data.get_sheet('Status')
action_sheet_eng = realm_eng.game_data.get_sheet('Action')
status_sheet_eng = realm_eng.game_data.get_sheet('Status')
action_transient_sheet = realm.game_data.get_sheet('ActionTransient')
fight_abbrev = [class_job['Abbreviation']
                for class_job in realm.game_data.get_sheet('ClassJob')
                if class_job['Abbreviation'] and class_job['ClassJobCategory'].key in {30, 31}]
fight_category = [class_job_category.key
                  for class_job_category in realm.game_data.get_sheet('ClassJobCategory')
                  if sum(class_job_category[class_job] for class_job in fight_abbrev)<3]
status_by_name = {}
for status in status_sheet:
    status_by_name.setdefault(status['Name'], []).append(status)

def to_under_line(s):
    return re.sub(r'([A-Z]| [a-z])', lambda m: '_' + m.group(0)[-1].lower(), s).replace(' ','')

def to_hump(s):
    return re.sub(r'[_ ]([a-zA-Z])', lambda m: m.group(1).upper(), s.capitalize()).replace(' ','').replace("'",'').replace(':','')

eng_cj_sheet = realm_eng.game_data.get_sheet('ClassJob')
for class_job in realm.game_data.get_sheet('ClassJob'):
    if class_job.key and class_job['Abbreviation'] and class_job['ClassJobCategory'].key in {30, 31} and not class_job['StartingTown'].key:
        print(class_job['Name'])
        with open(f'{to_under_line(eng_cj_sheet[class_job.key]["Name"])}.py', 'w+', encoding='utf-8') as f:
            f.write("""from ..base import ActionBase, StatusBase, physic, magic


class Actions:
""")
            for action in action_sheet:
                if (
                        action['Name'] and not action['IsPvP'] and action['ClassJobCategory'] and
                        action['ClassJobCategory'][class_job['Abbreviation']] and
                        action['ClassJobCategory'].key in fight_category and
                        action_transient_sheet[action.key]['Description']
                ):
                    desc = ui_glow.sub(
                        '', ui_foreground.sub(
                            '', line_break.sub(
                                ' ', action_transient_sheet[action.key]['Description']
                            )
                        )
                    )
                    while if_job.search(desc) or if_lv.search(desc):
                        desc = if_job.sub(r"(source.job==\1?\2:\3)", desc)
                        desc = if_lv.sub(r"(source.level>=\1?\2:\3)", desc)
                    f.write(f"""
    class {to_hump(action_sheet_eng[action.key]['Name'])}(ActionBase):
        \"""
        {desc}
""")
                    for status in status_by_name.get(action['Name'], []):
                        f.write(f"\n        {status.key}, {status['Name']}, {status_sheet_eng[status.key]['Name']}, {line_break.sub(' ', status['Description'])}")
                    f.write(f"""
        \"""
        id = {action.key}
        name = {{'{action_sheet_eng[action.key]['Name']}', '{action['Name']}'}}
""")
                    if action['Action{Combo}'].key:
                        f.write(f"        combo_action = {action['Action{Combo}'].key}\n")
