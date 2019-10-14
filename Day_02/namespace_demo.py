# global variable
pi = 'global pi variable'
  
def outer():
    # Enclosed variable
    pi = 'outer pi variable'
    def inner():
        # uncomment any one of the below and check the output
        # pi = 'inner pi variable' 
        # nonlocal pi
        # global pi
        print(pi) 
    inner()

outer()
print(pi)
