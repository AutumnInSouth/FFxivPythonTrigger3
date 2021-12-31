import traceback
import typing

import math

from FFxivPythonTrigger import plugins, PluginBase, PluginNotFoundException
from FFxivPythonTrigger.decorator import event

if typing.TYPE_CHECKING:
    from XivMemory.struct.coordinate import Coordinate

command = '@tp'


def get_coordinate() -> 'Coordinate':
    return plugins.XivMemory.coordinate


def tp_rxy(angle, dis):
    coordinate = get_coordinate()
    coordinate.x += math.sin(angle) * dis
    coordinate.y += math.cos(angle) * dis


def tp_rz(dis):
    get_coordinate().z += dis


class Teleporter(PluginBase):
    name = "Teleporter"

    def __init__(self):
        super().__init__()
        self.register_command()

    def get_zone_data(self):
        zid = plugins.XivMemory.zone_id
        return zid, self.storage.data.setdefault(str(zid), dict())

    def _process_cmd(self, args: list[str]):
        coordinate = get_coordinate()
        match args[0]:
            case 'set':
                return coordinate.set(*(float(a) for a in args[1:]))
            case 'get':
                return f'{coordinate.x:.2f} / {coordinate.y:.2f} / {coordinate.z:.2f}'
            case 'list':
                zone_id, data = self.get_zone_data()
                return f'{zone_id}({len(data)}):' + '/'.join(data.keys())
            case 'save':
                zone_id, data = self.get_zone_data()
                if args[1] in data: return f"key [{args[1]}] is already in zone [{zone_id}]"
                data[args[1]] = [coordinate.x, coordinate.y, coordinate.z]
                self.storage.save()
                return f'{zone_id}({len(data)}):' + '/'.join(data.keys())
            case 'goto':
                zone_id, data = self.get_zone_data()
                if args[1] not in data: return f"key [{args[1]}] is not in zone [{zone_id}]"
                coordinate.set(*data[args[1]])
                return 'success'
            case 'drop':
                zone_id, data = self.get_zone_data()
                if args[1] not in data: return f"key [{args[1]}] is not in zone [{zone_id}]"
                del data[args[1]]
                self.storage.save()
                return f'{zone_id}({len(data)}):' + '/'.join(data.keys())
            case 'mo':
                l = plugins.XivMemory.utils.mo_location
                if l is not None:
                    coordinate.set(*l)
                    return 'success'
                return 'mo location is not found'

        dis = float(args[1])
        match args[0]:
            case 'north' | 'n':
                tp_rxy(math.pi, dis)
                return "tp to north %s" % dis
            case 'east' | 'e':
                tp_rxy(math.pi / 2, dis)
                return "tp to east %s" % dis
            case 'west' | 'w':
                tp_rxy(math.pi / 2, dis)
                return "tp to west %s" % dis
            case 'south' | 's':
                tp_rxy(0, dis)
                return "tp to south %s" % dis
            case 'front' | 'f':
                tp_rxy(coordinate.r, dis)
                return "tp to front %s" % dis
            case 'back' | 'b':
                tp_rxy(coordinate.r - math.pi, dis)
                return "tp to back %s" % dis
            case 'left' | 'l':
                tp_rxy(coordinate.r + math.pi / 2, dis)
                return "tp to left %s" % dis
            case 'right' | 'r':
                tp_rxy(coordinate.r - math.pi / 2, dis)
                return "tp to right %s" % dis
            case 'up' | 'u':
                tp_rz(dis)
                return "tp to up %s" % dis
            case 'down' | 'd':
                tp_rz(-dis)
                return "tp to down %s" % dis
            case unk:
                return f"unknown command {unk}"

    @event("plugin_load:Command")
    def register_command(self, _=None):
        try:
            plugins.Command.register(self, command, self.process_cmd)
        except PluginNotFoundException:
            self.logger.warning("Command is not found")

    def process_cmd(self, args):
        try:
            cmd = self._process_cmd(args)
            if cmd is not None: self.logger.info(cmd)
        except Exception as e:
            self.logger.error(str(e))
            self.logger.error(traceback.format_exc())
