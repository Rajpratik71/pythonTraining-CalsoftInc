# Python program to illustrate  
# *args with first extra argument 
def argdemo(arg1, *args): 
    print ("First argument :", arg1) 
    for arg in args: 
        print("Next argument through *args :", arg) 
  
argdemo('Hello', "Welcome", "all")

# Python program to illustrate  **kargs for  
# variable number of keyword arguments with 
# one extra argument. 
  
def kwargdemo(arg1, **kwargs):
    print ("First argument :", arg1) 
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
kwargdemo("Hi", one ='one', two ='two', three='three')
