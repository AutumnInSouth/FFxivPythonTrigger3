from pathlib import Path
from json import load, decoder, dumps
from typing import Annotated, Union
from os import getcwd, environ
from inspect import getmodule, stack
from re import compile

STORAGE_DIRNAME: Annotated[str, "the directory name where the storage will be"] = environ.setdefault('fpt_data_dir', "AppData")
DATA_FILENAME: Annotated[str, "the file name where json data will be stored"] = "data.json"
MODULE_DIRNAME: Annotated[str, "the directory under base storage directory for modules"] = "Plugins"

BASE_PATH: Annotated[Path, "the base path of the storage"] = Path(getcwd()) / STORAGE_DIRNAME
BASE_PATH.mkdir(exist_ok=True, parents=True)

windows_unavailable_name_characters = compile(r"[<>:\"\\/|?*\x00-\x31]")


class ModuleStorage(object):
    _path: Path
    data: Annotated[dict, "data stored"]

    def __init__(self, path: Union[Path, str]):
        if type(path) == str:
            path = Path(path)
        self._path = path.absolute()
        self.data = self.load() if self._path.exists() else dict()

    @property
    def path(self) -> Path:
        """
        get the path assigned to the module
        """
        self._path.mkdir(exist_ok=True, parents=True)
        return self._path

    def load(self) -> dict:
        """
        try to load data from storage file

        :return: load data, if data file not exists, return a new dict
        """
        file = self._path / DATA_FILENAME
        if file.exists() and file.stat().st_size:
            with open(file, encoding='utf-8') as fi:
                try:
                    return load(fi)
                except decoder.JSONDecodeError:
                    return {"data": fi.read()}
        else:
            return dict()

    def save(self) -> bool:
        """
        save data to file

        :return: true is data is saved, false if no data to be saved
        """
        if self.data:
            self._path.mkdir(exist_ok=True, parents=True)
            with open(self._path / DATA_FILENAME, 'w+', encoding='utf-8') as fo:
                fo.write(dumps(self.data, indent=4, ensure_ascii=False))
            return True
        else:
            return False


def get_module_storage(module_name: str = None) -> ModuleStorage:
    """
    get the storage of a module

    :param module_name:(optional) used module name
    """
    if module_name is None:
        module_name = getmodule(stack()[1][0]).__name__
    module_name = windows_unavailable_name_characters.sub('', module_name).replace(" ", "_")
    return ModuleStorage(BASE_PATH / MODULE_DIRNAME / module_name)
