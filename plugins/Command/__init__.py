import os
import traceback
from ctypes import *
from pathlib import Path
import FFxivPythonTrigger
from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import event, unload_callback
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct
from FFxivPythonTrigger.utils import err_catch
from FFxivPythonTrigger.hook import PluginHook

"""
provide a service process echo message as commands
api:    command
            register(command: str, callback:callable)
            unregister(command:str)

privide some basic control commands
command:    @fpt
format:     /e @fpt [func] [args]...
functions (*[arg] is optional args):
    [list]:     list installed plugins
    [close]:    shut down the FFxiv Python trigger (recommend!!!!)
    [raise]:    try to raise an exception
    [log]:      log something
                format: /e @fpt log [message]
    [unload]:   unload (or named as disabled) an module
                format: /e @fpt unload [module_name]
    [reload]:   reload (or named as load) an module
                format: /e @fpt reload [module_name]
"""

update_event_key = 'commands_update'

TextCommandStruct = OffsetStruct({
    "cmd": c_wchar_p,
    "t1": c_longlong,
    "tLength": c_longlong,
    "t3": c_longlong,
}, full_size=400)


class CommandPlugin(PluginBase):
    name = "Command"
    layout = str(Path(__file__).parent / 'layout.js')

    def _fpt_commands(self, args):
        if args[0] == 'close':
            close()
        elif args[0] == 'raise':
            raise Exception("111aw")
        elif args[0] == 'unload':
            unload_module(args[1])
        elif args[0] == 'reload':
            reload_module(args[1])
        elif args[0] == 'log':
            self.logger.info(" ".join(args[1:]))
        elif args[0] == 'eval':
            exec(" ".join(args[1:]), {'print': self.logger} | FFxivPythonTrigger.__dict__)
        elif args[0] == 'script':
            self.logger.info(f"script id:{self.execute_script(args[1], args[2:])} executed")
        else:
            self.logger.error("Unknown command: {}".format(args[0]))

    def fpt_commands(self, args):
        self.create_mission(self._fpt_commands, args)

    @event("log_event")
    def deal_chat_log(self, event):
        if event.channel_id == 56:
            self.process_command(event.message)

    @PluginHook.decorator(c_void_p, [c_int64, c_int, c_int64, POINTER(c_char_p), c_int64], True)
    @err_catch
    def cmd_catch_hook(self, hook, a1, a2, a3, cmd_ptr, a5):
        msg = cmd_ptr[0].decode('utf-8', 'ignore')
        if msg.startswith('/') and self.process_command(msg[1:]):
            return
        hook.original(a1, a2, a3, cmd_ptr, a5)

    def process_command(self, command_line):
        args = command_line.split(' ')
        if args[0] in self.commands:
            self.logger.debug(command_line)
            try:
                self.commands[args[0]](args[1:])
            except Exception:
                self.logger.error('exception occurred:\n{}'.format(traceback.format_exc()))
            return True
        return False

    @unload_callback('unregister')
    def register(self, command: str, callback):
        if ' ' in command:
            raise Exception("Command should not contain blanks")
        if command in self.commands:
            raise Exception("Command %s already exists" % command)
        self.commands[command] = callback
        self.update_event()

    def unregister(self, command: str, callback):
        if command in self.commands:
            del self.commands[command]
        self.update_event()

    def command_list(self):
        return {k: f"{f.__module__}.{f.__name__}" for k, f in self.commands.items()}

    def update_event(self):
        self.client_event(update_event_key, self.command_list())

    def __init__(self):
        super(CommandPlugin, self).__init__()
        self.executing_scripts = {}
        self.scripts_counter = Counter()
        self.commands = dict()
        self.register(self, '@fpt', self.fpt_commands)
        self.cmd_catch_hook(self, AddressManager(self.name, self.logger).
                            scan_address('catch_cmd', "40 55 53 57 41 54 41 56 41 57 48 8D 6C 24 ?"))

        class Script:
            def __init__(_self, script_name, argus):
                if not script_name.endswith(".py"): script_name += ".py"
                with open(Path(os.getcwd()) / 'script' / script_name, encoding='utf-8') as f:
                    _self.script = f.read()
                _self.mission = None
                _self.script_name = script_name
                _self.argus = argus
                _self.id = self.scripts_counter.get()

            def exec(_self):
                self.executing_scripts[_self.id] = _self
                _self.mission = self.create_mission(_self._exec)
                return _self.id

            def _exec(_self, *args, **kwargs):
                self.client_event(f"update_scripts", self.list_script())
                try:
                    exec(_self.script, {
                        'print': self.logger,
                        'argus': _self.argus,
                        'script': _self,
                    })
                except Exception:
                    self.logger.error(f'exception occurred in mission {_self.id}({_self.script_name}):\n{traceback.format_exc()}')
                finally:
                    _self._end()

            def _end(_self):
                try:
                    del self.executing_scripts[_self.id]
                except KeyError:
                    pass
                else:
                    self.client_event(f"update_scripts", self.list_script())

            def stop(_self):
                if _self.mission is not None:
                    _self.mission.terminate()
                    _self.mission.join(5)
                    if not _self.mission.is_alive():
                        _self._end()

        self.Script = Script

    def execute_script(self, script_name, argus):
        return self.Script(script_name, argus).exec()

    def stop_script(self, script_id):
        try:
            self.executing_scripts[script_id].stop()
        except KeyError:
            return False
        else:
            return True

    def list_script(self):
        return [{
            'id': k,
            'name': s.script_name,
            'argus': s.argus,
            'is_alive': s.mission.is_alive(),
        } for k, s in self.executing_scripts.items()]
