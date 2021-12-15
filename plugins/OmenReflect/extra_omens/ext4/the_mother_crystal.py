from typing import TYPE_CHECKING

from FFxivPythonTrigger import PluginBase
from FFxivPythonTrigger.decorator import event, re_event

from ..utils import add_omen

if TYPE_CHECKING:
    from XivNetwork.extra_messages.actor_add_remove_effect import ActorAddEffectEvent


@event('network/zone/server/effect_add')
def effect_add(plugin: PluginBase, evt: 'ActorAddEffectEvent'):
    if not evt.actor: return
    match evt.effect_id:
        case 2878:
            pos = evt.actor.pos
            add_omen(evt.actor, (pos.x, pos.y, pos.z), pos.r, 13, 2, 40)  # 外40内5月环
        case 2877:
            pos = evt.actor.pos
            add_omen(evt.actor, (pos.x, pos.y, pos.z), pos.r, 1, 2, 10)  # 10钢铁
        case 2876:
            pos = evt.actor.pos
            add_omen(evt.actor, (pos.x, pos.y, pos.z), pos.r, 188, 11, 40, 10)  # 40*10十字


events = {
    'effect_add': effect_add,
}
