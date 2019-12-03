#!/usr/bin/env python
from math import sqrt

class Triangel(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a
        #return "aaa"

    def test_1(a, b, c):
        print(a)
        print(b)
        print(c)

    def perimeter(self, test):
        return self._a + self._b + self._c

    def area(self):
        half = (a + b + c) / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._C))

class test(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def print_test(self):
        print(self._a)
        print(self._b)
        print(self._c)

def main():
    t1 = Triangel(2, 3, 4)
    t2 = test(10, 10, 10)
    print(t1.is_valid(2,3,4))
    print(Triangel.is_valid(2,3,4))
    t1.test_1(2,3)
    #print(t1.perimeter("heh"))
    #print(Triangel.perimeter(t1,"heh"))
    #print(Triangel.perimeter("heh","shao"))

if __name__ == "__main__":
    main()
