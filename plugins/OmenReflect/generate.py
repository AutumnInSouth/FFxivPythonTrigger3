from pathlib import Path

import pysaintcoinach
# reflect

black_lists = {
    22000: {19789},
}
white_list = {
    22748: 229,  # 空无的恶意e12s
    22710: 229,  # 拒绝之手e12s
    22129: 2,  # 闪光e11s
    16524: 1,
    16525: 1,  # 赤烈风rdm
    16526: 1,  # 赤震雷rdm
    21998: 1,  # 暗黑领域|暗黑之云|暗黑森林
    21999: 1,  # 暗黑天空|暗黑之云|暗黑森林
    22332: 0,  # 凋零爆发e10s
    22333: 0,  # 凋零爆发e10s
    22306: 0,  # 影之沼泽e10s
    8075: 229,  # 神龙巨浪->击退
    22099: 114,  # 游末邦监狱|绝命战士|22099|火燃爆
    24522: 0,  # 钻石神兵ex|光子爆发
    24544: 0,  # 钻石神兵|光子爆发
    24516: 0,  # 钻石神兵ex|自控导弹
    24539: 0,  # 钻石神兵|自控导弹
    21966: 188,  # 绿宝石神兵|恩惠终结：叁
    21963: 188,  # 绿宝石神兵|恩惠终结：贰
    21950: 203,  # 绿宝石神兵|魔导加农炮
    21933: 27,  # 绿宝石神兵|消灭冲击
    19658: 1,  # 瓦厉斯·耶·加尔乌斯|19658|更高
    19681: 1,  # 瓦厉斯·耶·加尔乌斯|19681|更高
    9232: 2,  # 德尔塔幻境4|新生艾克斯迪司|9232|外围暗黑光
    9292: 2,  # 德尔塔幻境4|新生艾克斯迪司|9292|中核暗黑光
    15952: 244,  # 伊甸甲板|虚无行者|15952|末日虚无切
    24235: 0,  # 希望之炮台：“塔”|杰克|24235|魔法冲击弹α|
    23649: 0,  # 希望之炮台：“塔”|格雷特|23649|魔法弹α|
    23651: 0,  # 希望之炮台：“塔”|韩塞尔|23651|魔法弹放射|
    24588: 27,  # 希望之炮台：“塔”|红衣少女|24588|大爆炸：白|
    24589: 27,  # 希望之炮台：“塔”|红衣少女|24589|大爆炸：黑|
    23558: 2,  # 希望之炮台：“塔”|孟子|23558|全方位攻击|
    23552: 2,  # 希望之炮台：“塔”|荀子|23552|武装启动|
    23553: 2,  # 希望之炮台：“塔”|荀子|23553|武装启动|
    23555: 2,  # 希望之炮台：“塔”|荀子|23555|武装启动|
    23556: 2,  # 希望之炮台：“塔”|荀子|23556|武装启动|
    23540: 2,  # 希望之炮台：“塔”|开花的神明|23540|崩塌
    23510: 2,  # 希望之炮台：“塔”|伪造的神明|23510|释放魔力|
    23511: 2,  # 希望之炮台：“塔”|伪造的神明|23511|释放魔力|
    23515: 0,  # 希望之炮台：“塔”|伪造的神明|23515|
    23516: 0,  # 希望之炮台：“塔”|伪造的神明|23516|
    22357: 203,  # 女王古殿|大兀|22357|野性嚎叫
    22375: 203,  # 女王古殿|大兀|22375|野性嚎叫
    11080: 0,  # 禁绝幻想|迦楼罗|11080|烈风刃
    24087: 0,  # 扎杜诺尔高原|赫德提特|24087|碎片打击
    25324: 0,  # The Tower of Babil|Barnabas|25324|Shocking Force
    25352: 0,  # The Tower of Babil|Anima|25352|Erupting Pain
    27851: 0,  # Vanaspati|Terminus Wrecker|27851|Poison Heart
    25168: 0,  # Vanaspati|Svarbhanu|25168|Cosmic Kiss
    15512: 3,  # The Qitana Ravel|Batsquatch|15512|Towerfall
    25142: 0,  # Vanaspati|Terminus Snatcher|25142|Wallow
    27490: 0,  # The Dark Inside|Zodiark|27490|Ania
    26570: 2,  # The Dark Inside|Arcane Sigil|26570|Esoteric Ray
    26596: 2,  # The Dark Inside|Arcane Sigil|26596|Esoteric Ray
    25180: 0,  # Ktisis Hyperboreia|Lyssa|25180|Heavy Smash
    **{s: 5 for s in range(25734, 25740)},  # Ktisis Hyperboreia|Ladon Lord|25734|Pyric Breath
    25742: 0,  # Ktisis Hyperboreia|Ladon Lord|25742|Pyric Blast
    25897: 0,  # Ktisis Hyperboreia|Hermes|25897|True Aero II
    27036: 0,  # Magna Glacies|Terminus Vanquisher|27036|Depress
    27038: 0,  # Magna Glacies|Terminus Vanquisher|27038|Accursed Tongue
    25677: 0,  # The Aitiascope|Livia the Undeterred|25677|Ignis Odi
    25923: 0,  # The Dead Ends|Caustic Grebuloff|25923|Befoulment
    25924: 0,  # The Dead Ends|Caustic Grebuloff|25924|Befoulment
    28359: 0,  # The Dead Ends|Peacekeeper|28359|Infantry Deterrent
    25946: 0,  # The Dead Ends|Ra-la|25946|Benevolence
    25948: 0,  # The Dead Ends|Ra-la|25948|Still Embrace
    26190: 0,  # The Final Day|The Endsinger|26190|Nemesis|
    26197: 0,  # The Final Day|The Endsinger|26197|Nemesis|
    27480: 0,  # The Final Day|The Endsinger|27480|Planetes
    26195: 0,  # The Final Day|The Endsinger|26195|Hubris
    26432: 0,  # Smileton|Face|26432|Temper, Temper
    26451: 0,  # Smileton|The Big Cheese|26451|Electric Arc
    25386: 0,  # The Stigma Dreamscape|Proto-Omega|25386|Electric Slide|4.70s|0|0(2/6/0)=>1|
    25387: 0,  # The Stigma Dreamscape|Proto-Omega|25387|Mustard Bomb|4.70s|0|0(2/5/0)=>1|
    26053: 28,
    26256: 28,
    27793: 28,
    27794: 28,
    **{s: 28 for s in range(28433, 28437)},  # The Mothercrystal|Hydaelyn|Aureole|
}
# realm = pysaintcoinach.ARealmReversed(r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game', pysaintcoinach.Language.chinese_simplified)
realm = pysaintcoinach.ARealmReversed(
    r'D:\game\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game',
    pysaintcoinach.Language.english,
    Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3\DefinitionsExt4')
)
realm_chs = pysaintcoinach.ARealmReversed(
    r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game',
    pysaintcoinach.Language.chinese_simplified,
    Path(r'D:\game\ff14_res\FFxivPythonTrigger3\FFxivPythonTrigger3\DefinitionsExt4')
)
action_sheet = realm.game_data.get_sheet('Action')
action_sheet_chs = realm_chs.game_data.get_sheet('Action')
chs_name = lambda key:action_sheet_chs[key]['Name']

