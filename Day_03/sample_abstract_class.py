#!/usr/bin/env python
"""
Python program showing how abstract base class work
"""

from abc import ABC, abstractmethod


class Polygon(ABC):

    # abstract method
    def no_of_sides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("I have 4 sides")


if __name__ == "__main__":
    t = Triangle()
    t.no_of_sides()

    q = Quadrilateral()
    q.no_of_sides()

    r = Pentagon()
    r.no_of_sides()

    h = Hexagon()
    h.no_of_sides()
