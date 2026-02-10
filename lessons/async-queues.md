# Python by Example: Async Queues

`asyncio.Queue` is a FIFO queue for passing data between async tasks. Producers put items; consumers get them. Both `put()` and `get()` are coroutines—they yield while waiting. Use queues when one task produces data and another consumes it, like a pipeline. Use `None` or a sentinel to signal "no more items."

**What you'll learn:**
- Creating and using `asyncio.Queue`
- Producer-consumer pattern with async
- Signaling completion

```python
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
```

The producer puts 0, 1, 2, then `None` to signal "done." The consumer stops when it sees `None`. `task_done()` marks the item as processed (useful with `join()`).

To run this program:

```bash
$ python source/async-queues.py
Produced 0
Consumed 0
Produced 1
Consumed 1
Produced 2
Consumed 2
```

**Tip:** For multiple consumers, put one `None` per consumer, or use a different sentinel strategy.

**Try it:** Add a second consumer and see how they share the work.

Source: [async-queues.py](../source/async-queues.py)

Next: [Strings](strings.md)
