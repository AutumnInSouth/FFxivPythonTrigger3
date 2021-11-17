import pysaintcoinach

black_lists = {
    22000: {19789},
}
white_list = {
    22748: 229,  # 空无的恶意e12s
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
    24509: 0,  # 钻石神兵ex|敖龙厄运
    24536: 0,  # 钻石神兵|敖龙厄运
    24516: 0,  # 钻石神兵ex|自控导弹
    24539: 0,  # 钻石神兵|自控导弹

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
        203, 278,  # 击退
        27, 152, 165, 251  # 扩散
    }:
        action_idx.setdefault(key, []).append(action)
    action_name_idx.setdefault(action['Name'], {}).setdefault(key, []).append(action)


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
    return select['Omen'].key


# print(find_reflect(22294))


d = {action.key: (white_list[action.key] if action.key in white_list else find_reflect(action.key)) for action in action_sheet}
d = {a1: a2 for a1, a2 in d.items() if a2 and a1 != a2}
import pprint

with open('reflect.py', 'w') as f:
    f.write('reflect_data = ' + pprint.pformat(d, indent=4))
