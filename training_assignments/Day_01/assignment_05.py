"""
5. Write a Python program to remove duplicates from a list
sample input: [1, 3, 1, 'python', 'java', 'python']
sample output: [1, 3, 'python', 'java']
"""
input = [1, 3, 1, 'python', 'java', 'python']
output = list(set(input))
print(output)

"""
Output:
[1, 3, 'python', 'java']
"""