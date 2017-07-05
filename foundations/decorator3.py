import time


def dec(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("func run time is %s" % (end_time - start_time))


def func1():
    time.sleep(3)
    print("in the func")


def func2():
    time.sleep(3)
    print("in the func2")


dec(func2)
dec(func1)
