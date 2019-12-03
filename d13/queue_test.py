from multiprocessing import Process, Queue
import random, time, os

def proc_write(q, urls):
    print("process %s is writing..." % os.getpid())
    for url in urls:
        q.put(url)
        print("put %s to queue." % url)
        time.sleep(random.random())

def proc_read(q):
    print("process %s is reading..." % os.getpid())
    while True:
        url = q.get(True)
        print("get %s from queue." % url)

def main():
    q = Queue()
    w1 = Process(target=proc_write, args=(q, ['url_1', 'url_2', 'url_3']))
    w2 = Process(target=proc_write, args=(q, ['url_4', 'url_5', 'url_6']))
    p1 = Process(target=proc_read, args=(q, ))
    w1.start()
    w2.start()
    p1.start()
    w1.join()
    w2.join()
    p1.terminate()


if __name__ == "__main__":
    main()
