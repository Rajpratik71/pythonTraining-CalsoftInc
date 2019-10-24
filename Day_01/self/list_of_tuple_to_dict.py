from itertools import groupby
from operator import itemgetter

test_list = [(1, 'gfg'), (1, 'is'), (2, 'best'), (3, 'for'), (4, 'CS')]

# Convert list of tuples to dictionary value lists
result = dict((k, [v[1] for v in itr]) for k, itr in groupby(
    test_list, itemgetter(0)))

# printing result
print("The merged dictionary is : " + str(dict(result)))
