"""
3. Write a Python program to accept a filename from the user and print the extension of that.
sample input: python.py
sample output: py
"""
file_name = input("Enter any file name with its extension : ")
print("File extension => ", file_name.split(".")[1])

"""
Output:
Enter any file name with its extension : calsoft.txt
File extension =>  txt
"""