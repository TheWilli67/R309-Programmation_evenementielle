import socket

client_socket = socket.socket()
ip_ask = str(input('Destination IP : '))
port_ask = int(input('Port associé : '))
client_socket.connect((ip_ask, port_ask))
ask = str(input('[-] start chatting y/n : '))
