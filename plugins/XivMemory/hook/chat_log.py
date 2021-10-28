from ctypes import *
from datetime import datetime
from functools import cache, cached_property
from struct import pack
from traceback import format_exc

from FFxivPythonTrigger import EventBase, process_event
from FFxivPythonTrigger.hook import PluginHook

from ..se_string import ChatLog


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
        return f"chatlog|{self.channel_id:X}|{self.player.replace('|', '│')}|{self.message.replace('|', '│')}"

    def text(self):
        return "{}\t{}\t{}\t{}".format(self.time, self.channel_id, self.player or 'n/a', self.message)


class ChatLogHook(PluginHook):
    restype = c_int64
    argtypes = [c_int64, POINTER(c_ubyte), c_int]
    auto_install = True

    def hook_function(self, a1, buffer, size):
        try:
            process_event(ChatLogEvent(ChatLog.from_buffer(bytearray(buffer[:size]))))
        except Exception:
            self.plugin.logger.error(format_exc())
        return self.original(a1, buffer, size)
