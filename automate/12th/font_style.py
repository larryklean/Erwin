import openpyxl
from openpyxl.styles import Font, NamedStyle

# 创建新的Excel文件
wb = openpyxl.Workbook()
# 获取电子表格
sheet = wb.get_sheet_by_name('Sheet')
# 设置字体对象
italic_font = Font(size=24, italic=True)
# 设置样式对象
style_obj = NamedStyle(font=italic_font)
# 给第一列单元格设置样式
sheet['A'].style / style_obj
# 添加数据
sheet['A1'].value = 'HelloWorld!'
# 保存文件
wb.save('styled.xlsx')
