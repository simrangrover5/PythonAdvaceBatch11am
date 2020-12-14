
import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("\n Enter the ip at which you want to connect with server  : ")
port = 1234

sock.connect((host, port))
print("\n Successfully Connected.....")

file = input("\n Enter the file name : ")
sock.send(file.encode())

msg = sock.recv(1024).decode()
if msg == "true":
    print("\n SERVER IS SENDING THE FILE....")
    path = input("\n Enter the path where you want to save your file : ")
    if os.path.exists(path):
        fname = input("\n Enter the filename without ext : ")
        ext = file.split(".")[-1]
        fname = fname + "." + ext
        full_path = os.path.join(path, fname)
        fp = open(full_path, 'wb')
        cont = sock.recv(1024)
        while cont:
            fp.write(cont)
            cont = sock.recv(1024)

        print("\n Successfully Saved The File....")
        fp.close()
    else:
        print("\n NO SUCH PATH... PLEASE ENTER CORRECT PATH!!!!!")
        
else:
    print("\n NO SUCH FILE AVAILABLE....")
