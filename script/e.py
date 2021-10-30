import re


def fix(s: str):
    return re.sub(r"(?P<k>[A-Z])", "_\g<k>", s).lower().strip('_')


d = """
    'category': c_ushort,
    'padding0': c_ushort,
    'param1': c_uint,
    'param2': c_uint,
    'param3': c_uint,
    'param4': c_uint,
    'padding1': c_uint,
"""
#f = re.compile(r"['\"]([a-zA-Z0-9_]+)['\"]: \(([^,]+),(.*)\),?")
f = re.compile(r"['\"]([a-zA-Z0-9_]+)['\"]: ([^,]+)")
data = [search.groups() for search in [f.search(_line) for _line in d.split('\n')] if search]
#for name, v_type, offset in data:
for name, v_type in data:
    #print(f"'{name}': ({v_type}, {eval(offset):#x}),")
    if v_type in ['c_float']: v_type = 'float'
    elif v_type in ['c_uint','c_ushort','c_byte','c_int','c_short','c_ubyte',"c_ulonglong"]: v_type = 'int'
    elif v_type in ['c_bool']: v_type = 'bool'
    print(f"{name}: {v_type}")
