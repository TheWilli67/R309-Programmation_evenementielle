# coding: utf-8
import socket
import threading
import platform
import psutil
import os


def reply(conn):
    while True:
        reply = input('[+] ')
        conn.send(reply.encode())


def reception(conn,systeme_exploit,ipaddr):
    while True:
        data = conn.recv(1024).decode()
        print(data)
        try:
            data_split = data.split()[0]
            data_split1 = data.split(':')[1]
            print(data_split1)
        except:
            pass

        if data == 'os':
            uname = str(platform.uname().system)
            conn.send(uname.encode())

        if data == 'ip':
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
            essai = str(f"\n Hostname : {hostname}\n IP: {ipaddr}")
            conn.send(essai.encode())
        if data == 'kill':
            os.popen("shutdown /r").read()
            avertissement = "\n[!] Le Serveur va redémarrer dans >1 min \n[!]La connection va être perdue"
            conn.send(avertissement.encode())
        
        if data == 'kill -c':
            os.popen("shutdown /a").read()
            info = "\n[!] L'arrêt planifié a été annulé"
            conn.send(info.encode())
        try:
            if data == (f'dos:{data_split1}'):
                if systeme_exploit == 'windows':
                    task = os.popen(f"{data_split1}").read()
                    print(task)
                    conn.send(task.encode())
                else:
                    fail = f"tu  t'es trompé tu est sous {systeme_exploit} cette commande n'est pas disponible"
                    conn.send(fail.encode())
        except:
            pass

        try:
            if data == (f'linux:{data_split1}'):
                if systeme_exploit == 'linux':
                    task = os.popen(f"{data_split1}").read()
                    print(task)
                    conn.send(task.encode())
                else:
                    fail = f"tu t'es trompé tu est sous {systeme_exploit} cette commande n'est pas disponible"
                    conn.send(fail.encode())
        except:
            pass

        try:
            if data == (f'MacOS:{data_split1}') or (f'macos:{data_split1}'):
                if systeme_exploit == 'darwin':
                    task = os.popen(f"{data_split1}").read()
                    print(task)
                    conn.send(task.encode())
                else:
                    fail = f"tu t'es trompé tu est sous {systeme_exploit} cette commande n'est pas disponible"
                    conn.send(fail.encode())
        except:
            pass

        if data_split == 'ping':
            ipaddr = data.split()[1]
            pinging = os.popen(f"{data}"). read()
            print(pinging)
            conn.send(pinging.encode())

        if data == 'python --version':
            version = os.popen(f'python --version').read()
            conn.send(version.encode())

        if data == 'get-process':
            if systeme_exploit == 'windows':
                output = os.popen(
                    'wmic process get description, processid').read()
                conn.send(output.encode())
            else:
                fail = f"tu t'est trompé tu est sous {systeme_exploit} cette commande n'est pas disponible"
                conn.send(fail.encode())

        if data_split == ('powershell' or 'powershell.exe'):
            ps_data = os.popen(f'{data}').read()
            conn.send(ps_data.encode())


if __name__ == '__main__':
    #sys.tracebacklimit = 0
    server_socket = socket.socket()
    hostname = socket.gethostname()
    ipaddr = socket.gethostbyname(hostname)
    portask = int(input("Input a Port between 1 - 64738 : "))
    server_socket.bind((ipaddr, portask))  # 127.0.0.1
    systeme_exploit = str(platform.uname().system.lower())
    print(f"\n OS : {systeme_exploit}\n Hostname : {hostname}\n IP : {ipaddr}\n Port : {portask}")

    while True:
        server_socket.listen(10)
        conn, address = server_socket.accept()
        try:
            task_reply = threading.Thread(target=reply, args=[conn])
            task_reply.start()
            task_reception = threading.Thread(
                target=reception, args=[conn, systeme_exploit, ipaddr])
            task_reception.start()
        except (ConnectionResetError, ConnectionAbortedError, EOFError):
            print("[!] L'hôte s'est déconnecté . .. ...")