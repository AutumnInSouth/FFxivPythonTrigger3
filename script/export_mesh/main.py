import sys
from pathlib import Path
import threading

root_path = Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3')
sys.path.insert(0, str(root_path))

import pysaintcoinach

game_path_chs = r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game'
realm_chs = pysaintcoinach.ARealmReversed(game_path_chs, pysaintcoinach.Language.chinese_simplified, root_path / 'DefinitionsExt3')  # 国服

game_path_eng = r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game'
realm_eng = pysaintcoinach.ARealmReversed(game_path_eng, pysaintcoinach.Language.english, root_path / 'DefinitionsExt4')  # 国际服

realm = realm_eng

import lgb_define
import pcb_define
import sgb_define
import exporter
import common_define

print_lock = threading.Lock()
e_obj_sheet = realm.game_data.get_sheet('EObj')
territory_sheet = realm.game_data.get_sheet('TerritoryType')

_pcb_cache = {}


def file_name_safe_str(file_name: str):
    return ''.join(c for c in file_name if c.isalnum() or c in '._-')


def get_pcb_file(pcb_path: str) -> pcb_define.PcbFile | None:
    if pcb_path not in _pcb_cache:
        file = realm.packs.get_file(pcb_path)
        if file is None:
            # print(f"[!] {pcb_path} not found")
            # print(''.join(traceback.format_stack()))
            _pcb_cache[pcb_path] = None
        else:
            # print(f"[*] {pcb_path} found")
            _pcb_cache[pcb_path] = pcb_define.PcbFile(bytearray(file.get_data()))
    return _pcb_cache[pcb_path]


_sgb_cache = {}


def get_sgb_file(sgb_path: str) -> sgb_define.SgbFile | None:
    if sgb_path not in _sgb_cache:
        file = realm.packs.get_file(sgb_path)
        if file is None:
            # print(f"[!] {sgb_path} not found")
            _sgb_cache[sgb_path] = None
        else:
            # print(f"[*] {sgb_path} found")
            _sgb_cache[sgb_path] = sgb_define.SgbFile(bytearray(file.get_data()))
    return _sgb_cache[sgb_path]


def e_obj_sgb_path(e_obj_id: int):
    try:
        return e_obj_sheet[e_obj_id]['SgbPath']['SgbPath']
    except:
        return


def list_pcb(territory_path: str):
    file = realm.packs.get_file("bg/" + territory_path + "/collision/list.pcb")
    if file is None: return
    data = file.get_data()
    ptr = 0x20
    size = len(data)
    while ptr < size:
        yield int.from_bytes(data[ptr:ptr + 2], byteorder='little')
        ptr += 0X20


