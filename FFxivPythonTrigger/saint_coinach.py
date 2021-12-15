import os

import pysaintcoinach
from pathlib import Path
from FFxivPythonTrigger import game_ext,game_language

from .logger import info

if 'game_dir' in os.environ:
    game_dir = os.environ.get('game_dir')
else:
    from FFxivPythonTrigger.memory import PROCESS_FILENAME

    game_dir = Path(PROCESS_FILENAME).parent

match game_ext:
    case 3:
        def_path = Path(os.getcwd()) / 'DefinitionsExt3'
    case 4:
        def_path = Path(os.getcwd()) / 'DefinitionsExt4'
    case _:
        raise ValueError('Unsupported game version')

language = pysaintcoinach.ex.language.Language(game_language)
realm = pysaintcoinach.ARealmReversed(game_dir, language, def_path)
info("pysaintcoinach", f"{game_language} realm initialized")

"""realm._game_data.definition.sheet_definitions"""
"""realm.game_data.get_sheet()"""

action_sheet = realm.game_data.get_sheet('Action')
action_names = {row.key: row['Name'] for row in action_sheet}
item_sheet = realm.game_data.get_sheet('Item')
item_names = {row.key: row['Name'] for row in item_sheet}
status_sheet = realm.game_data.get_sheet('Status')
status_names = {row.key: row['Name'] for row in status_sheet}
class_job_sheet = realm.game_data.get_sheet('ClassJob')
class_job_names = {row.key: row['Name'] for row in class_job_sheet}
territory_type_sheet = realm.game_data.get_sheet('TerritoryType')
territory_type_names = {row.key: row['PlaceName'] for row in territory_type_sheet}
