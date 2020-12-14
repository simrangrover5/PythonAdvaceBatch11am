
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET --> IPv4, SOCK_STREAM --> TCP

host = "192.168.1.4"  # change with your ip 
port = 1234

server.bind((host, port))
server.listen()
print(f"\n SERVER IS READY TO LISTEN AT PORT {port} and HOST {host}")

client_socket, client_addr = server.accept()

msg = "Successfully Accepted the request"
client_socket.send(msg.encode())

msg = client_socket.recv(1024).decode()
print("Client --> ", msg)
