import itertools

import more_itertools

print(dir(itertools))

print(dir(more_itertools))

itercomblist = itertools.combinations([1, 2, 3], 2)

itercombstring = itertools.combinations([123], 2)

print(list(itercomblist))

print(itercombstring)
