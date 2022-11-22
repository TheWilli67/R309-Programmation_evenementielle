from client import	ask, client_socket
exec(open("./client_1.py").read())

if ask == 'y':
    while True:
        message = str(input('[+] '))
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)
        if message == 'end' or 'exit' or 'fin' or 'disconnect':
            client_socket.close()
            break

if ask == 'n':
    client_socket.close()
    reconnect = str(input('[-] reconnect y or n :'))
    if reconnect == 'y':
        exec(open("./client_1.py").read())
    else:
        client_socket.close
