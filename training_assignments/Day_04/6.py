def checker(func):
    def wrapper(a,b):
        if isinstance(a, int) == True and isinstance(b, int) == True:
            if a != 0 and b != 0:
                func(a,b)
            else:
                print("Don't enter 0")
        else:
            print("please enter only integers")
    return wrapper

@checker
def Method1(a,b):
    print(a+b)

if __name__ == '__main__':
    Method1('a', 1)
    Method1(1, 'b')
    Method1(0, 1)
    Method1(1, 0)
    Method1(1, 2)
