from ctypes import *
from random import randint

from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.memory.struct_factory import *
from FFxivPythonTrigger.saint_coinach import realm
from FFxivPythonTrigger.text_pattern import find_signature_point, find_signature_address
from XivMemory.se_string.messages import *

import glm
from OpenGL import GL as gl

_projection_matrix, (screen_x, screen_y) = plugins.XivMemory.calls.ray_cast.get_camera_matrix()
projection_matrix = glm.mat4(*_projection_matrix)

vertices = [
    glm.vec3(-1.0, -1.0, 0.0),
    glm.vec3(1.0, -1.0, 0.0),
    glm.vec3(1.0, 1.0, 0.0),
    glm.vec3(-1.0, 1.0, 0.0),
]

# project the vertices into screen space
vertices = [projection_matrix * glm.vec4(v, 1.0) for v in vertices]
vertices = [v / v.w for v in vertices]

# print vertices screen position in pixels
for v in vertices:
    print((v.x + 1) * screen_x / 2, (v.y + 1) * screen_y / 2)
