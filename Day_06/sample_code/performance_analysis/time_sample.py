import time
from functools import wraps


def exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, "took", end - start, "time")
        return result

    return wrapper


def get_number():
    for x in range(1, 5000000):
        yield x


@exec_time
def expensive_function():
    for x in get_number():
        i = x ^ x ^ x
    return "some result!"


if __name__ == "__main__":
    result = expensive_function()
