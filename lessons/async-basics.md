# Python by Example: Async Basics

Async lets you write non-blocking I/O code—useful when waiting on network or disk. Define coroutines with `async def` and call them with `await`. Use `asyncio.run()` to run an async function from synchronous code. Async is cooperative: a coroutine yields control when it awaits, so others can run.

**What you'll learn:**
- `async def` for coroutines
- `await` to call other coroutines
- `asyncio.run()` as the entry point

```python
import asyncio


async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


async def main():
    await say_hello()
    print("Done")


asyncio.run(main())
```

`asyncio.sleep(1)` doesn't block the whole program—it yields so other tasks can run. In a real app, you'd await network or file I/O instead.

To run this program:

```bash
$ python source/async-basics.py
Hello
World
Done
```

**Tip:** You can't call an async function directly—you must `await` it from another async function or run it with `asyncio.run()`.

**Try it:** Add a second `await asyncio.sleep(0.5)` and see the delay.

Source: [async-basics.py](../source/async-basics.py)

Next: [Async Concurrency](async-concurrency.md)
