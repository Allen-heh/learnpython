#!/usr/bin/env python
from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass = ABCMeta):
#class Fighter(object):

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass

class Ultraman(Fighter):

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15,25)

    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return "url %s,%s,%s" % (self._name, self._hp, self._mp)

class Monster(Fighter):

    __slots__ = ('_name', '_hp')

   #def __init__(self, name, hp):
   #    super().__init(name, hp)

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return "mon %s,%s" % (self._name, self._hp)


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    monster_len = len(monsters)
    while True:
        index = randrange(monster_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end=' ')



def main():
    u1 = Ultraman("heh", 1000, 100)
    m1 = Monster("mon1", 500)
    m2 = Monster("mon2", 600)
    m3 = Monster("mon3", 700)
    ms = [m1, m2, m3]

    #display_info(u1, ms)
    fight_round = 1
    while u1.alive and is_any_alive (ms):
        print("%02d round" % fight_round)
        m = select_alive_one(ms)
        skill = randint(1,10)
        if skill <= 6:
            print("%s attack %s" % (u1.name, m.name))
            u1.attack(m)
            print("%s resume %d" % (u1.name, u1.resume()))
        elif skill <= 9:
            if u1.magic_attack(ms):
                print("%s magic attack" % u1.name)
            else:
                print("magic attack is fail")
        else:
            if u1.huge_attack(m):
                print("%s use huge attack %s" % (u1.name, m.name))
            else:
                print("%s attack %s" % (u1.name, m.name))
                print("%s resume %d" % (u1.name, u1.resume()))
        if m.alive > 0:
            print("%s re attack %s" % (m.name, u1.name))
            m.attack(u1)
        display_info(u1, ms)
        fight_round += 1
    print("over")
    if u1.alive > 0:
        print("Win")
    else:
        print("Game Over")
    

if __name__ == "__main__":
    main()
