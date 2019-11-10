"""
Module to show counter decrement using 2 threads.
"""

import time
from threading import Thread

COUNT = 50000000  # 50 M


def countdown(counter):
    """
    function decrements counter by one each time, until counter becomes zero
    Args:
        counter (int): counter value
    """
    while counter > 0:
        counter -= 1


if __name__ == "__main__":
    THREAD1 = Thread(target=countdown, args=(COUNT // 2,))
    THREAD2 = Thread(target=countdown, args=(COUNT // 2,))

    START = time.time()
    THREAD1.start()
    print(THREAD1.isAlive())
    THREAD2.start()
    THREAD1.join()
    print(THREAD1.isAlive())
    print(THREAD2.isAlive())
    THREAD2.join()
    END = time.time()

    print("Time taken in seconds -", END - START)
