class Count:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __getattr__(self, item):
        self.__dict__[item] = 0

    def __getattr__(self, item):
        self.__dict__[item] = 0
        return 0


obj = Count(5, 10)

print(obj.min)
print(obj.max)
print(obj.current)
