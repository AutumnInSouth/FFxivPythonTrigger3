import pysaintcoinach
import re
from pathlib import Path

game_path_eng = r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game'  # 自行替换
realm_eng = pysaintcoinach.ARealmReversed(game_path_eng, pysaintcoinach.Language.english,
                                          Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3\DefinitionsExt4'))  # 国际服

line_break = re.compile(r'[\r\n\u3000]+')
ui_foreground = re.compile(r"</?UIForeground(\(\d+\))?>")
ui_foreground2 = re.compile(r"<UIForeground>[0-9A-F]+</UIForeground>")
ui_glow = re.compile(r"</?UIGlow(\(\d+\))?>")
ui_glow2 = re.compile(r"<UIGlow>[0-9A-F]+</UIGlow>")
if_job = re.compile(r"<If\(Equal\(PlayerParameter\(68\),(?P<job_id>\d+)\)\)>(?P<true_statement>[^<]*)<Else/>(?P<false_statement>[^<]*)</If>")
if_lv = re.compile(r"<If\(GreaterThanOrEqualTo\(PlayerParameter\(72\),(?P<min_lv>\d+)\)\)>"
                   r"(?P<true_statement>[^<]*)<Else/>(?P<false_statement>[^<]*)</If>")


def desc_process(desc: str):
    rtn = ui_glow.sub('', ui_foreground.sub('', ui_glow2.sub('', ui_foreground2.sub('', desc))))
    while if_job.search(rtn) or if_lv.search(rtn):
        rtn = if_job.sub(r"(source.job==\1?\2:\3)", rtn)
        rtn = if_lv.sub(r"(source.level>=\1?\2:\3)", rtn)
    return rtn


status_by_name = {}
for status in realm_eng.game_data.get_sheet('Status'):
    status_by_name.setdefault(status['Name'], []).append(status)

action_transient_sheet = realm_eng.game_data.get_sheet('ActionTransient')
for action in realm_eng.game_data.get_sheet('Action'):
    if action['Name'] and action_transient_sheet[action.key]['Description']:
        print(action.key, action['Name'])
        print(desc_process(action_transient_sheet[action.key]['Description']))
        for status in status_by_name.get(action['Name'], []):
            print('>>',status.key,status['Name'], desc_process(status['Description']))
        print()
