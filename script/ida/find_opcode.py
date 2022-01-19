from functools import cache

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


def process_refs(ea):
    xrefs = find_xrefs(ea)
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
        values = process_refs(eas[0])
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
            values = process_refs(get_func(ea).start_ea)
        except Exception as e:
            print(f"[!] {name}: {e}")
        else:
            print(f"[+] {name}: {'|'.join(map(hex, values))}")


def find_actor_control():
    try:
        eas = list(sig_search("40 55 53 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ?"
                              " 48 8B 05 ? ? ? ? 48 33 C4 48 89 85 ? ? ? ? 44 8B BD ? ? ? ?"))
        if len(eas) != 1: raise Exception(f"Error: found {len(eas)} addresses for actor_control main")
        all_values = list(process_refs(eas[0]))
    except Exception as e:
        print(f"[!] actor_control main: {e}")
        return

    for name, sig in {
        "ActorControl": "B8 ? ? ? ? 0F B7 13",
        "ActorControlSelf": "0F B7 13 B8 ? ? ? ?",
    }.items():
        try:
            eas = list(sig_search(sig))
            if len(eas) != 1: raise Exception(f"Error: found {len(eas)} addresses for {name}")
            values = find_switch_values(eas[0])
            if not values: raise Exception("No switch values near xrefs")
        except Exception as e:
            print(f"[!] {name}: {e}")
        else:
            for v in values: all_values.remove(v)
            print(f"[+] {name}: {'|'.join(map(hex, values))}")
    if len(all_values) != 1:
        print(f"[!] ActorControlTarget: remain {len(all_values)} values")
    else:
        print(f"[+] ActorControlTarget: {hex(all_values[0])}")


def find_actor_cast():
    eas = list(sig_search("40 55 56 48 81 EC ? ? ? ? 48 8B EA"))
    try:
        if len(eas) != 1: raise Exception("Error: found %d addresses" % len(eas))
        values = process_refs(eas[0])
    except Exception as e:
        print(f"[!] ActorCast: {e}")
    else:
        print(f"[+] ActorCast: {'|'.join(map(hex, values))}")


def find_craft_status():
    eas = list(sig_search("49 8B C1 48 C1 E8 ? 83 E0 ?"))
    try:
        if len(eas) != 1: raise Exception("Error: found %d addresses" % len(eas))
        values = find_switch_values(eas[0])
        if not values: raise Exception("No switch values near xrefs")
    except Exception as e:
        print(f"[!] CraftStatus: {e}")
    else:
        print(f"[+] CraftStatus: {'|'.join(map(hex, values))}")


def find_map_effect():
    eas = list(sig_search("48 89 5C 24 ? 57 48 83 EC ? 48 8B F9 48 8B DA 48 8B 89 58 01 00 00 48 85 C9 74 ? "
                          "48 8B 01 FF 50 ? 84 C0 74 ? 48 8B 8F ? ? ? ? 8B 03 48 8B 91 ? ? ? ? 39 02 75 ? 48 83 B9"))
    try:
        if len(eas) != 1: raise Exception("Error: found %d addresses" % len(eas))
        values = sum((list(process_refs(get_func(ea).start_ea)) for ea in find_xrefs(eas[0])[19]),start = [])
    except Exception as e:
        print(f"[!] MapEffect: {e}\n{traceback.format_exc()}")
    else:
        print(f"[+] MapEffect: {'|'.join(map(hex, values))}")

def find_effect_result():
    try:
        eas = list(sig_search("0F B6 ? ? 48 8D 8E ? ? ? ? E8 ? ? ? ? 8B"))
        if len(eas) != 1: raise Exception("Error: found %d addresses" % len(eas))
        values = process_refs(get_func(eas[0]).start_ea)
    except Exception as e:
        print(f"[!] EffectResult: {e}")
    else:
        print(f"[+] EffectResult: {'|'.join(map(hex, values))}")


if __name__ == "__main__":
    find_actor_cast()
    find_effect()
    find_aoe_effects()
    find_actor_control()
    find_craft_status()
    find_map_effect()
    find_effect_result()
    print('done')
