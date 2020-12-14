
import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("\n Enter the ip at which you want the server to run : ")
port = 1234

server.bind((host, port))

server.listen()
print("\n Server is ready to listen......")

client_socket, client_addr = server.accept()
print(f"\n Client is connected at ip {client_addr[0]} and port {client_addr[1]}")

file = client_socket.recv(1024).decode()
if os.path.exists(file) and os.path.isfile(file):
    msg = "true"
    client_socket.send(msg.encode())
    f = open(file, 'rb')
    cont = f.readline()
    while cont:
        client_socket.send(cont)
        cont = f.readline()
    print("\n Successfully Send The File....")
    f.close()
        
else:
    msg = "false"
    client_socket.send(msg.encode())
