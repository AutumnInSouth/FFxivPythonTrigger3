from pathlib import Path

import common_define


class Mesh:
    def __init__(self):
        self.vertices: list[common_define.Vec3] = []
        self.indices: list[tuple[int, int, int]] = []


class Model:
    def __init__(self):
        self.name = ""
        self.meshes: list[Mesh] = []


class Group:
    def __init__(self):
        self.name = ""
        self.models: dict[str, Model] = {}


class Zone:
    def __init__(self):
        self.groups: dict[str, Group] = {}

    def export_obj(self, output_path: Path):
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w+") as f:
            indices_offset = 0
            obj_count = 0
            for group_name, group in self.groups.items():
                current_group = obj_count
                f.write(f"o {group_name}_{current_group}\n")
                for model_name, model in group.models.items():
                    obj_count += 1
                    f.write(f"o {model_name}_{current_group}_{obj_count}\n")
                    mesh_count = 0
                    for mesh in model.meshes:
                        for vertex in mesh.vertices:
                            f.write(f"v {vertex.x} {vertex.y} {vertex.z}\n")
                        f.write(f"g {model_name}_{current_group}_{obj_count}_{mesh_count}\n")
                        mesh_count += 1
                        for index in mesh.indices:
                            f.write(f"f {index[0] + indices_offset + 1} {index[1] + indices_offset + 1} {index[2] + indices_offset + 1}\n")
                        indices_offset += len(mesh.vertices)
