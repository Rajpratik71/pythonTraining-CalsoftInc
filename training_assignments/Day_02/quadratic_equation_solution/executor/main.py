import sys
import os
sys.path.append(os.path.abspath("../controller"))
import quadratic
if __name__=='__main__':
	#print(sys.path)
	a,b,c = input("Enter values of a,b,c").split()
	x=int(a)
	y=int(b)
	z=int(c)
	print("Your quadratic equation is:{}x^2+{}x+{}".format(a,b,c))
	#print(type(x))
	#print(type(y))
	#print(type(z))
	x1,x2=quadratic.get_quadratic_solution(x,y,z)	
	print("Value of x={} or x={}".format(x1,x2))
