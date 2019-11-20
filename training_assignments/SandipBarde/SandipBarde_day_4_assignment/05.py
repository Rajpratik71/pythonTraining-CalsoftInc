def fiboGenerator(num):
    yield 1
    yield 1
    first = 1
    second = 1
    third = 1
    count = 2
    while(count != num):
        first = second
        second = third
        third = first + second
        count = count + 1
        yield third
if __name__ == "__main__":
    obj = fiboGenerator(5)
    print(next(obj))
    print(next(obj))
    print(next(obj))
    print(next(obj))
    print(next(obj))

