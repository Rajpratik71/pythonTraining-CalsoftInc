sample_str = "aIbohPhoBiA"

rev_sample_str = reversed(sample_str.casefold())

if list(sample_str.casefold()) == list(rev_sample_str):
    print(" String is a palindrome")
else:
    print(" String is not  a palindrome .")
