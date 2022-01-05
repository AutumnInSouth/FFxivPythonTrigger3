from time import sleep

from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.saint_coinach import realm, item_names

materia_sheet = realm.game_data.get_sheet('Materia')
for row in materia_sheet:
    item = row[f'Item[7]']
    if item and item.key:
        print(item_names.get(item.key))
        try:
            for item in plugins.Pmb.query(item.key):
                if item['price_per_unit'] <= 400:
                    plugins.Pmb.buy(item)
                    sleep(.5)
        except Exception as e:
            print(e)
        finally:
            sleep(1)
from ctypes import windll
windll.kernel32.Beep(500,1000)
