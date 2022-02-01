import pysaintcoinach
from pathlib import Path

root_path = Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3')

game_path_chs = r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game'
realm_chs = pysaintcoinach.ARealmReversed(game_path_chs, pysaintcoinach.Language.chinese_simplified, root_path / 'DefinitionsExt3')  # 国服

game_path_eng = r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game'
realm_eng = pysaintcoinach.ARealmReversed(game_path_eng, pysaintcoinach.Language.english, root_path / 'DefinitionsExt4')  # 国际服


def e_obj_sgb_path_mapping(e_obj_id, realm=realm_eng):
    pass


def export_collision_mesh(territory_id, realm=realm_eng, output_path=root_path / 'collision_mesh'):
    territory_path = realm.game_data.get_sheet('TerritoryType')[territory_id]['Bg']
