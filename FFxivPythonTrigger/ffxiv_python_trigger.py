import json
import os
import re
import sys
from importlib import import_module, reload
from inspect import isclass, getfile, getsourcelines
from pathlib import Path
from queue import Queue
from socketserver import StreamRequestHandler, ThreadingTCPServer
from threading import Thread
from time import time, sleep, perf_counter
from traceback import format_exc
from typing import List, Type, Dict, Set, Optional, Callable, Union, Tuple, Pattern

from . import server_enum
from .address_manager import AddressManager
from .decorator import ReEventCall, EventCall, BindValue, PluginHook
from .exceptions import NeedRequirementError, PluginNotFoundException
from .frame_inject import FrameInjectHook, sig as frame_inject_sig
from .logger import Logger, Log, log_handler, DEBUG
from .memory import PROCESS_FILENAME
from .requirements_controller import sub_process_install
from .storage import ModuleStorage, get_module_storage, BASE_PATH
from .utils import Counter, get_attr_by_str_path

EVENT_MULTI_THREAD = True
LOG_FILE_SIZE_MAX = 1024 * 1024
LOG_FILE_FORMAT = 'log_{int_time}.txt'
STORAGE_DIRNAME = "Core"
LOGGER_NAME = "Main"
re_pattern = Union[str, re.Pattern]


