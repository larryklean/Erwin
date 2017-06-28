from functools import reduce


# l = list(map(lambda x: x * x, [1, 2, 3, 4]))
# print(l)


def build(x, y):
    return x + y


l = reduce(lambda x, y: x + y, (i for i in range(1, 10)))
print(l)
