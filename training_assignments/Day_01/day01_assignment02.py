"""
                Data type assignment
"""
"""
1. Write a Python program to remove the characters which have odd index values of a given string.
sample input: "abcdef"
sample output: "ace"
"""

def removeOddIndexValues ( string ) :
  finalstring = ""
  for i in range(len(string)):
    if i % 2 == 0:
      finalstring = finalstring + string[i]
  return finalstring

#driver function
def call_removeOddIndexValues( ):
    string=input("Enter input string:")
    print("Modified string is : ")
    print(removeOddIndexValues(string))

"""
2. Write a Python program which accepts a sequence of comma-separated numbers from user and
 generate a list and a tuple with those numbers.
sample input: 3, 5, 7, 23
sample output:
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

def createListAndTuple ( ) :
    values = input("Enter comma separated numbers: ")
    list_ = values.split(',')
    tuple_ = tuple(list_)
    print('List : ', list_)
    print('Tuple : ', tuple_)

#driver function
def call_createListAndTuple( ):
     createListAndTuple ( )

"""
3. Write a Python program to accept a filename from the user and print the extension of that.
sample input: python.py
sample output: py
"""

import os
def GetFilenameAndPrintExtension( ):
    filename =input  ( "Enter file name : ")
    file , extension = os.path.splitext(filename)
    print( extension)

    fileparts = filename.split('.')
    print( fileparts[1])



#driver function
def call_GetFilenameAndPrintExtension() :
    GetFilenameAndPrintExtension()

"""
4. Write a python program to return number of vowels in a given string.
sample input: 'Getting started with python'
sample output: "Total vowels found in <sample_input>: 6"
"""
def countVowel( input_string) :
    count = 0
    vowels = "aeiuoAEIOU"

    for letter in input_string:
        if letter in vowels:
            count = count + 1

    print("No. of vowels :", count)

#driver function
def call_countVowel() :
    string = input("Enter input string:")
    countVowel(string)


"""
5. Write a Python program to remove duplicates from a list
sample input: [1, 3, 1, 'python', 'java', 'python']
sample output: [1, 3, 'python', 'java']
"""
def RemoveDuplicate(input_list):
    final_list = []
    for i in input_list:
        if i not in final_list:
            final_list.append(1)
    return final_list

#driver function
def call_RemoveDuplicate():
    List = [1, 3, 1, 'python', 'java', 'python']
    print ( RemoveDuplicate (List))


"""
6. Write a Python program to find the second largest number in a list.
sample input: [-8, 1, 2, -2, 0]
sample output: 1
"""
def find2ndMax (list):
    len = len(list)
    list.sort()
    print ("print 2nd max element in list : ",  list[-2] )

def call_find2ndMax ():
    list = [-8, 1, 2, -2, 0]
    find2ndMax(list)

"""
7. Write a Python program to replace last value of tuples in a list by 100.
sample input: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
sample output:[(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""

def replaceTupleValue (list):
    for tuple in list:
        tuple[:-1] = 100

    print ("Output : " , list )

def call_replaceTupleValue():
    list  = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    replaceTupleValue(list)

"""
8. Write a Python program to add the 10 to all the values of a dictionary.
sample input: dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
sample output: {1: 20, 2: 30, 3: 40, 4: 50, 5: 60}
"""
def modify_dictionary_values ( dict ):
    sample_dict = {1: 20, 2: 30, 3: 40, 4: 50, 5: 60}
    print("Input dictionary: ",sample_dict)
    for key in sample_dict.keys():
        sample_dict[key]+= 10
    print("Dictionary after adding 10 to values: ",sample_dict)

"""
9. Write a Python program to count number of items in a dictionary value that is a list.
sample input: d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
sample output: 5
"""
def  countListItemsInDictionary ( dict ):
    list( dict.values() )
    count=0
    for value in d.values():
        if(isinstance(value,list)):
            count+=len(value)
    print("Count : ",count)

def call_countListItemsInDictionary():
    dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
    countListItemsInDictionary(dict)

"""
10. Write a program to create two sets and print their union, intersection, difference and symmetric difference.
"""
def SetOperations ( ) :
    values = input("Enter comma separated numbers set1: ")
    list = values.split(",")
    set1 = set(list)
    print('Set1 : ', set1 )

    values = input("Enter comma separated numbers set2 : ")
    list = values.split(",")
    set2 = set(list)
    print('Set2 : ', set2)
    print('Operations: ')
    print ("set intersection:" , set1.intersection(set2) )
    print ("set union:" ,set1.union(set2) )
    print ("set diffrence:" ,set1.difference(set2))
    print ("set symmetric_difference:" ,set1.symmetric_difference(set2))

#driver program
def call_SetOperations ( ) :
    SetOperations()


if __name__=='__main__':

    print("\n1. Write a Python program to remove the characters which have odd index values of a given string.")
    call_removeOddIndexValues()
    print("\n2. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.")
    call_createListAndTuple()
    print("\n3. Write a Python program to accept a filename from the user and print the extension of that.")
    call_GetFilenameAndPrintExtension()
    print("\n4. Write a python program to return number of vowels in a given string.")
    call_countVowel()
    print("\n5. Write a Python program to remove duplicates from a list")
    call_RemoveDuplicate()
    print("\n6. Write a Python program to find the second largest number in a list.")
    call_find2ndMax()
    print("\n7. Write a Python program to replace last value of tuples in a list by 100.")
    call_replaceTupleValue()
    print("\n8. Write a Python program to add the 10 to all the values of a dictionary.")
    modify_dictionary_values()
    print("\n9. Write a Python program to count number of items in a dictionary value that is a list.")
    call_countListItemsInDictionary()
    print("\n10. Write a program to create two sets and print their union, intersection, difference and symmetric difference.")
    SetOperations()
