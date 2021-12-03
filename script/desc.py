import re

desc="""
Reduces damage taken by a party member or self by 10%.
<UIForeground>F201F8</UIForeground><UIGlow>F201F9</UIGlow>Duration: <UIGlow>01</UIGlow><UIForeground>01</UIForeground>10s
<UIForeground>F201F8</UIForeground><UIGlow>F201F9</UIGlow>Maximum Charges: <UIGlow>01</UIGlow><UIForeground>01</UIForeground>2
"""

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
print(desc_process(desc))
