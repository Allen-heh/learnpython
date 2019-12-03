#!/usr/bin/env python
class Person(object):
    
    # 实例方法
    def eat(self):
        print(self)
        print("this is eat")

    # 静态方法
    @staticmethod
    def say():
        print("Saying....")
    
    # 类方法
    @classmethod
    def play(cls):
        print(cls)
        print("this is play")

print("1.")
york = Person()

print("2.")     # 调用实例方法
Person.eat(york)
york.eat()

print("3.")     # 调用静态方法
Person.say()
york.say()

print("4.")     # 调用类方法
Person.play()
york.play()
