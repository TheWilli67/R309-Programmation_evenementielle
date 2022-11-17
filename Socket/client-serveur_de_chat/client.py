import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1',34800))

ask = str(input('[-] start chatting y/n : '))

if ask == 'y':
    while True:
        message = str(input('[+]'))
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)
        if message == 'end':
            client_socket.close()
            break

if ask == 'n':
    client_socket.close()
