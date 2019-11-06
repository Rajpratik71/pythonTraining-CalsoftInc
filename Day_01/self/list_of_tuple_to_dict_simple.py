from collections import defaultdict

test_list = [(1, "gfg"), (1, "is"), (2, "best"), (3, "for"), (4, "CS")]

res = defaultdict(list)
for i, j in test_list:
    res[i].append(j)

print("The merged dictionary is : " + str(dict(res)))