class FPTServer(StreamRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        self.client_id = None

    def send_event(self, data):
        self.wfile.write(server_enum.server_event(data))

    def _process(self, code: int, msg_id: int, namespace: str, data: dict):
        if not namespace:
            if code == server_enum.ClientSubscribe:
                _clients_subscribe.setdefault(data['name'], set()).add(self.client_id)
                return "success"
            elif code == server_enum.ClientUnsubscribe:
                try:
                    _clients_subscribe.setdefault(data['name'], set()).remove(self.client_id)
                except ValueError:
                    pass
                return "success"
            elif code == server_enum.ClientGet:
                return get_attr_by_str_path(globals(), data['name'])
            elif code == server_enum.ClientCall or code == server_enum.ClientCallReply:
                reply = get_attr_by_str_path(globals(), data['name'])(*data.get('args', []), **data.get('kwargs', {}))
                return reply if code == server_enum.ClientCallReply else None
            elif code == server_enum.ClientSet:
                value = data['value']
                try:
                    path, key = data['name'].rsplit('.', 1)
                except ValueError:
                    obj = globals()
                    key = data['name']
                else:
                    obj = get_attr_by_str_path(globals(), path)
                if isinstance(obj, dict):
                    obj[key] = value
                else:
                    setattr(obj, key, value)
                return "success"
            else:
                raise Exception("invalid unsubscribe arg")
        elif namespace in _plugins:
            return _plugins[namespace].controller.client_handle(code, msg_id, namespace, data)
        else:
            raise Exception("invalid namespace")

    def process(self, line):
        message_id = None
        try:
            data = json.loads(line)
            message_id = data['msg_id']
            code = data['code']
            namespace = data.get('namespace', '')
            reply = self._process(code, message_id, namespace, data)
            if reply is not None:
                self.wfile.write(server_enum.server_reply(message_id, reply))
        except Exception as e:
            self.wfile.write(server_enum.server_error(format_exc(), message_id))

    def handle(self):
        self.client_id = _client_counter.get()
        _clients[self.client_id] = self
        _logger.debug(f"new client id:{self.client_id}")
        try:
            for _line in self.rfile:
                append_missions(Mission("process_client", 0, self.process, _line))
        except ConnectionError:
            _logger.debug(f"disconnect client id:{self.client_id}")
        del _clients[self.client_id]


def process_clients(name: str, data: any):
    if name in _clients_subscribe:
        for client_id in _clients_subscribe[name].copy():
            if client_id in _clients:
                _clients[client_id].send_event(data)
            else:
                try:
                    _clients_subscribe[name].remove(client_id)
                except ValueError:
                    pass
        if not _clients_subscribe[name]:
            del _clients_subscribe[name]


def client_log(log: Log):
    process_clients('fpt_log', {
        'timestamp': log.datetime.timestamp(),
        'module': log.module,
        'level': log.level,
        'msg': log.message,
    })


class Mission(Thread):
    def __init__(self, mission_name: str, mission_id: int, mission, *args, callback=None, **kwargs):
        super(Mission, self).__init__(name="%s#%s" % (mission_name, mission_id))
        self.mission_name = mission_name
        self.mission_id = mission_id
        self.mission = mission
        self.args = args
        self.kwargs = kwargs
        self.callback = callback
        self.rtn = None

    def run(self):
        try:
            self.rtn = self.mission(*self.args, **self.kwargs)
        except Exception as e:
            _logger.error(f"error occurred in mission {self}:\n{format_exc()}")
            self.rtn = e
        try:
            _missions.remove(self)
        except KeyError:
            pass
        if self.callback is not None:
            try:
                self.callback(self.rtn)
            except Exception:
                _logger.error(f"error occurred in mission recall {self}:\n{format_exc()}")


class EventBase(object):
    id = 0
    name = "unnamed event"

    def str_event(self) -> Optional[Union[str, list[str], tuple[str]]]:
        pass

    def text(self) -> any:
        return str(self.id)

    def __str__(self):
        return f"<{self.name}>{self.text()}"


class EventCallback(object):
    def __init__(self, plugin: "PluginBase", call: Callable, limit_sec: Optional[float] = None):
        self.plugin = plugin
        self._call = call
        self.limit_sec = limit_sec

    def call(self, event: EventBase, *args):
        if self.limit_sec is not None:
            self.plugin.create_mission(self._call, event, *args, limit_sec=self.limit_sec)
        else:
            self.plugin.create_mission(self._call, event, *args)


class PluginBase(object):
    name = "unnamed_plugin"
    save_when_unload = True
    bind_values_store_key: str = 'bind_values'

    def __init__(self):
        self.logger = Logger(self.name)
        self.storage = get_module_storage(self.name)
        self.controller = PluginController(self)
        self.create_mission = self.controller.create_mission
        self.register_event = self.controller.register_event
        self.register_re_event = self.controller.register_re_event
        self.client_event = self.controller.client_event

    def onunload(self):
        pass

    def start(self):
        pass

    def client_handle(self, code: int, msg_id: int, namespace: str, data: dict):
        raise NotImplementedError()


class PluginController(object):
    def __init__(self, plugin: 'PluginBase'):

        self.bind_values = {}
        self.plugin: PluginBase = plugin
        self.events: list[Tuple[any, EventCallback]] = list()
        self.re_events: list[Tuple[re.Pattern, EventCallback]] = list()
        self.mission_count = Counter()
        self.missions: dict[int, Mission] = dict()
        self.installed_hooks: list[PluginHook] = list()
        self.hook_to_start: list[PluginHook] = list()
        self.main_mission: Optional[Mission] = None
        self.unload_callback: list[Tuple[Callable, list, dict]] = []
        self.started = False

        for attr_name, attr in self.plugin.__class__.__dict__.items():
            if isinstance(attr, ReEventCall):
                self.register_re_event(attr.pattern, getattr(self.plugin, attr_name), attr.limit_sec)
            elif isinstance(attr, EventCall):
                self.register_event(attr.event_id, getattr(self.plugin, attr_name), attr.limit_sec)

    def init_bind_values(self):
        store_values = self.plugin.storage.data.setdefault(self.plugin.bind_values_store_key, dict())
        for attr in self.plugin.__class__.__dict__.values():
            if isinstance(attr, BindValue):
                if attr.key in store_values:
                    setattr(self.plugin, attr.key, store_values[attr.key])
                elif attr.default is not None:
                    setattr(self.plugin, attr.key, attr.default)

    def create_mission(self, call: Callable, *args, limit_sec=0.1, put_buffer=True, callback: Optional[Callable] = None,
                       **kwargs) -> Mission:
        def function(*_args, **_kwargs):
            start = perf_counter()
            try:
                call(*_args, **_kwargs)
            except Exception:
                self.plugin.logger.error("error occurred in mission:" + format_exc())
            if limit_sec > 0:
                used = perf_counter() - start
                if used > limit_sec:
                    self.plugin.logger.warning(
                        "[{}:{}] run for {:2f}s".format(getfile(call), getsourcelines(call)[1], used))

        def _callback(res: any):
            if callback is not None:
                callback(res)
            if mid in self.missions:
                del self.missions[mid]

        mid = self.mission_count.get()
        mission = Mission(self.plugin.name, mid, function, *args, callback=_callback, **kwargs)
        if append_missions(mission, put_buffer=put_buffer):
            self.missions[mid] = mission
        return mission

    def register_event(self, event_id: any, call: Callable, limit_sec=None):
        callback = EventCallback(self.plugin, call, limit_sec)
        self.events.append((event_id, callback))
        register_event(event_id, callback)

    def register_re_event(self, pattern: Union[Pattern[str], re.Pattern], call: Callable, limit_sec=None):
        if not isinstance(pattern, re.Pattern):
            pattern = re.compile(pattern)
        callback = EventCallback(self.plugin, call, limit_sec)
        self.re_events.append((pattern, callback))
        register_re_event(pattern, callback)

    def start_plugin(self):
        for p_hook in self.hook_to_start:
            try:
                p_hook.install_and_enable()
            except Exception:
                self.plugin.logger.warning("an auto start hook initialize failed:\n" + format_exc())
        self.main_mission = self.create_mission(self.plugin.start, limit_sec=0)
        self.started = True

    def unload_plugin(self):
        for call, args, kwargs in self.unload_callback:
            try:
                call(*args, **kwargs)
            except Exception:
                self.plugin.logger.warning("an unload callback failed:\n" + format_exc())
        for event_id, callback in self.events:
            unregister_event(event_id, callback)
        for pattern, callback in self.re_events:
            unregister_re_event(pattern, callback)
        try:
            self.plugin.onunload()
        except Exception:
            self.plugin.logger.warning("unload function error occurred:\n" + format_exc())
        for mission in list(self.missions.values()):
            try:
                mission.join(-1)
            except RuntimeError:
                pass
        for p_hook in self.installed_hooks.copy():
            p_hook.uninstall()
        if self.plugin.save_when_unload:
            self.plugin.storage.save()

    def client_handle(self, code: int, msg_id: int, namespace: str, data: dict):
        if code == server_enum.ClientGet:
            return get_attr_by_str_path(self.plugin, data['name'])
        elif code == server_enum.ClientCall or code == server_enum.ClientCallReply:
            reply = get_attr_by_str_path(self.plugin, data['name'])(*data.get('args', []), **data.get('kwargs', {}))
            return reply if code == server_enum.ClientCallReply else None
        elif code == server_enum.ClientSet:
            value = data['value']
            try:
                path, key = data['name'].rsplit('.', 1)
            except ValueError:
                obj = globals()
                key = data['name']
            else:
                obj = get_attr_by_str_path(self.plugin, path)
            if isinstance(obj, dict):
                obj[key] = value
            else:
                setattr(obj, key, value)
            return "success"
        else:
            return self.plugin.client_handle(code, msg_id, namespace, data)

    def client_event(self, data: any):
        process_clients(self.plugin.name, data)


class PluginLoadEvent(EventBase):
    id = "plugin_load"
    name = "plugin_load_event"

    def __init__(self, plugin_name):
        self.plugin_name = plugin_name

    def str_event(self):
        return "plugin_load:" + self.plugin_name

    def text(self):
        return self.plugin_name


class PluginUnloadEvent(EventBase):
    id = "plugin_unload"
    name = "plugin_unload_event"

    def __init__(self, plugin_name):
        self.plugin_name = plugin_name

    def str_event(self):
        return "plugin_unload:" + self.plugin_name

    def text(self):
        return self.plugin_name


def append_missions(mission: Mission, guard=True, put_buffer=True) -> bool:
    if _allow_create_missions:
        if put_buffer:
            _missions_buffer.put((mission, guard))
        else:
            if guard:
                _missions.add(mission)
            mission.start()
        return True
    return False


def mission_starter():
    while True:
        mission, guard = _missions_buffer.get()
        if guard:
            _missions.add(mission)
        mission.start()


def register_plugin(plugin: Type[PluginBase]) -> PluginBase:
    if plugin.name in _plugins:
        raise Exception(f"Plugin {plugin.name} was already registered")
    _logger.debug(f"register plugin [start]: {plugin.name}")
    try:
        _plugins[plugin.name] = plugin()
    except Exception:
        _logger.error(f'error occurred during plugin initialization: {plugin.name}')
        _logger.error('error trace:\n' + format_exc())
        raise Exception('plugin initialization error')
    _logger.info(f"register plugin [success]: {plugin.name}")
    process_event(PluginLoadEvent(plugin.name))
    return _plugins[plugin.name]


def unload_plugin(plugin_name) -> bool:
    if plugin_name in _plugins:
        _logger.debug("unregister plugin [start]: %s" % plugin_name)
        try:
            _plugins[plugin_name].controller.unload_plugin()
            del _plugins[plugin_name]
            _logger.info("unregister plugin [success]: %s" % plugin_name)
        except Exception:
            _logger.error('error occurred during unload plugin\n %s' % format_exc())
            return False
        else:
            process_event(PluginUnloadEvent(plugin_name))
            return True
    return False


def register_module(module) -> List[PluginBase]:
    installed = []
    if type(module) == str:
        _logger.debug("try load plugin \"%s\" dynamically" % module)
        try:
            try:
                module = import_module(module)
            except NeedRequirementError as e:
                sub_process_install(*e.pkgs)
                module = import_module(module)
        except Exception:
            _logger.error('error occurred during import module:\" %s\"' % module)
            _logger.error('error trace:\n' + format_exc())
            raise Exception("module import error")
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if isclass(attr) and issubclass(attr, PluginBase) and attr != PluginBase:
            installed.append(register_plugin(attr))
    return installed


def unload_module(module):
    if type(module) == str:
        module = import_module(module)
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if isclass(attr) and issubclass(attr, PluginBase) and attr != PluginBase:
            unload_plugin(attr.name)


def reload_module(module):
    if type(module) == str:
        module = import_module(module)
    unload_module(module)
    module_name = module.__name__
    for sub_module in list(sys.modules.keys()):
        if sub_module.startswith(module_name):
            try:
                reload(import_module(sub_module))
            except Exception:
                del sys.modules[sub_module]
    for plugin in register_module(import_module(module_name)):
        plugin.controller.start_plugin()


def register_modules(modules: list):
    for module in modules:
        register_module(module)


def register_event(event_id: any, callback: EventCallback):
    _events.setdefault(event_id, set()).add(callback)


def unregister_event(event_id: any, callback: EventCallback):
    try:
        _events[event_id].remove(callback)
        if not _events[event_id]:
            del _events[event_id]
    except KeyError:
        pass


def register_re_event(pattern: re_pattern, callback: EventCallback):
    if not isinstance(pattern, re.Pattern):
        pattern = re.compile(pattern)
    _re_events.setdefault(pattern, set()).add(callback)


def unregister_re_event(pattern: re_pattern, callback: EventCallback):
    if not isinstance(pattern, re.Pattern):
        pattern = re.compile(pattern)
    try:
        _re_events[pattern].remove(callback)
        if not _re_events[pattern]:
            del _re_events[pattern]
    except KeyError:
        pass


def is_event_processable(event: EventBase):
    if '*' in _events: return True
    for key in event.id, event.str_event():
        if key is None: continue
        if key in _events: return True
        for pattern in list(_re_events.keys()):
            if pattern.search(key):
                return True
    return False


if EVENT_MULTI_THREAD:
    def process_event(event: EventBase):
        for callback in _events.get('*', []).copy():
            callback.call(event)
        e_ids = event.id if isinstance(event.id, (list, tuple)) else [event.id]
        for e_id in e_ids:
            for callback in _events.get(e_id, []).copy():
                callback.call(event)
            if isinstance(e_id, str):
                for pattern in list(_re_events.keys()):
                    match = pattern.search(e_id)
                    if match:
                        for callback in _re_events[pattern].copy():
                            callback.call(event, match)
        str_events = event.str_event()
        if str_events is None: return
        for str_event in (str_events if isinstance(str_events, (list, tuple)) else [str_events]):
            append_missions(Mission('client_event', 0, process_clients, 'fpt_event', str_event))
            for callback in _events.get(str_event, []).copy():
                callback.call(event)
            for pattern in list(_re_events.keys()):
                match = pattern.search(str_event)
                if match:
                    for callback in _re_events[pattern].copy():
                        callback.call(event, match)


    def event_processor():
        pass
else:
    _event_buffer: Queue['EventBase'] = Queue()


    def process_event(event: EventBase):
        _event_buffer.put(event)


    def _process_event(event: EventBase):
        for callback in _events.get('*', []).copy():
            callback._call(event)
        for key in event.id, event.str_event():
            if key is None:
                continue
            for callback in _events.get(key, []).copy():
                callback._call(event)
            for pattern in list(_re_events.keys()):
                match = pattern.search(key)
                if match:
                    for callback in _re_events[pattern].copy():
                        callback._call(event, match)


    def event_processor():
        while True:
            _process_event(_event_buffer.get())


def log_writer():
    with open(_log_path, 'a+') as fo:
        while _log_work:
            if _log_write_buffer.empty():
                fo.flush()
            fo.write(str(_log_write_buffer.get()))
            fo.write('\n')


def close():
    global _allow_create_missions, running
    _allow_create_missions = False
    for name in reversed(list(_plugins.keys())):
        unload_plugin(name)
    _storage.save()
    frame_inject.uninstall()
    running = False


def run():
    for plugin in _plugins.values():
        plugin.controller.start_plugin()
    global running
    running = True
    _logger.info('FFxiv Python Trigger started')
    while running or _missions:
        sleep(0.1)
    _logger.info('FFxiv Python Trigger closed')
    global _log_work
    _log_work = False
    _log_mission.join(1)
    _event_process_mission.join(1)
    _missions_starter_mission.join(1)
    _server_mission.join(1)


def init():
    global _allow_create_missions, _log_work
    ThreadingTCPServer.allow_reuse_address = True
    _server.server_address = ('127.0.0.1', int(os.environ.setdefault('FptSocketPort', "3520")))
    _server.server_bind()
    _server.server_activate()
    _server_mission.start()

    log_handler.add((DEBUG, _log_write_buffer.put))
    log_handler.add((DEBUG, client_log))
    plugin_path = Path(os.getcwd()) / 'plugins'
    plugin_path.mkdir(exist_ok=True)
    sys.path.insert(0, str(plugin_path))
    for path in _storage.data.setdefault('paths', list()):
        _logger.debug("add plugin path:%s" % path)
        sys.path.insert(0, path)
    _allow_create_missions = True
    _log_work = True
    _missions_starter_mission.start()
    _log_mission.start()
    _event_process_mission.start()
    frame_inject.install_and_enable()


class Plugins(object):
    def __init__(self, plugin_dict):
        self.plugin_dict = plugin_dict

    def __getattr__(self, name):
        return self[name]

    def __getitem__(self, name):
        if name not in self.plugin_dict:
            raise PluginNotFoundException(name)
        return self.plugin_dict[name]


_missions_buffer: Queue[tuple['Mission', bool]] = Queue()
_missions: Set['Mission'] = set()
_missions_starter_mission: 'Mission' = Mission('mission_starter', -1, mission_starter)

_storage: ModuleStorage = ModuleStorage(BASE_PATH / STORAGE_DIRNAME)
_logger: Logger = Logger(LOGGER_NAME)
_log_path: Path = _storage.path / LOG_FILE_FORMAT.format(int_time=int(time()))
_log_work = False
_log_write_buffer: Queue[Log] = Queue()
_log_mission: 'Mission' = Mission('logger', -1, log_writer)

running = False
_plugins: Dict[str, PluginBase] = {}
_events: Dict[any, Set['EventCallback']] = {}
_event_process_mission: 'Mission' = Mission('event_processor', -1, event_processor)
_re_events: Dict[re.Pattern, Set['EventCallback']] = dict()
_allow_create_missions: bool = False

plugins = Plugins(_plugins)
addresses = AddressManager(LOGGER_NAME, _logger).load({
    'frame_inject': frame_inject_sig,
})
frame_inject: FrameInjectHook = FrameInjectHook(addresses['frame_inject'])

_client_counter = Counter()
_clients: Dict[int, FPTServer] = dict()
_clients_subscribe: Dict[str, Set[int]] = dict()
_server = ThreadingTCPServer(('', 0), FPTServer, bind_and_activate=False)
_server_mission = Mission('server', -1, _server.serve_forever)

game_base_dir: Path = Path(PROCESS_FILENAME).parent.parent
if (game_base_dir / "FFXIVBoot.exe").exists() or (game_base_dir / "rail_files" / "rail_game_identify.json").exists():
    game_language = "chs"
else:
    game_language = _storage.data.setdefault('inter_lang', "en")
