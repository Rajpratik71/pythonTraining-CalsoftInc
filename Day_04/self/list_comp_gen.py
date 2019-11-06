lst = [1, 2, 3, 4, 5]

# List Comprehension
my_lst = [x ** 2 for x in lst]
print(my_lst)

# Generator expression
gen = (x ** 2 for x in lst)
print(gen)
