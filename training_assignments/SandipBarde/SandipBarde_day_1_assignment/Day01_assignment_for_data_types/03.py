def SeprateStringUsingDelimeter(s):
    s = s.split('.')
    return (s[1])

if __name__ == "__main__":
    s = input("Enter the filename with extension\n")
    print("Extension of file is:-", SeprateStringUsingDelimeter(s))