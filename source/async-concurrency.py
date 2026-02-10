import asyncio


async def fetch(id, delay):
    print(f"Task {id} starting")
    await asyncio.sleep(delay)
    print(f"Task {id} done")
    return id


async def main():
    # Run concurrently and collect results
    results = await asyncio.gather(
        fetch(1, 1),
        fetch(2, 0.5),
        fetch(3, 2),
    )
    print("Results:", results)


asyncio.run(main())
