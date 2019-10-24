class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    # iter method which returns an iterator object
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


obj = PowTwo(2)
# Iterator Object
iter_obj = iter(obj)
print(next(iter_obj))
print(next(iter_obj))
