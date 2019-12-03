#!/usr/bin/env python
class test(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        print("aaa")
        return "this is a test."

t1 = test("heh", 18)
#print(t1)
ttt = t1.__str__()
print(ttt)
print(t1)
