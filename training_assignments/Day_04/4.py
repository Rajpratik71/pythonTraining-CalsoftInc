def check_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
            break
    else:
        return True


class PrimeNum:
    def __init__(self,max,min):
        self.max = max
        self.min = min

    def __iter__(self):
        return self

    def __next__(self):
        while (self.min <= self.max):
           a = check_prime(self.min)
           if a == True:
               print(self.min)
           self.min += 1
        raise StopIteration

if __name__ =='__main__':
    a = int(input("enter max num"))
    b = int(input("enter min num"))
    obj = PrimeNum(a, b)
    iter_obj = iter(obj)
    try:
        print(next(iter_obj))
    except StopIteration:
        print("Above are the prime numbers")