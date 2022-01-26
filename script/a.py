from ctypes import *
from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.saint_coinach import realm
from FFxivPythonTrigger.text_pattern import find_signature_point
from XivMemory.se_string.messages import *


plugins.XivMemory.calls.do_text_command(b'/e '+Item(1).encode_group())