def export_collision_mesh(territory_id, output_path=root_path / 'mesh'):
    exported_zone = exporter.Zone()

    territory = territory_sheet[territory_id]
    territory_path = territory['Bg'].split('/level')[0]
    territory_name = territory['Name']

    collision_file_path = f"bg/{territory_path}/collision/"
    list_pcb_paths = [f"{collision_file_path}tr{t_id:04d}.pcb" for t_id in list_pcb(territory_path)]
    lgb_list = [
        lgb_define.LgbFile(bytearray(realm.packs.get_file(f"bg/{territory_path}/level/bg.lgb").get_data())),
        lgb_define.LgbFile(bytearray(realm.packs.get_file(f"bg/{territory_path}/level/planmap.lgb").get_data())),
    ]

    total_models = 0

    def build_model_entry(
            pcb_file: pcb_define.PcbFile,
            exported_group: exporter.Group,
            name, group_name,
            scale: common_define.Vec3 = None,
            rotation: common_define.Vec3 = None,
            translation: common_define.Vec3 = None,
            sgb_entry: sgb_define.SgbModelEntry = None,
    ):
        nonlocal total_models
        model = exporter.Model()
        model.name = f"{name}_{total_models:04d}"
        total_models += 1
        for entry in pcb_file.entries:
            mesh = exporter.Mesh()
            start_v = entry.header.v1
            x_base = abs(entry.header.v2.x - start_v.x)
            y_base = abs(entry.header.v2.y - start_v.y)
            z_base = abs(entry.header.v2.z - start_v.z)

            def make_translate(v: common_define.Vec3):
                if sgb_entry is not None:
                    _scale = sgb_entry.header.scale
                    v.scale(_scale.x, _scale.y, _scale.z)
                    _rotation = sgb_entry.header.rotation
                    v.rotate_x(_rotation.x).rotate_y(-_rotation.y).rotate_z(_rotation.z)
                    _translation = sgb_entry.header.translation
                    v.transform(_translation.x, _translation.y, _translation.z)
                if scale is not None:
                    v.scale(scale.x, scale.y, scale.z)
                    v.rotate_x(rotation.x).rotate_y(-rotation.y).rotate_z(rotation.z)
                    v.transform(translation.x, translation.y, translation.z)
                return v

            for v in entry.data.vertices:
                mesh.vertices.append(make_translate(common_define.Vec3(v.x, v.y, v.z)))
            for v in entry.data.vertices_i16:
                mesh.vertices.append(make_translate(common_define.Vec3(
                    v.x / 0xffff, v.y / 0xffff, v.z / 0xffff
                ).scale(
                    x_base, y_base, z_base
                ).transform(
                    start_v.x, start_v.y, start_v.z
                )))
            for i in entry.data.indices:
                mesh.indices.append(i.index[:])
            model.meshes.append(mesh)
        exported_group.models[model.name] = model

    def pcb_transform_model(
            pcb_file_name: str,
            exported_group: exporter.Group,
            scale: common_define.Vec3 = None,
            rotation: common_define.Vec3 = None,
            translation: common_define.Vec3 = None,
            sgb_model: sgb_define.SgbModelEntry = None,
    ):
        pcb_file = get_pcb_file(pcb_file_name)
        if pcb_file is not None:
            build_model_entry(
                get_pcb_file(pcb_file_name),
                exported_group,
                pcb_file_name,
                exported_group.name,
                scale,
                rotation,
                translation,
                sgb_model
            )

    def export_sgb_model(sgb_path: str, exported_group: exporter.Group, gimmick_entry: lgb_define.GimmickData):
        sgb_file = get_sgb_file(sgb_path)
        if sgb_file is None: return
        for sgb_entry in sgb_file.iter_group_entries():
            if sgb_entry.model_entry_type == sgb_define.SgbGroupEntryType.Gimmick:
                sub_sgb_file = get_sgb_file(sgb_entry.model_file_name)
                if sub_sgb_file is not None:
                    for sub_entry in sub_sgb_file.iter_group_entries():
                        if sub_entry.model_entry_type == sgb_define.SgbGroupEntryType.Model:
                            pcb_transform_model(
                                sub_entry.model_file_name
                                    .replace('/bgparts/', '/collision/')
                                    .replace('.mdl', '.pcb'),
                                exported_group,
                                gimmick_entry.header.scale,
                                gimmick_entry.header.rotation,
                                gimmick_entry.header.translation,
                                sub_entry
                            )
            pcb_transform_model(
                sgb_entry.collision_file_name,
                exported_group,
                gimmick_entry.header.scale,
                gimmick_entry.header.rotation,
                gimmick_entry.header.translation,
                sgb_entry
            )

    exported_terrain_group = exporter.Group()
    exported_terrain_group.name = f"{territory_name}_terrain"

    for file_name in list_pcb_paths:
        pcb_transform_model(file_name, exported_terrain_group)

    exported_zone.groups[exported_terrain_group.name] = exported_terrain_group

    for lgb_file in lgb_list:
        for group in lgb_file.groups:
            sub_exported_group = exporter.Group()
            sub_exported_group.name = group.name
            for entry in group.entries:
                match entry.entry_type():
                    case lgb_define.LgbEntryType.BgParts:
                        header = entry.header
                        pcb_transform_model(entry.collision_file_name, sub_exported_group, header.scale, header.rotation, header.translation)
                    case lgb_define.LgbEntryType.Gimmick:
                        export_sgb_model(entry.gimmick_file_name, sub_exported_group, entry)
                    case lgb_define.LgbEntryType.EventObject:
                        # unk file_name in https://github.com/SapphireServer/Sapphire/blob/master/src/tools/pcb_reader/main.cpp#L495 ?
                        # header = entry.header
                        # pcb_transform_model(file_name, sub_exported_group, header.scale, header.rotation, header.translation)
                        sgb_path = e_obj_sgb_path(entry.header.e_obj_id)
                        if sgb_path:
                            export_sgb_model(sgb_path, sub_exported_group, entry)
                            sgb_file = get_sgb_file(sgb_path)
                            if sgb_file is not None:
                                for offset_1c_file in sgb_file.state_entries:
                                    export_sgb_model(offset_1c_file, sub_exported_group, entry)
            exported_zone.groups[sub_exported_group.name] = sub_exported_group
    exported_zone.export_obj(output_path / f"{territory_id}.obj")
    try:
        territory = realm_chs.game_data.get_sheet('TerritoryType')[territory_id]
    except:
        pass
    print(
        f"Exported {territory_name} {territory['PlaceName{Region}']} - {territory['PlaceName{Zone}']} - {territory['PlaceName']} => {territory_id}.obj")


def export_all_multi_thread():
    jobs = []
    for row in realm.game_data.get_sheet('TerritoryType'):
        if row['Bg']:
            t = threading.Thread(target=export_collision_mesh, args=(row.key,))
            t.start()
            jobs.append(t)
    for job in jobs:
        job.join()


def export_all_normal():
    for row in realm.game_data.get_sheet('TerritoryType'):
        if row['Bg']:
            export_collision_mesh(row.key)


try:
    export_all_normal()
except Exception as e:
    import traceback

    traceback.print_exc()
#     input()
#
# for t_id in range(128, 134):
#     export_collision_mesh(t_id)
