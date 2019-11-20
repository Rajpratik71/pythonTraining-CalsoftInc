def func():
    print(5/0)
try:
    func()
except Exception as e:
    print(e)