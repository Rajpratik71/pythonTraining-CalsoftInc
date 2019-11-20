"""
6. Write a Python program to find the second largest number in a list.
sample input: [-8, 1, 2, -2, 0]
sample output: 1
"""
input = [9, 8, 1, -2, 4, 13, 15, -2, 0]
if len(input) < 2:
    print("list requires at least 2 numbers")
else:
    largest = input[1] if input[0] < input[1] else input[0]
    sec_largest = input[1] if input[0] > input[1] else input[0]
    for next in input[2:]:
        if next > largest:
            sec_largest = largest
            largest = next
        elif next > sec_largest and next < largest:
            sec_largest = next
    else:
        print("second largest : {}".format(sec_largest))


"""
Output:
second largest : 13
"""