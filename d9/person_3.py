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

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print("%s is playing" % self._name)

    def watch_tv(self):
        if self._age > 18:
            print("%s is watch av" % self._name)
        else:
            print("%s is watch naruto" % self._name)

class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print("%s is studing %s" % (self._name, course))

class Teacher(Person):
    
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print("%s is teaching %s" % (self._name, course)) 

def main():
    p1 = Person("heh", 16)
    s1 = Student("hey", 8, "1")
    t1 = Teacher("shao", 9, "English")
    #print(p1)
    #print(s1)
    #print(t1)
    

if __name__ == "__main__":
    main()
