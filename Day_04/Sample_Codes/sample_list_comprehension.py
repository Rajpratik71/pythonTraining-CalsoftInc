#general syntax of list comprehension:
#   [expression for item in list]

#simple example of list comprehension
lst = [letter for letter in 'human']
print(lst)
#The above comprehension is similar to:
# lst = []
# for letter in 'human':
#     lst.append(letter)
# print(lst)



# #list comprehension with for loop in it
sample_lst = [1,2,3,4]
lst_for = [x for x in sample_lst if x%2 == 0]
print(lst_for)
 # The above comprehension is similar to:
# lst_for = []
# for x in sample_lst:
#     if x%2 == 0:
#         lst_for.append(x)
# print(lst_for)

#list comprehension with multiple loops and condition
tags = ['egg', 'milk', 'bread', 'butter']
entries = ['bread', 'egg']
lst_multiple = [entry for tag in tags for entry in entries if tag in entry]
print(lst_multiple)
# The above comprehension is similar to:
# lst_multiple = []
# for tag in tags:
#     for entry in entries:
#         if tag in entry:
#             lst_multiple.append(entry)
# print(lst_multiple)