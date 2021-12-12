from FFxivPythonTrigger import PluginBase

from .ext4 import events as ext4_events

data = {'name': 'ExtraOmens'} | {'ext4_' + k: v for k, v in ext4_events.items()}

ExtraOmens = type('ExtraOmens', (PluginBase,), data)
