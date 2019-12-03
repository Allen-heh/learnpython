#!/usr/bin/env python
import math

class point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.__z = x

    def move_to(self, x1, y1):
        self._x = x1
        self._y = y1

    def move_by(self, dx, dy):
        self._x += dx
        self._y += dy

    def distance(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        return math.sqrt(dx**2 + dy**2)

    def print_xy(self):
        print(self._x)
        print(self._y)

def main():
    p1 = point(10,10)
    p2 = point(2,2)
    #print(p1)
    #print(p1._point__z)
    #p1.print_xy()
    #print(p2)
    #p2.print_xy()
    #print(p1.distance(p2))
    print(p1._x)
    #p1.move_to(1,2)
    #print(p1._x)
    point.move_to(p1,2,2)
    print(p1._x)

if __name__ == "__main__":
    main()
