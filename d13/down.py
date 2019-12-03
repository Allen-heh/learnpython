from random import randint
from time import time, sleep

def download_task(filename):
    print("start downloading %s..." % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print("%s use %d" % (filename, time_to_download))

def main():
    start = time()
    download_task("aaa.pdf")
    download_task("bbb.avi")
    end = time()
    print("all use %.2f" % (end - start))


if __name__ == "__main__":
    main()
