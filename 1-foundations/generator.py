# list comprehension
l = [x * x for x in range(1, 11)]
# print(l)

# generator
l = (x * x for x in range(1, 11))


# print(l)
# print(next(l))
# for item in l:
#     print(item)

# fib
# def fib(m):
#     n, a, b = 0, 0, 1
#     while n < m:
#         print(b)
#         a, b = b, a + b
#         n += 1
#     return "done"


# yield
def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield 3
    print("step 3")
    yield 5


# g = odd()
# next(g)
# next(g)
# next(g)
# print(g)

def fib(m):
    a, b, n = 0, 1, 0
    while n < m:
        yield b
        a, b = b, a + b
        n += 1
    return "done"


# for item in fib(10):
#     print(item)
g = fib(6)
while True:
    try:
        x = next(g)
        print("g : ", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break
