from FFxivPythonTrigger import *

def main():
    me = plugins.XivMemory.actor_table.me
    e = me.effects[0]
    e.buff_id = 0

main()
