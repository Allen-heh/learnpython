#!/usr/bin/env python
class Test(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @classmethod
    def test(cls):
        d = 5
        e = 6
        f = 7
        return cls(d, e, f)

    def print_abc(self):
        print(self._a)
        print(self._b)
        print(self._c)

def main():
    t1 = Test(1,2,3)
    #print(t1)
    #t1.print_abc()
    #a = t1.test()
    #print(a)
    t2 = Test.test()
    print(t2)
    print(Test)
    print(Test.test)
    print(Test.print_abc)
    print(t1.print_abc)
    #print(t2)
    #t2.print_abc()
    #print(type(t2.print_abc()))

if __name__ == "__main__":
    main()
