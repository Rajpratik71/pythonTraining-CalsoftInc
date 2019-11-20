# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:45:51 2019

@author: vamsi.reddy
"""

with open('calsoftinc.txt','w') as file:
    file.write('This is Calsoft Banglore')
with open('calsoftinc.txt','r') as file:
    print(list(file))