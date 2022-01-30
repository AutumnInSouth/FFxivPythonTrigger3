c1 = 41 / 2048


def in_game_to_map_coord(pos, scale=100, offset=0): return (pos + offset) * c1 + 2050 / scale + 1


import pysaintcoinach
from pathlib import Path

game_path_chs = r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game'
game_path_eng = r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game'

rp = Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3')
realm_chs = pysaintcoinach.ARealmReversed(game_path_chs, pysaintcoinach.Language.chinese_simplified, rp / 'DefinitionsExt3')  # 国服
realm_eng = pysaintcoinach.ARealmReversed(game_path_eng, pysaintcoinach.Language.english, rp / 'DefinitionsExt4')  # 国际服

quest_sheet = realm_chs.game_data.get_sheet("Quest")
quest_by_name = {}
for quest in quest_sheet: quest_by_name.setdefault(quest['Name'], []).append(quest)

map_sheet = realm_chs.game_data.get_sheet("Map")
maps = {}
for row in map_sheet: maps.setdefault(getattr(row['TerritoryType'], 'key', 0), {})[row['MapIndex']] = row.key


def q(q_name):
    for row in quest_by_name[q_name]:
        print(f"{q_name} <q quest_id={row.key}> 要求等级:{row['ClassJobLevel[0]']}")
        if row['PreviousQuest[0]']:
            prev = row['PreviousQuest[0]']
            print(f"    前置: {prev['Name']} 等级:{prev['ClassJobLevel[0]']} <q quest_id={prev.key}>")
        location = row['Issuer{Location}']
        print(f"    接取：[{row['Issuer{Start}']}] <p map_id={location['Map'].key} x={location['X']:.1f} y={location['Z']:.1f} z=0>")


for name in [
    "暗黑骑士的传言",
    "如何成为占星术士",
    "如何成为机工士",
    "武士之路",
    "成为赤魔法师",
    "舞者降临",
    "成为绝枪战士",
    "自称青魔法师的男人",
    "我的专属陆行鸟（双蛇党）",
    "我的专属陆行鸟（黑涡团）",
    "我的专属陆行鸟（恒辉队）",
    "可靠的搭档",
    "身着幻影的男人",
    "华丽的投影世界",
]: q(name)
