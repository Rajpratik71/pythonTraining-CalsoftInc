#!usr/bin/env python

"""
This program performs operations like union, intersection, difference and symmetric difference on two sets.

"""

s1 = {'BMW', 'Audi', 'RR', 'Suzuki', 'Skoda', 'Hyundai'}
s2 = {'Audi', 'Mercedes', 'Hyundai', 'BMW', 'Tata', 'Honda'}

# Union of set s1 and s2
print("Union of set s1 ad s2: {}".format(s1.union(s2)))

# Intersection of s1 and s2
print("Intersection of s1 and s2 {}".format(s1.intersection(s2)))

# Difference of s1 and s2
print("Difference of s1 and s2 {}".format(s1.difference(s2)))

# Symmetric Difference of s1 and s2
print("Symmetric Difference of s1 and s2: {}".format(s1.symmetric_difference(s2)))