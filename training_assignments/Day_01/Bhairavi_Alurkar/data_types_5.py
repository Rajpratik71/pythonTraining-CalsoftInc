#!/usr/bin/python

"""
Python program to remove duplicates from a list
"""


def remoce_duplicate_from_list():
    sample_input = [1, 3, 1, 'python', 'java', 'python']
    return set(sample_input)


if __name__ == "__main__":
    res = remoce_duplicate_from_list()
    print(res)

