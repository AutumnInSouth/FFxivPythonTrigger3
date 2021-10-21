import traceback

from FFxivPythonTrigger import *
from FFxivPythonTrigger.decorator import event, unload_callback

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


class CommandPlugin(PluginBase):
    name = "Command"
    layout = [
        {
            'type': 'bind param',
            'key': 'enable',
            'label': '启用',
            'display': 'switch',
        },
        {
            'type': 'func get',
            'key': 'command_list',
            'label': '注册指令',
            'display': 'key_value_table',
            'update_evt': update_event_key
        },
        {
            'type': 'func run',
            'key': 'process_command',
            'label': '执行指令',
            'kwargs': {'command_line': 'string'}
        }
    ]

    def FptManager(self, args):
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
            exec(" ".join(args[1:]))

    @event("log_event")
    def deal_chat_log(self, event):
        if event.channel_id == 56: self.process_command(event.message)

    def process_command(self, command_line):
        args = command_line.split(' ')
        if args[0] in self.commands:
            self.logger.debug(command_line)
            try:
                self.commands[args[0]](args[1:])
            except Exception:
                self.logger.error('exception occurred:\n{}'.format(traceback.format_exc()))

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

        self.commands = dict()
        self.register(self, '@fpt', self.FptManager)
