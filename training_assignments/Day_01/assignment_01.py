"""
1. Write a Python program to remove the characters which have odd index values of a given string.
sample input: "abcdef"
sample output: "ace"
"""
input_string = input("Enter any string : ")
i = 0
for ch in input_string:
    print("index : {} => {} ".format(input_string.index(ch), ch))
new_string = input_string[::2]
print(new_string)

"""
Output:
Enter any string : india is country
index : 0 => i 
index : 1 => n 
index : 2 => d 
index : 0 => i 
index : 4 => a 
index : 5 =>   
index : 0 => i 
index : 7 => s 
index : 5 =>   
index : 9 => c 
index : 10 => o 
index : 11 => u 
index : 1 => n 
index : 13 => t 
index : 14 => r 
index : 15 => y 
idai onr
"""