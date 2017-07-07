# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
#
# # run
# c = consumer()
# produce(c)


def consumer():
    r = ''
    while True:
        # 执行到yield会直接返回到调用位置
        n = yield r
        print(n)
        # if n is None:
        #     return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    # 第一次发送 None?
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] produce %s' % n)
        # 当n+1的时候进行send，会得到一个新的返回值
        r = c.send(n)
        print('[CONSUMER] response %s' % r)
        print()

c = consumer()
produce(c)