#!/usr/bin/python

"""
Python program to print second largest number
"""


def find_second_largest_number():
    sample_input = [-8]
    new_list = list(set(sample_input))
    if len(new_list) >= 2:
        new_list.sort()
        return new_list[-2]
    else:
        return new_list[0]


if __name__ == "__main__":
    res = find_second_largest_number()
    print(res)




