import re


def fix(s: str):
    return re.sub(r"(?P<k>[A-Z])", "_\g<k>", s).lower().strip('_')


d = """
    'index': c_uint,
    'unk0': c_uint,
    'container_id': c_ushort,
    'slot': c_ushort,
    'count': c_uint,
    'item_id': c_uint,
    'reserved_flag': c_uint,
    'signature_id': c_ulonglong,
    'quality': c_ubyte,
    'attribute2': c_ubyte,
    'condition': c_ushort,
    'spiritbond': c_ushort,
    'stain': c_ushort,
    'glamour_catalog_id': c_ushort,
    'unk6': c_ushort,
    'materia1': c_ushort,
    'materia2': c_ushort,
    'materia3': c_ushort,
    'materia4': c_ushort,
    'materia5': c_ushort,
    'materia1_tier': c_ubyte,
    'materia2_tier': c_ubyte,
    'materia3_tier': c_ubyte,
    'materia4_tier': c_ubyte,
    'materia5_tier': c_ubyte,
    'unk10': c_ubyte,
    'unk11': c_uint,
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
