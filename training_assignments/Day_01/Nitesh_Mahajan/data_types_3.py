#!usr/bin/env python

"""
    This program accepts filename from the user and prints it extension
"""

filename = input("Enter file name:")

ext = filename.split('.')[-1]  # Splits the filename by '.' then assigns the extension part
print("File extension: "+ext)
