
import socket

c=socket.socket()

host="127.0.0.1"
port=5555

c.connect((host,port))

msg=c.recve(1024).decode()
print("Server Message ---->",msg)

m="Thank You For Accepte My Request"
c.send(m.encoden)
