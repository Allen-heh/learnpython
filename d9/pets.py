#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class Pets(object, metaclass = ABCMeta):

    def __init__(self, name, test):
       self._name = name
       self._test = test

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def make_voice(self):
        print("this is pets.")

class Dog(Pets):

    #def __init__(self, name, age):
    #    super().__init__(name)
    #    self._age = age

    #@property
    #def age(self):
    #    return self._age

    #@age.setter
    #def age(self, age):
    #    self._age = age

    def make_voice(self):
        print("wang wang wang")

class Cat(Pets):

    def __init__(self, name, eat, test):
        super().__init__(name, test)
        self._eat = eat

    @property
    def eat(self):
        return self._eat

    @eat.setter
    def eat(self, eat):
        self._eat = eat

    def make_voice(self):
        print("miao miao miao")

def main():
    #p1 = Pets("ppp", "test1")
    d1 = Dog("ddd", " test2")
    c1 = Cat("ccc", "food", "test3")
    #p1.make_voice()
    d1.make_voice()
    c1.make_voice()

if __name__ == "__main__":
    main()
