import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # flexible parameters
        func(*args, **kwargs)
        end_time = time.time()
        print("runtime is %s" % (end_time - start_time))

    return wrapper


@timer  # func1 = timer(func1)
def func1():
    print("func1 begin".center(20, "="))
    time.sleep(3)
    print("func1 end".center(20, "="))


@timer  # func = timer(func2)
def func2(*params):
    print("func2 begin".center(20, "="))
    print(params)
    time.sleep(2)
    print("func2 end".center(20, "="))


# func2 = timer(func2)
# func2()

func1()
# func2(["tom", "john"])
