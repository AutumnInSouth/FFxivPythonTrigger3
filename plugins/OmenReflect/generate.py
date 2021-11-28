import pysaintcoinach

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
    24087: 0, # 扎杜诺尔高原|赫德提特|24087|碎片打击
}
realm = pysaintcoinach.ARealmReversed(r'D:\game\WeGameApps\rail_apps\ffxiv(2000340)\game', pysaintcoinach.Language.chinese_simplified)
action_sheet = realm.game_data.get_sheet('Action')
import pprint

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


d = {action.key: (white_list[action.key] if action.key in white_list else find_reflect(action.key)) for action in action_sheet}
d = {a1: a2 for a1, a2 in d.items() if a2 and a1 != a2}
import pprint

with open('reflect.py', 'w') as f:
    f.write('reflect_data = ' + pprint.pformat(d, indent=4))
