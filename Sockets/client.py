
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.4"  # server ip
port = 1234

sock.connect((host, port))

msg = sock.recv(1024).decode()
print("Server --> ", msg)

m = "Thankyou For Accepting My Request"
sock.send(m.encode())
