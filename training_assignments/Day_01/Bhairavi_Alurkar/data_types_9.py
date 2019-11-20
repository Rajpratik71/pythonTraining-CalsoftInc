#!/usr/bin/python

"""
program to create two sets and print their union, intersection, difference and symmetric difference.
"""


def operation_on_sets():
    first_set = {9,5,6,7,3,4}
    second_set = {5,6,7,1,8,33}

    print("Union :", first_set.union(second_set))
    print("Intersection  :", first_set.intersection(second_set))
    print("Difference  :", first_set.difference(second_set))
    print("Symmetric difference  :", first_set.symmetric_difference(second_set))


if __name__ == "__main__":
    operation_on_sets()