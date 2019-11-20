#!usr/bin/env python

"""
    This program accepts comma-separated numbers from user and generates list and tuple from them
"""
# Takes input from user
in_str = input("Enter comma separated numbers:")

out_list = in_str.split(",")  # Splits the string by comma into a list
print("List: "+str(out_list))

out_tup = tuple(out_list)  # Type conversion from List to Tuple
print("Tuple: "+str(out_tup))
