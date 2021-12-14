from FFxivPythonTrigger.saint_coinach import status_sheet
print(status_sheet[0]['as'])

for col_id in range(31):
    col = status_sheet.header.get_column(col_id)
    print(status_sheet.header.sheet_definition.get_column_name(col_id),col.offset,col.type)
