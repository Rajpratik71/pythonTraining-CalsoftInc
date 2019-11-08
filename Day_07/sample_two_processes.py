"""
Module to show counter decrement using 2 processes.
"""

import multiprocessing
import time

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
    # creating processes
    START = time.time()
    PROCESS1 = multiprocessing.Process(target=countdown, args=(COUNT // 2,))
    PROCESS2 = multiprocessing.Process(target=countdown, args=(COUNT // 2,))

    # starting process 1
    PROCESS1.start()
    # starting process 2
    PROCESS2.start()

    # wait until process 1 is finished
    PROCESS1.join()
    # wait until process 2 is finished
    PROCESS2.join()
    END = time.time()
    print("Time taken in seconds -", END - START)
