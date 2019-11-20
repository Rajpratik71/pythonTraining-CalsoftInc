class NegativePriceException(Exception):
    pass
try:
    price = int(input("Please give me the price"))
    if price<0:
        raise NegativePriceException
    else:
        print (price)
except NegativePriceException:
    print("Price can't be negative")