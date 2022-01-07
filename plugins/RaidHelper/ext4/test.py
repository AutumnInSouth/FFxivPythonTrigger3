from typing import TYPE_CHECKING

from FFxivPythonTrigger import plugins

from RaidHelper.utils import map_trigger, common_trigger

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.ability import ActionEffectEvent


@common_trigger('测试', 'network/zone/server/action_effect')
def test1(output, evt: 'ActionEffectEvent'):
    output(f'{evt.source_actor.name} use {evt.action_name}')


mist = map_trigger(339)


@mist('测试', 'network/zone/server/action_effect')
def test2(output, evt: 'ActionEffectEvent'):
    output(f'{evt.source_actor.name} use {evt.action_name} in mist')

