import pdb
num = int(input("enter a number: "))

length = len(str(num))
sum = 0
temp = num

while (temp != 0):
    pdb.set_trace()
    sum = sum + ((temp % 10) ** length)
    temp = temp // 10

if sum == num:
    print("armstrong number")
else:
    print("not armstrong number")