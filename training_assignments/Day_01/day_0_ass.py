#!/usr/bin/python
"""
   Assignment : Day_0 : List of assignment for data-types
"""

def even_index_characters():
    string = "My first python function."
    print("Original string : ", string)
    print("Even index characters in the string : ", string[1::2])

def generate_list_tuple():
    num_input = input("Please enter comman seperated numbers : ")
    print("Generatng list from input numbers : ", num_input.split(','))
    print("Generatng tuple from list : ", tuple(num_input.split(',')))

def string_extension():
    file_name = input("Enter file name with 2 character extension  : ")
    print("File extension : ", file_name[-3:])

def count_vowels():
    string = "Getting started with python"
    count = 0

    vowels = set('aeiouAEIOU')

    for s in string:
        if s in vowels:
            count = count + 1

    print("Total no of vowels are : ", count)

def remove_dulpicates():
    list_ele = [1, 3, 1, 'python', 'java', 'python']
    print("Removing dulpicate elements from list : ", set(list_ele))

def remove_dulpicates():
    list_ele = [1, 3, 1, 'python', 'java', 'python']
    print("Removing dulpicate elements from list : ", set(list_ele))

def second_largest_num():
    list_ele = [-8, 1, 2, -2, 0]
    list_ele.sort()
    print("Second largest number in the list : ", list_ele[-2])

def replace_last_val():
    list_ele = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

    print("Replacing last value of tuples in a list by 100 : ", [ele[:-1] + (100,) for ele in list_ele])

def add_in_values():
    dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

    for key, val in dict_num.items():
        dict_num[key] = dict_num[key] + 10

    print("Adding 1o to dictionary vales : ", dict_num)

def count_dict_vals_in_list():
    d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
    cnt_vals = sum(map(len, d.values()))
    print("count number of items in a dictionary value that is a list : ", cnt_vals)

def set_operation():
    set1 = {1,2,3,4}
    set2 = {3,4,5,10}

    print("Set operations:")
    print("1. Uninon : ", set1.union(set2))
    print("2. Intersection : ", set1.intersection(set2))
    print("3. Difference : ", set1.difference(set2))
    print("4. Symmetric dictionary : ", set1.symmetric_difference(set2))

if __name__ == '__main__':
    print("\n1. Write a Python program to remove the characters which have odd index values of a given string.")
    even_index_characters()
    print("\n2. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.")
    generate_list_tuple()
    print("\n3. Write a Python program to accept a filename from the user and print the extension of that.")
    string_extension()
    print("\n4. Write a python program to return number of vowels in a given string.")
    count_vowels()
    print("\n5. Write a Python program to remove duplicates from a list")
    remove_dulpicates()
    print("\n6. Write a Python program to find the second largest number in a list.")
    second_largest_num()
    print("\n7. Write a Python program to replace last value of tuples in a list by 100.")
    replace_last_val()
    print("\n8.  Write a Python program to add the 10 to all the values of a dictionary.")
    add_in_values()
    print("\n9. Write a Python program to count number of items in a dictionary value that is a list.")
    count_dict_vals_in_list()
    print("\n10. Write a program to create two sets and print their union, intersection, difference and symmetric difference.")
    set_operation()
