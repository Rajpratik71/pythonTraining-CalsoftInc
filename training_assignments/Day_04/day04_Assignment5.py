'''
5)Write a generator to return fibonacci series from 0 untill the number of times the input provided by the user 

Example:
input:5 
output:
0
1
1
2
3 
Explanation:
Here the input value provided by the user is '5' which means the generator should return the fibonacci values 5 times and on
6th atempt it should return a StopIteration Error
'''
def fibonacci_series():
	a=0
	b=1
	while 1:
		yield a
		c=a+b
		a=b
		b=c
if __name__=='__main__':
	generator = fibonacci_series()
	for i in range(6):
		print(next(generator))
