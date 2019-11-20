'''
2. Write a program to count positive and negative numbers in a list.
Task is to add break point in code to check we are getting correct count for every ieration, 
also check all debugging commands given in PPT.
'''
import pdb
def count_positive_negative(sample_list):
	positive_count = 0
	negative_count = 0
	for element in sample_list:
		if(element>0):
			pdb.set_trace()
			positive_count+=1
		elif(element<0):
			pdb.set_trace()
			negative_count+=1
	return positive_count,negative_count

if __name__=='__main__':
	sample_list=[0,1,-2,4,3,5,-6,-8]
	positive_count,negative_count=count_positive_negative(sample_list)
			