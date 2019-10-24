test_str = "GfG is good website"
test_list = ["GfG", "site", "CS", "Geeks", "Tutorial" ]

print(" The original string is : " + test_str)
print()
print(" The original string list is : " + str(test_list))


# Method 1. Using list Comprehension
res = [sub for sub in test_list if sub in test_str]


# Method 2. Using lamda and filter
res2 = list(filter(lambda x: x in test_str, test_list))


print()
print(" The list of found substring , using list comprehension is :" + str (res))
print()
print(" The list of found substring , using lambda and filter is :" + str (res2))