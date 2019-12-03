def main():
    try:
        with open('timg.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('yys.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print(e)
        print('file not found.')
    print('ss over')

if __name__ == "__main__":
    main()
