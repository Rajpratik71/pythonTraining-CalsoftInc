import math as m
def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)

def square(x):
    return x*x

def cube(x):
    return x*x*x

def sqrt(x):
    return m.sqrt(x)


def gcd(a,b):
    return m.gcd(a,b)



