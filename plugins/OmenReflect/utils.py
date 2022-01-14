from ctypes import *

from FFxivPythonTrigger.saint_coinach import action_sheet
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct

c = 3.0518043 * 0.0099999998


def web_to_raw(pos):
    return pos * c - 1000


def raw_to_web(pos):
    return int((pos + 1000) / c)


def col_offset(col_name):
    return action_sheet.header.get_column(action_sheet.header.sheet_definition.find_column(col_name)).offset


action_struct = OffsetStruct({
    'omen': (c_ushort, col_offset('Omen')),
    'cast_type': (c_ubyte, col_offset('CastType')),
    'effect_range': (c_ubyte, col_offset('EffectRange')),
    'x_axis_modifier': (c_ubyte, col_offset('XAxisModifier')),
    'cast_100ms': (c_ushort, col_offset('Cast<100ms>')),
})

"""
常用标记
*关于月环：月环内圈为等比缩放，请根据内圈半径/外圈半径比例选择 omen
1：圆形
2：矩形

146：20扇形
105：30扇形
206：45扇形
3：60扇形 （183高亮）
4：90扇形 （184高亮）
5：120扇形 （185高亮）
28：150扇形
107：180扇形 （194高亮）
128：210扇形
15：270扇形

14：6%月环
13：13%月环
228：23%月环
227：25%月环
12：36.8%月环
220：40%月环
108：50%月环
112：66%月环
137：46%月环
78：80%月环

229：纵向击退(矩形)
203：圆心击退(圆形)
114：直线两侧击退(矩形)
188: 十字(矩形*2)
139：浪柱（？）
90：塔
"""

"""
cast type:
[0] = "Any",
[1] = "Cone / Fan",
[2] = "Circle - No Padding",
[3] = "Cone / Fan - With Padding",
[4] = "Line - Static Length",
[5] = "Circle - With Padding",
[6] = "Circle - Meteor Types",
[7] = "Circle - Ground Targeting, sometimes leaves a puddle",
[8] = "Line - Follows Player so Length Adjusts",
[9] = "", -- No Action has CastType 9
[10] = "Donut - No Padding",
[11] = "Cross (Two Lines) - No Padding",
[12] = "Line - No Padding",
[13] = "Cone / Fan - No Padding",
"""

cast_type_name = {
    0: 'unk_0',
    1: 'unk_1',
    2: 'Circle - No Padding',
    3: 'Cone / Fan - With Padding',
    4: 'Line - Static Length',
    5: 'Circle - With Padding',
    6: 'Circle - Meteor Types',
    7: 'Circle - Ground Targeting, sometimes leaves a puddle',
    8: 'Line - Follows Player so Length Adjusts',
    9: 'unk_9',
    10: 'Donut - No Padding',
    11: 'Cross (Two Lines) - No Padding',
    12: 'Line - No Padding',
    13: 'Cone / Fan - No Padding',
}
