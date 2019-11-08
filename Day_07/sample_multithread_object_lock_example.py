"""
Module to understand python multi threading
"""

import os
import threading
import time

NEW_LOCK = threading.Lock()


def make_dir():
    """
    Creates the new directory if doesn't exists
    """
    dir_path = "test123"
    print("1" * 20)
    # with NEW_LOCK:
    if not os.path.exists(dir_path):
        print("2" * 20)
        time.sleep(1)
        os.makedirs(dir_path)


if __name__ == "__main__":
    THREAD1 = threading.Thread(target=make_dir)
    THREAD2 = threading.Thread(target=make_dir)

    THREAD1.start()
    THREAD2.start()
    THREAD1.join()
    THREAD2.join()
