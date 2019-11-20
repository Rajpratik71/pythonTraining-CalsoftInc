#!/usr/bin/python

"""
Python program which accepts a sequence of comma-separated numbers from user and
 generate a list and a tuple with those numbers
"""


def generate_list_and_tupple(input_value):
    input_list = input_value.split(',')
    print("Generated list is {}".format(input_list))

    print("Generated tuple is {}".format(tuple(input_list)))


if __name__ == "__main__":
    input_value = input("Enter numbers seperated by comma : ")
    generate_list_and_tupple(input_value)

