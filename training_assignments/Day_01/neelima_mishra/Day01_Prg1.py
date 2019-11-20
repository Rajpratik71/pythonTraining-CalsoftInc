'''
1. Write a Python program to remove the characters which have odd index values of a given string.
sample input: "abcdef"
sample output: "ace"
'''

str1 = input('Enter any string')
print('Entered string is: ', str1)
out_str1 = ''
flag = True
for ele in str1:
    if flag == True:
        out_str1 += ele # oddindex values
        flag = False
    else:
        flag = True
print('Output string is: ', out_str1)
