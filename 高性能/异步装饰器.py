import time
import aiohttp
import asyncio


def cal_decorate(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(t2-t1)
    return wrapper


def cal_even(num):
    if num%2==0:
        return True
    else:
        return False


@cal_decorate
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            html = await response.text()
            print("Body:", html[:15], "...")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
