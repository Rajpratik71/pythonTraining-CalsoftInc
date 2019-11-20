#!usr/bin/env python


def remove_odd_index(in_str):
    """
    This function removes odd index values from a given string
    Args: in_str
    Returns: out_str
    """
    out_str = in_str[::2]
    return out_str

sample_input = "abcdef"
output = remove_odd_index(sample_input)
print(output)
