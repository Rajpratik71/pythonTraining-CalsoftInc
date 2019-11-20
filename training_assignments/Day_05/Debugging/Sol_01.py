num = int(input("enter a number: "))
 
length = len(str(num))
sum = 0
temp = num
 
while(temp != 0):
	sum = sum + (int(temp % 10) ** length)
	temp = temp / 10
print(sum)
if sum == num:
	print("armstrong number")
else:
	print("not armstrong number")