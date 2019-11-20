#!usr/bin/env python
"""
Module to write into file, read it and then print its content using 'with'.
"""

with open('file.txt', 'w') as f:
    f.write('Writing into the file!')
with open('file.txt', 'r') as f:
    content = f.read()
print(content)
