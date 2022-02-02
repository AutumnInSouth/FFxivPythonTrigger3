from ctypes import *
from ctypes.wintypes import *

import glfw
import imgui
from imgui.integrations import compute_fb_scale
from imgui.integrations.glfw import GlfwRenderer
from win32con import WM_LBUTTONDOWN, WM_LBUTTONUP, WM_RBUTTONUP, WM_RBUTTONDOWN, WM_MBUTTONUP, WM_MBUTTONDOWN
from win32gui import GetForegroundWindow, GetWindowRect

from FFxivPythonTrigger.window import CURRENT_HWND

evt_map = {
    WM_LBUTTONDOWN: (glfw.MOUSE_BUTTON_1, glfw.PRESS),
    WM_LBUTTONUP: (glfw.MOUSE_BUTTON_1, glfw.RELEASE),
    WM_RBUTTONDOWN: (glfw.MOUSE_BUTTON_2, glfw.PRESS),
    WM_RBUTTONUP: (glfw.MOUSE_BUTTON_2, glfw.RELEASE),
    WM_MBUTTONDOWN: (glfw.MOUSE_BUTTON_3, glfw.PRESS),
    WM_MBUTTONUP: (glfw.MOUSE_BUTTON_3, glfw.RELEASE),
}

default_mouse_state = [glfw.RELEASE, glfw.RELEASE, glfw.RELEASE]


class CustomGlfwRenderer(GlfwRenderer):
    def __init__(self, window, fpt_plugin):
        super().__init__(window)
        self.fpt_plugin = fpt_plugin

    def process_inputs(self):
        io = imgui.get_io()

        window_size = glfw.get_window_size(self.window)
        fb_size = glfw.get_framebuffer_size(self.window)
        io.display_size = window_size
        io.display_fb_scale = compute_fb_scale(window_size, fb_size)

        if GetForegroundWindow() != CURRENT_HWND:
            io.mouse_pos = (0, 0)

        current_time = glfw.get_time()

        if self._gui_time:
            self.io.delta_time = current_time - self._gui_time
        else:
            self.io.delta_time = 1. / 60.

        self._gui_time = current_time
