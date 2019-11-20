#!usr/bin/env python


def replace_last_value(input_list):
    """
    This function replaces last value of tuples in a list by 100
    Args: input_list
    Returns: output_list
    """
    output_list = []
    for tup in input_list:
        new_list = list(tup[:-1])  # Convert each tuple into a list leaving last element
        new_list.append(100)  # Appends 100 to each new_list
        new_tup = tuple(new_list)  # Again type cast from list to tuple
        output_list.append(new_tup)  # Appends each new_tup in the output_list
    return output_list


input_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
output = replace_last_value(input_list)
print(output)
