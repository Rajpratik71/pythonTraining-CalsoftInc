"""
Module to understand asyncio
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
    print(f"started at {time.strftime('%X')}")

    await say_after(1, "Awesome")
    await say_after(2, "Stuff")

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
