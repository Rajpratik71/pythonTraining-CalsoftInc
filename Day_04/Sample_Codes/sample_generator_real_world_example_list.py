def caller_function():
    print("Inside the caller function")

    print("I have performed some operations. Now yielding")
    yield

    print("I am back in caller function")

    print("I have again performed some operation. Now yielding")
    yield


def called_function():
    print("Inside called function")

    print("Creating generator object")

    gen_obj = caller_function()

    next(gen_obj)

    next(gen_obj)

called_function()