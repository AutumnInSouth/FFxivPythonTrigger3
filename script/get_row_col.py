
from ctypes import *

from FFxivPythonTrigger.saint_coinach import realm

sheet = realm.game_data.get_sheet('Mount')

for i in range(99):
    col=sheet.header.get_column(i)
    print(col.name,col.offset,col.type)

