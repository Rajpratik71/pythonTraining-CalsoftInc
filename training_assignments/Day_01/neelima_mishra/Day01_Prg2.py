'''
2. Write a Python program which accepts a sequence of comma-separated numbers from user and
 generate a list and a tuple with those numbers.
sample input: 3, 5, 7, 23
sample output:
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''
numbers = input('Enter comma-separated integers: ')
print('User entered: ', numbers)
list_out_num = numbers.split(',')
print('List is:', list_out_num)
tuple_out_num = tuple(list_out_num)
print('Tuple is: ', tuple_out_num)