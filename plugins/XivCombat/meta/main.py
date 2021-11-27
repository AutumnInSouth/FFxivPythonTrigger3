import pysaintcoinach
import re

"""
依赖fpt pysaintcoinach
作业目标： 
格式化描述，支持中英描述，输出文件 output.py，格式可参考 example_output.py
提供代码输出为 desc_output.txt
"""
#game_path = r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game'  # 自行替换
game_path = r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game'  # 自行替换
line_break = re.compile(r'[\r\n\u3000]+')
ui_foreground = re.compile(r"</?UIForeground(\(\d+\))?>")
ui_glow = re.compile(r"</?UIGlow(\(\d+\))?>")
if_job = re.compile(r"<If\(Equal\(PlayerParameter\(68\),(?P<job_id>\d+)\)\)>(?P<true_statement>[^<]*)<Else/>(?P<false_statement>[^<]*)</If>")
if_lv = re.compile(r"<If\(GreaterThanOrEqualTo\(PlayerParameter\(72\),(?P<min_lv>\d+)\)\)>"
                   r"(?P<true_statement>[^<]*)<Else/>(?P<false_statement>[^<]*)</If>")

# realm = pysaintcoinach.ARealmReversed(game_path, pysaintcoinach.Language.chinese_simplified)  # 国服
realm = pysaintcoinach.ARealmReversed(game_path, pysaintcoinach.Language.english)  # 国际服
action_sheet = realm.game_data.get_sheet('Action')
action_transient_sheet = realm.game_data.get_sheet('ActionTransient')
fight_abbrev = [class_job['Abbreviation']
                for class_job in realm.game_data.get_sheet('ClassJob')
                if class_job['Abbreviation'] and class_job['ClassJobCategory'].key in {30, 31}]
fight_category = [class_job_category.key
                  for class_job_category in realm.game_data.get_sheet('ClassJobCategory')
                  if any(class_job_category[class_job] for class_job in fight_abbrev)]
cnt = 0
for action in action_sheet:
    if (
            action['Name'] and not action['IsPvP'] and action['ClassJobCategory'] and
            action['ClassJobCategory'].key in fight_category and
            action_transient_sheet[action.key]['Description']
    ):
        print(action.key, action['Name'], action['Action{Combo}'].key if action['Action{Combo}'] else 'no combo')
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
        print(desc)
        print()
        cnt += 1
print(cnt)
