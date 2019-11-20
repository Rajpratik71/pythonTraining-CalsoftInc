'''
3. Write a Python program to accept a filename from the user and print the extension of that.
sample input: python.py
sample output: py
'''

user_input = input('Enter a filename: ')
print('Filename entered by user is: ', user_input)
extension = user_input.split('.')
print('File extension is: ', extension[-1])