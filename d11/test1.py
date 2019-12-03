def main():
    try:
        #f = open('zen_of_python.txt', 'r', encoding='utf-8')
        #print(f.read())
        #f.close()
        with open('azen_of_python.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('file is not found.')


if __name__ == "__main__":
    main()
