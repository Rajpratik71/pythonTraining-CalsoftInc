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


# Dictionary

sampledict = dict()

sampledict2 = {}

# Adding value to dictionary

sampledict['xyz'] = 123

print(sampledict)

sampledict2['abc'] = 234

print(sampledict2)

# Printing Only key or values

print(sampledict.keys())

print(sampledict.values())

# Iterate over dictionary by address

for i in sampledict:
    print(" %s %d" %(i,sampledict[i]))

# Iterate over dictionary by iteration

for index, key in enumerate(sampledict):
    print(index, key, sampledict[key])

# Checking If key exist

print( 'abc' in sampledict)

print( 'abc' in sampledict2)

# Deleting the key value pair:

del sampledict['abc']

print(sampledict)

del sampledict2['abc']

print(sampledict)

