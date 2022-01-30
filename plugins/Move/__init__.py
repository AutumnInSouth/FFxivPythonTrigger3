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
        self.last_zone = None
        am = AddressManager(self.name, self.logger)
        self.auto_move = cast(am.scan_point(
            'auto_move_flag', "48 8D 0D * * * * E8 ? ? ? ? 84 C0 74 ? 48 8B 0D ? ? ? ? B2 ?",
            add=read_int(am.scan_address('auto_move_offset', "0F B6 83 ? ? ? ? 84 C0 74 ? 0F B6 C8 83 E9 ?", add=3))
        ), POINTER(c_ubyte))
        self.depression_angle_ptr = cast(am.scan_point(
            'depression_angle', "48 8D 0D * * * * E8 ? ? ? ? 48 8D 0D ? ? ? ? E8 ? ? ? ? C6 47 ? ?",
            add=read_int(am.scan_address('depression_angle_offset', "F3 44 0F 10 AF ? ? ? ? 33 C0", add=5))
        ), POINTER(c_float))

        frame_inject.register_continue_call(self.frame_work)

    def onunload(self):
        self.auto_move[0] = 1
        frame_inject.unregister_continue_call(self.frame_work)

    pos_dis_walk = BindValue(default=.5)
    pos_dis_mount = BindValue(default=1)
    pos_dis_fly = BindValue(default=2)

    @BindValue.decorator(default=False)
    def pause(self, new_value, old_value):
        if new_value:
            self.auto_move[0] = 1
        return True

    def stop(self):
        self.waypoint_list.clear()
        self.current_waypoint = None
        self.auto_move[0] = 1

    def next_waypoint(self):
        try:
            self.current_waypoint = self.waypoint_list.pop(0)
            # self.logger.info("Move to next waypoint: ", self.current_waypoint)
        except IndexError:
            self.current_waypoint = None
            self.auto_move[0] = 1
            # self.logger.info("Move to last waypoint")
            return False
        return True

    def process_fly(self):
        coordinate = plugins.XivMemory.coordinate
        t_x, t_y, t_z = self.current_waypoint
        x_dis = t_x - coordinate.x
        y_dis = t_y - coordinate.y
        z_dis = coordinate.z - t_z
        xy_dis = x_dis ** 2 + y_dis ** 2
        xyz_dis = xy_dis + z_dis ** 2
        if xyz_dis < self.pos_dis_fly ** 2:
            self.next_waypoint()
        else:
            coordinate.r = atan2(x_dis, y_dis)
            self.depression_angle_ptr[0] = atan2(z_dis, xy_dis ** .5)

    def process_walk(self):
        coordinate = plugins.XivMemory.coordinate
        t_x, t_y = self.current_waypoint
        x_dis = t_x - coordinate.x
        y_dis = t_y - coordinate.y
        if x_dis ** 2 + y_dis ** 2 < self.pos_dis_walk ** 2:
            self.next_waypoint()
        else:
            coordinate.r = atan2(x_dis, y_dis)

    def frame_work(self):
        if self.current_waypoint is not None:
            if not self.pause:
                self.auto_move[0] = 3
                current_zone_id = plugins.XivMemory.zone_id
                me = plugins.XivMemory.actor_table.me
                if self.last_zone is None:
                    self.last_zone = current_zone_id
                elif self.last_zone != current_zone_id or me is None:
                    self.stop()
                    self.last_zone = current_zone_id
                elif len(self.current_waypoint) == 2:
                    self.process_walk()
                else:
                    self.process_fly()
        elif self.waypoint_list:
            self.current_waypoint = self.waypoint_list.pop(0)
