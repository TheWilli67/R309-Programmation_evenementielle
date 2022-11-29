import socket
import threading

def envoi(ask,client_socket):
    if ask == 'y':
        while True:
            message = input('[+] ')
            client_socket.send(message.encode())
            if message == 'end':
                client_socket.close()
                print(f"[-] disconnected ...")
                break


def reception(ask, client_socket):
    if ask == 'y':
        while True:
            data = client_socket.recv(1024).decode()
            print(data)

if __name__ == '__main__':
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 6969))#127.0.0.1
    ask = str(input('[-] start chatting y/n : '))
    if ask == 'n':
        client_socket.close()
    elif ask == 'y':
        task_message = threading.Thread(
            target=envoi, args=[ask, client_socket])
        task_reception = threading.Thread(
            target=reception, args=[ask, client_socket])
        task_message.start()
        task_reception.start()
    else:
        client_socket.close()
