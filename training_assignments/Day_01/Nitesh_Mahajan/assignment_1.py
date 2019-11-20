#!usr/bin/env python

"""
    This program generates factorial or fibonacci series based on user inputs
"""

def find_factorial():
    """
    This function takes a number from user and generates it factorial
    Args:
    Returns:
    """
    num = int(input("Enter number to find factorial:"))
    factorial = num
    for i in range(1, num):
        factorial = factorial*i
    print("Factorial is: {}".format(factorial))


def find_fibonacci():
    """
    This function takes a count from user and generates it fibonacci series upto the count
    Args:
    Returns:
    """
    count = int(input("Enter count to generate fibonacci series:"))
    fibb = [1]
    total = 0
    while len(fibb) < count:
        total += fibb[-1]
        fibb.append(total)
        total = fibb[-2]
    print("Fibonacci Series is: {}".format(fibb))


if __name__ == '__main__':
    print("1: Generate Factorial")
    print("2: Generate Fibonacci series")
    choice = input("Enter operation to perform:")
    if choice == '1':
        find_factorial()
    elif choice == '2':
        find_fibonacci()
    else:
        print("Invalid selection! Please enter 1 or 2")