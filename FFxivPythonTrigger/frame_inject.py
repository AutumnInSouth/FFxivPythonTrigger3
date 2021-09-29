from ctypes import *
from queue import Queue
from traceback import format_exc
from time import perf_counter
from inspect import getfile, getsourcelines

from .logger import Logger
from .hook import Hook
from .text_pattern import find_unique_signature_address
from .memory import BASE_ADDR

MISSION_TIME_LIMIT = 0.05

sig = {
    'call': find_unique_signature_address,
    'param': "4C 8B DC 53 56 48 81 EC 18 02 00 00 48 8B 05",
    'add': BASE_ADDR,
}


class FrameInjectHook(Hook):
    _continue_works = dict()
    _once_works = Queue()

    def __init__(self, func_address: int):
        super().__init__(func_address)
        self.logger = Logger("Frame Inject")

    def register_continue_call(self, call, *args, **kwargs):
        self._continue_works[call] = (args, kwargs)

    def unregister_continue_call(self, call):
        try:
            del self._continue_works[call]
        except KeyError:
            pass

    def register_once_call(self, call, *args, **kwargs):
        self._once_works.put((call, args, kwargs))

    argtypes = [c_void_p, c_void_p]

    def call(self, call, *args, **kwargs):
        start = perf_counter()
        call(*args, **kwargs)
        use = perf_counter() - start
        if use > MISSION_TIME_LIMIT:
            self.logger.warning(f"frame mission over time {use:.2f}s (limit:{MISSION_TIME_LIMIT:.2f}s):")
            try:
                self.logger.warning(f"at:\t{getfile(call)}:{getsourcelines(call)[1]}")
            except:
                pass

    def hook_function(self, *oargs):
        try:
            while not self._once_works.empty():
                try:
                    call, a, k = self._once_works.get(False)
                    self.call(call, *a, **k)
                except Exception:
                    self.logger.error("error in frame call:\n" + format_exc())
            for c, v in self._continue_works.copy().items():
                try:
                    self.call(c, *v[0], **v[1])
                except Exception:
                    del self._continue_works[c]
                    self.logger.error("error in frame call, continue work will be removed:\n" + format_exc())
        except Exception:
            self.logger.error("error in frame inject:\n" + format_exc())
        return self.original(*oargs)
