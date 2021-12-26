from typing import Callable

from . import game_version
from .storage import ModuleStorage, BASE_PATH
from .memory import BASE_ADDR
from .logger import Logger
from .text_pattern import find_signature_point, find_signature_address

_storage = ModuleStorage(BASE_PATH / "Address")
_storage_data = _storage.data.setdefault(game_version, {})
_storage.save()


class AddressManager(object):
    def __init__(self, key: str, logger: Logger, force_search: bool = False):
        self.storage = _storage_data.setdefault(key, {})
        self.logger = logger
        self.force_search = force_search

    def scan_address(self, key: str, sig: str, add=0):
        return self.get(key, find_signature_address, sig, add=BASE_ADDR + add)

    def scan_point(self, key: str, sig: str, add=0):
        return self.get(key, find_signature_point, sig, add=BASE_ADDR + add)

    def get(self, key: str, call: Callable, param: any = None, add=0, **kwargs):
        if key in self.storage and param == self.storage[key]['param'] and not self.force_search:
            offset = self.storage[key]['offset']
            address = offset + BASE_ADDR
            msg = "address load [{address}] [+{offset}] \"{name}\""
        else:
            address = call(param, **kwargs)
            address += add
            offset = address - BASE_ADDR
            self.storage[key] = {
                'call': call.__name__,
                'param': param,
                'offset': offset,
            }
            msg = "address found [{address}] [+{offset}] \"{name}\""
            _storage.save()
        self.logger.debug(msg.format(name=key, address=hex(address), offset=hex(offset)))
        return address

    def load(self, sig_data: dict[str, dict]):
        return {
            key: self.get(key, _sig_data['call'], _sig_data['param'], add=_sig_data.get('add', 0), **_sig_data.get('kwargs', {}))
            for key, _sig_data in sig_data.items()
        }
