from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import BindValue, re_event


class DebugPlugin(PluginBase):
    name = "DebugPlugin"
    layout = str(Path(__file__).parent / 'layout.js')

    @re_event(r"^network\/zone")
    def discover_event(self, evt, _):
        self.logger(evt.id,evt)
        self.logger('',evt.str_event())
