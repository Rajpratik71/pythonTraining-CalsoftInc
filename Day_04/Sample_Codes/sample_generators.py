# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Returns the value but maintains the state
    yield n

    # When the next() is called second time the Generator resumes from here
    n += 1
    print('This is printed second')
    yield n

    # When the next() is called third time the Generator resumes from here
    n += 1
    print('This is printed at last')
    yield n


if __name__ == '__main__':
    gen_obj = my_gen()
    next(gen_obj)
    next(gen_obj)
    next(gen_obj)
    # Will raise StopIteration Error because no more value can be yielded
    next(gen_obj)
