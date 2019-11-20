import pdb

rows = int(input("enter the rows"))
cols = int(input("enter the cols"))
search = int(input("enter the search value"))
matrix =[]
count = 0

for i in range(0,rows):
    a=[]
    for j in range(0,cols):
        c = i+(j*j)
        a.append(c)
    matrix.append(a)

for i in matrix:
    for j in i:
        if j == search:
            pdb.set_trace()
            count = count+1

print(f"searched number {search} appears {count} times")