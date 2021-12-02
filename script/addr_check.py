import json
import pathlib
import pefile
import sys

from FFxivPythonTrigger import text_pattern

path = r"D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game\ffxiv_dx11.exe"
text_pattern.section = text_pattern.get_text_section(pefile.PE(path, fast_load=True))
text_pattern.section_data = text_pattern.section.get_data()
text_pattern.section_virtual_address = text_pattern.section.VirtualAddress

souce_path = pathlib.Path(__file__).parent.parent / 'AppData' / 'Address' / 'data.json'
with open(souce_path, 'r', encoding='utf-8') as fo:
    source = json.load(fo)['2021.10.26.0000.0000']
    for module, addrs in source.items():
        for addr_key, addr_data in addrs.items():
            ans = text_pattern.search_from_text(addr_data['param'])
            if len(ans) != 1:
                #print to stderr
                print('*>>', module, addr_key, ans,file=sys.stderr,flush=True)
            else:
                print('>>', module, addr_key, ans[0])
