import re


def fix(s: str):
    return re.sub(r"(?P<k>[A-Z])", "_\g<k>", s).lower().strip('_')


d = """
    'action_2_id': (c_uint, 0x1c),
    'action_1_id': (c_uint, 0x20),
    'action_1_cool_down_duration': (c_float, 0x34),
    'action_1_cool_down_total': (c_float, 0x38),
    'action_2_cool_down_duration': (c_float, 0x48),
    'action_2_cool_down_total': (c_float, 0x4c),
    'action_1_remain': (c_ubyte, 0x54),
    'action_2_remain': (c_ubyte, 0x55),
    'remain_time': (c_float, 0x90),
"""
f = re.compile(r"['\"]([a-zA-Z0-9_]+)['\"]: \(([^,]+),(.*)\),?")
data = [search.groups() for search in [f.search(_line) for _line in d.split('\n')] if search]
for name, v_type, offset in data:
    #print(f"'{name}': ({v_type}, {eval(offset):#x}),")
    if v_type in ['c_float']: v_type = 'float'
    elif v_type in ['c_uint','c_ushort','c_byte','c_int','c_short','c_ubyte']: v_type = 'int'
    elif v_type in ['c_bool']: v_type = 'bool'
    print(f"{name}: {v_type}")
