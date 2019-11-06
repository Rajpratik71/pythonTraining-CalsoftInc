print("===========================Zip example================================")
l1 = ['a', 'b', 'c']
l2 = [1, 2]
z = zip(l1, l2)
print(z)
print([i for i in z])
print("===========================map example================================")
items = [1, 2, 3, 4, 5]
m = map(lambda x: x ** 2, items)
print(m)
print(list(m))
print("===========================enumerate example================================")
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(enumerate(seasons))
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))
print("===========================reduce example================================")
from functools import reduce

print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))
