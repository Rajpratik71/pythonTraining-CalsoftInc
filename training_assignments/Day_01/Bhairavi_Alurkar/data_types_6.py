#!/usr/bin/python

"""
Python program to find the second largest number in a list.
"""


def find_second_largest_number():
    sample_input = [-8, 1, 2, -2, 0]
    sample_input.sort()
    count = sample_input.count(sample_input[-1])
    return sample_input[count-3]


if __name__ == "__main__":
    res = find_second_largest_number()
    print(res)


