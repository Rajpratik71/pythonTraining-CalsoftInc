# 1 Remove odd indices from string.
sample = "abcdef"
print("String after removing odd indices:", sample[::2])

# 2 Generate list and tuple from comma separated inputs(numbers).
string = str(input("Enter comma separated numbers: "))
list1 = string.split(",")
test_list = [int(i) for i in list1]
test_tuple = tuple(test_list)
print("Input converted into list:", test_list)
print("Input converted into tuple:", test_tuple)

# 3 Print extension of a filename accepted from user.
filename = str(input("Enter filename: "))
extension = filename.split(".")[-1]
print("Extension of file:", extension)

# 4 Print number of vowels in a string.
string = "This is a sentence"
vowels = "aAeEiIoOuU"
count = 0
for item in string:
    if item in vowels:
        count += 1
print(f"Total number of vowels in '{string}' is {count}.")

# 5 Remove duplicates from a list.
sample_list = [1, 3, 1, 'python', 'java', 'python']
no_duplicates = []
for item in sample_list:
    if item not in no_duplicates:
        no_duplicates.append(item)
print("Removing duplicates from list: ", no_duplicates)

# 6 Find second largest number in list.
list1 = [-8, 1, 2, -2, 0]
list1.sort()
print("Second largest number in the list is: ", list1[-2])

# 7 Modify last element of each tuple in the list to 100.
list2 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list3 = []
for item in list2:
    l1 = list(item)
    l1[-1] = 100
    item = tuple(l1)
    list3.append(item)
print("Updated list: ", list3)

# 8 Add 10 to all values of a dictionary.
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
for key,value in dict_num.items():
    value += 10
    dict_num.update({key: value})
print("Updated dict is: ", dict_num)

# 9 Count total number of elements in list where value of dictionary is list.
d = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2'], 'Ben': 'sub5'}
count = 0
for value in d.values():
    if isinstance(value, list):
        count += len(value)
print("Count of items within all 'list' values is:", count)

# 10 Set Operations.
s1 = set(['Pune', 'Mumbai', 'Delhi', 'Kolkata', 'Bangalore', 'Delhi'])
s2 = {'Hyderabad', 'Mumbai', 'Nashik'}
print("Union of s1 and s2: ", s1.union(s2))
print("Intersection of s1 and s2: ", s1.intersection(s2))
print("Difference of s2 and s1: ", s2-s1)
print("Symmetric difference of s1 and s2: ", s1 ^ s2)
