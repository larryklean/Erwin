# 返回值数=0 返回None
# 返回值数=1 返回Object
# 返回值数>1 返回tuple

# def file_func():
#     time_format = "%y-%m-%d %X"
#     time_current = time.strftime(time_format)
#     with open("text.txt", "a+") as file:
#         file.write("time %s end file \n" % time_current)
#
#
# file_func()
#
# return
# def func_test():
#     return 1, "hello", ["hello", "world"], {"name", "john"}
#
#
# x = func_test()
# print(x)


# parameter of function
# def func_test2(x, y):
#     print("1st parameter is %s" % x)
#     print("2rd parameter is %s" % y)
#
#
# key word of parameter
# func_test2(y="hello", x="world")
# print("XXX".center(20, "="))
# func_test2("hello", "world")
# print("XXX".center(20, "="))
#
#
# default parameter
# def func_test3(x=1, y=2):
#     print(x)
#     print(y)
#
#
# func_test3(3)

# flexible parameters
# def func_test4(*args):
#     print(args)
#
#
# func_test4(1, 2, 3, 4)

# def func_test5(x, *args):
#     print(x)
#     print(args)
#
#
# func_test5(1, 2, 3, 4)

# def func_test6(**kwargs):
#     print(kwargs)
#
#
# func_test6(name="john", age=24, gender="male")

# *args 接收位置参数 元组
# **kwargs 接收关键字参数 字典
# 位置参数不可以写在关键字参数的后面
# def func_test7(name, age=24, **kwargs):
#     print(name)
#     print(age)
#     print(kwargs)
#
# func_test7("john", age=24, gender="male")


# 成员变量 局部变量
# school = "sut"
#
# def func_test8(name):
#     global school
#     school = "SUT"
#     print(name)
#     name = "tom"
#     print(name)
#
# print(school)
# func_test8("s")
# print(school)

def calc(*numbers):
    sum = 0
    for item in numbers:
        sum = sum + item * item
    return sum


# print(calc((1, 2, 3)))

# def person(name, age, *, city, job):
#     print(name, age, city, job)


# person("xiaoming", 15, city="ss", job="sss")

def person(**kwargs):
    for item in kwargs:
        print(item)


person(**{"age": 25, "name": "xiaoming"})
