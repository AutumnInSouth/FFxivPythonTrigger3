import re

import pefile

from .memory import PROCESS_FILENAME


def wild_card(count: int):
    if not count:
        return b''
    ans = b"(?:.|\\n)"
    if count > 1:
        ans += ("{" + str(count) + "}").encode()
    return ans


def sig_to_pattern(sig: str):
    ans = bytearray()
    flag1 = False
    wild_card_counter = 0
    offset = []
    i = 0
    for i, s in enumerate(sig.split(' ')):
        if not s:
            raise Exception(f'Bad at sig[{i}]')
        if s.startswith('*'):
            if not flag1:
                ans += wild_card(wild_card_counter)
                wild_card_counter = 0
                ans += b'('
                flag1 = True
        elif flag1:
            ans += wild_card(wild_card_counter)
            wild_card_counter = 0
            ans += b')'
            flag1 = False
            offset.append(i)
        if flag1 or s.startswith('?'):
            wild_card_counter += 1
        else:
            if wild_card_counter:
                ans += wild_card(wild_card_counter)
                wild_card_counter = 0
            temp = int(s, 16)
            if temp in special_chars_map:
                ans += b'\\'
            ans.append(temp)
    ans += wild_card(wild_card_counter)
    if flag1:
        ans += b')'
        offset.append(i + 1)
    return bytes(ans), offset


def get_text_section(pe):
    for sect in pe.sections:
        if sect.Name.rstrip(b'\0') == b'.text':
            return sect


def _search_from_text(pattern: bytes):
    return [(
        match.span()[0] + section_virtual_address,
        [int.from_bytes(g, byteorder='little', signed=True) for g in match.groups()]
    ) for match in re.finditer(bytes(pattern), section_data)]


def search_from_text(sig: str):
    pattern, offsets = sig_to_pattern(sig)
    return [(
        address, [g + offsets[i] for i, g in enumerate(groups)]
    ) for address, groups in _search_from_text(pattern)]


def find_signature_address(signature: str, unique=True):
    data = search_from_text(signature)
    if unique and len(data) != 1:
        raise ValueError(f"Signature is not unique, {len(data)} results found")
    return data[0][0]


def find_signature_point(signature: str, unique=True):
    data = search_from_text(signature)
    if unique and len(data) != 1:
        raise ValueError(f"Signature is not unique, {len(data)} results found")
    address, offsets = data[0]
    if len(offsets) != 1:
        raise ValueError(f"Bad Signature, {len(offsets)} offsets found in signature")
    return offsets[0] + address


def get_original_text(offset: int, length: int):
    start = offset - section_virtual_address
    return section_data[start:start + length]


special_chars_map = {i for i in b'()[]{}?*+-|^$\\.&~# \t\n\r\v\f'}
section = get_text_section(pefile.PE(PROCESS_FILENAME, fast_load=True))
section_data = section.get_data()
section_virtual_address = section.VirtualAddress
