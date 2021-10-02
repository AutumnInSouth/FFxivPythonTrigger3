from ctypes import *
from datetime import datetime
from functools import cache
from traceback import format_exc

from FFxivPythonTrigger import EventBase, PluginBase, process_event
from FFxivPythonTrigger.address_manager import AddressManager
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import read_memory
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from .chat_log import ChatLog

sig = "48 89 ? ? ? 48 89 ? ? ? 48 89 ? ? ? 57 41 ? 41 ? 48 83 EC ? 48 8B ? ? 48 8B ? 48 2B ? ? 4C 8B"


class ChatLogTable(OffsetStruct({
    'count': (c_ulong, 5 * 4),
    'check_update': (c_ulonglong, 5 * 8),
    'lengths': (POINTER(c_uint), 9 * 8),
    'data': (POINTER(c_ubyte), (12 * 8))
})):
    def get_raw(self, idx: int):
        if idx < 0:
            idx = self.count + idx
        if not max(-1, self.count - 1000) < idx < self.count:
            raise IndexError('list index %s out of range' % idx)
        idx %= 1000
        start = self.lengths[idx - 1] if idx > 0 else 0
        return bytearray(self.data[start:self.lengths[idx]])

    def get(self, idx: int):
        return ChatLog.from_buffer(self.get_raw(idx))


class ChatLogEvent(EventBase):
    id = "log_event"
    name = "log event"

    def __init__(self, chat_log: ChatLog):
        self.time = datetime.fromtimestamp(chat_log.timestamp)
        self.channel_id = chat_log.channel_id
        self.player = chat_log.sender_text
        self.message = chat_log.messages_text
        self.chat_log = chat_log

    @cache
    def str_event(self):
        return f"00:{self.channel_id:X}:{self.player.replace(':', '：')}:{self.message.replace(':', '：')}"

    def text(self):
        return "{}\t{}\t{}\t{}".format(self.time, self.channel_id, self.player or 'n/a', self.message)


class ChatLogPlugin(PluginBase):
    name = "ChatLog"

    def __init__(self):
        super(ChatLogPlugin, self).__init__()

        self.chat_log = None
        self.LogHook(self, AddressManager(self.name, self.logger).scan_address("hook addr", sig))

    @PluginHook.decorator(_restype=c_int64, _argtypes=[c_int64, POINTER(c_ubyte), c_int], _auto_install=True)
    def LogHook(self, hook, a1, buffer, size):
        try:
            if self.chat_log is None: self.chat_log = read_memory(ChatLogTable, a1 - 72)
            process_event(ChatLogEvent(ChatLog.from_buffer(bytearray(buffer[:size]))))
        except Exception:
            self.logger.error(format_exc())
        return hook.original(a1, buffer, size)
