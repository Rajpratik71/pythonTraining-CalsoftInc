# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:27:17 2019

@author: pentela.srikrishna
"""

alphabet = 'M'
class firstAlphabetException(self,msg):
    self.msg=msg
class secondAlphabetException(self,msg):
    self.msg=msg

while True:
	try:
             foo = int(input ( "Enter an alphabet: " ))
        
             if foo < alphabet:
            
                     raise firstAlphabetException(foo,alphabet)
            
             elif foo > alphabet:
            
			          raise secondAlphabetException(foo,alphabet)
            
	except firstAlphabetException as firstAE:
        
            print(firstAE)
            
	except secondAlphabetException as secondAE:
        
            print(secondAE)
            
print(" You guessed it correctly.")
