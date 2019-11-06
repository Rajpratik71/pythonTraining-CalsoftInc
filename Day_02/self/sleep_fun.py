import time


# Code to demonstrate sleep

print("Print Immediately")
time.sleep(10)
print("Slept for 10s")


# Code to generate digital clock

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)
    time.sleep(1)


# Code to generate digital clock advance

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result, end="", flush=True)
    print("\r", end="", flush=True)
    time.sleep(1)
