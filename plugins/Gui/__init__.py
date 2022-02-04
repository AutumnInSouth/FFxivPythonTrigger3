import os
import pathlib
import queue
import traceback
import threading
from math import atan2
import glm
from win32gui import GetForegroundWindow

from FFxivPythonTrigger.decorator import unload_callback
from FFxivPythonTrigger.utils import WaitTimeoutException, err_catch
from FFxivPythonTrigger.window import CURRENT_HWND

dir_path = pathlib.Path(__file__).parent.absolute()
os.environ['PYGLFW_PREVIEW'] = 'True'
os.environ['PYGLFW_LIBRARY'] = str(dir_path / 'res' / 'glfw3.dll')

xiv_fnt = str(dir_path / 'res' / 'FFXIV_Lodestone_SSF.ttf')

import glfw
import imgui
import OpenGL.GL as gl

from FFxivPythonTrigger import PluginBase, BindValue, frame_inject, wait_until, AddressManager
from . import window, custom_glfw_renderer, test_window, key_hook, view
from .utils import common_shader, models


class Gui(PluginBase):
    name = "Gui"
    layout = str(dir_path / 'layout.js')

    separate_thread = BindValue(default=True, auto_save=True)

    font_size = BindValue(default=18, auto_save=True)
    font_path = BindValue(default=str(dir_path / 'res' / 'msyh.ttc'), auto_save=True)

    def __init__(self):
        super().__init__()
        self.program = None
        self.models: models.Models | None = None
        self.window = None
        self.impl = None
        self.frame_cnt = 0
        self.err_cnt = 0
        self.work_thread = None
        self.font = None
        self._view = None
        self.work_queue = queue.Queue()
        self.interfaces = set()
        self.ini_name = str(self.storage.path / "imgui.ini").encode('utf-8')
        # self.interfaces.add(test_window.show_test_window)
        # self.interfaces.add(problem_draw)
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
        self._view = None
        glfw.poll_events()
        gl.glClearColor(0, 0, 0, 0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glClear(gl.GL_DEPTH_BUFFER_BIT)

        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        gl.glEnable(gl.GL_BLEND)
        gl.glEnable(gl.GL_DEPTH_TEST)

        while not self.work_queue.empty():
            try:
                f, a = self.work_queue.get(block=False)
            except queue.Empty:
                break
            try:
                f(*a)
            except Exception:
                self.logger.error(f"work queue error:\n", traceback.format_exc())
        if GetForegroundWindow() == CURRENT_HWND:
            window.set_window_cover(self.window)
            self.impl.process_inputs()
            self.frame_cnt += 1
            imgui.new_frame()
            self.key_hook.export_imgui_key()
            try:
                imgui.push_font(self.font)
                for draw_func in self.interfaces.copy():
                    try:
                        draw_func()
                    except Exception:
                        self.logger.error(f"draw_func error, func will be remove:\n", traceback.format_exc())
                        self.unregister_interface(draw_func)
                        imgui.pop_font()
                        raise
                imgui.pop_font()
            except Exception:
                while 1:
                    try:
                        imgui.end_frame()
                    except Exception:
                        imgui.end()
                    else:
                        return

            imgui.render()
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
            self.work_thread = None
            return
        self.process_single_frame()

    def start_frame(self):
        self._init_everything_in_work_process()
        glfw.swap_interval(0)
        frame_inject.register_continue_call(self.frame_work)
        self.logger(f"start in frame")

    def _init_everything_in_work_process(self):
        self.work_thread = threading.get_ident()
        self.window = window.init_window()

        imgui.create_context()
        imgui.get_io().ini_file_name = self.ini_name
        key_hook.init_imgui_key_code_map()

        self.impl = custom_glfw_renderer.CustomGlfwRenderer(self.window, self)
        self.program = common_shader.get_common_shader()
        self.models = models.Models()

        # imgui.get_io().add_font_from_file_ttf(xiv_fnt, self.font_size)
        fonts = imgui.get_io().fonts
        self.font = fonts.add_font_from_file_ttf(self.font_path, self.font_size, fonts.get_glyph_ranges_chinese_full())
        self.impl.refresh_font_texture()

    def start(self):
        if self.separate_thread:
            self._init_everything_in_work_process()
            glfw.swap_interval(1)
            self.logger(f"start in single")
            while not glfw.window_should_close(self.window):
                self.process_single_frame()
            self.impl.shutdown()
            self.work_thread = None
        else:
            frame_inject.register_once_call(self.start_frame)
        glfw.terminate()

    def onunload(self):
        if self.work_thread:
            self.work_queue.put((glfw.set_window_should_close, (self.window, True)))
            try:
                wait_until(lambda: not self.work_thread or None, timeout=5)
            except WaitTimeoutException:
                self.logger.error("Failed to wait for window close")
        glfw.terminate()

    def get_view(self) -> view.View:
        if threading.get_ident() != self.work_thread:
            raise Exception("must be called in gui work thread")
        if self._view is None:
            self._view = view.View()
        return self._view

    def add_point(self, pos: glm.vec3, point_color: glm.vec4, point_size: float = 5.0):
        self.models.point.render(
            self.program,
            mvp=self.get_view().projection_view,
            transform=glm.translate(pos),
            point=point_color,
            point_size=point_size
        )

    def add_line(self, start: glm.vec3, end: glm.vec3, line_color: glm.vec4 = None, line_width: float = 3.0,
                 point_color: glm.vec4 = None, point_size: float = 5.0):
        self.models.line.render(
            self.program,
            mvp=self.get_view().projection_view,
            transform=glm.translate(start) * glm.rotate(
                atan2(start.z - end.z, end.x - start.x), glm.vec3(0, 1, 0)
            ) * glm.rotate(
                atan2(end.y - start.y, glm.distance(start.xz, end.xz)), glm.vec3(0, 0, 1)
            ) * glm.scale(glm.vec3(glm.length(end - start))),
            edge=line_color,
            line_width=line_width,
            point=point_color,
            point_size=point_size
        )

    def add_plane(self, transform: glm.mat4, surface_color: glm.vec4 = None, line_color: glm.vec4 = None,
                  line_width: float = 3.0, point_color: glm.vec4 = None, point_size: float = 5.0):
        self.models.plane_xz.render(
            self.program,
            mvp=self.get_view().projection_view,
            transform=transform,
            surface=surface_color,
            edge=line_color,
            line_width=line_width,
            point=point_color,
            point_size=point_size
        )
