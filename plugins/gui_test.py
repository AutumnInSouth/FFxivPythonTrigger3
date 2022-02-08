import math
from ctypes import addressof

from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import event

import imgui
import glm
import OpenGL.GL as gl
import glfw
import pprint


def draw_2d():
    view = plugins.Gui.get_view()
    me_pos = view.me_pos
    if me_pos is None: return
    coor = plugins.XivMemory.coordinate
    transform = glm.translate(
        glm.vec3(coor.x, coor.z, coor.y)
    ) * glm.rotate(
        coor.r, glm.vec3(0, 1, 0)
    ) * glm.scale(
        glm.vec3(1, 1, 1)
    )
    _vertices = [
        transform * glm.vec4(1, 0, 1, 1),
        transform * glm.vec4(1, 0, -1, 1),
        transform * glm.vec4(-1, 0, -1, 1),
        transform * glm.vec4(-1, 0, 1, 1),
    ]

    vertices = [
        (pos if in_screen else view.cut_point_at_border(me_pos.x, me_pos.y, pos.x, pos.y))
        for pos, in_screen in (view.world_to_screen(v.x, v.z, v.y) for v in _vertices)
    ]
    vertices = [v for v in vertices if v is not None]
    imgui.begin("vertices")
    for _v, v in zip(_vertices, vertices):
        imgui.text(f"{_v.x:.2f} {_v.y:.2f} {_v.z:.2f} -> {v.x:.2f} {v.y:.2f}")
    imgui.end()

    # draw vertices on the screen
    gl.glPointSize(5)
    gl.glBegin(gl.GL_POINTS)
    gl.glColor3f(1.0, 0.0, 0.0)
    for v in vertices:
        gl.glVertex2f(v.x, v.y)
    gl.glColor3f(0.0, 0.0, 1.0)
    gl.glVertex2f(*me_pos)
    gl.glEnd()

    gl.glColor3f(0.0, 1.0, 0.0)
    gl.glBegin(gl.GL_LINES)
    for v in vertices:
        gl.glVertex2f(v.x, v.y)
        gl.glVertex2f(me_pos.x, me_pos.y)
    gl.glEnd()

    gl.glColor4f(1.0, 1.0, 0.0, .3)
    gl.glBegin(gl.GL_POLYGON)
    for v in vertices:
        gl.glVertex2f(v.x, v.y)
    gl.glEnd()


def test_plane():
    gl.glDisable(gl.GL_DEPTH_TEST)
    for a in plugins.XivMemory.actor_table:
        if a.type == "player":
            pos = a.pos
            sin_time = (math.sin(glfw.get_time()) + 1) / 2
            plugins.Gui.add_plane(
                glm.translate(
                    glm.vec3(pos.x, pos.z + sin_time, pos.y)
                ) * glm.rotate(
                    pos.r + sin_time * math.pi, glm.vec3(0, 1, 0)
                ) * glm.scale(
                    glm.vec3(1, 1, 1)
                ),
                surface_color=glm.vec4(1, 0, 0, .3),
                line_color=glm.vec4(1, 0, 0, .7),
                point_color=glm.vec4(0, 1, 1, 1),
            )

            cos_time = (math.cos(glfw.get_time()) + 1) / 2
            plugins.Gui.add_plane(
                glm.translate(
                    glm.vec3(pos.x, pos.z + cos_time, pos.y)
                ) * glm.rotate(
                    pos.r + cos_time * math.pi, glm.vec3(0, 1, 0)
                ) * glm.scale(
                    glm.vec3(1, 1, 1)
                ),
                surface_color=glm.vec4(0, 1, 0, .3),
                line_color=glm.vec4(0, 1, 0, .7),
                point_color=glm.vec4(1, 0, 1, 1),
            )

    gl.glEnable(gl.GL_DEPTH_TEST)


def test_line():
    me = plugins.XivMemory.actor_table.me
    if me is None: return
    current = plugins.XivMemory.targets.current
    if current is None: return
    t = glfw.get_time()
    plugins.Gui.add_line(
        start=glm.vec3(me.pos.x, me.pos.z, me.pos.y),
        end=glm.vec3(current.pos.x, current.pos.z, current.pos.y),
        line_color=glm.vec4(math.cos(t), math.cos(t / 1.5), math.cos(t / 2), 1),
        line_width=1,
        point_color=glm.vec4(0, 1, 0, 1),
        point_size=5,
    )


def test_point():
    for a in plugins.XivMemory.actor_table:
        if a.type == "player":
            plugins.Gui.add_point(glm.vec3(a.pos.x, a.pos.z, a.pos.y), glm.vec4(1, 0, 0, 1))


class GuiTest(PluginBase):
    name = "GuiTest"

    def __init__(self):
        super().__init__()
        self.register_gui()

    def _reg_gui(self):
        plugins.Gui.register_interface(self, self.draw_test)

    @event("plugin_load:Gui")
    def register_gui(self, _):
        plugins.Gui.work_queue.put((self._reg_gui, tuple()))

    def draw_test(self):
        io = imgui.get_io()
        imgui.begin("gui data")
        imgui.text(f"fps: {io.framerate:.2f}")
        imgui.end()

        me = plugins.XivMemory.actor_table.me
        if me is not None:
            imgui.begin("me")
            imgui.text(f"{addressof(me):x}")
            for row in pprint.pformat(me.get_data()).split("\n"):
                imgui.text(row)
            imgui.end()

        current = plugins.XivMemory.targets.current
        if current is not None:
            imgui.begin("target")
            imgui.text(f"{addressof(current):x}")
            for row in pprint.pformat(current.get_data()).split("\n"):
                imgui.text(row)
            imgui.end()

        # test_line()
