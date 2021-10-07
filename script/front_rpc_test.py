import zerorpc
c=zerorpc.Client()
c.connect("tcp://127.0.0.1:12344")
for pid in sorted(c.get_game_process("notepad.exe")):
    print(pid,c.inject_process(pid, 3520, "AppData", []),c.is_process_injected(pid))