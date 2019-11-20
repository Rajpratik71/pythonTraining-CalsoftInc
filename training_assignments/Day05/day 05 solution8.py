# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:27:36 2019

@author: pentela.srikrishna
"""

import pdb
def cre_matrix(rows,columns):
    matrix=[]
    for row in range(rows):
        matrix_row=[]
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