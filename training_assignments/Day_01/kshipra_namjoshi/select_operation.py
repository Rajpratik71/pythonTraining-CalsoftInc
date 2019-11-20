"""
Module to choose function and perform operation for the specified user input.
"""

import math


def generate_factorial(num):
    """
    Calculates factorial of a number.

    Args:
        num: Number whose factorial is to be calculated.
    """
    print(f"Factorial of {num} is {math.factorial(num)}.")


def fibonnaci(num):
    """
    Calculates fibonacci series.

    Args:
        num: Count till which fibonacci is to be calculated.
    """
    fibo_series = []
    count = 0
    n1 = 0
    n2 = 1
    if num < 0 or num == 0:
        print("Invalid choice")
    elif num == 1:
        print(f"Fibonacci series upto {num} is [{num-1}].")
    else:
        while count < num:
            fibo_series.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        print(f"Fibonacci series upto {num} is {fibo_series}.")


if __name__ == '__main__':
    choice = str(input("Enter function to perform:"))
    if choice not in ["factorial", "fibonacci"]:
        print("Invalid choice.")
    else:
        num = int(input("Number to perform function on:"))
        if choice == "factorial":
            generate_factorial(num)
        elif choice == "fibonacci":
            fibonnaci(num)
