class ContextManager:
    def __enter__(self):
        self.d = dict()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.d.clear()

with ContextManager() as c:
    print(c.d) # printing default dictionary