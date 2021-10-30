from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import BindValue, re_event


class DebugPlugin(PluginBase):
    name = "DebugPlugin"
    layout = str(Path(__file__).parent / 'layout.js')

    @re_event(r"^network/[^(undefined|unknown)]")
    def discover_event(self, evt, match:re.Match):
        self.logger(evt.id,evt,'\n',evt.str_event())

    #@re_event(r"^network/")
    def discover_event2(self, evt, match:re.Match):
        self.logger.debug(evt.id,evt,'\n',evt.str_event())
