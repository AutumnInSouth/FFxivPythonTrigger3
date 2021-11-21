from _ctypes import Array
from ctypes import *
from functools import cache, cached_property
from inspect import isclass
from json import JSONEncoder, JSONDecodeError
from typing import Type, List, Tuple, Dict

from . import read_pointer_shift, read_memory


def get_data(data, full=False):
    if isinstance(data, _OffsetStruct):
        return {k: get_data(v, full) for k, v in (data.get_full_item if full else data.get_item)()}
    if isinstance(data, _EnumStruct):
        return data.value
    if isinstance(data, Array):
        return [get_data(i, full) for i in data]
    return data


def obj_set_item(obj, _t, key, val):
    if isclass(_t):
        if issubclass(_t, _OffsetStruct):
            obj[key] = _t.from_dict(val)
            return
        elif issubclass(_t, Array):
            _bt = _t._type_
            for i, v in enumerate(val):
                obj_set_item(obj[key], _t._type_, i, v)
            return
        elif issubclass(_t, _EnumStruct):
            obj[key].value = val
            return
    obj[key] = val


def obj_set_attr(obj, _t, key, val):
    if isclass(_t):
        if issubclass(_t, _OffsetStruct):
            return setattr(obj, key, _t.from_dict(val))
        elif issubclass(_t, Array):
            _bt = _t._type_
            for i, v in enumerate(val):
                obj_set_item(getattr(obj, key), _t._type_, i, v)
            return
        elif issubclass(_t, _EnumStruct):
            getattr(obj, key).value = val
            return
    setattr(obj, key, val)


class _OffsetStruct(Structure):
    _pack_ = 1
    raw_fields: Dict[str, Tuple[any, int]] = None
    struct_size = 0

    @cache
    def _properties(self):
        return [k for k, v in type(self).__dict__.items() if not k.startswith('_') and isinstance(v, (property, cached_property))]

    @classmethod
    def from_dict(cls, data: dict):
        new_obj = cls()
        for key, _t in cls._fields_:
            if key in data:
                obj_set_attr(new_obj, _t, key, data[key])
        return new_obj

    def __str__(self):
        return str(get_data(self))

    def get_data(self, full=False):
        return get_data(self, full)

    def get_full_item(self):
        for k, _ in self._fields_:
            yield k, getattr(self, k)
        for k in self._properties():
            yield k, getattr(self, k)

    def get_item(self):
        for k in self.raw_fields.keys():
            if not k.startswith('_'):
                yield k, getattr(self, k)
        for k in self._properties():
            yield k, getattr(self, k)

    def __hash__(self):
        return addressof(self)


def _(res) -> Tuple[any, int]:
    return (res[0], res[1]) if type(res) == tuple else (res, -1)


def pad_unk(current: int, target: int, max_pad_length: int = 4):
    remain = target - current
    if current % 2 or remain == 1 or max_pad_length == 1: return c_ubyte, 1, "byte"
    if current % 4 or remain < 4 or max_pad_length == 2: return c_ushort, 2, "ushort"
    return c_uint, 4, "uint"


def OffsetStruct(fields: dict, full_size: int = None, name=None, max_pad_length: int = 4) -> Type[_OffsetStruct]:
    set_fields = []
    current_size = 0
    for name, data in sorted(fields.items(), key=lambda x: _(x[1])[1]):
        d_type, offset = _(data)
        if offset < 0: offset = current_size
        if current_size > offset:
            raise Exception(f"block [{name}] is invalid {current_size}/{offset}")
        while current_size < offset:
            t, s, n = pad_unk(current_size, offset, max_pad_length)
            set_fields.append((f"_{n}_{hex(current_size)}", t))
            current_size += s
        data_size = sizeof(d_type)
        set_fields.append((name, d_type))
        current_size += data_size
    if full_size is not None:
        if full_size < current_size:
            raise Exception("full size is smaller than current size")
        while current_size < full_size:
            t, s, n = pad_unk(current_size, full_size, max_pad_length)
            set_fields.append((f"_{n}_{hex(current_size)}", t))
            current_size += s
    return type(
        (name or f"OffsetStruct_{current_size:#X}"),
        (_OffsetStruct,),
        {'raw_fields': fields, '_fields_': set_fields, 'struct_size': current_size}
    )


class _OffsetStructJsonEncoder(JSONEncoder):
    def default(self, data):
        if isinstance(data, _OffsetStruct):
            _data = {}
            for k, v in data.get_item():
                try:
                    _data[k] = self.default(v)
                except JSONDecodeError:
                    pass
            data = _data
        elif isinstance(data, _EnumStruct):
            data = data.value
        elif isinstance(data, Array):
            _data = []
            for v in data:
                try:
                    _data.append(self.default(v))
                except JSONDecodeError:
                    _data.append(None)
            data = _data
        return super().default(data)


OffsetStructJsonEncoder = _OffsetStructJsonEncoder()


class _PointerStruct(c_void_p):
    shifts: List[int] = []
    d_type = c_void_p
    _fields_ = [('base', c_ulonglong)]

    def __getattr__(self, item):
        return getattr(self.value, item)

    @property
    def value(self):
        address = read_pointer_shift(addressof(self), self.shifts)
        return read_memory(self.d_type, address) if address else None


def PointerStruct(i_d_type: any, *i_shifts: int, name=None) -> Type[_PointerStruct]:
    return type((name or "PointerStruct"), (_PointerStruct,), {
        'shifts': i_shifts,
        'd_type': i_d_type,
    })


class _EnumStruct(Structure):
    _default: any
    _data: dict
    _reverse: dict
    raw_value: int

    def __eq__(self, other):
        return self.raw_value == other or self.value == other

    @property
    def value(self):
        try:
            return self._data[self.raw_value]
        except KeyError:
            return self.raw_value if self._default is None else self._default

    @value.setter
    def value(self, value):
        try:
            self.raw_value = self._reverse[value]
        except KeyError:
            self.raw_value = value


def EnumStruct(raw_type: any, enum_data: dict, default=None, name=None) -> Type[_EnumStruct]:
    return type((name or "EnumStruct"), (_EnumStruct,), {
        '_default': default,
        '_data': enum_data,
        '_reverse': {v: k for k, v in enum_data.items()},
        '_fields_': [('raw_value', raw_type)],
    })
