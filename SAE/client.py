import socket
import threading
import os
import sys


def envoi(ask, client_socket):
    if ask == 'y':
        while True:
            message = input('[+] ')
            client_socket.send(message.encode())
            if message == 'help':
                print("Command usable during server connection: \n os : Display what os is running on the server \n whoami : get IP address \n name : get hostname \n cpu : get CPU percentage after 3s \n ram : get percentage of ram used \n resume : display ip and hostname \n kill : shutdown the server connection \n ping : ping the @IP wanted \n dir : show directory list \n mkdir : create a directory \n python --version : display python version currently installed \n get-process : Powershell command that display all the current running process")
            if message == 'suicide':
                client_socket.close()
                quit()
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
    ask = str(input('[-] connect to server y/n : '))
    print("[?] type help")

    if ask == 'n':
        client_socket.close()
    elif ask == 'y':
        task_message = threading.Thread(
            target=envoi, args=[ask, client_socket])
        task_reception = threading.Thread(
            target=reception, args=[ask, client_socket])
        task_message.start()
        task_reception.start()
