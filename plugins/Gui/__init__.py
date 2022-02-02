import os
import pathlib
import queue
import traceback

from win32gui import GetForegroundWindow

from FFxivPythonTrigger.decorator import unload_callback
from FFxivPythonTrigger.utils import WaitTimeoutException, err_catch
from FFxivPythonTrigger.window import CURRENT_HWND

dir_path = pathlib.Path(__file__).parent.absolute()
os.environ['PYGLFW_PREVIEW'] = 'True'
os.environ['PYGLFW_LIBRARY'] = str(dir_path / 'res' / 'glfw3.dll')

import glfw
import imgui
import OpenGL.GL as gl

from FFxivPythonTrigger import PluginBase, BindValue, frame_inject, wait_until, AddressManager
from . import window, custom_glfw_renderer, test_window, key_hook


def problem_draw():
    imgui.begin("Problem")
    raise Exception("Test")


class Gui(PluginBase):
    name = "Gui"
    separate_thread = BindValue(default=True, auto_save=True)

    def __init__(self):
        super().__init__()

        self.window = None
        self.impl = None
        self.frame_cnt = 0
        self.err_cnt = 0
        self.on_work = False
        self.work_queue = queue.Queue()
        self.interfaces = set()
        self.interfaces.add(test_window.show_test_window)
        self.interfaces.add(problem_draw)
        self.key_hook = key_hook.KeyHook(self, AddressManager(self.name, self.logger).scan_address(
            "key_hook", "48 89 5C 24 ? 55 56 57 41 56 41 57 48 83 EC ? 4D 8B F1"
        ))

    @unload_callback('unregister_interface')
    def register_interface(self, draw_func):
        self.interfaces.add(draw_func)

    def unregister_interface(self, draw_func):
        try:
            self.interfaces.remove(draw_func)
        except Exception:
            pass

    def process_single_frame(self):
        try:
            self._process_single_frame()
        except Exception:
            self.logger.error(f"process_single_frame error {self.err_cnt}:\t", traceback.format_exc())
            self.err_cnt += 1
            if self.err_cnt > 10:
                glfw.set_window_should_close(self.window, True)
        else:
            self.err_cnt = 0

    def _process_single_frame(self):
        while not self.work_queue.empty():
            try:
                f, a = self.work_queue.get(block=False)
            except queue.Empty:
                break
            else:
                f(*a)
        glfw.poll_events()
        if GetForegroundWindow() == CURRENT_HWND:
            window.set_window_cover(self.window)
            self.impl.process_inputs()
            self.frame_cnt += 1
            imgui.new_frame()
            self.key_hook.export_imgui_key()

            for draw_func in self.interfaces.copy():
                try:
                    draw_func()
                except Exception:
                    self.logger.error(f"draw_func error, func will be remove:\t", traceback.format_exc())
                    self.unregister_interface(draw_func)
                    while 1:
                        try:
                            imgui.end_frame()
                        except Exception:
                            imgui.end()
                        else:
                            break
                    return
            gl.glClearColor(0, 0, 0, 0)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)
            i = 1
            while i:
                try:
                    imgui.render()
                except Exception:
                    self.logger.warning(f"render fail,try end window-{i}")
                    i += 1
                    imgui.end()
                else:
                    break
            self.impl.render(imgui.get_draw_data())
        else:
            gl.glClearColor(0, 0, 0, 0)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        glfw.swap_buffers(self.window)

    def frame_work(self):
        if glfw.window_should_close(self.window):
            self.logger(f"end")
            frame_inject.unregister_continue_call(self.frame_work)
            self.impl.shutdown()
            glfw.terminate()
            self.on_work = False
            return
        self.process_single_frame()

    def start_frame(self):
        self.window = window.init_window()
        self.imgui_init()
        self.impl = custom_glfw_renderer.CustomGlfwRenderer(self.window, self)
        glfw.swap_interval(0)
        frame_inject.register_continue_call(self.frame_work)
        self.logger(f"start in frame")

    def start(self):
        self.on_work = True
        if self.separate_thread:
            self.window = window.init_window()
            self.imgui_init()
            self.impl = custom_glfw_renderer.CustomGlfwRenderer(self.window, self)
            glfw.swap_interval(1)
            self.logger(f"start in single")
            while not glfw.window_should_close(self.window):
                self.process_single_frame()
            self.impl.shutdown()
            glfw.terminate()
            self.on_work = False
        else:
            frame_inject.register_once_call(self.start_frame)

    def imgui_init(self):
        imgui.create_context()
        # imgui.get_io().ini_file_name = str(self.storage.path / "imgui.ini").encode('utf-8') + b'\0'
        key_hook.init_imgui_key_code_map()

    def onunload(self):
        if self.on_work:
            self.work_queue.put((glfw.set_window_should_close, (self.window, True)))
            try:
                wait_until(lambda: not self.on_work or None, timeout=5)
            except WaitTimeoutException:
                self.logger.error("Failed to wait for window close")
