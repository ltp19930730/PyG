import socket

s = socket.socket()
port = 3456
host = socket.gethostname()

s.connect((host,port))

print s.recv(1024)

