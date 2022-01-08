import re
from pathlib import Path
import threading


class Vertex:
    def __init__(self, x, z, y):
        self.x = x
        self.z = z
        self.y = y
        self.north = None
        self.south = None
        self.west = None
        self.east = None

    def __hash__(self):
        return hash((self.x, self.z, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.z == other.z and self.y == other.y


def get_vertex(map_id, step, x, z, y):
    map_vertices = vertices.setdefault((map_id, step), {})
    k = (x, z, y)
    if k not in map_vertices: map_vertices[k] = Vertex(x, z, y)
    return map_vertices[k]


class Mesh:
    def __init__(self, path):
        self.path = Path(path)
        match = re.match(r'mesh_(\d+)_(\d+)_', self.path.name)
        if not match: raise ValueError('Invalid mesh name')
        self.map_id = int(match.group(1))
        self.step = int(match.group(2))
        self.vertices = []

    def load(self):
        with self.path.open('r') as f:
            for line in f:
                if line.startswith('v '):
                    x, z, y = [int(float(v) * 100) for v in line.split()[1:]]
                    vertex = get_vertex(self.map_id, self.step, x, z, y)
                    self.vertices.append(vertex)
                    vertex.idx = len(self.vertices)
                elif line.startswith('f '):
                    try:
                        p1, p2, p3, p4 = [self.vertices[int(v) - 1] for v in line.split()[1:]]
                    except IndexError:
                        with print_lock:
                            print(f'Invalid face at {self.path}: {line.strip()}')
                    else:
                        p1.north = p2
                        p2.west = p3
                        p3.south = p4
                        p4.east = p1
        with print_lock:
            print(f'Loaded {self.path}, {len(self.vertices)} vertices')


def write_mesh(map_id, map_step):
    with open(f'merge_mesh_{map_id:03d}_{map_step:03d}.obj', 'w') as f:
        map_vertices = list(vertices[(map_id, map_step)].values())
        vertices_idx = {}
        for vertex in map_vertices:
            f.write(f'v {vertex.x / 100:.2f} {vertex.z / 100:.2f} {vertex.y / 100:.2f}\n')
            vertices_idx[vertex] = len(vertices_idx)+1
        for vertex in map_vertices:
            p2 = vertex.north
            if p2 is None: continue
            p3 = p2.west
            if p3 is None: continue
            p4 = p3.south
            if p4 is None: continue
            f.write(f'f {vertices_idx[vertex]} {vertices_idx[p2]} {vertices_idx[p3]} {vertices_idx[p4]}\n')
    with print_lock:
        print(f'Wrote merge_mesh_{map_id:03d}_{map_step:03d}.obj with {len(map_vertices)} vertices')


if __name__ == '__main__':
    vertices = {}
    print_lock = threading.Lock()

    meshes = [Mesh(p) for p in Path('.').glob('mesh_*.obj')]
    print(f'select {len(meshes)} meshes')

    threads = []
    for mesh in meshes:
        t = threading.Thread(target=mesh.load)
        t.start()
        threads.append(t)
    for t in threads: t.join()

    threads = []
    for k in vertices:
        t = threading.Thread(target=write_mesh, args=k)
        t.start()
        threads.append(t)
    for t in threads: t.join()
