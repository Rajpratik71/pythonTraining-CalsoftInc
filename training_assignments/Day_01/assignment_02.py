"""
2. Write a Python program which accepts a sequence of comma-separated numbers from user and
 generate a list and a tuple with those numbers.
sample input: 3, 5, 7, 23
sample output:
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
seq_num = input("Enter comma separated numbers : ")
num_list= []
num_tuple = ()  # OR # num_tuple = tuple()

for i in seq_num:
    num_list.extend(i)  # OR # num_list = num_list + [i]
    # this will update the id(num_tuple) every time
    num_tuple = num_tuple + tuple(i)

print("type(num_list)=>{}, {} ".format(type(num_list), num_list))
print("type(num_tuple)=>{}, {}".format(type(num_tuple), num_tuple))

"""
Observation:
It takes string without comma
It takes string of integer as character
output of observation:
Enter comma separated numbers : 23zxc
type(num_list)=><class 'list'>, ['2', '3', 'z', 'x', 'c'] 
type(num_tuple)=><class 'tuple'>, ('2', '3', 'z', 'x', 'c')

Output:
Enter comma separated numbers : 4,5,6,7,8
type(num_list)=><class 'list'>, ['4', '5', '6', '7', '8'] 
type(num_tuple)=><class 'tuple'>, ('4', '5', '6', '7', '8')
"""