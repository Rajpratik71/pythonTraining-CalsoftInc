"""set operations"""
s1 = set(["mango", "apple", "mango", "grape", "pear"])
# or s1 = {'mango', 'apple', 'mango', 'grape', 'pear'}
print(f"value of set_s: {s1}")  # no duplicates

# set_s = {1,2,[3,4,5])} # will give error because only immutable objects are alowed but list is mutable
# add an element(must be immutable) into set
s1.add("kiwi")
print("after s1.add('kiwi'): ", s1)

# add multiple element(must be immutable) into set
s1.update(("banana", "watermelon"))
print("s1.update(('banana', 'watermelon')): ", s1)

# remove an element from set
s1.remove("banana")  # will throw error if element is not present
print("after s1.remove('banana'): ", s1)
s1.discard("banana")  # will do nothing if element is not present
s1.pop()  # remove and return random element from set. It will throw error if set is empty.
print("after s1.pop(): ", s1)

"""union 2 or more sets: can be achieved using .union() method or | operator"""
s2 = {"mango", "banana", "orange", "apple"}
print("The union of s1 and s2 is: ", s1.union(s2))
print("The union of s1 and s2 is using s1|s2: ", s1 | s2)

"""Note: Notice that the element 'mango', which appears in both s1 and s2, appears only once in the union. Sets never contain duplicate values.
When you use the | operator, both operands must be sets. The .union() method, on the other hand, will take any iterable as an argument,
convert it to a set, and then perform the union."""
# print(s1 | (1,2,3)) # it will throw TypError
print(s1.union((1, 2, 3)))  # it will work

# you can provide multiple sets to get their union
print(
    "Union of multiple sets s1.union(s2, {1,2,3}, {2,3,4}, {3,4,5}): ",
    s1.union(s2, {1, 2, 3}, {2, 3, 4}, {3, 4, 5}),
)

"""intersection of 2 or more sets: can be achieved using .intersection() method or & operator"""
print(f"Intersection of {s1} and {s2} is: {s1.intersection(s2)}")
# You can specify multiple sets with the intersection method and operator, just like you can with set union.

"""difference of 2 or more sets: s1.difference(s2) method or 's1 - s2' operator -> return the set of all elements that are in x1 but not in x2"""
print(f"Difference of {s1} and {s2}: {s1.difference(s2)}")

"""Symmetric difference(opposit of intersection) of s1 and s2: s1.symetric_difference or s1^s2"""
print(f"symmetric difference of {s1} and {s2}: {s1.symmetric_difference(s2)}")

# Frozen Sets
"""Python provides another built-in type called a frozenset, which is in all respects exactly like a set, except that a frozenset is immutable.
Frozensets are useful in situations where you want to use a set, but you need an immutable object. 
You can perform non-modifying operations on a frozenset"""
