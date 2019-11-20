'''
6. Write a Python program to find the second largest number in a list.
sample input: [-8, 1, 2, -2, 0]
sample output: 1
'''
l1 = [-8, 1, 2, -2, 0]
sec_larg = None
count = 0
while count < len(l1):
    for i in range(len(l1)-1):
        if sec_larg == None:
            sec_larg = l1[i]
            continue
        elif l1[i] > l1[i+1]:
            sec_larg = l1[i]
            l1[i] = l1[i+1]
            l1[i+1] = sec_larg
    count += 1
print('second largest element in list is: ', l1[-2])