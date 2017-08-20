#! python3
# read census excel file

import openpyxl
import pprint
import os

print('Opening workbook...')
# 加载xlsx工作簿
wb = openpyxl.load_workbook('res/censuspopdata.xlsx')

# 加载其中的一个表
sheet = wb.get_sheet_by_name('Population by Census Tract')

# 数据字典
country_data = {}

# 遍历所有的行
for row_index in range(2, sheet.max_row + 1):
    # 获取每行中每一列的数据
    state = sheet['B' + str(row_index)].value
    country = sheet['C' + str(row_index)].value
    pop = sheet['D' + str(row_index)].value
    # 填充数据结构
    # setdefault如果键存在 则不会执行任何动作
    country_data.setdefault(state, {})
    country_data[state].setdefault(country, {'tracts': 0, 'pop': 0})
    # 变更数据
    country_data[state][country]['tracts'] += 1
    country_data[state][country]['pop'] += int(pop)

print('Writing results...')
with open('census_2010.txt', 'w') as result_file:
    result_file.write(pprint.pformat(country_data))
print('Write done')
