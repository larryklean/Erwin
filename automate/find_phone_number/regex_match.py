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

# | 管道 会返回出现的第一个
hero_regex = re.compile(r'batmen|superman')
mo3 = hero_regex.search('you are batmen or superman?')
print(mo3.group())
# | + ()  分组+管道
hero_regex2 = re.compile(r'bat(mobile|man|woman)')
mo4 = hero_regex2.search('batman use a batmobile')
print(mo4.group())

# ? 可选 代表出现0次或1次
batman = re.compile(r'bat(wo)?man')
mo5 = batman.search('batwoman or batman')
print(mo5.group())
# ? 练习
phone_number_regex3 = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo5 = phone_number_regex3.search('my phone number is 421-736-5743')
mo6 = phone_number_regex3.search('my phone number is 736-5743')
print(mo5.group())
print(mo6.group())

# * 表示零次或多次
batRegex = re.compile(r'Bat(wo)*man')
mo7 = batRegex.search('The Adventure of Batman')
mo8 = batRegex.search('The Adventures of Batwowowowoman')
print(mo7.group())

# + 表示至少出现一次
batRegex2 = re.compile(r'Bat(wo)+man')
mo9 = batRegex2.search('The Adventure of Batwoman')
print(mo9.group())

# {次数} 表示重复的次数
# {3}三次
# {3,}三次以上
# {,5}零到五次
# {3,5}三到五次
# 在都满足情况下会尽可能匹配最长的字符串 贪心匹配
haRegex = re.compile(r'(Ha){3,5}')
mo10 = haRegex.search('HaHaHa')
print(mo10.group())
# 在后面添加？后表示非贪心算法 匹配最短的那个
greedyRegex = re.compile(r'(Ha){3,5}?')
mo11 = greedyRegex.search('HaHaHaHaHa')
print(mo11.group())

# findAll() 不仅匹配第一次出现的字符串 会返回所有匹配的情况 以列表的形式返回
phone_number_regex4 = re.compile(r'\d{3}-\d{3}-\d{4}')
# 有分组和无分组是有区别的 有分组的情况下会返回元组
# phone_number_regex4 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
phone_list = phone_number_regex4.findall('Cell：415-555-9999 Work：212-555-0000')
print(phone_list)

# \d 任意数字 0-9
# \D 除了 0-9 的任意字符
# \w 任何数字、字母或下划线
# \W 除了数字、字母或下划线之外的任何字符
# \s 空格或者制表符
# \S 除空格和制表符之外的字符
xmas_regex = re.compile(r'\d+\s\w+')

# 通过[]自定义字符
# 因为 \d \w \s 太宽泛了
# [^a-zA-Z0-9] 前面加^表示非

# ^表示发生在开始处 ，$表示发生在结尾处
begins_with = re.compile(r'^Hello')
print(begins_with.search('Hello').group())
ends_with = re.compile(r'Hello$')
print(ends_with.search('World Hello').group())
whole_number_regex = re.compile(r'^\d+$')

# . 表示通配符 可以匹配除了换行之外的所有字符
at_regex = re.compile(r'.at')
print(at_regex.findall('The cat in the hat sat on the flat mat.'))

# .* 可以匹配任意文本
name_regex = re.compile(r'First Name:(.*) Last Name:(.*)')
print(name_regex.search('First Name: AI Last Name: Sweigart').group(1))
# 非贪心模式 .*?
nogreedy_regex = re.compile(r'<.*?>')
# greedy_regex = re.compile(r'<.*>')
print(nogreedy_regex.search('<To server man> for dinner.>').group())
# compile 的第二个参数使用 re.DOTALL 可以匹配换行在内的所有字符
no_new_line_regex = re.compile('.*')
print('不包括换行符：')
print(no_new_line_regex.search('server the public true.\nProtect the innocent.\nUpload the public').group())
# 包括换行符
print('包括换行符：')
new_line_regex = re.compile('.*', re.DOTALL)
print(new_line_regex.search('server the public true.\nProtect the innocent.\nUpload the public').group())


print('=====================')

