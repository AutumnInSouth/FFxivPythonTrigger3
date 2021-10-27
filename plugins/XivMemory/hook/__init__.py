from FFxivPythonTrigger.hook import PluginHook


class ValueBindHook(PluginHook):
    value: any
    auto_install = True

    def __init__(self, plugin, func_address: int):
        super().__init__(plugin, func_address)
        self.value = None

    def hook_function(self, *args):
        self.value = self.get_value(*args)
        return self.original(*args)

    def get_value(self, *args):
        return args[0]
