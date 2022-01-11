from ctypes import *

from FFxivPythonTrigger.memory import BASE_ADDR
from FFxivPythonTrigger.text_pattern import find_signature_point

print(
    CFUNCTYPE(c_char_p, c_char_p)(
        find_signature_point("48 8D 05 * * * * 45 33 C0 48 89 05 ? ? ? ?") + BASE_ADDR
    )(
        c_char_p(b"_rsv_27174_-1_1_C0_0Action")
    ).decode("utf-8")
)
