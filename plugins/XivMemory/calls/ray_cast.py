from ctypes import *

import glm
import win32api
import win32gui

from FFxivPythonTrigger.window import CURRENT_HWND

get_camera_matrix_interface = CFUNCTYPE(c_int64)
screen_to_world_interface = CFUNCTYPE(c_bool, POINTER(c_float), POINTER(c_float), c_float, POINTER(c_float), POINTER(c_int))
flag = (c_int * 3)(0x4000, 0x4000, 0x0)


def trans(v4: glm.vec4): return glm.vec3(v4 / v4.w)


class RayCast:
    def __init__(self, screen_to_world_address, get_camera_matrix_address):
        self._original = screen_to_world_interface(screen_to_world_address)
        self._get_camera_matrix = get_camera_matrix_interface(get_camera_matrix_address)

    def get_camera_matrix(self):
        matrix_singleton = cast(self._get_camera_matrix() + 0x1b4, POINTER(c_float))
        return matrix_singleton[:16], (matrix_singleton[16], matrix_singleton[17])

    def original(self, local_x, local_y, ray_distance=10000.):
        camera_matrix,(screen_x,screen_y) = self.get_camera_matrix()
        view_projection_matrix = glm.inverse(glm.mat4(*camera_matrix))
        screen_pos_3d = glm.vec4(
            local_x / screen_x * 2 - 1,
            -(local_y / screen_y * 2 - 1),
            0, 1
        )
        cam_pos = trans(view_projection_matrix * screen_pos_3d)
        screen_pos_3d.z = 1
        clip_pos = trans(view_projection_matrix * screen_pos_3d) - cam_pos
        world_pos_array = (c_float * 32)()
        success = self._original(glm.value_ptr(cam_pos), glm.value_ptr(glm.normalize(clip_pos)), ray_distance, world_pos_array, flag)
        if not success: raise ValueError('screen_to_world failed')
        return world_pos_array[0], world_pos_array[2], world_pos_array[1]

    def cursor_to_world(self):
        x, y = win32api.GetCursorPos()
        x1, y1, x2, y2 = win32gui.GetWindowRect(CURRENT_HWND)
        if not (x1 < x < x2 and y1 < y < y2): raise ValueError('Cursor not in game window')
        return self.original(x - x1, y - y1)

    def __call__(self, local_x: int, local_y: int, ray_distance: float = 10000.):
        return self.original(local_x, local_y, ray_distance)
