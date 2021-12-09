from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.saint_coinach import realm


def main():
    if not plugins.XivMemory.targets.current or not plugins.XivMemory.targets.current.b_npc_id:
        raise plugins.XivException("No target selected.")
    t_npc_id = plugins.XivMemory.targets.current.b_npc_id
    current_map_id = plugins.XivMemory.zone_id
    aetherytes = {row.key for row in realm.game_data.get_sheet('Aetheryte')
                  if getattr(row['Territory'], 'key', 0) == current_map_id and
                  (not row['RequiredQuest'] or plugins.XivMemory.calls.is_quest_finished(row['RequiredQuest'].key))}
    for aetheryte in aetherytes:
        print(f"trying Aetheryte {aetheryte:x}(zone:{current_map_id}) on b_npc {t_npc_id:x}")
        plugins.XivNetwork.send_messages('zone', ('EventStart', {
            'target_id': t_npc_id,
            'unk0': 1,
            'event_id': aetheryte,
            'category': 5,
        }), "EventFinish", response_timeout=10)


main()
