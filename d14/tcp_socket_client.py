from socket import socket

def main():
    client = socket()
    client.connect(('172.30.0.15', 11211))
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()
