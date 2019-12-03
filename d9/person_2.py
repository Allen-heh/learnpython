#!/usr/bin/env python
class person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def eat(self):
        print("eat")
        print(self)

    @staticmethod
    def say():
        print("say")

    @classmethod
    def play(cls, test):
        print("play")
        print(cls)
        print(test)

def main():
    p1 = person("heh", 16)

    #print(p1.eat())
    print(p1)
    print(person.eat(p1))
    #person.eat("aaa")
    print("----------")

    p1.say()
    person.say()
    print("----------")

    p1.play("aaa")
    person.play("aaa")

if __name__ == "__main__":
    main()
