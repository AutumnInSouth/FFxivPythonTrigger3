from pathlib import Path
import pysaintcoinach

game_path_eng = r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game'
game_path_chs = r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game'
rp = Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3')
realm_eng = pysaintcoinach.ARealmReversed(game_path_eng, pysaintcoinach.Language.english, rp / 'DefinitionsExt4')
realm_chs = pysaintcoinach.ARealmReversed(game_path_chs, pysaintcoinach.Language.chinese_simplified, rp / 'DefinitionsExt3')

realm_chs_bp_sheet = realm_chs.game_data.get_sheet('BaseParam')

for row in realm_eng.game_data.get_sheet('Recipe'):
    rlv = row['RecipeLevelTable']
    if rlv.key >= 580:
        item = row['Item{Result}']
        if item['ClassJobCategory']['DRK']:

            ingredient = []
            for i in range(10):
                ii=row['Item{Ingredient}['+str(i)+']']
                if ii and ii.key: ingredient.append((ii['Name'],row['Amount{Ingredient}['+str(i)+']']))

            item_base_param = []
            for i in range(6):
                bp = item['BaseParam['+str(i)+']']
                if bp and bp.key: item_base_param.append((realm_chs_bp_sheet[bp.key]['Name'],item['BaseParamValue['+str(i)+']']))

            print(f"{item} | {item['ClassJobCategory']} | {', '.join(f'{i_n}+{i_v}' for i_n,i_v in item_base_param)}\n"
                  f"\tdif:{rlv['Difficulty'] * row['DifficultyFactor']/100:.0f}\tquality:{rlv['Quality'] * row['QualityFactor']/100:.0f}\tdur:{rlv['Durability'] * row['DurabilityFactor']/100:.0f}\n"
                  f"\t{','.join(str(i) for i in ingredient)}\n")
