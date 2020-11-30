#客户端
import socket
socket2 = socket.socket()
host2 = '127.0.0.1'
port = 12456

socket2.connect((host2, port))
print (socket2.recv(1024))
socket2.close()