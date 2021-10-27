from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import BindValue


class Test(PluginBase):
    name = "Test"
    layout = str(Path(__file__).parent / 'layout.js')
    num2 = BindValue(default=1)

    @BindValue.decorator(default=1)
    def num(self, new_val, old_val):
        self.logger(f'change num from {old_val} to {new_val}')
        return True
