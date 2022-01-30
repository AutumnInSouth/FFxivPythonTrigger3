from ctypes import *
from math import atan2

from FFxivPythonTrigger import plugins, frame_inject, PluginBase, AddressManager
from FFxivPythonTrigger.decorator import BindValue
from FFxivPythonTrigger.memory import read_int


# way_marks = plugins.XivMemory.markings.way_mark
# for point in (way_marks.a, way_marks.b, way_marks.c, way_marks.d):
#     plugins.Move.waypoint_list.append((point.x, point.y))

class Move(PluginBase):
    name = "Move"

    def __init__(self):
        super().__init__()
        self.current_waypoint = None
        self.waypoint_list = []
        self.last_map = None
        am = AddressManager(self.name, self.logger)
        offset = read_int(am.scan_address('offset', "0F B6 83 ? ? ? ? 84 C0 74 ? 0F B6 C8 83 E9 ?", add=3))
        self.auto_move = cast(am.scan_point(
            'auto_move_flag', "48 8D 0D * * * * E8 ? ? ? ? 84 C0 74 ? 48 8B 0D ? ? ? ? B2 ?", add=offset
        ), POINTER(c_ubyte))
        frame_inject.register_continue_call(self.frame_work)

    def onunload(self):
        self.auto_move[0] = 1
        frame_inject.unregister_continue_call(self.frame_work)

    pos_dis = BindValue(default=.5)

    @BindValue.decorator(default=False)
    def pause(self, new_value, old_value):
        if new_value:
            self.auto_move[0] = 1
        return True

    def stop(self):
        self.waypoint_list.clear()
        self.current_waypoint = None
        self.auto_move[0] = 1

    def frame_work(self):
        if self.current_waypoint is not None:
            if not self.pause:
                self.auto_move[0] = 3
                current_map_id=plugins.XivMemory.map_id
                if self.last_map is None:
                    self.last_map = current_map_id
                elif self.last_map != current_map_id:
                    self.stop()
                    self.last_map = current_map_id
                else:
                    coordinate = plugins.XivMemory.coordinate
                    t_x, t_y = self.current_waypoint
                    if ((t_x - coordinate.x) ** 2 + (t_y - coordinate.y) ** 2) ** 0.5 < self.pos_dis:
                        try:
                            self.current_waypoint = self.waypoint_list.pop(0)
                        except IndexError:
                            self.current_waypoint = None
                            self.auto_move[0] = 1
                    else:
                        coordinate.r = atan2(t_x - coordinate.x, t_y - coordinate.y)
        elif self.waypoint_list:
            self.current_waypoint = self.waypoint_list.pop(0)
