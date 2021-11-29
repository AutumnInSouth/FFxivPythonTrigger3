from time import sleep

from FFxivPythonTrigger import plugins



def main():
    for i in range(200):
        try:
            plugins.XivMemory.calls.way_mark('b', plugins.XivMemory.utils.mo_location)
        except Exception as e:
            print(e)
        sleep(0.1)


if __name__ == '__main__':
    main()
