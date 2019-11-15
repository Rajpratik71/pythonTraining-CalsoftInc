"""Write a Python program to find sequences of lowercase letters joined with a underscore."""
import re

def text_match(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')

print(text_match("xxy_cbbbc"))
print(text_match("aab_Xbbbz"))
print(text_match("Yaab_zZbbc"))