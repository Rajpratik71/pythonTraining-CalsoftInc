#!usr/bin/env python

"""
This program adds 10 to all the values of a dictionary
"""

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

# Iterates through keys of dict_num
for key in dict_num.keys():
    dict_num[key] += 10  # Adds 10 to 'value' of 'key'

print(dict_num)
