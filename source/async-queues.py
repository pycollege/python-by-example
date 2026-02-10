import asyncio


async def producer(queue):
    for i in range(3):
        await queue.put(i)
        print(f"Produced {i}")
    await queue.put(None)  # Signal done


async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed {item}")
        queue.task_done()


async def main():
    q = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))


asyncio.run(main())
