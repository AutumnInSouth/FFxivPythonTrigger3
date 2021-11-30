from time import sleep

from FFxivPythonTrigger import plugins



def main():
    data = {plugins.XivMemory.actor_table.me:0}
    data[plugins.XivMemory.actor_table.me.id] = 1
    print(data)


if __name__ == '__main__':
    main()
