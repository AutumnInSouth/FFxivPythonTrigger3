from itertools import chain

from idc import *
from idaapi import *
from idautils import *

min_ea = inf_get_min_ea()
max_ea = inf_get_max_ea()


def sig_search(sig: str, max_search_cnt: int = 10):
    addr = min_ea
    while max_search_cnt > 0:
        addr = find_binary(addr, max_ea, sig, 16, SEARCH_DOWN | SEARCH_NEXT)
        if addr == BADADDR: break
        yield addr
        max_search_cnt -= 1


def find_xrefs(ea: int) -> dict:
    xrefs = {}
    for xref in XrefsTo(ea, 0):
        xrefs.setdefault(xref.type, []).append(xref.frm)
    return xrefs


find_address = set()


def find_values(ea: int, depth=0):
    for xref in XrefsTo(ea, 0):
        _ea = xref.frm
        if get_operand_value(_ea, 1) == 321:
            find_address.add(_ea)
        elif depth > 0:
            find_values(_ea, depth - 1)


for addr in sig_search("48 89 5C 24 ? 48 89 6C 24 ? 57 48 83 EC ? 48 63 C2 48 8B D9"):
#for addr in sig_search("48 89 5C 24 ? 56 41 56 41 57 48 83 EC ? 48 63 C2"):
    xrefs = find_xrefs(addr)
    for addr in chain(xrefs.get(19, []), xrefs.get(17, [])):
        find_values(addr, 10)
for a in find_address:
    print(hex(a), f"ffxiv_dx11.exe + {a - 0x140000000:x}")
print("Done")
