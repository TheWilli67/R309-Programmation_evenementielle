import socket
import threading
import sys
import platform


def reply(conn):
    while True:
        reply = input('[+] ')
        conn.send(reply.encode())
        if reply == 'end':
            try:
                print("[-] L'hôte a décider de se déconnecter ...")
            except (KeyboardInterrupt):
                print("[!] Keyboard interrupt")
            except (ConnectionResetError, EOFError):
                print("[!] L'hôte s'est déconnecté . .. ...")
        if reply == 'killServer':
            try:
                server_socket.close()
                break
            except (ConnectionAbortedError, EOFError):
                print("[!] L'hôte a décider de tuer la connection serveur sad_4_u ...")
                


def reception(conn):
        while True:
            try:
                data = conn.recv(1024).decode()
                print(data)
            except (ConnectionResetError, ConnectionAbortedError, EOFError):
                print("[!] L'hôte s'est déconnecté . .. ...")
            if data == 'os':
                systeme_exploitation = platform.uname()
                conn.send(systeme_exploitation.encode())


if __name__ == '__main__':
    sys.tracebacklimit = 0
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 6969))  # 127.0.0.1
    server_socket.listen(1)
    conn, address = server_socket.accept()
    try:
        task_reply = threading.Thread(target=reply, args=[conn])
        task_reply.start()
        task_reception = threading.Thread(target=reception, args=[conn])
        task_reception.start()
    except (ConnectionResetError, ConnectionAbortedError, EOFError):
        print("[!] L'hôte s'est déconnecté . .. ...")
