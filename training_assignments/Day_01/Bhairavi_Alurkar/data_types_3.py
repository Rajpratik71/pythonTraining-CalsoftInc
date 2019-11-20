#!/usr/bin/python

"""
Python program to accept a filename from the user and print the extension of that.
"""


def return_file_extension(file_name):
    return file_name.split(".")[-1]


if __name__ == "__main__":
    file_name = input("Enter filename with extension : ")
    res = return_file_extension(file_name)
    print(res)

