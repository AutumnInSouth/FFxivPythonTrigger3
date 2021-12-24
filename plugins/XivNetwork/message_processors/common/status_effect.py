from typing import TYPE_CHECKING

from FFxivPythonTrigger.memory.struct_factory import *

"""
 /**
  * Structural representation of the packet sent by the server
  * Send the entire StatusEffect list
  */
  struct StatusEffect
  {
    uint16_t effect_id;
    uint16_t param;
    float duration;
    uint32_t sourceActorId;
  };
"""


class StatusEffect(OffsetStruct({
    'effect_id': c_uint16,
    'param': c_uint16,
    'duration': c_float,
    'source_actor_id': c_uint32
})):
    effect_id: int
    param: int
    duration: float
    source_actor_id: int


class StatusEffect30(StatusEffect * 30):
    if TYPE_CHECKING:
        def __iter__(self) -> StatusEffect: pass

        def __getitem__(self, item: int) -> StatusEffect: pass
