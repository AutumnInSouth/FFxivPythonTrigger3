import action as action

import pysaintcoinach

black_lists = {
    22000: {19789},
}
white_list = {
    # 22642: 22642,
    # 22646: 22646,
    22748: 15942
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
    if action_data['Omen'].key or action_data['CastType'] < 2 or not action_data['Cast<100ms>']: return action_id
    key = action_data['CastType'], action_data['EffectRange'], action_data['XAxisModifier']
    allow_action = action_name_idx.get(action_data['Name'], {}).get(key) or action_idx.get(key)
    if not allow_action: return action_id
    black_list = black_lists.get(action_id)
    if black_list: allow_action = [a for a in allow_action if a.key not in black_list]
    if not allow_action: return action_id
    select = min(allow_action, key=lambda a: (-sum(a[f] == action_data[f] for f in compare_field), a['Omen'].key))
    # print(action_id, action_data, select, ';', ','.join(a['Name'] for a in allow_action))
    return select.key

#print(find_reflect(22294))


d = {action.key: white_list.get(action.key) or find_reflect(action.key) for action in action_sheet}
d = {a1: a2 for a1, a2 in d.items() if a1 != a2}
import pprint
with open('reflect.py','w')as f:
    f.write('reflect_data = '+pprint.pformat(d, indent=4))

