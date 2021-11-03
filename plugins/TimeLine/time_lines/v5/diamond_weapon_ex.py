from FFxivPythonTrigger import game_language


def cast(*args, **kwargs):
    pass


def effect(*args, **kwargs):
    pass


def jmp_if(*args, **kwargs):
    pass


def jmp(*args, **kwargs):
    pass


class TimeLine(object):
    def __getattr__(self, item):
        pass


match game_language:
    case 'chs':
        boss_name = '钻石神兵'
        diamond_rain = '钻石雨'
        adamant_purge = '装甲展开'
    case 'en':
        boss_name = 'The Diamond Weapon'
        diamond_rain = "Diamond Rain"
        adamant_purge = 'Adamant Purge'
    case l:
        raise Exception(f'Unsupported language [{l}]')


class DiamondWeaponEx(TimeLine):
    map_id = 123
    mission_id = 123

    def time_line(self):
        return {
            16.3: cast(source=boss_name, action_id=24487),
            21.3: effect(source=boss_name, action_id=24487, title=diamond_rain),
            36.5: effect(source=boss_name, action_id=[i for i in range(24482, 24485)], title=adamant_purge),
            37: jmp_if(condition=cast(source=boss_name, action_id=1121), to=49),
            40: effect(source=boss_name, action_id=1111, title="action a1"),
            45: effect(source=boss_name, action_id=1112, title="action a2"),
            46: jmp(target=59),
            50: effect(source=boss_name, action_id=1121, title="action b1"),
            55: effect(source=boss_name, action_id=1122, title="action b2"),
            60: effect(source=boss_name, action_id=1131, title="action c"),
        }
