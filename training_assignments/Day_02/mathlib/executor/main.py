import sys
import os
import mathlib.controller.operations as operations
sys.path.append(os.path.abspath("../controller"))

if __name__ == "__main__":

    print("1. Get square root")
    print("2. Get the power")
    print("3. Get the Factorial")
    print("Enter the operation :", end = " ")
    operationID = int(input())

    if operationID == 1:
        print("Enter the number to find the square root:", end = " ")
        number = int(input())
        print("square root of {} is {}".format(number,operations.get_sqrt(number)))
    elif operationID == 2:
        print("Enter the Base:", end = " ")
        base = int(input())
        print("Enter the Power:", end = " ")
        power = int(input())
        print("Base {} to the power {} is : {}".format(base,power,operations.get_power(base,power)))
    elif operationID == 3:
        print("Enter the number:", end = " ")
        factorial = int(input())
        print("factorial of {} is : {}".format(factorial,operations.get_factorial(factorial)))
