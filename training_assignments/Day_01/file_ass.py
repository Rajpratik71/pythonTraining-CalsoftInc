#!/usr/bin/python

def file_operations():
    with open("file.txt", "w") as w_file:
        w_file.write("my file")

    with open("file.txt", "r") as r_file:
        data = r_file.read()
        print(data)

if __name__ == '__main__':
    file_operations()
