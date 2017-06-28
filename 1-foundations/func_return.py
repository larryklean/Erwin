# def calc_sum(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# sum = calc_sum(1, 2, 3, 4)
# print(sum)


def calc_sum(*args):
    def sum():
        ax = 0
        for item in args:
            ax += item
        return ax

    return sum


func1 = calc_sum(1, 2, 3, 4)
func2 = calc_sum(1, 2, 3, 4)
# print(func1)
# print(func2)

