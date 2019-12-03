import time

def main():
    with open('zen_of_python.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    with open('zen_of_python.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.1)
    print()

    with open('zen_of_python.txt') as f:
        lines = f.readlines()
        print(lines)


if __name__ == "__main__":
    main()
