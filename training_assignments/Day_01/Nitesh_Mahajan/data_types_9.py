#!usr/bin/env python

"""
This program counts number of items in a dictionary value that is a list
"""

count = 0
d = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

# Iterates through keys of d
for key in d.keys():
    # Checks if the 'value' of 'key' is list
    if type(d[key]) == list:
        count += len(d[key])  # Add count of items in list into variable 'count'

print(count)
