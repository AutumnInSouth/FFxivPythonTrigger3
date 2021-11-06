from ctypes import *
from typing import Optional, Iterator, TYPE_CHECKING

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct, PointerStruct

from .enum import INVENTORY_CONTAINERS


class InventoryItem(OffsetStruct({
    'container_id': (c_short, 0x0),
    'idx': (c_short, 0x4),
    'item_id': (c_uint, 0x8),
    'count': (c_uint, 0xc),
    'collectability': (c_ushort, 0x10),
    'durability': (c_ushort, 0x12),
    'is_hq': (c_bool, 20)
}, full_size=56)):
    container_id: int
    idx: int
    item_id: int
    count: int
    collectability: int
    durability: int
    is_hq: bool


class InventoryPage(OffsetStruct({
    'page': POINTER(InventoryItem),
    'container_id': c_uint,
    'size': c_uint
}, full_size=24)):
    page: list[InventoryItem]
    container_id: int
    size: int

    def __iter__(self) -> Iterator[InventoryItem]:
        if not self.page: return
        for i in range(self.size):
            item = self.page[i]
            if item.item_id:
                yield self.page[i]


class InventoryPagePtr(PointerStruct(InventoryPage * 74, 0)):

    def get_item_in_containers(self, item_id: Optional[int], containers: set[int]) -> Iterator[InventoryItem]:
        containers = containers.copy()
        inventory = self.value
        if inventory is not None:
            for page in inventory:
                if page.container_id in containers:
                    containers.remove(page.container_id)
                    for item in page:
                        if item_id is None or item_id == item.item_id:
                            yield item
                    if not containers:
                        break

    def get_item_in_containers_by_key(self, item_id: Optional[int], *keys: str):
        containers = set()
        if keys[0] == "*":
            for pages in INVENTORY_CONTAINERS.values(): containers |= pages
        else:
            for key in keys: containers |= INVENTORY_CONTAINERS.get(key, set())
        return self.get_item_in_containers(item_id, containers)
