import socket
import os
from _thread import *


def main():
    print("hi")
    ServerSideSocket = socket.socket()
    host = '127.0.0.1'
    port = 2004
    ThreadCount = 0

    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print('Socket is listening..')
    ServerSideSocket.listen(5)

    def multi_threaded_client(connection):
        connection.send(str.encode('Server is working:'))
        while True:
            data = connection.recv(2048).decode('utf-8')
            print(f"Got: {data}")
            response = 'Server message: ' + data
            if not data:
                break
            resp_str = str.encode(response)
            print(f"Will Send: {response}")
            connection.sendall(resp_str)
        connection.close()
        

    while True:
        Client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        multi_threaded_client(Client)
        print("only one client")
        # start_new_thread(
        #  multi_threaded_client, (Client, )
        # )
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSideSocket.close()
    
if __name__ == '__main__':
    main()