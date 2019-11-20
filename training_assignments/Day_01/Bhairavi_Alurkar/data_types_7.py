#!/usr/bin/python

"""
Python program to replace last value of tuples in a list by 100.
"""


def find_second_largest_number():
    sample_input = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    new_list = []
    for each in sample_input:
        updated_tuple = list(each)
        updated_tuple.pop()
        updated_tuple.append(100)
        new_list.append((tuple(updated_tuple)))
    return new_list


if __name__ == "__main__":
    res = find_second_largest_number()
    print(res)


