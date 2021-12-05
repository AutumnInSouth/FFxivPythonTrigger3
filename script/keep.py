import ctypes.wintypes
import random
import win32con
import time
p_hwnds = []


def _filter_func(hwnd, param):
    rtn_value = ctypes.wintypes.DWORD()
    ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(rtn_value))
    str_buffer = (ctypes.c_char * 512)()
    ctypes.windll.user32.GetClassNameA(hwnd, str_buffer, 512)
    if str_buffer.value == b'FFXIVGAME':
        p_hwnds.append(hwnd)


_c_filter_func = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.wintypes.HWND, ctypes.wintypes.LPARAM)(_filter_func)
ctypes.windll.user32.EnumWindows(_c_filter_func, 0)

def send_key(hwnd:int,key_code: int,period:float):
    ctypes.windll.user32.SendMessageA(hwnd, win32con.WM_KEYDOWN, key_code, 0)
    time.sleep(period)
    ctypes.windll.user32.SendMessageA(hwnd, win32con.WM_KEYUP, key_code, 0)
seq=list(b'WASD')
seq.append(win32con.VK_SPACE)
seq.append(win32con.VK_NUMPAD9)
while True:
    for hwnd in p_hwnds:
        send_key(hwnd, random.choice(seq), random.random()+.5)
    time.sleep(random.random()*20+50)
