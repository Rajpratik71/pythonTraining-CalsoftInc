'''
4. Write a python program to return number of vowels in a given string.
sample input: 'Getting started with python'
sample output: "Total vowels found in <sample_input>: 6"
'''

str1 = 'Getting started with python'
count = 0
for ele in str1:
    if ele == 'a' or ele == 'e' or ele == 'i' or ele == 'o' or ele == 'u':
        count += 1
print('Total number of vowels found in str1 is: ', count)