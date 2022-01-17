from idc import *
from idaapi import *
from idautils import *

test_sig = "E8 ? ? ? ? B0 ? 48 8B 5C 24 ? 48 8B 74 24 ? 48 83 C4 ? 5F C3 48 8B CB " \
           "E8 ? ? ? ? B0 ? 48 8B 5C 24 ? 48 8B 74 24 ? 48 83 C4 ? 5F C3 0F B6 43 ?"

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


def _find_switch_values(_si: int, ea: int):
    si = ida_nalt.switch_info_t()
    if ida_nalt.get_switch_info(si, _si):
        results = calc_switch_cases(_si, si)
        for idx in range(len(results.cases)):
            if results.targets[idx] == ea:
                cases = results.cases[idx]
                return [cases[idx] for idx in range(len(cases))]
    return []


def find_switch_values(ea: int):
    xrefs = find_xrefs(ea)
    while True:
        if 19 in xrefs:
            res = sum((_find_switch_values(si, ea) for si in xrefs[19]), [])
            if res:
                return sorted(set(res))
            else:
                res = sum((find_switch_values(_ea) for _ea in xrefs[19]), [])
        else:
            res = []

        if 21 in xrefs:
            res = sum((find_switch_values(_ea) for _ea in xrefs[21]), res)

        return sorted(set(res))


def process_refs(xrefs):
    if 17 not in xrefs:
        raise Exception("No call near xrefs")
    else:
        values = set(sum(map(find_switch_values, xrefs[17]), []))
        if not values:
            raise Exception("No switch values near xrefs")
        else:
            return values


def find_effect():
    eas = list(sig_search("48 89 5C 24 ? 57 48 83 EC ? 48 8B 05 ? ? ? ? 48 33 C4 48 89 44 24 ? 48 8B DA 8B F9"))
    try:
        if len(eas) != 1: raise Exception("Error: found %d addresses for Effect" % len(eas))
        values = process_refs(find_xrefs(eas[0]))
    except Exception as e:
        print(f"[!] Effect: {e}")
    else:
        print(f"[+] Effect: {'|'.join(map(hex, values))}")


def find_aoe_effects():
    for ea in sig_search("48 8D 93 ?? ?? ?? ?? 48 8D 4C 24 ?? E8 ?? ?? ?? ?? 8B 15 ?? ?? ?? ??"):
        match get_operand_value(ea, 1):
            case 0x270:
                l = 8
            case 0x4b0:
                l = 16
            case 0x6f0:
                l = 24
            case 0x930:
                l = 32
            case v:
                print(f"[!] AoeEffect: Unknown value {v:#X} at {ea:#X}")
                continue
        name = f"AoeEffect{l}"
        try:
            values = process_refs(find_xrefs(get_func(ea).start_ea))
        except Exception as e:
            print(f"[!] {name}: {e}")
        else:
            print(f"[+] {name}: {'|'.join(map(hex, values))}")


if __name__ == "__main__":
    find_effect()
    find_aoe_effects()
    print('done')
