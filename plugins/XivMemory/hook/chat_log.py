import time
from ctypes import *
from datetime import datetime
from functools import cache
from traceback import format_exc

from FFxivPythonTrigger import EventBase, process_event
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.game_utils.std_string import StdString
from FFxivPythonTrigger.saint_coinach import item_names, realm

from ..se_string import ChatLog, get_message_chain

event_item_names = {row.key: row['Singular'] for row in realm.game_data.get_sheet('EventItem')}


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


def fix_chat_log(grouped_msg):
    fix = False
    for msg in grouped_msg:
        if msg.Type == "Interactable/Item":
            if msg.item_id in item_names:
                if msg.is_hq and msg.is_collect:
                    fix = True
                    msg._display_name = msg.display_name + "[item hq & collect]"
                    msg.is_collect = False
            elif msg.item_id in event_item_names:
                if msg.is_hq or msg.is_collect:
                    msg._display_name = msg.display_name + f"[evt_item hq:{msg.is_hq} collect:{msg.is_collect}]"
                    fix = True
                    msg.is_collect = False
                    msg.is_hq = False
            else:
                fix = True
                msg._display_name = msg.display_name + f"[未知的item_id:{msg.item_id}]"
                msg.item_id = 1
                msg.is_collect = False
                msg.is_hq = False
    return fix


class PrintChatLogHook(PluginHook):
    restype = c_int64
    argtypes = [c_int64, c_ushort, POINTER(c_char_p), POINTER(c_char_p), c_uint, c_ubyte]
    auto_install = True

    def hook_function(self, manager, channel_id, p_sender, p_msg, sender_id, parm):
        try:
            chat_log = ChatLog(
                int(time.time()),
                channel_id,
                get_message_chain(bytearray(p_sender[0])),
                get_message_chain(bytearray(p_msg[0]))
            )
            process_event(ChatLogEvent(chat_log))

            if fix_chat_log(chat_log.messages_grouped):
                self.plugin.logger.debug(f"a msg is fixed")
                new_msg = StdString(b''.join(m.encode_group() for m in chat_log.messages_grouped))
                p_msg = cast(addressof(new_msg), POINTER(c_char_p))

            if fix_chat_log(chat_log.sender_grouped):
                self.plugin.logger.debug(f"a sender is fixed")
                new_sender = StdString(b''.join(m.encode_group() for m in chat_log.sender_grouped))
                p_sender = cast(addressof(new_sender), POINTER(c_char_p))

        except:
            self.plugin.logger.error(format_exc())
        return self.original(manager, channel_id, p_sender, p_msg, sender_id, parm)
