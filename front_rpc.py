import argparse
import ctypes
import sys
import time
import os

application_path = os.path.dirname(__file__)
os.chdir(application_path)
sys.path.insert(0, application_path)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int)
parser.add_argument('-sr', dest='skip_requirement_check')
args = parser.parse_args()


def e_print(*args, **kwargs): print(*args, file=sys.stderr, **kwargs)


try:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin()
except:
    is_admin = False
if not is_admin:
    e_print("please start as admin")
    exit(1)

if not args.port: exit(1)

if not args.skip_requirement_check:
    from FFxivPythonTrigger import requirements_controller

    requirements = [i for i in open('requirements.txt', encoding='utf-8', mode='r').read().split('\n') if i]
    if not requirements_controller.test_requirements(requirements):
        if requirements_controller.pip_source is None:
            e_print("no valid pip source")
            exit(1)
        print('using pypi source [%s]' % requirements_controller.pip_source_name)
        requirements_controller.install(*requirements)
        if not requirements_controller.test_requirements(requirements):
            e_print("cant install requirements")
            exit(1)

import locale
import _thread
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.rpc_server import RpcServer

ep = process.enable_privilege()
if ep:
    e_print(f"enable privileges failed with err code {ep}")
    exit(1)
python_version = "python{0}{1}.dll".format(sys.version_info.major, sys.version_info.minor)
python_lib = process.module_from_name(python_version).filename
local_handle = kernel32.GetModuleHandleW(python_version)
funcs = {k: kernel32.GetProcAddress(local_handle, k) for k in
         [b'Py_InitializeEx', b'PyRun_SimpleString', b'Py_FinalizeEx']}


class FrontRpc(object):
    def get_game_process(self, game_execution: str):
        return [p.th32ProcessID for p in process.list_processes()
                if game_execution in p.szExeFile.decode(locale.getpreferredencoding()).lower()]

    def is_process_injected(self, pid: int):
        handler = kernel32.OpenProcess(structure.PROCESS.PROCESS_ALL_ACCESS.value, False, pid)
        if handler:
            return process.module_from_name(python_version, handler) is not None
        else:
            e_print(f"can't open process {pid} with error {ctypes.windll.kernel32.GetLastError()}")
            return False

    def inject_process(self, pid: int, socket_port: int, data_dir: str, init_plugins: list):
        ctypes.windll.kernel32.SetLastError(0)
        handler = kernel32.OpenProcess(structure.PROCESS.PROCESS_ALL_ACCESS.value, False, pid)
        if not handler:
            e_print(f"could not open process {pid} with error code {ctypes.windll.kernel32.GetLastError()}")
            return False
        python_lib_h = process.module_from_name(python_version, handler)
        if python_lib_h is None:
            dll_base = process.inject_dll(bytes(python_lib, 'utf-8'), handler)
            if not dll_base:
                e_print(f"inject dll failed on process {pid}")
                return False
        else:
            dll_base = python_lib_h.lpBaseOfDll
        dif = dll_base - local_handle
        param_addr = memory.allocate_memory(4, handler)
        memory.write_memory(ctypes.c_int, param_addr, 1, handler)
        process.start_thread(funcs[b'Py_InitializeEx'] + dif, param_addr, handler)
        err_path = os.path.join(application_path, f'InjectErr_{int(time.time())}.log').replace("\\", "\\\\")
        game_environ = {
            'fpt_socket_port': str(socket_port),
            'fpt_data_dir': str(data_dir),
            'python_interpreter': sys.executable
        }
        shellcode = f"""
import sys
import os
from os import chdir,environ
from traceback import format_exc
init_modules = set(sys.modules.keys())
try:
    os.environ|={game_environ}
    sys.path={sys.path}
    os.chdir(sys.path[0])
    from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())
    from FFxivPythonTrigger import *
    from FFxivPythonTrigger import logger
    logger.print_log_level = logger.DEBUG
    try:
        init()
        register_modules({init_plugins})
        run()
    except Exception:
        pass
    finally:
        close()
except:
    err_text=format_exc()
    with open("{err_path}", "w+") as f:
        f.write(err_text)
    import ctypes
    ctypes.windll.user32.MessageBoxW(0,"error occur:\\n"+err_text,"fpt inject error",0x10)
finally:
    for key in sys.modules.keys():
        if key not in init_modules:
            del sys.modules[key]
        """.encode('utf-8')
        shellcode_addr = memory.allocate_memory(len(shellcode), handler)
        memory.write_bytes(shellcode_addr, shellcode, handler=handler)
        _thread.start_new_thread(
            process.start_thread,
            (funcs[b'PyRun_SimpleString'] + dif, shellcode_addr,),
            {'handler': handler}
        )
        return True


print(f"server will listen at [tcp://127.0.0.1:{args.port}]", flush=True)
server = RpcServer(('127.0.0.1', args.port), FrontRpc())
server.serve_forever()
