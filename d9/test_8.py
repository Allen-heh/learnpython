#!/usr/bin/env python
class Test(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return "test"

    def __repr__(self):
        return "test2"

def main():
    t1 = Test("heh", 16)
    print(t1)
    print(t1.__repr__())
    #t1.__repr__()

if __name__ == "__main__":
    main()
