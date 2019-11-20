#!/usr/bin/python

"""
Write a python script to open a file with "with open", add some content , read it and print the same.
"""

import os


def io_operations():

    file_name = "python_training.txt"
    with open(file_name, "w+") as fd:
        fd.write("Hello python...")
    with open(file_name, "r") as fd:
        data = fd.read()
        print(data)
    os.remove(file_name)


if __name__ == "__main__":
    io_operations()
