import socket
import threading
import sys


def envoi(ask, client_socket):
    if ask == 'y':
        while True:
            message = input('[+] ')
            client_socket.send(message.encode())
            if message == 'end':
                try:
                    client_socket.close()
                    break
                except ConnectionAbortedError:
                    print("[-] disconnected ...")
                except KeyboardInterrupt:
                    print("[!] Keyboard interrupt")


def reception(ask, client_socket):
    if ask == 'y':
        while True:
            data = client_socket.recv(1024).decode()
            print(data)


if __name__ == '__main__':
    sys.tracebacklimit = 0
    client_socket = socket.socket()
    ip_ask = str(input('Destination IP : '))
    port_ask = int(input('Port associé : '))
    client_socket.connect((ip_ask, port_ask))
    ask = str(input('[-] start chatting y/n : '))

    if ask == 'n':
        client_socket.close()
    elif ask == 'y':
        task_message = threading.Thread(target=envoi, args=[ask, client_socket])
        task_reception = threading.Thread(target=reception, args=[ask, client_socket])
        task_message.start()
        task_reception.start()
    else:
        client_socket.close()
