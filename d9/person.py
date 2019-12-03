#!/usr/bin/env python
class person(object):

    __slots__ = ('_name', '_age', '_gender')

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

    def play(self):
        if self._age >= 16:
            print("%sdoudizhu." % self._name)
        else:
            print("%sdonghuapian" % self._name)

def main():
    p1 = person("heh", 16)
    p2 = person("shao", 15)
    print(p1._name, p1._age)
    print(p2._name, p2._age)
    p1.play()
    p2.play()
    p1._age = 17
    p2._age = 14
    print(p1._name, p1._age)
    print(p2._name, p2._age)
    p1.play()
    p2.play()
    #p1.name = "heh1"
    #p2.name = "shao1"
    p1.age = "18"
    p2.age = "13"
    print(p1.name, p1.age)
    print(p2.name, p2.age)
    p1._gender = "male"
    print(p1._gender)


if __name__ == "__main__":
    main()
