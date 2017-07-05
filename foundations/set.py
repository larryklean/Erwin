list_1 = [1, 2, 3, 4, 5, 4, 5, 6, 3]
list_2 = [3, 2, 9, 7]

list_1 = set(list_1)
list_2 = set(list_2)

# 交
print(list_1.intersection(list_2))
# 并
print(list_1.union(list_2))
# 差
print(list_1.difference(list_2))
print(list_2.difference(list_1))
# 子集判断
print(list_1.issubset(list_2))
# 父集判断
print(list_1.issuperset(list_2))

# 添加
list_2.add(99)
print(list_2)

# 修改
list_2.update([1, 2, 3])
print(list_2)

# 长度
print(len(list_2))

# 删除
# print(list_2.discard())
print(list_2.remove(2))
