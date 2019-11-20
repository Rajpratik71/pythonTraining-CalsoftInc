class User_defined_exception1(Exception):
    pass

class User_defined_exception2(Exception):
    pass

alphabet = 'k'

while True:
    try:
        foo = input( "Enter an alphabet: " )
        if foo < alphabet:
            raise User_defined_exception1
        elif foo > alphabet:
            raise User_defined_exception2
        elif foo == alphabet:
            break
    except User_defined_exception1:
        print("please try alphabets bigger than this")
    except User_defined_exception2:
        print("please try alphabets smaller than this")


print("Congratulations! You guessed it correctly.")
