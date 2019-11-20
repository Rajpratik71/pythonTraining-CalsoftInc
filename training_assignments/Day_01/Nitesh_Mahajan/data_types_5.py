#!usr/bin/env python


def remove_duplicates(input_list):
    """
    This function finds total number of vowels present in given string
    Args: input_list
    Returns: output_list
    """
    unique_set = frozenset(input_list)  # Type cast to Frozenset to remove duplicates and retain order
    output_list = list(unique_set)  # Again Type cast to list from frozenset
    return output_list


list1 = [1, 3, 1, 'python', 'java', 'python']
output = remove_duplicates(list1)
print(output)