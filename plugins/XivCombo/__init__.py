from ctypes import *
from importlib import import_module
from pathlib import Path
from traceback import format_exc

from FFxivPythonTrigger import PluginBase, AddressManager, BindValue, process_event, plugins
from FFxivPythonTrigger.hook import PluginHook

get_icon_sig = "E8 * * * * 44 8B C0 8B D7 48 8B CB E8 ? ? ? ? 84 C0"
is_icon_replaceable_sig = "81 F9 ?? ?? ?? ?? 7F 39 81 F9 ?? ?? ?? ??"


class XivCombo(PluginBase):
    name = "XivCombo"
    layout = str(Path(__file__).parent / 'layout.js')

    def __init__(self):
        super().__init__()
        self.combos = {}
        am = AddressManager(self.name, self.logger)
        self.OnGetIconHook(self, am.scan_point('get_icon', get_icon_sig))
        self.OnCheckIsIconReplaceableHook(self, am.scan_address('is_icon_replaceable', is_icon_replaceable_sig))
        self.all_combo = {}
        for f in (Path(__file__).parent / 'combos').glob('*.py'):
            if f.stem == '__init__': continue
            module = import_module(f'.combos.{f.stem}', __name__)
            if hasattr(module, 'combos') and isinstance(module.combos, list):
                for combo in module.combos:
                    self.all_combo.setdefault(combo.action_id, {})[combo.combo_id] = combo
                self.logger.debug(f"loaded combos from .combos.{f.stem}")
        for action_id, combo_id in list(self.combo_select.items()):
            n_action_id = int(action_id)
            combo = self.all_combo.get(n_action_id, {}).get(combo_id)
            if combo:
                self.combos[n_action_id] = combo.combo
            else:
                del self.controller.bind_values['combo_select'][action_id]

    @BindValue.decorator(default={}, auto_save=True)
    def combo_select(self, new_val, old_val):
        new_combo = {}
        for action_id, combo_id in new_val.items():
            if combo_id: new_combo[int(action_id)] = self.all_combo[int(action_id)][combo_id].combo
        self.combos = new_combo
        self.logger.debug(f"combo_select update: {new_val}")
        return True

    @PluginHook.decorator(c_ulonglong, [c_ubyte, c_uint], True)
    def OnGetIconHook(self, hook, a1, action_id):
        if action_id in self.combos:
            try:
                me = plugins.XivMemory.actor_table.me
                if me is not None:
                    return hook.original(a1, self.combos[action_id](me))
            except Exception:
                self.logger.error("error occured:\n" + format_exc())
                temp_combo = self.combo_select
                temp_combo[str(action_id)] = ''
                self.combo_select = temp_combo
        return hook.original(a1, action_id)

    @PluginHook.decorator(c_uint, [c_ulonglong], True)
    def OnCheckIsIconReplaceableHook(self, hook, action_id):
        return int((action_id in self.combos) or (hook.original(action_id)))

    def get_all_combo(self):
        return {action_id: {
            combo.combo_id: {'title': combo.title, 'desc': combo.desc}
            for combo in combos.values()
        } for action_id, combos in self.all_combo.items()}
