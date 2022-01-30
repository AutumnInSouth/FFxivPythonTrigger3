from ctypes import *
from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.memory.struct_factory import *
from FFxivPythonTrigger.saint_coinach import realm
from FFxivPythonTrigger.text_pattern import find_signature_point, find_signature_address
from XivMemory.se_string.messages import *

coordinate = plugins.XivMemory.coordinate

way_marks = plugins.XivMemory.markings.way_mark
for _ in range(5):
    for point in (way_marks.a, way_marks.b, way_marks.c, way_marks.d):
        plugins.Move.waypoint_list.append((point.x, point.y))
