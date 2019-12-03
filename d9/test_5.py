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

    def play(self):
        print("%s is playing." % self._name)

    def study(self, course):
        if self._age > 18:
            print("%s is studying %s." % (self._name, course))

class Teacher(Person):

    def __init__(self, name, age, kemu):
        super().__init__(name, age)
        self._kemu = kemu

    @property
    def kemu(self):
        return self._kemu

    @kemu.setter
    def kemu(self, kemu):
        self._kemu = kemu

    def teach(self, course):
        print("%s is teaching %s" %(self._name, course))

class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        #self._name = name
        #self._age = age
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def listen(self, music):
        print("%s is listening %s" % (self._name, music))

def main():
    p1 = Person("heh", 18)
    t1 = Teacher("allen", 20, "math")
    s1 = Student("shao", 16, "s3")
    print(p1)
    print(t1)
    print(s1)
    print(p1.name,t1.name,s1.name)
    print(p1.age,t1.age,s1.age)
    p1.play()
    t1.play()
    s1.play()
    t1.teach("yuwen")
    s1.listen("music")
    print(s1._name,s1.name)
    print(s1._age,s1.age)

if __name__ == "__main__":
    main()
