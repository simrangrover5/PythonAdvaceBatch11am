
import socket

s = socket.socket()

host="127.0.0.1"
port=5555

s.bind((host,port))
s.listen()

print(f"\n SERVER READY TO TAKE REQUEST AT PORT {port} and {host}")

client_socket,client_add=s.accept()

msg="Request is Accepted Succefully"
client_socket.send(msg.encode)
