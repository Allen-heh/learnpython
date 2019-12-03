from abc import ABCMeta, abstractmethod

class Personnal(object, metaclass=ABCMeta):

    def __init__(self, name, post):
        self._name = name
        self._post = post

    @property
    def name(self):
        return self._name

    @property
    def post(self):
        return self._post

    @abstractmethod
    def salary(self):
        pass


class Manage(Personnal):

    def salary(self):
        count = 15000
        print("%s is %s, salary is %d" % (self._name, self._post, count))


class Programmer(Personnal):

    #def __init__(self, name, post, work_hour):
    def __init__(self, name, work_hour):
        #super().__init__(name, post)
        super().__init__(name, "Programmer")
        self._work_hour = work_hour

    @property
    def work_hour(self):
        return self._work_hour

    @work_hour.setter
    def work_hour(self):
        self._work_hour = work_hour

    def salary(self):
        count = 150 * self._work_hour
        print("%s is %s, salary is %d" % (self._name, self._post, count)) 


class Saleperson(Personnal):

    pass


def main():
    m1 = Manage("heh", "manager")
    #p1 = Programmer("allen", "Programmer", 120)
    p1 = Programmer("allen", 120)
    m1.salary()
    p1.salary()

if __name__ == "__main__":
    main()
