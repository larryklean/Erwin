# 3rd parameter is step
# for i in range(0, 10, 3):
#     print(i)

# for i in range(1, 10):
#     if i < 5:
#         print(i)
#     else:
#         continue
#     print("continue...")

for i in range(1, 10):
    print("--{_i}".format(_i=i))
    for j in range(1, 10):
        print(j)
