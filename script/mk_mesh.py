from ctypes import *
from functools import cached_property, cache
from pathlib import Path

from FFxivPythonTrigger import plugins
argus: list[str]
step = .25
b_step = int(step * 100)
extra_height = 1.5
walk_height = .75
try:
    distance_limit = eval(argus[0])
except IndexError:
    distance_limit = 100
player_can_pass = (c_int * 3)(0x2000, 0x2000, 0x0)
camera_can_pass = (c_int * 3)(0x4000, 0x4000, 0x0)
ray_cast = plugins.XivMemory.calls.screen_to_world._original
float_array_3 = (c_float * 3)
down = float_array_3(0, -1, 0)
west = float_array_3(-1, 0, 0)
east = float_array_3(1, 0, 0)
south = float_array_3(0, 0, 1)
north = float_array_3(0, 0, -1)

point_cache = {}
points = []


def get_direction(x, z, y, direction):
    world_pos_array = (c_float * 32)()
    if ray_cast(float_array_3(x / 100, z / 100 + walk_height, y / 100), direction, step, world_pos_array, player_can_pass):
        return None
    return get_point(x + direction[0] * b_step, z, y + direction[2] * b_step)


@cache
def get_point(x, init_z, y):
    world_pos_array = (c_float * 32)()
    if not ray_cast(float_array_3(x / 100, init_z / 100 + extra_height, y / 100), down, 9999, world_pos_array, camera_can_pass):
        return None
    k = (x, int(world_pos_array[1] * 100), y)
    if k not in point_cache: point_cache[k] = Point(*k)
    return point_cache[k]


class Point:
    def __init__(self, x, z, y):
        self.x = x
        self.y = y
        self.z = z
        points.append(self)
        self.idx = None

    @cached_property
    def north(self):
        return get_direction(self.x, self.z, self.y, north)

    @cached_property
    def south(self):
        return get_direction(self.x, self.z, self.y, south)

    @cached_property
    def east(self):
        return get_direction(self.x, self.z, self.y, east)

    @cached_property
    def west(self):
        return get_direction(self.x, self.z, self.y, west)

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** .5 / 100

    def __str__(self):
        return f"(x:{self.x / 100:.2f}, z:{self.z / 100:.2f}, y:{self.y / 100:.2f})"

    def __hash__(self):
        return hash((self.x, self.z, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.z == other.z and self.y == other.y


c = plugins.XivMemory.coordinate
start_point = get_point(int(c.x) * 100, int(c.z + 1) * 100, int(c.y) * 100)
print(start_point)
point_history = set()
point_queue = [start_point]
cnt = 0

while point_queue:
    cnt += 1
    current_point = point_queue.pop()
    point_history.add(current_point)
    if not cnt % 10000: print(cnt, len(point_history), len(point_queue), current_point)
    for point in [current_point.north, current_point.south, current_point.east, current_point.west]:
        if point is not None and point not in point_history and (not distance_limit or point.distance(start_point) < distance_limit):
            point_queue.append(point)

print(len(point_history), len(points))

mesh_dir = Path('mesh')
mesh_dir.mkdir(parents=True, exist_ok=True)

cnt = 0
while (mesh_dir / f"mesh_{plugins.XivMemory.zone_id}_{b_step:02d}_{cnt:03d}.obj").exists():
    cnt += 1

with open(mesh_dir / f"mesh_{plugins.XivMemory.zone_id}_{b_step:02d}_{cnt:03d}.obj", 'w+') as f:
    points.sort(key=lambda p: (p.x, p.y, p.z))
    point_cnt = 0
    for point in points:
        f.write(f"v {point.x / 100:.2f} {point.z / 100:.2f} {point.y / 100:.2f}\n")
        point_cnt += 1
        if not point_cnt % 100000: print('v', point_cnt)
        point.idx = point_cnt
    cnt = 0
    for point in points:
        cnt += 1
        if not cnt % 100000: print('f', cnt)
        point1 = point.north
        if point1 is None or abs(point.z - point1.z) > 500: continue
        point2 = point1.west
        if point2 is None or abs(point.z - point2.z) > 500: continue
        point3 = point2.south
        if point3 is None or abs(point.z - point3.z) > 500: continue

        for p in [point, point1, point2, point3]:
            if p.idx is None:
                f.write(f"v {p.x / 100:.2f} {p.z / 100:.2f} {p.y / 100:.2f}\n")
                point_cnt += 1
                p.idx = point_cnt

        f.write(f"f {point.idx} {point1.idx} {point2.idx} {point3.idx}\n")
