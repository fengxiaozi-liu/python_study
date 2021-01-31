import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 8000))
    sock.listen(128)
    while True:
        client, addr = sock.accept()
        data = client.recv(1024)
        print(data)
        client.send('HTTP/1.1 200 OK\n'.encode('utf8'))
        client.send('content-type:text/html;charset=utf8\n'.encode('utf8'))
        client.send('\n'.encode('utf8'))
        client.send('你长的真好看'.encode('utf8'))
        client.close()


if __name__ == '__main__':
    main()
