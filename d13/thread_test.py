from random import randint
from threading import Thread
from time import time, sleep

def download(filename):
    print("start download %s" % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print("%s download over, use %d" % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('python',))
    t1.start()
    t2 = Thread(target=download, args=('java',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print("all use %.3f" % (end-start))


if __name__ == "__main__":
    main()
