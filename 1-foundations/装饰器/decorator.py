import time


# 函数是一个对象，可以把函数当作参数传递给一个变量进行调用
def func():
    l = []
    for i in range(1, 10):
        l.append(i)
    print(l)


# 可以通过属性 __name__ 来获取函数的名称
f = func
print(f.__name__)


# 装饰器 在运行期间不修改代码动态增强函数功能
def log(func):
    def wrapper(*args, **kwargs):
        print("call %s() %s" % (func.__name__,text))
        return func(*args, **kwargs)
        # func()

    return wrapper


# @语法调用装饰函数 相当于 f = log(now) or now = log(now)
# @log
def now():
    print(time.time())

now = log(now,"ss")
# f = now
now()
