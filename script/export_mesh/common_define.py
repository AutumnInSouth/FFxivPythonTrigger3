from ctypes import *
import math


class Vec3(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
    ]

    def scale(self, x: float, y: float, z: float):
        self.x *= x
        self.y *= y
        self.z *= z
        return self

    def transform(self, x: float, y: float, z: float):
        self.x += x
        self.y += y
        self.z += z
        return self

    def rotate_x(self, x: float):
        cos_x = math.cos(x)
        sin_x = math.sin(x)
        new_y = self.y * cos_x - self.z * sin_x
        new_z = self.y * sin_x + self.z * cos_x
        self.y = new_y
        self.z = new_z
        return self

    def rotate_y(self, y: float):
        cos_y = math.cos(y)
        sin_y = math.sin(y)
        new_x = self.x * cos_y - self.z * sin_y
        new_z = self.x * sin_y + self.z * cos_y
        self.x = new_x
        self.z = new_z
        return self

    def rotate_z(self, z: float):
        cos_z = math.cos(z)
        sin_z = math.sin(z)
        new_x = self.x * cos_z - self.y * sin_z
        new_y = self.x * sin_z + self.y * cos_z
        self.x = new_x
        self.y = new_y
        return self


vec3_size = sizeof(Vec3)


def get_string(buf: bytearray, offset: int = 0, encoding='utf-8') -> str:
    return buf[offset:buf.find(b'\0', offset)].decode(encoding)
