# Flow Control example

# if, elif else example
x = "one"
if x == "one":
    print("one is selected")

elif x == "two":
    print("two is selected")

else:
    print("Something else is selected")


# if -- else:
if x == "one":
    print("one is selected")
else:
    print("Something else is selected")



for i in in range(2, 100, 2);
    # prints a list of even numbers uptil 98
    # Note: 100 is exclusive in range function
    print(i)


# Use of break statement inside loop
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")


# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")


# In this program, 
# we check if the number is positive or
# negative or zero and 
# display an appropriate message

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
    
 
 # With example to open a file
 with open('output.txt', 'w') as f:
    f.write('Hi there!')


# Function example:
def is_prime(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            break
    else:
        return True
    return False
