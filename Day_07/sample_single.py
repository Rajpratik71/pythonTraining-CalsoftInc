"""
Module to show counter decrement using single process/thread
"""
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


START = time.time()
countdown(COUNT)
END = time.time()

print("Time taken in seconds -", END - START)
