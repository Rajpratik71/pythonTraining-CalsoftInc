"""
10. Write a program to create two sets and print their union, intersection, difference and symmetric difference.
"""
A = {0, 2, 4, 6, 8}
B = set([1, 2, 3, 4, 5])

def Set_Union(s1, s2):
    union_list = []
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    else:
        for ele in s1:
            union_list.append(ele)
        for ele in s2:
            union_list.append(ele)
    return set(union_list)

def Set_Intersection(s1, s2):
    intersection_list = []
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    else:
        for ele in s1:
            if ele in s2:
                intersection_list.append(ele)
    return set(intersection_list)

def Set_Difference(s1, s2):
    difference_list = []
    for ele in s1:
        if ele not in s2:
            difference_list.append(ele)
    return set(difference_list)

def Symmetric_Difference(s1,s2):
    symm_diff_list = []
    for ele in s1:
        if ele not in s2:
            symm_diff_list.append(ele)
    for ele in s2:
        if ele not in s1 and ele not in symm_diff_list:
            symm_diff_list.append(ele)
    return set(symm_diff_list)

print(f"A = {A}\nB = {B}")

union_of_set = Set_Union(A, B)
print("Union : ",union_of_set)

intersection_of_set = Set_Intersection(A, B)
print("Intersection : ",intersection_of_set)

difference_of_set = Set_Difference(A, B)
print("Difference : ",difference_of_set)

symmetric_diff_of_set = Symmetric_Difference(A, B)
print("Symmetric diff : ",symmetric_diff_of_set)

"""
Output:
=======
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
Union :  {0, 1, 2, 3, 4, 5, 6, 8}
Intersection :  {2, 4}
Difference :  {0, 8, 6}
Symmetric diff :  {0, 1, 3, 5, 6, 8}
"""