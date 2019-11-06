# A simple generator function

def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed first')
    yield n

    n += 2
    print('This is printed first')
    yield n
