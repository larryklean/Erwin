from collections import Iterable, Iterator


# print(isinstance([], Iterable))
# print(isinstance((), Iterable))
# print(isinstance({}, Iterable))
# print(isinstance({}, Iterator))
# print(isinstance(iter({}), Iterator))

# for i in range(1, 1):
#     print(i)#
def tri():
    l = [1]
    while True:
        yield l
        l = [1] + [l[i - 1] + l[i] for i in range(1, len(l))] + [1]
        if len(l) == 10:
            return


for item in tri():
    print(item)

# def tri():
#     l = [1]
#     while True:
#         yield l
#         l = [sum(i) for i in zip([0] + l, l + [0])]
#         if len(l) == 10:
#             return
#
#
# g = tri()
# for x in range(10):
#     print(next(g))
