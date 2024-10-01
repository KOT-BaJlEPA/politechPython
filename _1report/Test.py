import os

import openpyxl
wb = openpyxl.Workbook()
ws = wb.active

ws.append(['one', 'two', 'three'])
ws.append(['four', 'five', 'six'])
ws.append(['seven', 'eight', 'nine'])
rooot_path = os.getcwd() + r'\TempEMail'
os.mkdir(rooot_path)
resutFolder = rooot_path + '\\test2.xlsx'
wb.save(resutFolder)