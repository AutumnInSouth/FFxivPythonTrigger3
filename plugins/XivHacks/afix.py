import math

from shapely.geometry import Point
from shapely.ops import cascaded_union, nearest_points

from FFxivPythonTrigger import game_ext
from FFxivPythonTrigger.utils.shape import sector

FRONT = 1
SIDE = 2
BACK = 3
angle = math.pi / 2 - 0.1

afix_skills = {
    7481: BACK,  # 月光，背
    7482: SIDE,  # 花车，侧
    53: BACK,  # 连击，背，武僧
    54: BACK,  # 正拳，背，武僧
    56: SIDE,  # 崩拳，侧，武僧
    74: SIDE,  # 双龙脚，侧，武僧
    61: SIDE,  # 双掌打，侧，武僧
    66: BACK,  # 破碎拳，背，武僧
    2255: BACK,  # 旋风刃，背
    3563: SIDE,  # 强甲破点突，侧
    2258: BACK,  # 攻其不备，背
    88: BACK,  # 樱花怒放，背
    3556: BACK,  # 龙尾，背
    3554: SIDE,  # 龙牙，侧
}


def get_nearest(me_pos, target, mode, dis=6):
    radius = target.hitbox_radius + dis - 0.5
    if mode == SIDE:
        area1 = sector(target.pos.x, target.pos.y, radius, angle, target.pos.r + math.pi / 2)
        area2 = sector(target.pos.x, target.pos.y, radius, angle, target.pos.r - math.pi / 2)
        area = cascaded_union([area1, area2])
    elif mode == FRONT:
        area = sector(target.pos.x, target.pos.y, radius, angle, target.pos.r)
    elif mode == BACK:
        area = sector(target.pos.x, target.pos.y, radius, angle, target.pos.r - math.pi)
    else:
        area = Point(target.pos.x, target.pos.y).buffer(radius)

    area = area.difference(Point(target.pos.x, target.pos.y).buffer(0.5))
    me = Point(me_pos.x, me_pos.y)
    if area.contains(me):
        return None
    p1 = nearest_points(area, me)[0]
    return p1.x, p1.y


def distance(xy1, xy2):
    return math.sqrt((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2)
