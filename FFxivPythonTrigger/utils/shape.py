from math import sin, cos
from shapely.affinity import rotate
from shapely import geometry


def rotated_rect(cx: float, cy: float, w: float, h: float, facing_rad: float) -> 'geometry.Polygon':
    return rotate(geometry.box(cx - w / 2, cy, cx + w / 2, cy + h), -facing_rad, origin=(cx, cy), use_radians=True)


def circle(cx: float, cy: float, radius: float) -> 'geometry.Polygon':
    return geometry.Point(cx, cy).buffer(radius)


def sector(cx: float, cy: float, radius: float, angle_rad: float, facing_rad: float,
           steps: int = 100) -> 'geometry.Polygon':
    step_angle_width = angle_rad / steps
    segment_vertices = [(cx, cy), (cx, cy + radius)]
    segment_vertices += [(cx + sin(i * step_angle_width) * radius, cy + cos(i * step_angle_width) * radius) for i in
                         range(1, steps)]
    return rotate(geometry.Polygon(segment_vertices), -(facing_rad - angle_rad / 2), origin=(cx, cy), use_radians=True)
