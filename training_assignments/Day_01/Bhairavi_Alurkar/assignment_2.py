#!/usr/bin/python

"""
Below functionality will calculate fibonacci and factorial
"""


def cal_factorial(num):
    if num == 0:
        return 1
    else:
        return num * cal_factorial(num-1)


def cal_fibonacci(num):
    i = 0
    present = 1
    previous = 0
    while i <= num:
        nextterm = present+previous
        present = previous
        previous = nextterm
        i = i+1
        print("The fibonacci number for", i, "is", nextterm)


def call_functions():
    s = input('Fib or Fac?')
    if s == 'Fib':
        num = input('Up to what number?')
        print(cal_fibonacci(int(num)))
    elif s == 'Fac':
        n = input('What number?')
        print(cal_factorial(int(n)))


if __name__ == "__main__":
    call_functions()
