#!/usr/bin/env python
aaa = [-1,-2,-3]
def alive(ms):
    for m in ms:
        print("aaa")
        if m > 0:
            return True
    return False

print(alive(aaa))
