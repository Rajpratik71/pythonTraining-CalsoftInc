# Declearing a list

samplelist = [1, 'a', 'string' , 1+2]

samplelist.append(6)

print(samplelist)

samplelist.pop()

print(samplelist[1])


# Declaring a tuple

sampletuple = (1 , 'a' , "abs" , 'abc')

print(sampletuple[2])

# Iteration

# printing 1 to 10

i = 0
while (i < 10):
    i += 1
    print(i)


# Iterating Strings

samplestring = "Sample test string"

for i in samplestring:
    print(i)

# Iteration by loop in list

for i in samplelist:
    print(i)


#  Iteration by loop for range

for i in range(0,10):
    print(i)
