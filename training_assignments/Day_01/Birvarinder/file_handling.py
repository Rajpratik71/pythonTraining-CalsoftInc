#!/usr/bin/env python

#writing into file
def write_file(text):
    with open("samplefile.txt","a") as f:
        f.write(" "+text)

#reading the file
def read_file():
    with open("samplefile.txt","r") as f:
        data=f.read()
    print(data)


if __name__=='__main__':
    choice=int(input("1.read sample file     2. write into sample file 3.exit"))
    while choice != 3:
        if choice == 1:
            read_file()
            choice=int(input("1.read sample file     2. write into sample file 3.exit"))
        else:
            text=input("please enter text to be written in file")
            write_file(text)
            choice=int(input("1.read sample file     2. write into sample file 3.exit"))
    
