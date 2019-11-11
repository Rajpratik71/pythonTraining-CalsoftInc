class Parent:
    def __init__(self):
        print('initializing parent')

    def parent_method(self):
        print('inside parent method')


class Child(Parent):
    def __init__(self):
        print('initializing child')
        super().__init__()
        # super()

    def child_method(self):
        print('inside child method')


childObj = Child()
childObj.child_method()

childObj.parent_method()
