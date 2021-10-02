import ctypes
import re
from typing import Callable, Union, TYPE_CHECKING, Optional

from .hook import Hook

if TYPE_CHECKING:
    from .ffxiv_python_trigger import PluginBase, EventBase

re_pattern = Union[str, re.Pattern]

ConditionType = Union[str, Callable[[], bool]]
ReEventType = Callable[['PluginBase', 'EventBase', 're.Match'], any]
EventType = Callable[['PluginBase', 'EventBase'], any]


class ReEventCall(object):
    def __init__(
            self,
            pattern: re_pattern,
            func: Optional[ReEventType],
            limit_sec: float = 0.1,
            condition: Optional[ConditionType] = None
    ):
        self.pattern = pattern if isinstance(pattern, re.Pattern) else re.compile(pattern)
        self.func = func
        self.limit_sec = limit_sec
        self.condition = condition

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self

        if self.condition is None:
            def callback(evt: 'EventBase' = None, match: re.Match = None):
                self.func(obj, evt, match)
        else:
            condition = getattr(obj, self.condition) if isinstance(self.condition, str) else self.condition

            def callback(evt: 'EventBase' = None, match: re.Match = None):
                if condition():
                    self.func(obj, evt, match)

        callback.__name__ = self.func.__name__
        return callback


class EventCall(object):
    def __init__(
            self,
            event_id: any,
            func: Optional[EventType],
            limit_sec: float = 0.1,
            condition: Optional[ConditionType] = None
    ):
        self.event_id = event_id
        self.func = func
        self.limit_sec = limit_sec
        self.condition = condition

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self

        if self.condition is None:
            def callback(evt: 'EventBase' = None):
                self.func(obj, evt)
        else:
            condition = getattr(obj, self.condition) if isinstance(self.condition, str) else self.condition

            def callback(evt: 'EventBase' = None):
                if condition():
                    self.func(obj, evt)

        callback.__name__ = self.func.__name__
        return callback


def re_event(pattern: re_pattern, limit_sec: float = 0.1, condition: Optional[ConditionType] = None):
    def decorator(func: ReEventType):
        return ReEventCall(pattern=pattern, func=func, limit_sec=limit_sec, condition=condition)

    return decorator


def event(event_id: any, limit_sec: float = 0.1, condition: Optional[ConditionType] = None):
    def decorator(func: EventType):
        return EventCall(event_id=event_id, func=func, limit_sec=limit_sec, condition=condition)

    return decorator


def unload_callback(callback: Union[str, Callable]):
    def decorator(func):
        def wrapper(self: 'PluginBase', plugin: 'PluginBase', *args, **kwargs):
            _callback = getattr(self, callback) if isinstance(callback, str) else callback
            plugin.controller.unload_callback.append((_callback, args, kwargs))
            return func(self, *args, **kwargs)

        return wrapper

    return decorator


class BindValue(object):
    def __init__(
            self,
            key: str,
            on_change: Optional[Callable] = None,
            default=None,
            do_save=True,
            auto_save=False,
    ):
        self.key = key
        self.default = default
        self.on_change = on_change
        self.do_save = do_save
        self.auto_save = auto_save

    def __get__(self, instance: 'PluginBase', owner):
        return self if instance is None else instance.controller.bind_values[self.key]

    def __set__(self, instance: 'PluginBase', value):
        if self.on_change is None or self.on_change(instance, value):
            if self.do_save:
                instance.storage.data.setdefault(instance.bind_values_store_key, dict())[self.key] = value
                if self.auto_save:
                    instance.storage.save()
            instance.controller.bind_values[self.key] = value


def bind_value(**kwargs):
    def decorator(func):
        return BindValue(func.__name__, on_change=func, **kwargs)

    return decorator


class PluginHook(Hook):
    auto_install: bool

    def __init__(self, plugin: 'PluginBase', func_address: int):
        super().__init__(func_address)
        self.plugin = plugin
        if self.auto_install:
            if plugin.controller.started:
                self.install_and_enable()
            else:
                plugin.controller.hook_to_start.append(self)

    def install(self):
        super(PluginHook, self).install()
        self.plugin.controller.installed_hooks.append(self)

    def uninstall(self):
        super(PluginHook, self).uninstall()
        try:
            self.plugin.controller.installed_hooks.remove(self)
        except ValueError:
            pass


def plugin_hook(_restype=ctypes.c_void_p, _argtypes: Optional[list] = None, _auto_install: bool = False):
    if _argtypes is None:
        _argtypes = []

    def decorator(func):
        class _PluginHook(PluginHook):
            auto_install = _auto_install
            argtypes = _argtypes
            restype = _restype

            def hook_function(self, *args):
                return func(self.plugin, self, *args)

        return _PluginHook

    return decorator
