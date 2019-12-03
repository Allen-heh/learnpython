#!/usr/bin/env python
import time

class clock(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def pointer(self):
        self.second +=1
        if self.second == 60:
            self.second = 0
            self.minute +=1
        if self.minute == 60:
            self.minute = 0
            self.hour +=1
        if self.hour == 24:
                self.hour = 0
        return ("%02d:%02d:%02d" % (self.hour, self.minute, self.second))

def main(h, m, s):
    c1 = clock(h, m, s)
    while True:
        print(c1.pointer())
        time.sleep(0.1)

if __name__ == "__main__":
    main(23, 57, 23)
