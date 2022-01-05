
from ctypes import *

from FFxivPythonTrigger.saint_coinach import action_sheet


for i in range(65):
    col=action_sheet.header.get_column(i)
    print(col.name,col.offset,col.type)
