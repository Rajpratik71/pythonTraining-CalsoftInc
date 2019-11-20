

class NegativePriceException(Exception):
    def __init__(self, msg):
        self.message = msg

if __name__ == "__main__":
    price = float(input("Enter the price\n"))
    try:
        if(price < 0):
            raise NegativePriceException("Inside the Exception:- Price is less than zero.")
        else:
            print("Execution completed successfully.")
    except NegativePriceException as e:
        print(e.message)