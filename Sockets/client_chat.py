
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.4"  # server ip
port = 1234

sock.connect((host, port))

msg = sock.recv(1024).decode()
print("Server --> ", msg)

m = "Thankyou For Accepting My Request"
sock.send(m.encode())

while True:
    smsg = sock.recv(1024).decode()
    print("Server --> ", smsg)
    if "bye" in smsg.strip().lower() or "byebye" in smsg.strip().lower() or "bubye" in smsg.strip().lower():
        print("Server Closed the connection")
        sock.close()
        break
    
    cmsg = input("Client --> ")
    sock.send(cmsg.encode())
    if "bye" in cmsg.strip().lower() or "byebye" in cmsg.strip().lower() or "bubye" in cmsg.strip().lower():
        print("Client Closed the connection")
        sock.close()
        break
