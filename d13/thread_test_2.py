from random import randint
from threading import Thread
from time import time, sleep

class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print("start download %s" % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print("%s download over, use %d" % (self._filename, time_to_download))

def main():
    start = time()
    t1 = DownloadTask("python")
    t1.start()
    t2 = DownloadTask("java")
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print("download all use %.2f" % (end - start))


if __name__ == "__main__":
    main()
