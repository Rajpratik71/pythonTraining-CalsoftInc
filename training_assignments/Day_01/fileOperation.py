"""
3) Write a python script to open a file with "with open", add some content , read it and print the same.
"""

def fileOperations():
    with open("File.txt",'w') as file:
        file.write( "Welcome to python training !!!")

    with open("File.txt",'r') as file:
	    data = file.read()
	    print( data )

if __name__=='__main__':
	fileOperations()