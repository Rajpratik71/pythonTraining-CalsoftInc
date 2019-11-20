def func(*args, a=[]):
    a.append(args)
    print(id(a))
    print(a)


func(1, 2, 3)
"""A new list 'a' is created with default value [] and 
all the arguments packed in a tuple because of *args will get append in the list"""

func(7, 8, 9, a=[])
"""As we are passing a list again, it will create a new list 'a' again
and will append new args to this list instead of first created list"""

func(8, 9, 10)
"""This time we are not passing the the list 'a' hence it will consider the default list in the function
and will append new *args to it"""
