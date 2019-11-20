#1. Write a Python program to remove the characters which have odd index values of a given string.
def remove_odd_index_values():
        s = "Starting with Python."
        print("Original String: ",s)
        print("String after removing odd index values: ",s[::2])


#2. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
def generate_list_and_tuple():
        numbers = input("Enter comma-separated numbers to generate list and tuple ")
        list_ = numbers.split(',')
        tuple_ = tuple((list_))
        print("List from entered numbers: ",list_)
        print("Tuple from entered numbers: ",tuple_)

#3. Write a Python program to accept a filename from the user and print the extension of that.
def file_extension():
        filename = input("Enter file name with extension: ")
        parts = filename.split('.')
        print("Extension of filename entered: ",parts[1])

#4. Write a python program to return number of vowels in a given string.
def count_vowels_in_string():
        sample_input = "Getting started with python"
        vowels = ['a','e','i','o','u']
        vowels_count=0
        for s in sample_input:
                if(s in vowels):
                        vowels_count+=1
        print("Total vowels found in < {} >: {}" .format(sample_input,vowels_count))

#5. Write a Python program to remove duplicates from a list
def remove_duplicates():
        sample_list = [1, 3, 1, 'python', 'java', 'python']
        unique_list = list(dict.fromkeys(sample_list))
        print("Original List: ",sample_list)
        print("Unique List: ",unique_list)

#6. Write a Python program to find the second largest number in a list.
def print_second_largest_in_list():
        sample_list=[-8, 1, 2, -2, 0]
        print("Input List: ",sample_list)
        sample_list.sort()
        print("Second largest number in list is: {} ".format(sample_list[-2]))

#7. Write a Python program to replace last value of tuples in a list by 100.
#sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

#8. Write a Python program to add the 10 to all the values of a dictionary.
def update_dict_values():
        sample_dict = {1: 20, 2: 30, 3: 40, 4: 50, 5: 60}
        print("Input dictionary: ",sample_dict)
        for key in sample_dict.keys():
                sample_dict[key]+= 10
        print("Dictionary after adding 10 to values: ",sample_dict)

#9. Write a Python program to count number of items in a dictionary value that is a list.
def count_listmembers_in_dict():
        d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
        print("Input dictioanry: ",d)
        count=0
        for value in d.values():
                if(isinstance(value,list)):
                        count+=len(value)
        print("Number of items in dictionary value that is list: ",count)

#10. Write a program to create two sets and print their union, intersection, difference and symmetric difference.
def set_operations():
        set1 = {1,2,3,4,5,6,7,8}
        set2 = {2,3,4,5,1}
        print("Set1: ",set1)
        print("Set2: ",set2)
        print("Union of sets: ",set1.union(set2))
        print("Difference of sets: ",set1.difference(set2))
        print("Symmetric Difference of sets: ",set1.symmetric_difference(set2))
        print("Intersection of sets: ",set1.intersection(set2))

if __name__=='__main__':
        print("\n1. Write a Python program to remove the characters which have odd index values of a given string.")
        remove_odd_index_values()
        print("\n2. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.")
        generate_list_and_tuple()
        print("\n3. Write a Python program to accept a filename from the user and print the extension of that.")
        file_extension()
        print("\n4. Write a python program to return number of vowels in a given string.")
        count_vowels_in_string()
        print("\n5. Write a Python program to remove duplicates from a list")
        remove_duplicates()
        print("\n6. Write a Python program to find the second largest number in a list.")
        print_second_largest_in_list()
        print("\n8. Write a Python program to add the 10 to all the values of a dictionary.")
        update_dict_values()
        print("\n9. Write a Python program to count number of items in a dictionary value that is a list.")
        count_listmembers_in_dict()
        print("\n10. Write a program to create two sets and print their union, intersection, difference and symmetric difference.")
        set_operations()
