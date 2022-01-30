from ctypes import *
from random import randint

from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.memory.struct_factory import *
from FFxivPythonTrigger.saint_coinach import realm
from FFxivPythonTrigger.text_pattern import find_signature_point, find_signature_address
from XivMemory.se_string.messages import *

coordinate = plugins.XivMemory.coordinate

way_marks = plugins.XivMemory.markings.way_mark
# z_base = coordinate.z
# for point in (way_marks.a, way_marks.b, way_marks.c, way_marks.d):
#     z_base += randint(5, 20)
#     point.z = z_base
#     plugins.Move.waypoint_list.append((point.x, point.y, point.z))
for point in (way_marks.a, way_marks.b, way_marks.c, way_marks.d, way_marks.one, way_marks.two, way_marks.three, way_marks.four):
    if point.is_active:
        print(f"{point.x:.1f}, {point.y:.1f}")
        plugins.Move.waypoint_list.append((point.x, point.y))
