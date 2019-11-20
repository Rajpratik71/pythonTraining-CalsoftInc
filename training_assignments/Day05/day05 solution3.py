# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:22:29 2019

@author: pentela.srikrishna
"""

import logging
logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.DEBUG)  
class string:
    def __init__(self,firstname ,secondname):
        self.firstname= firstname
        self.secondname=secondname
    def __add__(self,other):
        logging.debug("Entry:__add__")
        logging.info("my name is  {} my fashion is playing   {}".format(self,other))
        return string(self.firstname+other.firstname, self.secondname+other.secondname)
    def __repr__(self):
        return '{}+{}'.format(self.firstname,self.secondname)
if __name__=='__main__':
  obja = string("dhoni")
  objb = string("cricket")
  objc = obja + objb
  logging.warning("Addition is: %s",objc)