from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy

set_event_loop_policy(WindowsSelectorEventLoopPolicy())

from FFxivPythonTrigger import *
from FFxivPythonTrigger import logger

logger.print_log_level = logger.DEBUG

try:
    init()

    # register_module("SocketLogger")
    register_modules([
        'ChatLog',
        'Command',
        'HttpApi',
        'DebugExec',
        'XivMemory',
    ])
    run()
except Exception:
    pass
finally:
    close()
