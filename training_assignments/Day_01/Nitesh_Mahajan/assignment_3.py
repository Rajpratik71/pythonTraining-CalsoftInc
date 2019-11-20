#!usr/bin/env python

"""
    This program opens a file, add some content, read it and print the same
"""


with open("a.txt", 'w') as file:
    file.write("abcdefghijklw")

with open("a.txt", "r") as file:
    p = file.read()
    print(p)
