class Test(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print("run is test.")

def main():
    t1 = Test("heh", 16)
    t1.run()

if __name__ == "__main__":
    main()
