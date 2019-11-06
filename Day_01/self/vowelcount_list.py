# Program to count the number of
# each vowel in a string using
# dictionary and list comprehension

# change this value for a different result
ip_str = "Hello, have you tried our turorial section yet?"

# uncomment to take input from the user
# ip_str = input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# count the vowels
count = {x: sum([1 for char in ip_str if char == x]) for x in "aeiou"}

print(count)
