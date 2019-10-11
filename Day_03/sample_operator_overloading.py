class Ramayan:

    def __init__(self, pages):
        self.pages = pages

    def __gt__(self, other):
        return self.pages > other.pages

class Mahabharat:

    def __init__(self, pages):
        self.pages = pages


book_1 = Ramayan(1000)
book_2 = Mahabharat(2000)

# If __get__ removed: TypeError: '>' not supported between instances of 'Ramayan' and 'Mahabharat'

if (book_1 > book_2):
    print("Ramayan book has more pages")
else:
    print("Mahabharat book has more pages")
