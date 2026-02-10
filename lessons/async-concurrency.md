# Python by Example: Async Concurrency

Run multiple coroutines at the same time with `asyncio.gather()`. It starts all of them, waits for each to finish, and returns their results in order. Use this for parallel I/O—e.g., fetching several URLs. Concurrency here is cooperative: only one coroutine runs at a time, but they overlap while waiting.

**What you'll learn:**
- `asyncio.gather()` for concurrent execution
- Collecting results from multiple coroutines

```python
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
```

All three tasks start; task 2 finishes first (0.5s), then task 1 (1s), then task 3 (2s). Results are returned in the order you passed the coroutines.

To run this program:

```bash
$ python source/async-concurrency.py
Task 1 starting
Task 2 starting
Task 3 starting
Task 2 done
Task 1 done
Task 3 done
Results: [1, 2, 3]
```

**Tip:** Use `asyncio.gather()` when you have independent I/O tasks. For more control, use `asyncio.create_task()` and manage tasks yourself.

**Try it:** Add a fourth task with a different delay and observe the order of completion.

Source: [async-concurrency.py](../source/async-concurrency.py)

Next: [Async Queues](async-queues.md)
