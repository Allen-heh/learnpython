#!/usr/bin/env python
class Test(object):

    aaa = "aaa"

    def __init__(self, name, content):
        self._name = name
        self._content = content

    def normal_method(self):
        print(self._content)

    @classmethod
    def class_method(cls):
        print(cls.aaa)

    @staticmethod
    def static_method():
        print(self._content)


def main():
    t1 = Test("heh","python")
    t1.normal_method()
    t1.class_method()

if __name__ == "__main__":
    main()
