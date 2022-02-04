from ctypes import *
import glm
import OpenGL.GL as gl


class BaseModel3d:
    _surface_vertices = []
    _surface_mode = gl.GL_TRIANGLE_FAN

    _edge_vertices = []
    _edge_mode = gl.GL_LINE_LOOP

    _point_vertices = []
    _point_mode = gl.GL_POINTS

    def __init__(self):
        t_len = len(self._point_vertices) + len(self._edge_vertices) + len(self._surface_vertices)
        self.point_range = [0, len(self._point_vertices) // 3]
        self.edge_range = [sum(self.point_range), len(self._edge_vertices) // 3]
        self.surface_range = [sum(self.edge_range), len(self._surface_vertices) // 3]

        data = (c_float * t_len)(*self._point_vertices, *self._edge_vertices, *self._surface_vertices)
        self.vao = gl.glGenVertexArrays(1)
        gl.glBindVertexArray(self.vao)
        self.vbo = gl.glGenBuffers(1)

        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, sizeof(data), data, gl.GL_STATIC_DRAW)
        gl.glEnableVertexAttribArray(0)
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, None)

        gl.glBindVertexArray(0)

    def render(
            self,
            program,
            transform: glm.mat4,
            mvp: glm.mat4,
            surface: glm.vec4 = None,
            edge: glm.vec4 = None, line_width: float = 3.0,
            point: glm.vec4 = None, point_size: float = 5.0
    ):
        gl.glPushMatrix()
        gl.glUseProgram(program)

        gl.glUniformMatrix4fv(
            gl.glGetUniformLocation(program, "transform"),
            1, gl.GL_FALSE, glm.value_ptr(transform)
        )
        gl.glUniformMatrix4fv(
            gl.glGetUniformLocation(program, "mvp"),
            1, gl.GL_FALSE, glm.value_ptr(mvp)
        )

        gl.glBindVertexArray(self.vao)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        color_location = gl.glGetUniformLocation(program, "inColor")
        if surface is not None:
            gl.glUniform4fv(color_location, 1, glm.value_ptr(surface))
            gl.glDrawArrays(self._surface_mode, *self.surface_range)

        if edge is not None:
            gl.glUniform4fv(color_location, 1, glm.value_ptr(edge))
            gl.glLineWidth(line_width)
            gl.glDrawArrays(self._edge_mode, *self.edge_range)

        if point is not None:
            gl.glUniform4fv(color_location, 1, glm.value_ptr(point))
            gl.glPointSize(point_size)
            gl.glDrawArrays(self._point_mode, *self.point_range)

        gl.glBindVertexArray(0)
        gl.glUseProgram(0)
        gl.glPopMatrix()


class Line(BaseModel3d):
    _edge_vertices = [
        0, 0, 0,
        1, 0, 0
    ]
    _edge_mode = gl.GL_LINE_STRIP
    _point_vertices = _edge_vertices


class Point(BaseModel3d):
    _point_vertices = [0, 0, 0]


class PlaneXY(BaseModel3d):
    _surface_vertices = [
        -.5, -.5, 0.0,
        .5, -.5, 0.0,
        .5, .5, 0.0,
        -.5, .5, 0.0
    ]
    _edge_vertices = _surface_vertices
    _point_vertices = _surface_vertices


class Models:
    def __init__(self):
        self.line = Line()
        self.point = Point()
        self.plane_xy = PlaneXY()
