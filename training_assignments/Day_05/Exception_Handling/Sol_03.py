class Error(Exception):
    pass
class User_defined_exception1(Error):
    pass
class User_defined_exception2(Error):
    pass

alphabet = 'k'

while True:
    try:
        foo = input("Enter the alphabet:")
        if foo < alphabet:
            raise User_defined_exception1
        elif foo > alphabet:
            raise User_defined_exception2
        else:
            print("Congratulations! You guessed it correctly.")
            break
    except User_defined_exception1:
        print("given alphabet is less than the guessed please choose another")	
    except User_defined_exception2:
        print("given alphabet is greater than the guessed please choose another")