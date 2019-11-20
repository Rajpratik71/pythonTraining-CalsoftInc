#!usr/bin/env python


def find_vowles_count(in_str):
    """
    This function finds total number of vowels present in given string
    Args: in_str
    Returns: count
    """
    count = 0
    vowels = ('a', 'e', 'i', 'o', 'u')
    for i in in_str:
        if i in vowels:
            count += 1
    return count


sample_input = "Getting started with python"
output = find_vowles_count(sample_input)
print("Total vowels found in <sample_input>: "+str(output))
