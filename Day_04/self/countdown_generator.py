def countdown(n):
    print("Counting down from ,{}")

    while n > 0:
        yield n
        n -= 1


obj = countdown(10)
print(obj)
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
