'''
Below function will return solution of quadratic equation of form ax^2+bx+c
'''
import math 

def get_quadratic_solution(a,b,c):
	x1 = -b/(2*a)
	discriminant = (b*b - 4*a*c)
	if discriminant<0:
		x2 = complex(0,math.sqrt(abs(discriminant)))/(2*a)
	else:	
		x2 = math.sqrt(discriminant) / (2*a)
	return (x1+x2), (x1-x2)