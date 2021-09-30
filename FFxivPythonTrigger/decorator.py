import re
from typing import Callable, Union, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .ffxiv_python_trigger import PluginBase

re_pattern = Union[str, re.Pattern]


class ReEventCall(object):
    def __init__(self, pattern: re_pattern, func: Callable, limit_sec: float):
        self.pattern = pattern if isinstance(pattern, re.Pattern) else re.compile(pattern)
        self.func = func
        self.limit_sec = limit_sec

    def __get__(self, obj, obj_type=None):
        return self if obj is None else lambda evt=None, match=None: self.func(obj, evt, match)


class EventCall(object):
    def __init__(self, event_id: any, func: Callable, limit_sec: float):
        self.event_id = event_id
        self.func = func
        self.limit_sec = limit_sec

    def __get__(self, obj, obj_type=None):
        return self if obj is None else lambda evt=None: self.func(obj, evt)


def re_event(pattern: re_pattern, limit_sec: float = 0.1):
    def decorator(func: Callable):
        return ReEventCall(pattern, func, limit_sec)

    return decorator


def event(event_id: any, limit_sec: float = 0.1):
    def decorator(func: Callable):
        return EventCall(event_id, func, limit_sec)

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
