import _thread
import time


def thread_test(name, wait):
    i = 0
    while i <= 3:
        time.sleep(wait)
        print("Running %s\n" % name)
        i = i + 1

    print("%s has finished execution" % name)


if __name__ == "__main__":
    _thread.start_new_thread(thread_test, ("First Thread", 1))
    _thread.start_new_thread(thread_test, ("Second Thread", 2))
    _thread.start_new_thread(thread_test, ("Third Thread", 3))
