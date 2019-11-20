#!/usr/bin/python

"""
This program removes the characters which have odd index values of a given strin
"""


def remove_odd_character():
    input_string = "abcdef"
    return input_string[::2]


if __name__ == "__main__":
    res = remove_odd_character()
    print(res)
