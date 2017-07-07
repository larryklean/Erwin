import asyncio


async def hello():
    print('Hello World!')
    await asyncio.sleep(1)
    print('Hello World!')
