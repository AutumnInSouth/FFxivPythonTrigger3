from ..message_processors.utils import NetworkZoneServerEvent


class CombatResetEvent(NetworkZoneServerEvent):
    id = NetworkZoneServerEvent.id + 'combat_reset'

    def __init__(self, server_event: NetworkZoneServerEvent):
        super().__init__(server_event.bundle_header, server_event.message_header, server_event.raw_message, server_event.struct_message)
