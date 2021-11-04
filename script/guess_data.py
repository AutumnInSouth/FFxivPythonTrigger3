import pysaintcoinach

realm = pysaintcoinach.ARealmReversed(r"D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game", pysaintcoinach.Language.chinese_simplified)
for sheet in realm._game_data.definition.sheet_definitions:
    try:
        print(sheet.name,realm.game_data.get_sheet(sheet.name)[478])
    except:
        pass
