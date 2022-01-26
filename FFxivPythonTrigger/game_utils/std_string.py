from ctypes import *
from FFxivPythonTrigger.memory import BASE_ADDR
from FFxivPythonTrigger.text_pattern import find_signature_address

sigs = {
    "StdStringInitialize": {
        'call': find_signature_address,
        'param': "48 89 5C 24 08 48 89 74 24 10 57 48 83 EC 20 48 8D 41 22 66 C7 41 20 01 01 48 89 01 49 8B D8",
        'add': BASE_ADDR,
    },
    "StdStringDeallocate": {
        'call': find_signature_address,
        'param': "80 79 21 00 75 12 48 8B 51 08 41 B8 33 00 00 00 48 8B 09 E9 ?? ?? ?? 00 C3",
        'add': BASE_ADDR,
    }
}
std_string_initialize_interface = CFUNCTYPE(
    c_void_p,  # std_string_ptr
    *[
        c_void_p,  # std_string_ptr
        c_void_p,  # char_p
        c_uint,  # length
    ]
)
std_string_deallocate_interface = CFUNCTYPE(
    c_void_p,
    *[
        c_void_p,  # std_string_ptr
    ]
)

# set as real func when fpt initialized
_std_string_initialize = lambda std_string_ptr, char_p, length: None
_std_string_deallocate = lambda std_string_ptr: None


class StdString(c_ubyte * 256):
    def __init__(self, content: str | bytes):
        super().__init__()
        if isinstance(content, str): content = content.encode('utf-8')
        self.content = content
        self.length = len(content)
        _std_string_initialize(byref(self), c_char_p(content), self.length)

    def __del__(self):
        _std_string_deallocate(byref(self))
