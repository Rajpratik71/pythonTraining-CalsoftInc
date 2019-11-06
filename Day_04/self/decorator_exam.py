def evil(func):
    def wrapper(a, b):
        func(a, b)

    return '*** OFF'


@evil
def func(a, b):
    print('I am in func')
    print('adding values', a + b)


func(10, 5)
