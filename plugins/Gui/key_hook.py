import imgui
from FFxivPythonTrigger.hook import *
from FFxivPythonTrigger.utils import err_catch


def init_imgui_key_code_map():
    io = imgui.get_io()
    io.key_map[imgui.KEY_TAB] = 9
    io.key_map[imgui.KEY_LEFT_ARROW] = 37
    io.key_map[imgui.KEY_RIGHT_ARROW] = 39
    io.key_map[imgui.KEY_UP_ARROW] = 38
    io.key_map[imgui.KEY_DOWN_ARROW] = 40
    io.key_map[imgui.KEY_PAGE_UP] = 33
    io.key_map[imgui.KEY_PAGE_DOWN] = 34
    io.key_map[imgui.KEY_HOME] = 36
    io.key_map[imgui.KEY_END] = 35
    io.key_map[imgui.KEY_DELETE] = 46
    io.key_map[imgui.KEY_BACKSPACE] = 8
    io.key_map[imgui.KEY_ESCAPE] = 27
    io.key_map[imgui.KEY_ENTER] = 13
    io.key_map[imgui.KEY_SPACE] = 32
    io.key_map[imgui.KEY_A] = 65
    io.key_map[imgui.KEY_C] = 67
    io.key_map[imgui.KEY_V] = 86
    io.key_map[imgui.KEY_X] = 88
    io.key_map[imgui.KEY_Y] = 89
    io.key_map[imgui.KEY_Z] = 90


class KeyHook(PluginHook):
    restype = c_int64
    argtypes = [c_int64, POINTER(c_int), POINTER(c_int), POINTER(c_int), c_int, c_int]
    auto_install = True

    def __init__(self, plugin: 'PluginBase', func_address: int):
        super().__init__(plugin, func_address)
        self.key_data = None
        self.mouse_data = None

    @err_catch
    def hook_function(self, a1, a2, mouse_data, key_data, a5, a6):
        self.mouse_data = mouse_data[:12]
        self.key_data = key_data[1:288]

        try:
            io = imgui.get_io()
            io.mouse_pos = (mouse_data[0], mouse_data[1])
            if io.want_capture_mouse:
                mouse_data[3] = 0
        except:
            pass
        return self.original(a1, a2, mouse_data, key_data, a5, a6)

    def export_imgui_key(self):
        io = imgui.get_io()
        if self.mouse_data and self.key_data:
            for i in range(287):
                io.keys_down[i] = bool(self.key_data[i])
            io.key_ctrl = io.keys_down[17]
            io.key_alt = io.keys_down[18]
            io.key_shift = io.keys_down[16]
            io.key_super = io.keys_down[91]
            io.mouse_pos = (self.mouse_data[0], self.mouse_data[1])
            io.mouse_wheel = self.mouse_data[2]
            io.mouse_down[0] = bool(self.mouse_data[3] & 1)
            io.mouse_down[1] = bool(self.mouse_data[3] & 2)
            io.mouse_down[2] = bool(self.mouse_data[3] & 4)
            io.mouse_down[3] = bool(self.mouse_data[3] & 8)
            io.mouse_down[4] = bool(self.mouse_data[3] & 16)
        return io
