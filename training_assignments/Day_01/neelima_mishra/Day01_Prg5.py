'''
5. Write a Python program to remove duplicates from a list
sample input: [1, 3, 1, 'python', 'java', 'python']
sample output: [1, 3, 'python', 'java']
'''

l1 = [1, 3, 1, 'python', 'java', 'python']
out_l1 = []
for ele in l1:
    if ele not in out_l1:
        out_l1.append(ele)
print('List without duplicates: ', out_l1)