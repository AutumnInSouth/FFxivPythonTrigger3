from threading import Lock
from typing import TYPE_CHECKING
from .api import get_me_actor

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.actor_control_self import AcceptActionEvent
    from XivNetwork.message_processors.zone_server.actor_control import CastCancelEvent


class LastActionRecorder:
    def __init__(self):
        self._last_message_epoch = 0
        self._record_lock = Lock()
        self.last_action = None
        self._last_action_backup = None

    def on_accept_action(self, event: 'AcceptActionEvent'):
        if event.struct_message.param1 == 58: return
        with self._record_lock:
            if self._last_message_epoch != event.bundle_header.epoch:
                self._last_message_epoch = event.bundle_header.epoch
            else:
                return
            self._last_action_backup = self.last_action
            self.last_action = event.action_id

    def on_cast_cancel(self, event: 'CastCancelEvent'):
        if event.action_type != 1 or event.action_id != self.last_action: return
        me = get_me_actor()
        if me is None or event.target_id != me.id: return
        with self._record_lock:
            self.last_action = self._last_action_backup
            self._last_action_backup = None
