import time
import traceback
from ctypes import *
from threading import Lock
from typing import TYPE_CHECKING

from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.utils import err_catch
from .decoder import PacketProcessor, pack_message

if TYPE_CHECKING:
    from . import XivNetwork

SEND_DEBUG = False


class SendHook(PluginHook):
    auto_install = True
    argtypes = [c_int64, POINTER(c_ubyte), c_int]
    restype = c_int
    plugin: 'XivNetwork'

    def __init__(self, plugin, func_address):
        super().__init__(plugin, func_address)
        self.original_lock = Lock()
        self.send_locks = {}
        self.processors = dict()

    @err_catch
    def hook_function(self, socket, buffer, size):
        raw_data = bytearray(buffer[:size])
        if SEND_DEBUG:
            self.plugin.logger('send_start')
            self.plugin.logger('send socket', hex(socket))
            self.plugin.logger('send buffer', hex(cast(buffer, c_void_p).value))
            self.plugin.logger('send size', size)
        with self.original_lock:
            if socket not in self.processors:
                self.plugin.logger.debug(f"Initial send decoder of {socket:x}")
                self.processors[socket] = PacketProcessor()
        processor = self.processors[socket]
        with processor.lock:
            to_send = processor.process(raw_data)
            if to_send is None:
                self.plugin.logger('send none')
            data = bytearray()
            while to_send is not None:
                if isinstance(to_send, bytearray):
                    data += to_send
                else:
                    bundle_header, messages = to_send
                    bundle_header, messages = self.plugin.process_messages(bundle_header, messages, False, socket)
                    if messages:
                        data += pack_message(bundle_header, messages)
                to_send = processor.get()
            if data:
                new_size = len(data)
                if SEND_DEBUG:
                    self.plugin.logger('send', new_size)
                with self.send_locks.setdefault(socket, Lock()):
                    success_size = self.original(socket, (c_ubyte * new_size).from_buffer(data), new_size)
                if success_size < 1:
                    self.plugin.logger.error("send error", success_size)
                    return success_size
        if SEND_DEBUG:
            self.plugin.logger('finish send', size)
        return size


class BufferProcessorHook(PluginHook):
    auto_install = True
    argtypes = [c_int64, POINTER(c_ubyte), c_int]
    plugin: 'XivNetwork'

    def __init__(self, plugin, func_address, socket_type):
        super().__init__(plugin, func_address)
        self.lock = Lock()
        self.processor = PacketProcessor()
        self.socket_type = socket_type

    @err_catch
    def hook_function(self, a1, buffer, size):
        raw_data = bytearray(buffer[:size])
        with self.lock:
            data = bytearray()
            res = self.processor.process(raw_data)
            while res is not None:
                if isinstance(res, tuple):
                    bundle_header, messages = res
                    bundle_header, messages = self.plugin.process_messages(bundle_header, messages, True, self.socket_type)
                    if messages: data += pack_message(bundle_header, messages)
                else:
                    data += res
                res = self.processor.get()
            if data:
                data_size = len(data)
                self.original(a1, (c_ubyte * data_size).from_buffer(data), data_size)
