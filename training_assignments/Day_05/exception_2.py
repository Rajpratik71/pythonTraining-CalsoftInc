class NegativePriceException(Exception):
    pass

item_count = int(input("enter the number of items"))
a = []
items = item_count
while item_count > 0:
    try:
        for i in range(items):
            item = int(input("enter item num"))
            if item > 0 :
                a.append(item)
                item_count = item_count - 1
            else:
                raise NegativePriceException
    except NegativePriceException:
        print("sorry negitive numbers not allowed")

print(a)