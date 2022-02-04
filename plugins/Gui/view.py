from functools import cached_property

import glm

from FFxivPythonTrigger import plugins


class View:
    def __init__(self):
        self._projection_view = None
        self._screen_size = None
        self._me_pos = None

        self._camera_pos = None
        self._camera_rot = None

    def _init_camera_data(self):
        _projection_matrix, _screen_size = plugins.XivMemory.calls.ray_cast.get_camera_matrix()
        self._projection_view = glm.mat4(*_projection_matrix)
        self._screen_size = glm.vec2(*_screen_size)

    @property
    def projection_view(self):
        if self._projection_view is None:
            self._init_camera_data()
        return self._projection_view

    @property
    def screen_size(self):
        if self._screen_size is None:
            self._init_camera_data()
        return self._screen_size

    @property
    def me_pos(self):
        if self._me_pos is None:
            me = plugins.XivMemory.actor_table.me
            if me:
                pos = me.pos
                _me_pos, in_screen = self.world_to_screen(pos.x, pos.y, pos.z)
                if in_screen: self._me_pos = _me_pos
        return self._me_pos

    def world_to_screen(self, x, y, z) -> tuple[glm.vec2, bool]:
        mvp = self.projection_view * glm.vec4(x, z, y, 1)
        pos = glm.vec2(mvp.x, mvp.y) / abs(mvp.w)
        out_of_screen = mvp.w < 0 or pos.x < -1 or pos.x > 1 or pos.y < -1 or pos.y > 1
        return pos, not out_of_screen

    def cut_point_at_border(self, start_x, start_y, end_x, end_y):
        if (abs(start_x) > 1 or abs(start_y) > 1) and (abs(end_x) > 1 or abs(end_y) > 1):
            return None
        if start_x == end_x:
            if start_y == end_y: return glm.vec2(start_x, start_y)
            return glm.vec2(start_x, (1 if end_y > start_y else -1))
        elif start_y == end_y:
            return glm.vec2((1 if end_x > start_x else -1), start_y)
        else:
            slope = (end_y - start_y) / (end_x - start_x)
            x_border = 1 if end_x > start_x else -1
            y_at_x_border = (x_border - start_x) * slope + start_y
            if 1 >= y_at_x_border >= -1:
                return glm.vec2(x_border, y_at_x_border)
            else:
                y_border = 1 if end_y > start_y else -1
                return glm.vec2((y_border - start_y) / slope + start_x, y_border)
