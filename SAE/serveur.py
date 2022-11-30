import socket
import threading
import platform
import psutil
import os

def reply(conn):
    while True:
        reply = input('[+] ')
        conn.send(reply.encode())
        

def reception(conn, server_socket, systeme_exploit):
    while True:
        data = conn.recv(1024).decode()
        print(data)
        if data == 'os':
            uname = str(platform.uname().system)
            conn.send(uname.encode())
        if data == 'whoami':
            hostname = socket.gethostname()
            ipaddr = socket.gethostbyname(hostname)
            conn.send(ipaddr.encode())
        if data == 'name':
            hostname = socket.gethostname()
            conn.send(hostname.encode())
        if data == 'cpu':  # fonctionne pas !
            cpu = str(f"{psutil.cpu_percent(3)} %")
            conn.send(cpu.encode())
        if data == 'ram':  # fonctionne pas !
            ram = str(f"{psutil.virtual_memory()[2]} %")
            conn.send(ram.encode())
        if data == 'resume':
            hostname = socket.gethostname()
            ipaddr = socket.gethostbyname(hostname)
            essai = str(f"\n Hostname : {hostname}\n IP: {ipaddr}")
            conn.send(essai.encode())
        if data == 'kill':
            server_socket.close()
            quit()
        if systeme_exploit =='Windows':
            try:
                if data == 'dir':
                    commande = os.popen("dir").read()
                    print(commande)
                    conn.send(commande.encode())
            except:
                pass
        if data == 'ping':
            ipaddr = '1.1.1.1'
            pinging = os.popen(f"ping {ipaddr}"). read()
            print(pinging)
            conn.send(pinging.encode())
        if data == 'python --version':
            version = os.popen(f'python --version').read()
            conn.send(version.encode())
        if systeme_exploit =='Windows':
            try:
                if data == 'get-process':
                    output = os.popen('wmic process get description, processid').read()
                    conn.send(output.encode())
            except:
                pass

if __name__ == '__main__':
    #sys.tracebacklimit = 0
    server_socket = socket.socket()
    systeme_exploit = str(platform.uname().system)
    hostname = socket.gethostname()
    ipaddr = socket.gethostbyname(hostname)
    print(f" OS : {systeme_exploit}\n Hostname : {hostname}\n IP : {ipaddr}")
    server_socket.bind(('0.0.0.0', 6969))  # 127.0.0.1
    while True:
        server_socket.listen(1)
        conn, address = server_socket.accept()
        try:
            task_reply = threading.Thread(target=reply, args=[conn])
            task_reply.start()
            task_reception = threading.Thread(
                target=reception, args=[conn, server_socket, systeme_exploit])
            task_reception.start()
        except (ConnectionResetError, ConnectionAbortedError, EOFError):
            print("[!] L'hôte s'est déconnecté . .. ...")
