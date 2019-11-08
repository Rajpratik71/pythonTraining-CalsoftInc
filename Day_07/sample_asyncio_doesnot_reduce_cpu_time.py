"""
Module to understand time performance impact using asyncio for CPU extensive operations
"""

import asyncio
import time

COUNT = 50000000  # 50 M


async def countdown(counter):
    """
        function decrements counter by one each time, until counter becomes zero
    Args:
        counter (int): counter value
    """
    while counter > 0:
        counter -= 1


async def main():
    """
        async function to create tasks and run them at same time
    """
    task1 = asyncio.create_task(countdown(COUNT // 2))

    task2 = asyncio.create_task(countdown(COUNT // 2))

    start = time.time()
    # Start both tasks at same time
    await task1
    await task2
    end = time.time()

    print("Time taken in seconds -", end - start)


if __name__ == "__main__":
    asyncio.run(main())
