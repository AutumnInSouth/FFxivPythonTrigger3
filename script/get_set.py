from typing import Optional, Callable


class BindVal:
    def __init__(self, key: Optional[str] = None, default: any = None, on_change: Callable[[any, any], bool] = None):
        self.key = key
        self.default = default
        self.on_change = on_change

    def init(self, obj: Optional['Parent']):
        self.__set__(obj, self.default)

    def __get__(self, obj: Optional['Parent'], obj_type=None):
        return self if obj is None else obj.bind_val.setdefault(self.key, self.default)

    def __set__(self, obj, value):
        if self.on_change is None or self.on_change(obj, value):
            obj.bind_val[self.key] = value

    @classmethod
    def decorate(cls, default=None):
        def wrapper(func: Callable[[any, any], bool]):
            return cls(key=func.__name__, default=default, on_change=func)

        return wrapper


class Parent(object):
    def __init__(self):
        self.bind_val = {}
        cls = self.__class__
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if isinstance(attr, BindVal):
                if attr.key is None:
                    attr.key = attr_name
                attr.init(self)

    flagA = BindVal(default="flagA!")

    @BindVal.decorate(default=65535)
    def flagX(self, new_val):
        print("new val of flag x:", new_val)
        return True


parent = Parent()
print(parent.bind_val)
print(parent.flagA, parent.flagX, parent.bind_val)
parent.flagA = "flagB?"
parent.flagX = 0x1234
print(parent.flagA, parent.flagX, parent.bind_val)
print(getattr(parent,"flagX"))
