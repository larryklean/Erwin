from functools import reduce


#
# def add(x, y):
#     return x + y
#
#
# print(reduce(add, [1, 3, 5, 7]))
#
# print(list(map(str, [1, 2, 3, 4, 5])))
#
#
# def fn(x, y):
#     return x * 10 + y
#
#
# print(reduce(fn, [1, 3, 5, 7, 9]))

# def fn(x, y):
#     return x * 10 + y
#
#
# def char2num(ch):
#     return {'0': 0, "1": 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ch]


# print(reduce(fn, map(char2num, '13579')))

# print(list("Test"))

def normalize(name):
    return name.lower().capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))


# print(L2)

def prod(l):
    def multi(x, y):
        return x * y

    # lambda
    # return reduce(lambda x, y: x * y,l )
    return reduce(multi, l)


# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# >>> from functools import reduce
# >>> def fn(x, y):
# ...     return x * 10 + y
# ...
# >>> def char2num(s):
# ...     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# ...
# >>> reduce(fn, map(char2num, '13579'))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def str2float(s):
    s = s.split('.')

    def func1(x, y):
        return x * 10 + y

    def func2(x, y):
        return x / 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(func1, map(char2num, s[0])) + reduce(func2, list(map(char2num, s[1]))[::-1]) / 10


print(str2float("123.4567"))
