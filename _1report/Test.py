
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active

ws.append(['one', 'two', 'three'])
ws.append(['four', 'five', 'six'])
ws.append(['seven', 'eight', 'nine'])
wb.save('test2.xlsx')