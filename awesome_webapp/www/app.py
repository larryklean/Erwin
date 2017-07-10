# numbers = lists(range(1, 6))

squares = []

for value in range(1, 11):
    squares.append(value ** 2)
# print(squares)

# for value in range(2, 11, 2):
#     print(value)

# for value in range(1,1000):
#     print(value)

print(sum([value for value in range(1, 101)]))

# odd_numbers = [value for value in range(1, 21, 2)]
# for value in odd_numbers:
#     print(value)

# lists = []
# for value in range(3, 31):
#     if value % 3 == 0:
#         lists.append(value)
# for value in lists:
#     print(value)

list3s = [value ** 3 for value in range(1, 11)]
for value in list3s:
    print(value)

list4s = ['a', 'b', 'c', 'd', 'e']
list5s = list4s[:]

# list4s.append('f')
# print(list4s)
# print(list5s)
# print(list4s[-3:])
# print(list4s[:3])

