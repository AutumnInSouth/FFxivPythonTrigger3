class NeedRequirementError(Exception):
    def __init__(self, *pkgs):
        super().__init__("some requirements are missing")
        self.pkgs = pkgs


class PluginNotFoundException(Exception):
    def __init__(self, plugin_name):
        self.name = plugin_name
        super().__init__(f"Plugin {plugin_name} not found")
