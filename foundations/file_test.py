import sys
import time

# open file
# file = open("source.txt", "w", encoding="utf-8")

# get position of iterator
# print("目前所在位置", file.tell())

# read all
# print(file.read())

# data = file.readline()
# print(data)

# read 5 lines
# for i in range(5):
#     print(file.readline())

# allLines = file.readlines()
# for index, line in enumerate(allLines):
#     print(index, " ：", line)

# count = 0
# for line in file:
#     if count == 10:
#         print("====")
#         count += 1
#         continue
#     print(line)
#     count += 1

# print(file.tell())
# print(file.readline())
# print(file.readline())
# print(file.tell())

# change position of iterator
# file.seek(13)
# print(file.readline())
#
# print(file.encoding)
#
# file.close()

# for i in range(30):
#     sys.stdout.write("#")
#     sys.stdout.flush()
#     time.sleep(0.1)

# replace
# file = open("source.txt", "r", encoding="utf-8")
# file_new = open("text2.txt", "w", encoding="utf-8")
#
# for line in file:
#     if "玫瑰" in line:
#         line = line.replace("玫瑰", "茉莉")
#     file_new.write(line)
#
# file.close()
# file_new.close()

# with
with open("source.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
