import re

# 初体验
phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_number_regex.search('My number is 433-222-6291')
print('Phone number found:', mo.group())

# 用()进行分组
phone_number_regex2 = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo2 = phone_number_regex2.search('My number is 433-222-6291')
# group(数组) 分组中的某一个 从1开始 0代表匹配的全部
print('Phone number found:', mo2.group(1))
print('Phone number found:', mo2.group(2))
print('Phone number found:', mo2.group(0))
area_code, main_code = mo2.groups()
print('area code:', area_code)
print('main code', main_code)

# | 管道 返回出现的第一个
hero_regex = re.compile(r'batmen|superman')
mo3 = hero_regex.search('you are batmen or superman?')
print(mo3.group())
# | + ()  分组+管道
hero_regex2 = re.compile(r'bat(mobile|man|woman)')
mo4 = hero_regex2.search('batman use a batmobile')
print(mo4.group())

# ? 可选 代表出现1次或0次
batman = re.compile(r'bat(wo)?man')
mo5 = batman.search('batwoman or batman')
print(mo5.group())
# ? 练习
phone_number_regex3 = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo5 = phone_number_regex3.search('my phone number is 421-736-5743')
mo6 = phone_number_regex3.search('my phone number is 736-5743')
print(mo5.group())
print(mo6.group())
