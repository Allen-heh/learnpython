from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    #family=AF_INET --ipv4
    #family=AF_INET6  --ipv6
    #type=SOCK_STREAM  --tcp
    #type=SOCK_DGRAM  --udp
    #type=SOCK_RAW
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('172.30.0.15', 11211))
    server.listen(512)
    print('server start listening...')

    while True:
        client, addr = server.accept()
        print(str(addr) + 'is comming...')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()

if __name__ == '__main__':
    main()
