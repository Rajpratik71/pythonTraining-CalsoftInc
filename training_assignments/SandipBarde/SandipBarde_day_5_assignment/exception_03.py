
class User_defined_exception1(Exception):
    def __init__(self):
        self.message = "Please enter greater char"
class User_defined_exception2(Exception):
    def __init__(self):
        self.message = "Please enter lesser char"

alphabet = 'k'
if __name__ == "__main__":
    print("Welcome for char guess\n")
    while True:
        try:
            foo = input ( "Enter an alphabet: " )
            if foo < alphabet:
                raise User_defined_exception1
            elif foo > alphabet:
                raise User_defined_exception2
            if foo == alphabet:
                break
        except User_defined_exception1 as ex1:
            print(ex1.message)
        except User_defined_exception2 as ex2:
            print(ex2.message)
    print("Congratulations! You guessed it correctly.")