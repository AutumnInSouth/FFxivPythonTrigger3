from ctypes import *
from queue import Queue, Empty as QueueEmpty
from typing import TYPE_CHECKING

from FFxivPythonTrigger.hook import PluginHook
from .decoder import process_hook_msg

if TYPE_CHECKING:
    from . import XivNetwork


class WebActionHook(PluginHook):
    auto_install = True
    argtypes = [c_int64, POINTER(c_ubyte), c_int]
    restype = c_int
    plugin: 'XivNetwork'
    n = ""

    def __init__(self, plugin, func_address):
        super().__init__(plugin, func_address)
        self.zone_socket = 0
        self.zone_buffer = bytearray()
        self.zone_in_queue: Queue[bytearray] = Queue()
        self.zone_out_queue: Queue[bytearray] = Queue()
        self.non_zone_socket = 0
        self.non_zone_buffer = bytearray()
        self.non_zone_in_queue: Queue[bytearray] = Queue()
        self.non_zone_out_queue: Queue[bytearray] = Queue()
        self.zone_process_mission = None
        self.non_zone_process_mission = None

    def install(self):
        self.non_zone_in_queue.queue.clear()
        self.non_zone_out_queue.queue.clear()
        self.zone_process_mission = self.plugin.create_mission(f'zone_process_{self.n}', 0)
        self.non_zone_process_mission = self.plugin.create_mission(f'non_zone_process_{self.n}', 0)
        super().install()

    def uninstall(self):
        super().uninstall()
        if self.zone_process_mission is not None:
            self.zone_process_mission.join(0)
            self.zone_out_queue.put(bytearray())
        if self.non_zone_process_mission is not None:
            self.non_zone_process_mission.join(0)
            self.non_zone_out_queue.put(bytearray())

    def process_zone_buffer(self):
        process_hook_msg(self.zone_buffer, self.zone_in_queue, self.zone_out_queue)

    def process_non_zone_buffer(self):
        process_hook_msg(self.non_zone_buffer, self.non_zone_in_queue, self.non_zone_out_queue)

    def select_queue(self, socket):
        is_zone = self.plugin.is_zone_socket(socket)
        if is_zone:
            if self.zone_socket != socket:
                self.zone_in_queue.queue.clear()
                self.zone_out_queue.queue.clear()
                self.zone_socket = socket
            return is_zone, self.zone_in_queue, self.zone_out_queue
        else:
            if self.non_zone_socket != socket:
                self.non_zone_in_queue.queue.clear()
                self.non_zone_out_queue.queue.clear()
                self.non_zone_socket = socket
            return is_zone, self.non_zone_in_queue, self.non_zone_out_queue


class SendHook(WebActionHook):
    def hook_function(self, socket, buffer, size):
        is_zone, in_queue, out_queue = self.select_queue(socket)
        in_queue.put(bytearray(buffer[:size]))
        while not out_queue.empty():
            out_msg = out_queue.get()
            if out_msg:
                new_size = len(out_msg)
                success_size = self.original(socket, (c_ubyte * new_size).from_buffer(out_msg), new_size)
                if success_size: pass
        return size


class RecvHook(WebActionHook):
    def __init__(self, plugin, func_address):
        super().__init__(plugin, func_address)
        self.buffers = dict()

    def hook_function(self, socket, buffer, size):
        is_zone, in_queue, out_queue = self.select_queue(socket)
        _buffer = self.buffers.setdefault(socket, bytearray())
        if buffer:
            rtn_size = min(size, len(_buffer))
            memmove(buffer, _buffer, rtn_size)
            del _buffer[:rtn_size]
            return rtn_size
        try:
            rtn_msg = out_queue.get(block=False)
        except QueueEmpty:
            pass
        else:
            if rtn_msg:
                rtn_size = len(rtn_msg)
                if rtn_size > size:
                    memmove(buffer, rtn_msg, size)
                    _buffer.extend(rtn_msg[size:])
                    return size
                else:
                    memmove(buffer, rtn_msg, rtn_size)
                    return rtn_size
        rtn_msg = bytearray()
        while not rtn_msg:
            success_size = self.original(socket, buffer, size)
            if not success_size: return 0
            in_queue.put(bytearray(buffer[:success_size]))
            rtn_msg = out_queue.get()
        rtn_size = len(rtn_msg)
        if rtn_size > size:
            memmove(buffer, rtn_msg, size)
            _buffer.extend(rtn_msg[size:])
            return size
        else:
            memmove(buffer, rtn_msg, rtn_size)
            return rtn_size
