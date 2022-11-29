import socket
import threading
    
def reply(ask,conn):
    if ask == 'y':
        while True:
            reply = input('[+] ')
            conn.send(reply.encode())
            if reply == 'end':
                conn.close()
                break

def reception(ask,conn):
    if ask == 'y':
        while True:
            data = conn.recv(1024).decode()
            print(data)            
            
if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 6969))#127.0.0.1
    server_socket.listen(1)
    conn, address = server_socket.accept()
    ask = str(input('[-] start chatting y/n : '))
    #reply = str(input('[-]'))
    
    if ask == 'n':
        server_socket.close()

    elif ask == 'y':
        task_reply = threading.Thread(target=reply,args=[ask,conn])
        task_reply.start()
        task_reception = threading.Thread(target=reception,args=[ask,conn])
        task_reception.start()
        
    else:
        server_socket.close()

