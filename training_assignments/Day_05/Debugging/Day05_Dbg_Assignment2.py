'''
3. Write a program that will accept input from user,
X = row, Y = col, serach_value = V

create a X*Y matrix and store numbers in it in order i.e. X+(Y*Y) 
then search the number V in matrix and add break-point in code if cell value is equal to V and 
finally program will return the number of occurences of V in matrix.
'''
import pdb
def create_matrix(rows,columns):
	matrix = []
	for row in range(rows):
		matrix_row = []
		for column in range(columns):
			matrix_row.append(row + (column*column))
		matrix.append(matrix_row)
	return matrix

if __name__=='__main__':
	rows, columns = input("Enter number of rows and columns space separated").split()
	rows = int(rows)
	columns = int(columns)
	element = int(input("Enter element to search in matrix"))
	element_occurrence = 0
	matrix=create_matrix(rows,columns)
	for row in range (rows):
		for column in range(columns):
			print(matrix[row][column], end=" ")
			if(matrix[row][column]==element):
				pdb.set_trace()
				element_occurrence+=1
		print()
	print("Element {} occurred {} times in matrix".format(element,element_occurrence))