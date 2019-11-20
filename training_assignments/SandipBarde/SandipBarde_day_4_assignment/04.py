import sympy as sp
class PrimeNumbers:
    def __init__(self, limit, start):
        self.limit = limit
        self.start = start
    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.limit:
            while(not sp.isprime(self.start)):
                self.start = self.start + 1
                if self.start == self.limit:
                    raise StopIteration
            result = self.start
            self.start = self.start + 1
            if self.start == self.limit:
                raise StopIteration
            return result
        else:
            raise StopIteration

if __name__ == "__main__":
    print("Enter the upper limit of prime numbers ")
    limit = int(input())
    print("Enter the starting for prime numbers ")
    start = int(input())
    obj = PrimeNumbers(limit,start)
    iterObj = iter(obj)
    try:
        while(1):
            print(next(iterObj))
    except StopIteration:
        exit()