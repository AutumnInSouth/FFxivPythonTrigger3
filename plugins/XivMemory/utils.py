from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import XivMemory


class Utils(object):
    def __init__(self, plugin: 'XivMemory'):
        self.plugin = plugin

    @property
    def mo_entity(self):
        return self.plugin.mo_ui_entity or self.plugin.targets.mouse_over

    @property
    def mo_location(self):
        entity = self.mo_entity
        if entity: return entity.pos.x, entity.pos.y, entity.pos.z
        try:
            return self.plugin.calls.ray_cast.cursor_to_world()
        except ValueError:
            return None
