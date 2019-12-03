from time import time

def main():
    total = 0
    number_list = [x for x in range(1, 10000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('use time: %.3f' % (end - start))


if __name__ == "__main__":
    main()