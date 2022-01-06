from FFxivPythonTrigger import *
unload_module('XivCombat')
import sys
for m in list(sys.modules.keys()):
    if m.startswith('FFxivPythonTrigger.meta_data'):
        del sys.modules[m]
reload_module('XivCombat')
