# -*- coding:utf-8 -*-

# init personal info
name = input("please input your name：")
balance = float(input("please input your balance："))

# init store
store = [["iphone", 5000], ["MacBook", 12000], ["Bike", 800], ["StarBuck", 30]]
# init cart
cart = []

# shopping
while True:
    if len(store) > 0:
        # print current goods of store
        for item in store:
            print("id：%s name：%s price：%s" % (store.index(item) + 1, item[0], item[1]))
    else:
        print("nothing to show,exit...")
        break

    goods_id = input("please input the id of goods you want to buy(q to exit")
    if goods_id.isdigit():
        goods_id = int(goods_id)
        if len(store) > goods_id >= 0:
            # check balance
            goods_price = float(store[goods_id - 1][1])
            if goods_price <= balance:
                print("you have add goods into cart")
                # add goods into cart
                cart.append(store[goods_id - 1][0])
                # delete goods from store
                del store[goods_id - 1]
                # show goods of cart
                for item in cart:
                    print(item)
                # refresh balance
                print("your balance is %d" % (balance - goods_price))
                # show goods of store
                for item in store:
                    print("编号：%s 名称：%s 价格：%s" % (store.index(item) + 1, item[0], item[1]))
            else:
                print("your balance is not enough")
                continue
        else:
            print("invalid id")
            continue
    elif goods_id == "q":
        print("exit store")
        break
    else:
        print("Invalid option")
        continue

    print("=============")
    # print("do you want to continue? y or n")
    # judge = input()
    # if judge == "y":
    #     continue
    # else:
    #     print("goodbye")
    #     break
