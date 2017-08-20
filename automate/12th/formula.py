import openpyxl

wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()
sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = '=SUM(A1:A2)'
wb.save('res/write_formula.xlsx')

wb = openpyxl.load_workbook('res/write_formula.xlsx', data_only=True)
# sheet = wb.get_sheet_by_name('Sheet')
sheet = wb.get_active_sheet()
data = sheet['A3'].value
print(data)
