#!/usr/bin/env python
"""
Program on operator overloading(< - less than operator)
"""


class Ramayan:
    def __init__(self, pages):
        self.pages = pages

    # Overloading gt('>') operator to work as '<'
    def __gt__(self, other):
        return self.pages < other.pages

    # Overloading lt('<') operator to to work as '<'
    # def __lt__(self, other):
    #     return self.pages > other.pages


class Mahabharat:
    def __init__(self, pages):
        self.pages = pages


if __name__ == "__main__":
    book_1 = Ramayan(1000)
    book_2 = Mahabharat(2000)

    # If __gt__ not overloaded in class then arises a
    # TypeError: '>' not supported between instances of 'Ramayan' and 'Mahabharat'
    # print(book_1 > book_2)

    print(book_1 > book_2)  # 1000 > 2000

    if book_1 > book_2:
        print("Ramayan book has more pages")
    else:
        print("Mahabharat book has more pages")

    # If we overload less than(<) operator
    # print(book_1 < book_2)  # 1000 < 2000
