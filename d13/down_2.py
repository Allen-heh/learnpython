from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print("start process, pid is %d" % getpid())
    print("start download %s" % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print("%s is ok, use %d" % (filename, time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task, args=("aaa.pdf", ))
    p1.start()
    p2 = Process(target=download_task, args=("bbb.avi", ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print("all use %.2f" % (end - start))


if __name__ == "__main__":
    main()
