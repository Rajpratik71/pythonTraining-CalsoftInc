#!/usr/bin/python

"""
Python program to return number of vowels in a given string.
"""


def count_vowels():
    string = "Getting started with python"
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in string:
        if i in vowels_list:
            count += 1
    return count


if __name__ == "__main__":
    res = count_vowels()
    print(res)

