import os
import socket
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('192.168.2.108',1027))

print(s.recv(1024).decode('utf-8'))
while True:
    data=input()
    s.send(data.encode())
    if data=='exit':
        break
s.close()
exit()
