import time
from ctypes import *
from threading import Lock
from typing import TYPE_CHECKING

from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.utils import err_catch
from .decoder import PacketProcessor, pack_message

if TYPE_CHECKING:
    from . import XivNetwork

RECV_DEBUG = False
SEND_DEBUG = False


class WebActionHook(PluginHook):
    auto_install = True
    argtypes = [c_int64, POINTER(c_ubyte), c_int]
    restype = c_int
    plugin: 'XivNetwork'

    def __init__(self, plugin, func_address):
        super().__init__(plugin, func_address)
        self.original_lock = Lock()
        self.processors = dict()


class SendHook(WebActionHook):
    @err_catch
    def hook_function(self, socket, buffer, size):
        if SEND_DEBUG: self.plugin.logger('start send', hex(socket))
        if SEND_DEBUG:
            self.plugin.logger('_send', hex(socket), size, hash(bytes(buffer[:size])))
        with self.original_lock:
            if socket not in self.processors:
                self.plugin.logger.debug(f"Initial send decoder of {socket:x}")
                self.processors[socket] = PacketProcessor()
        processor = self.processors[socket]
        with processor.lock:
            to_send = processor.process(bytearray(buffer[:size]))
            if to_send is None:
                self.plugin.logger('send none')
            while to_send is not None:
                if isinstance(to_send, bytearray):
                    data = to_send
                else:
                    bundle_header, messages = to_send
                    bundle_header, messages = self.plugin.process_messages(bundle_header, messages, False, socket)
                    if messages:
                        data = pack_message(bundle_header, messages)
                    else:
                        to_send = processor.get()
                        continue
                new_size = len(data)
                if SEND_DEBUG:
                    self.plugin.logger('send', hex(socket), new_size, hash(bytes(data)))
                success_size = self.original(socket,
                                             (c_ubyte * new_size).from_buffer(data),
                                             new_size)
                if success_size < 1:
                    self.plugin.logger.error("send error", success_size)
                    return success_size
                to_send = processor.get()
        if SEND_DEBUG:
            self.plugin.logger('finish send', size)
        return size


class RecvHook(WebActionHook):
    def __init__(self, plugin, func_address):
        super().__init__(plugin, func_address)
        self.buffers = dict()

    @err_catch
    def hook_function(self, socket, buffer, size):
        # return self.original(socket,buffer,size)
        with self.original_lock:
            if socket not in self.processors:
                self.plugin.logger.debug(f"Initial recv decoder of {socket:x}")
                self.processors[socket] = PacketProcessor()
        processor = self.processors[socket]
        original_hash = 0
        with processor.lock:
            if RECV_DEBUG: self.plugin.logger('start recv', hex(socket),hex(addressof(buffer)))
            if socket in self.buffers and self.buffers[socket]:
                rtn = self.buffers[socket]
                del self.buffers[socket]
            else:
                rtn = processor.get()
                if rtn is None:
                    success_size = self.original(socket, buffer, size)
                    if success_size < 1:
                        self.plugin.logger.error("recv error", success_size)
                        return success_size
                    new_hash = hash(bytes(buffer[:success_size]))
                    if RECV_DEBUG:  self.plugin.logger('_recv', hex(socket), f"{success_size}/{size}", new_hash)
                    original_hash = new_hash
                    rtn = processor.process(bytearray(buffer[:success_size]))
                    if rtn is None:
                        if RECV_DEBUG:  self.plugin.logger('_recv', "return -2")
                        return -2
                if not isinstance(rtn, bytearray):
                    bundle_header, messages = rtn
                    bundle_header, messages = self.plugin.process_messages(bundle_header, messages, True, socket)
                    rtn = pack_message(bundle_header, messages)
            extra_rtn = processor.get()
            while extra_rtn is not None:
                if not isinstance(extra_rtn, bytearray):
                    bundle_header, messages = extra_rtn
                    bundle_header, messages = self.plugin.process_messages(bundle_header, messages, True, socket)
                    extra_rtn = pack_message(bundle_header, messages)
                rtn += extra_rtn
                extra_rtn = processor.get()
            rtn_size = len(rtn)
            new_hash = hash(bytes(rtn))
            if new_hash != original_hash:
                self.plugin.logger.debug(f'fix_recv\t{socket:x}\t{original_hash}=>{new_hash}')
                if rtn_size > size:
                    self.buffers[socket] = rtn[size:]
                    rtn_size = size
                # elif processor.buffer:
                #     rtn_size = rtn_size - min(10, rtn_size - 1)
                #     self.buffers[socket] = rtn[rtn_size:]
                try:
                    memmove(buffer, (c_char * rtn_size).from_buffer(rtn), size)
                except OSError as e:
                    self.plugin.logger.error(f"{e} at writing to recv buffer from socket {socket:x}")
                    return -1
            if RECV_DEBUG: self.plugin.logger('finish recv', hex(socket), rtn_size)
            return rtn_size
