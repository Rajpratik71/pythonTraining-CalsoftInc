"""List operations"""
fruits = ['orange', 'apple', 'pear', 'banana', 'apple']
print('value of list: ', fruits)
fruits.append('grape') # append element at end
fruits.insert(0, 'kiwi') # insert element at 0th index
print("fruits after fruits.append('grape') & fruits.insert(0, 'kiwi'): ", fruits)
fruits.extend(['orange', 'pear']) # takes iterable and extend the list
print("fruits after fruits.extend(['orange', 'pear'])", fruits)
print("fruits.count('apple'): ", fruits.count('apple'))
# list.copy() - returns swallow copy of list
fruits_new = fruits.copy()
fruits_new.append('mango')
print(f"fruits_new: {fruits_new} and fruits: {fruits}")
print("fruits after fruits.sort():", fruits.sort()) # sort in ascending default if 'reverse=True' then descending
fruits.remove('apple') # removes 1st occurence
print("fruits after fruits.remove('apple'): ", fruits)
print("result of fruits.pop(1): ", fruits.pop(1))
print('fruits after fruits.pop(1): ', fruits) # if no index then removes last
fruits.clear()
print('after fruits.clear(): ', fruits) # empty the list
del fruits
print("after 'del fruits': ", fruits) # NameError
