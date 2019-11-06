def caller_function:
    print('Inside the caller function')

    print('I have performed some operations. Now yielding')

    yield

    print(' I am back in caller function')

    yield
