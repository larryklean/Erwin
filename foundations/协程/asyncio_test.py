import asyncio
import threading


# @asyncio.coroutine
# def hello():
#     print('Hello World')
#     r = yield from asyncio.sleep(3)
#     print('Hello Again!')
#
#
# @asyncio.coroutine
# def hello2():
#     print('Hello World 2')
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.run_until_complete(hello2())
# loop.close()

@asyncio.coroutine
def hello():
    print('Hello World! (%s)' % threading.current_thread().name)
    yield from asyncio.sleep(1)
    print('Hello World! (%s)' % threading.current_thread().name)


@asyncio.coroutine
def hello2():
    print('Hello World 2!(%s)' % threading.current_thread().name)


loop = asyncio.get_event_loop()
tasks = [hello2(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
