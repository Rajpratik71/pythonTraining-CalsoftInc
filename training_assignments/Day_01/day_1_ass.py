#!/usr/bin/python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    print("-----Opeartions-----")
    print("1. factorial")
    print("2. fibonacci")
    op_name = int(input("\nEnter opearion name to perform operation : "))
    print("Entered operation is : ", op_name)

    if op_name == 1:
        num = int(input("Enter num for factorial : "))
        fact = factorial(num)
        print("Factorial of {} is : {}".format(num, fact))
    elif op_name == 2:
        num = int(input("Enter num for fibonacci series : "))
        fibo_series = fibonacci(num)
        print("Fibonacci series for {} is : {}".format(num, fibo_series))
    else:
        print("Invalid Choice....")
