#!usr/bin/env python


def find_second_largest(input_list):
    """
    This function finds total number of vowels present in given string
    Args: input_list
    Returns: second_large_num
    """
    length = len(input_list)
    input_list.sort()  # Sorts the list in ascending order
    large_num = input_list[-1]
    cnt = input_list.count(large_num)  # Number of times the largest number occurred in the list
    second_large_num = input_list[length-cnt-1]  # Gets Second largest number from the sorted list
    return second_large_num


input_list = [-8, 1, 2, -2, 0]
output = find_second_largest(input_list)
print(output)
