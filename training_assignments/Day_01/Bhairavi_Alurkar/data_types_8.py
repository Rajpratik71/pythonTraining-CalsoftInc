#!/usr/bin/python

"""
Python program to add the 10 to all the values of a dictionary.
"""


def add_10_to_each_value():
    sample_input = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    for each in sample_input:
        sample_input[each] += 10
    return sample_input


if __name__ == "__main__":
    res = add_10_to_each_value()
    print(res)


