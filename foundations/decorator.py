import time


# 装饰器本质是一个函数
#   1.装饰器不修改被装饰函数的代码
#   2.不改变被装饰函数的调用模式
# 所需
#   1.函数即变量
#   2.高阶函数
#   3.嵌套函数
def decoration(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        print("run time is %s" % (end_time - start_time))

    return wrapper


@decoration
def test():
    time.sleep(3)
    print("time function")


test()
