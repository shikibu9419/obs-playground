import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

rst = s.send('1'.encode())
print(rst)
msg = s.recv(1024)
print('received:', msg.decode("utf-8"))
