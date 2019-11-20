# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:13:58 2019

@author: venkata.ramaiah
"""
def function(*args, a=[]):
    a.append(args)
    print(a)
if __name__=='__main__':
    function(1,2,3)
