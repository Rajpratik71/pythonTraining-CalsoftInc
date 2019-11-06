"""String operations"""
# take input from user:
# user_input = input('Enter data: ')
s = "Starting with Python."
print("value of s : ", s)
print("x in s: ", "Python" in s)
print("x not in s: ", "Python" not in s)
print("s + t: ", s + " Good work")
print("s * n: ", s * 2)
print(15 * "*")
print("len(s): ", len(s))
print("min(s), max(s): ", min(s), max(s))  # min would give ' '
print("s.index(x): ", s.index("t"))  # s.index('t', 4,10) in between 4 to 10
print("s.count(x): ", s.count("t"))
print("str(123): ", str(123))
print("'*'.join(['ab', 'pq', 'rs']): ", "*".join(["ab", "pq", "rs"]))
print("s.upper(): ", s.upper())
print("s.lower(): ", s.lower())
print("s.startswith('S'): ", s.startswith("S"))
print("s.endswith('S'): ", s.endswith("S"))
print("s.find('with'): ", s.find("with"))
print("s.find('calsoft'): ", s.find("calsoft"))
# slicing
print("s[3] : ", s[3])
print("s[2:4]: ", s[2:4])
print("s[:] ", s[:])
print("s[-1:3]: ", s[-1:3])
print("s[::-1]: ", s[::-1])
print("s[::-2]: ", s[::-2])
