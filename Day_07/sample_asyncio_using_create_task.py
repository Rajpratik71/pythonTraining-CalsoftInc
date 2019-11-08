"""
Module to understand asyncio create_task
"""

import asyncio
import time


async def say_after(delay, what):
    """
    Args:
        delay (int):  number of second to wait before printing message
        what (str): text or message to print
    """
    await asyncio.sleep(delay)
    print(what)


async def main():
    """
        async function to create coroutine and run them
    """
    task1 = asyncio.create_task(say_after(1, "Awesome"))

    task2 = asyncio.create_task(say_after(2, "Stuff"))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
