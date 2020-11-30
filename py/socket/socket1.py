#服务端
import socket
#初始化一个tcp socket 参数默认
s = socket.socket()
host = socket.gethostname() # 获取本地主机名
port = 10350 #设置端口
s.bind((host, port))        # 绑定端口

s.listen(5) #开启监听，最多连接五个客户机
while True:
    c,addr = s.accept()     # 建立客户端连接
    print ('连接地址：', addr)
    c.sendall('欢迎'.encode())
    c.close()                # 关闭连接
