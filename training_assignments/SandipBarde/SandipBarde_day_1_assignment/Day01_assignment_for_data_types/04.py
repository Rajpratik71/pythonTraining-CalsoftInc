def ReturnCountOfOvels(s):
    c = s.count('a')
    c += s.count('e')
    c += s.count('i')
    c += s.count('o')
    c += s.count('u')
    return c

if __name__ == "__main__":
    s = input("Enter the string for find ovels in it\n")
    print("Total vowels found in <" + s + ">:",ReturnCountOfOvels(s))