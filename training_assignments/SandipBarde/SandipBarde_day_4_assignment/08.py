class MonkeyPaching:
    def originalMethod(self):
        print("I am from original method")

def patchMethod():
    print("I am from monkey patch method")

if __name__ == "__main__":
    obj  = MonkeyPaching()
    obj.originalMethod = patchMethod # we are patching the new method with original method.
    obj.originalMethod() # this will not call to original method but will call to patched method