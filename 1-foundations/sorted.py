# print(sorted([3, 4, 2, 1], reverse=True))
# 忽略大小写
# print(sorted(['A', 'D', 'C', 'B'], key=str.lower, reverse=True))

l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


def by_score(t):
    return t[1]


l2 = sorted(l, key=by_score)
print(l2)
