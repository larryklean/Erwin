# with open('text.txt') as file_obj:
#     file_content = file_obj.read()
#     print(file_content.strip())

# with open('source.txt') as file_obj:
#     print(type(file_obj.read()))
#     print(type(file_obj))
# for line in file_obj.read():
#     if len(line) < 30:
#         print(line.strip())

import json

# numbers = [1, 2, 3, 4, 5]
#
# with open('test.txt', 'w') as file_obj:
#     json.dump(numbers, file_obj)

# with open('test.txt', 'r') as file_obj:
#     numbers = json.load(file_obj)
# print(numbers)

# filename = 'username.txt'
#
# try:
#     with open(filename, 'r') as file_obj:
#         username = json.load(file_obj)
# except FileNotFoundError:
#     username = input('input your name：')
#     with open(filename, 'w') as file_obj:
#         json.dump(username, file_obj)
# else:
#     print('welcome back %s' % username)
