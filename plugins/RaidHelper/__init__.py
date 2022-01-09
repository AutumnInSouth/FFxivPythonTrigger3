from pathlib import Path
from traceback import format_exc
from importlib import import_module
from itertools import chain
from FFxivPythonTrigger import PluginBase, plugins
from FFxivPythonTrigger.decorator import BindValue
from FFxivPythonTrigger.saint_coinach import territory_type_names
from .utils import RaidTrigger

exts = ['ext4']


class RaidHelper(PluginBase):
    name = "RaidHelper"
    layout = str(Path(__file__).parent / 'layout.js')

    def __init__(self):
        super().__init__()

        self.triggers_map = {}
        self.triggers_evt = {}
        self.triggers_re_evt = {}

        dir_path = Path(__file__).parent
        for ext in exts:
            ext_path = dir_path / ext
            if ext_path.exists() and (ext_path / '__init__.py').exists():
                self.logger.debug(f"Loading {ext}...")
                cnt = 0
                for file in ext_path.glob('*.py'):
                    if file.name == '__init__.py': continue
                    module = import_module(f'.{ext}.{file.stem}', package=__package__)
                    for name, obj in module.__dict__.items():
                        if isinstance(obj, RaidTrigger):
                            cnt += 1
                            self.triggers_map.setdefault(obj.map_id, {})[obj.title] = obj
                            if obj.event is not None:
                                self.triggers_evt.setdefault(obj.event, {}).setdefault(obj.map_id, []).append(obj)
                            elif obj.re_event is not None:
                                self.triggers_re_evt.setdefault(obj.re_event, {}).setdefault(obj.map_id, []).append(obj)
                self.logger.info(f"Loaded {cnt} triggers from {ext}")

        for evt, map_triggers in self.triggers_evt.items():
            self.register_event(evt, self.process_event(map_triggers))
            self.logger.debug(f"Registered event {evt} for {sum(len(m) for m in map_triggers.values())} triggers")
        for evt, map_triggers in self.triggers_re_evt.items():
            self.logger.debug(f"Registered re_event {evt} for {sum(len(m) for m in map_triggers.values())} triggers")
            self.register_re_event(evt, self.process_event(map_triggers))
        enable_triggers = self.storage.data.get("bind_values", {}).get("enable_triggers", {})

        self.enable_triggers = {
            str(map_id): {
                title: enable_triggers.get(str(map_id), {}).get(title, False)
                for title in triggers.keys()
            }
            for map_id, triggers in self.triggers_map.items()
        }

    in_game_output = BindValue(default=0, auto_save=True)
    in_game_output_sound_effect = BindValue(default=0, auto_save=True)
    log_output = BindValue(default=True, auto_save=True)

    @BindValue.decorator(default={}, auto_save=True, init_set=True)
    def enable_triggers(self, new_val, old_val):
        self.logger.debug(f"enable_triggers: {new_val}")
        for map_id, triggers in new_val.items():
            map_triggers = self.triggers_map.get(int(map_id), {})
            for title, enabled in triggers.items():
                if title in map_triggers:
                    map_triggers[title].enabled = enabled
        return True

    def trigger_output(self, output_str: str, log_output: bool = None, in_game_output: bool = None, in_game_output_sound_effect: bool = None):
        if log_output is None:
            log_output = self.log_output
        if in_game_output is None:
            in_game_output = self.in_game_output
        if in_game_output_sound_effect is None:
            in_game_output_sound_effect = self.in_game_output_sound_effect
        if log_output:
            self.logger.info(output_str)
        if in_game_output:
            msg = f"{output_str} <se.{in_game_output_sound_effect}>" if in_game_output_sound_effect else output_str
            match self.in_game_output:
                case 1:  # echo
                    plugins.XivMemory.calls.do_text_command('/e ' + msg)
                case 2:  # party
                    plugins.XivMemory.calls.do_text_command('/p ' + msg)

    def process_event(self, event_map_triggers):
        def _process_event(*args):
            for trigger in chain(
                    event_map_triggers.get(int(plugins.XivMemory.zone_id), []),
                    event_map_triggers.get(-1, [])
            ):
                if trigger.enabled:
                    self.create_mission(trigger.func, self.trigger_output, *args, limit_sec=0)

        return _process_event

    def layout_get_triggers_list(self):
        return {map_id: [title for title in triggers.keys()] for map_id, triggers in self.triggers_map.items()}

    def map_names(self):
        return {map_id: str(territory_type_names[map_id]) if map_id > 0 else 'common' for map_id in self.triggers_map.keys()}
