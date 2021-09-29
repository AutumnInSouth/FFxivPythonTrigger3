from ctypes import *
from typing import Optional

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct

from .actor import Actor


class Target(OffsetStruct({
    "_current": (POINTER(Actor), 0x80),
    "_mouse_over": (POINTER(Actor), 0xD0),
    "_focus": (POINTER(Actor), 0xF8),
    "_previous": (POINTER(Actor), 0x110),
})):
    @property
    def current(self) -> Optional[Actor]:
        return self._current[0] if self._current else None

    @property
    def mouse_over(self) -> Optional[Actor]:
        return self._mouse_over[0] if self._mouse_over else None

    @property
    def focus(self) -> Optional[Actor]:
        return self._focus[0] if self._focus else None

    @property
    def previous(self) -> Optional[Actor]:
        return self._previous[0] if self._previous else None

    @current.setter
    def current(self, actor=None):
        self._current = pointer(actor) if actor is not None else None

    @focus.setter
    def focus(self, actor=None):
        self._focus = pointer(actor) if actor is not None else None


class Movement(OffsetStruct({
    "speed": (c_float, 68)
})):
    speed: float
