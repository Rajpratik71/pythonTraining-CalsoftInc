"""
4. Write a python program to return number of vowels in a given string.
sample input: 'Getting started with python'
sample output: "Total vowels found in <sample_input>: 6"
"""
sample_input = "Getting started with python"
vowels = ['a','e','i','o','u']
cnt = 0
for ch in sample_input:
    if ch in vowels:
        cnt = cnt + 1
    else:
        pass
print("Total vowels found in <sample_input>: {}".format(cnt))

"""
Output:
Total vowels found in <sample_input>: 6
"""