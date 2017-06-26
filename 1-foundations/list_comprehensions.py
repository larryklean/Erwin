# print(list(range(1, 11)))

# l = []
# for x in range(1, 11):
#     l.append(x * x)
#
# print(l)

# l = [x * x for x in range(1, 11)]
# print(l)

# l = [x * x for x in range(1, 11) if x % 2 == 0]
# print(l)

# l = list(range(1, 11))
# print(l)

l = [m + n for m in 'ABC' for n in 'XYZ']
print(l)

# import os
#
# l = [d for d in os.listdir('.')]
# print(l)

# m = {'a': 'A', 'b': 'B', 'c': 'C'}
# for k, v in m.items():
#     print(k, '=', v)

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [item.lower() for item in L1 if isinstance(item, str)]
# print(L2)
