
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("\n Enter the host ip : ")

for i in range(80, 100):
    try:
        sock.connect((host, i))
    except:
        print(f" {i} is available")
