"""
8. Write a Python program to add the 10 to all the values of a dictionary.
sample input: dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
sample output: {1: 20, 2: 30, 3: 40, 4: 50, 5: 60}
"""
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print("sample_input :",dict_num)
all_key = dict_num.keys()
for key in all_key:
    dict_num[key] += 10
print("sample_output :",dict_num)

"""
Output:
=======
sample_input : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
sample_output : {1: 20, 2: 30, 3: 40, 4: 50, 5: 60}
"""