import asyncio
import aiohttp

url = 'https://www.baidu.com'
tasks = []
count = 0


async def func():
    global count
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, verify_ssl=False) as response:
            if response.status == 200:
                await response.text()
                count += 1
                print(count)


async def main():
    for i in range(100):
        tasks.append(asyncio.create_task(func()))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    asyncio.run(main())