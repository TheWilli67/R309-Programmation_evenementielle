import socket

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 34800))
server_socket.listen(1)
conn, address = server_socket.accept()
ask = str(input('[-] start chatting y/n : '))
#reply = str(input('[-]'))
if ask == 'y':
    while True:
        data = conn.recv(1024).decode()
        print(data)
        reply = str(input('[+]'))
        conn.send(reply.encode())
        if reply == 'end':
            conn.close()
            break
if ask == 'n':
    conn.close()
