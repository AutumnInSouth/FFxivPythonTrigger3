from pathlib import Path

import pysaintcoinach

root_path = Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3')

game_path_chs = r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game'
realm_chs = pysaintcoinach.ARealmReversed(game_path_chs, pysaintcoinach.Language.chinese_simplified, root_path / 'DefinitionsExt3')  # 国服

game_path_eng = r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game'
realm_eng = pysaintcoinach.ARealmReversed(game_path_eng, pysaintcoinach.Language.english, root_path / 'DefinitionsExt4')  # 国际服

realm = realm_eng

e_obj_sheet = realm.game_data.get_sheet('EObj')
territory_sheet = realm.game_data.get_sheet('TerritoryType')


def e_obj_sgb_path(e_obj_id: int):
    return e_obj_sheet[e_obj_id]['SgbPath']['SgbPath']


def export_collision_mesh(territory_id, output_path=root_path / 'collision_mesh'):
    territory = territory_sheet[territory_id]
    territory_path = territory['Bg']
    territory_name = territory['Name']
    list_pcb_path = "bg/" + territory_path + "/collision/list.pcb"
    bg_lgb_path = "bg/" + territory_path + "/level/bg.lgb"
    planmap_lgb_path = "bg/" + territory_path + "/level/planmap.lgb"
    collision_file_path = "bg/" + territory_path + "/collision/"

    s0 = realm.packs.get_file(bg_lgb_path).get_data()
    s1 = realm.packs.get_file(list_pcb_path).get_data()
    s2 = realm.packs.get_file(planmap_lgb_path).get_data()

    total_groups = 0
    total_entries = 0
