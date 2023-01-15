import openpyxl 
import csv

wb = openpyxl.load_workbook(filename='data.xlsx', data_only=True)

sh = wb.active
with open('output.csv', 'w', newline="") as f:
    c = csv.writer(f, delimiter=';')
    for r in sh.rows:
        c.writerow([cell.value for cell in r])
