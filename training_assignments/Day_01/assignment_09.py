"""
9. Write a Python program to count number of items in a dictionary value that is a list.
sample input: d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
sample output: 5
"""
d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2'], 'shown': 'sub1'}
cnt = 0
dict_values = d.values()
for val in dict_values:
    if isinstance(val, list):
        cnt = cnt + len(val)
print(cnt)
"""
Output:
=======
5
"""