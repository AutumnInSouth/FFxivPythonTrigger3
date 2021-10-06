import time
from threading import Lock


class Ping(object):
    def __init__(self):
        self.is_send = False
        self._ping = 0
        self.last_send = time.perf_counter()
        self.lock = Lock()

    def get(self):
        if self.is_send:
            return max(self._ping, time.perf_counter() - self.last_send)
        else:
            return self._ping

    def set(self, is_send: bool):
        with self.lock:
            if is_send != self.is_send:
                if is_send:
                    self.last_send = time.perf_counter()
                else:
                    self._ping = time.perf_counter() - self.last_send
                self.is_send = is_send
                return 1
            return 0
