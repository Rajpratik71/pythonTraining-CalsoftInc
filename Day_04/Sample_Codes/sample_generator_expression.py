# Initialize the list
my_list = [1,3]

# List comprehension
lst = [x**2 for x in my_list]
print(lst)

# Generator Expression
gen = (x**2 for x in my_list)
print(gen)
print(next(gen))
print(next(gen))
