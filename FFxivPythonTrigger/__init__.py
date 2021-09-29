try:
    from pathlib import Path

    from .memory import PROCESS_FILENAME

    with open(Path(PROCESS_FILENAME).parent / "ffxivgame.ver") as fi:
        game_version = fi.read()
except FileNotFoundError:
    game_version = None
else:
    from .ffxiv_python_trigger import *
