def facto(num):
	if (num==0 or num==1):
		return 1
	else:
		return num*facto(num-1)

def fibo(num):
    a=0
    b=1
    if(num<=0):
        print("Number must be greater than 0")
    elif(num==1):
        print(a)
    else:
        for i in range(0,num):
            print(a, end=' ')
            c=a+b
            a=b
            b=c

if __name__=="__main__":
	operation = int(input("Enter operation name to be perform::\n For Factorial Please enter 1 \n For Fibonacci Series please enter 2\n"))
	if(operation==1):
		number = int(input("Enter number to calculate factorial: "))
		fact = facto(number)
		print("Factorial of {} is {}".format(number,fact))
	elif(operation==2):
		count = int(input("Enter count to generate fibonacci series: "))
		print("Fibonacci series for count {} is::".format(count))
		fibo(count)
