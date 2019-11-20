"""
7. Write a Python program to replace last value of tuples in a list by 100.
sample input: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
sample output:[(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""
sample_input = [(),(10, 20, 40), (22,), (40, 50, 60), (70, 80, 90)]
sample_output = []
print("sample_input : ",sample_input)
for tpl in sample_input:
    sample_output.append(tpl[:-1] + (100,))
else:
    print("sample_output : ",sample_output)
"""
Output:
=======
sample_input :  [(), (10, 20, 40), (22,), (40, 50, 60), (70, 80, 90)]
sample_output :  [(100,), (10, 20, 100), (100,), (40, 50, 100), (70, 80, 100)]
"""