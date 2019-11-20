'''
2. Write a python program that will change the logger format on the fly.
'''

import logging
logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.DEBUG)

class Complex:
        def __init__(self,real,imaginary):
                self.real = real
                self.imaginary = imaginary

        def __add__(self,other):
                logging.debug("Entry:__add__")
                logging.info("Adding {} and {}".format(self,other))
                return Complex(self.real+other.real, self.imaginary+other.imaginary)

        def __repr__(self):
                return '{}+{}j'.format(self.real,self.imaginary)

if __name__=='__main__':

        complex_obj1 = Complex(2,3)
        complex_obj2 = Complex(3,4)
        complex_obj3 = complex_obj1 + complex_obj2
        logging.warning("Addition is: %s",complex_obj3)