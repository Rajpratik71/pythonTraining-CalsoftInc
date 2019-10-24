import threading
import time

def print_hello_three_times():
    for i in range(99):
        time.sleep(0.5)
        print("Hello")

def print_hi_three_times():
    for i in range(99):
        time.sleep(0.5)
        print("Hi")

thread1 = threading.Thread(target=print_hello_three_times())

thread2 = threading.Thread(target=print_hi_three_times())

thread1.start()
thread2.start()
