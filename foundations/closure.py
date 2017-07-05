# def count():
#     funcs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#
#         funcs.append(f)
#     return funcs

# f1, f2, f3 = count()

# print(f1())
# print(f2())
# print(f3())


# def count():
#     def f(j):
#         def g():
#             return j * j
#
#         return g
#
#     funcs = []
#     for i in range(1, 4):
#         funcs.append(f(i))
#     return funcs
#
#
# f1, f2, f3 = count()
#
# print(f1())
# print(f2())
# print(f3())


def f():
    l = []
    for i in range(1, 4):
        def g():
            return i * i

        l.append(g)
    return l


f1, f2, f3 = f()

print(f1())
print(f2())
print(f3())


def count():
    def f(j):
        def g():
            return j * j

        return g

    l = []
    for i in range(1, 4):
        l.append(f(i))
    return l


f1, f2, f3 = count()
