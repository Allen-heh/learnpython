#!/usr/bin/env python
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

def main():
    p1 = Person("shao", 18)
    print(p1.name)
    print(p1.age)
    p1.name = "heh"
    p1.age = 20
    print(p1.name)
    print(p1.age)

if __name__ == "__main__":
    main()