compare_field = ['Animation{Start}', 'VFX', 'Animation{End}', 'ActionTimeline{Hit}']
# idx: 'CastType', 'EffectRange', 'XAxisModifier'
action_with_omen = [action for action in action_sheet if action['Omen'].key]
action_idx = {}
action_name_idx = {}
for action in action_with_omen:
    key = action['CastType'], action['EffectRange'], action['XAxisModifier']
    if action['Omen'].key not in {
        203, 278, 139, 229, 314,  # 击退
        27, 152, 165, 251  # 扩散
    }:
        action_idx.setdefault(key, []).append(action)
    action_name_idx.setdefault(action['Name'], {}).setdefault(key, []).append(action)

translate = {
    110: 1,
    104: 1,
    290: 1,
    59: 1,
    181: 1,
    170: 243,
    173: 243,
    169: 1,
    57: 1,
    172: 1,
    171: 2,
    174: 2,
    326: 2,
    182: 2,
    357: 1,
    350: 1,
    66: 1,
}


def find_reflect(action_id):
    if not action_id % 1000: print(action_id)
    action_data = action_sheet[action_id]
    if action_data['Omen'].key or action_data['CastType'] < 2 or not action_data['Cast<100ms>']: return 0
    key = action_data['CastType'], action_data['EffectRange'], action_data['XAxisModifier']
    allow_action = action_name_idx.get(action_data['Name'], {}).get(key) or action_idx.get(key)
    if not allow_action: return 0
    black_list = black_lists.get(action_id)
    if black_list: allow_action = [a for a in allow_action if a.key not in black_list]
    if not allow_action: return 0
    select = min(allow_action, key=lambda a: (-sum(a[f] == action_data[f] for f in compare_field), a['Omen'].key))
    # print(action_id, action_data, select, ';', ','.join(a['Name'] for a in allow_action))
    return translate.get(select['Omen'].key, select['Omen'].key)


# print(find_reflect(22294))


d = {action.key: (white_list[action.key] if action.key in white_list else find_reflect(action.key))
                            for action in action_sheet}
d = {a1: a2 for a1, a2 in d.items() if a2 and a1 != a2}
import pprint

with open('reflect.py', 'w') as f:
    f.write('reflect_data = ' + pprint.pformat(d, indent=4))
