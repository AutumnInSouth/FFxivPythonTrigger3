import random
import re
import string
import threading
import time
from traceback import format_exc
from typing import Callable

from ..logger import error


class Counter(object):
    def __init__(self):
        self.current = 0
        self._lock = threading.Lock()

    def get(self):
        with self._lock:
            self.current += 1
            return self.current

    def reset(self):
        with self._lock:
            self.current = 0


class WaitTimeoutException(Exception):
    def __init__(self):
        super(WaitTimeoutException, self).__init__("Wait Timeout")


def wait_until(statement: Callable[[], any], timeout: float = None, period: float = 0.1):
    temp = statement()
    start = time.perf_counter()
    while temp is None:
        if timeout is not None and time.perf_counter() - start >= timeout:
            raise WaitTimeoutException()
        time.sleep(period)
        temp = statement()
    return temp


def err_catch(func):
    def warper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            error('error_catch', format_exc())

    return warper


utf8_remove = re.compile(r'(\a|\b|\f|\n|\r|\t|\v|[\x01-\x1F])')


def utf8_clean_up(string_bytes: bytes):
    return utf8_remove.sub("", string_bytes.decode('utf-8', errors='ignore'))


def rand_char(length=16):
    return ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(length))
