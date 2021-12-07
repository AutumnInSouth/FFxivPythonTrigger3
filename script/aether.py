from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.saint_coinach import realm


def main():
    if not plugins.XivMemory.targets.current:
        raise plugins.XivException("No target selected.")
    t_npc_id = plugins.XivMemory.targets.current.b_npc_id
    current_map_id = plugins.XivMemory.zone_id
    aether_currents = {row.key for row in realm.game_data.get_sheet('AetherCurrent')}
    zone_aether_currents = {row['Object']['Data'] for row in realm.game_data.get_sheet('Level') if
                            getattr(row['Territory'], 'key', 0) == current_map_id and
                            getattr(getattr(row['Object'], 'sheet', None), 'name', None) == 'EObj' and
                            row['Object']['Data'] in aether_currents}
    for zone_aether_current in zone_aether_currents:
        print(f"trying aether_current {zone_aether_current:x}(zone:{current_map_id}) on b_npc {t_npc_id:x}")
        plugins.XivNetwork.send_messages('zone', ('EventStart', {
            'target_id': t_npc_id,
            'unk0': 1,
            'event_id': zone_aether_current & 0xffff,
            'category': 0x2b,
        }), "EventFinish", response_timeout=10)


def test():
    plugins.XivNetwork.send_messages('zone', ('EventStart', {
        'target_id': plugins.XivMemory.targets.current.b_npc_id,
        'unk0': 1,
        'event_id': 0x13a,
        'category': 0x2b,
    }), "EventFinish", response_timeout=10)
    print(1)


test()
