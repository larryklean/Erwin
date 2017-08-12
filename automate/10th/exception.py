#! python3

# 抛出异常
# raise
# 其后的代码不会执行
"""
raise Exception('This is a exception!')
"""

# print a box
"""
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('The symbol must be a single character')
    if width < 2:
        raise Exception('The value of width must larger than 2')
    if height < 2:
        raise Exception('The value of height must larger than 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + ' ' * (width - 2) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('An error happened:' + str(err))
"""

# 断言 assert
# 判断某个条件是否为真，针对编程人员的错误而不是用户，可以第一时间定为问题
# 如果条件为真则执行对应的语句，否则直接崩溃
# 例如像文件无法找到这种可以恢复的错误，应该使用try...catch
"""
assert condition
"""

# 日志 logging
# logging模块可以将部分信息打印到控制台上,一共分为5个级别
# 这是一种比print()更好的打印方式
