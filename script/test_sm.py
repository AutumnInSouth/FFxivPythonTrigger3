from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.saint_coinach import status_sheet
call = CFUNCTYPE(c_int64,c_int64)(BASE_ADDR+0x68B020)
l=50
col = status_sheet.header.find_column('LockMovement')
for i in range(1,10):
    d=read_ubytes(call(i), l)
    r=status_sheet[i].source_row.sheet.active_sheet[i]
    print(r.sheet.get_buffer()[r.offset+col.offset],d[col.offset])
