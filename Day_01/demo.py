#!usr/bin/env python
"""
This is module level docstring
"""

# import statement to import external lib in the current module
import demo_lib


# Function definition with argument `limit`
def get_all_prime(limit):
    # This is a docstring of a function
    """
    This is function level docstring
    Args:
        limit:
    Returns:
    """
    i = 2  # local variable
    # while statement with condition
    while limit > 0:
        # If statement with external lib function call
        if demo_lib.is_prime(i):
            limit = limit - 1
            print(i)
        i = i+1
# Function scope finishes when the indent is over


# Entry point for the execution of the script
if __name__ == "__main__": # Checking the the script name is __main__
    # Getting input from stdin
    count = int(input("Enter count of prime numbers:"))
    # function call
    get_all_prime(count)
