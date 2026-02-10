import asyncio


async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


async def main():
    await say_hello()
    print("Done")


asyncio.run(main())
