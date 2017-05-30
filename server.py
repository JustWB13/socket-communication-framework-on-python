#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import socket
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('192.168.2.108',1027))

s.listen(5)
print("waiting...")


def Tcp(sock,addr):
    print("connection from %s:%s..."%addr)
    sock.send(b'Welcome')
    data=sock.recv(1024)
    while data.decode('utf-8')!='exit':
        print(data.decode('utf-8'))
        data=sock.recv(1024)
    sock.close()
    print("connection end(%s:%s)"%addr)


while True:
    sock,addr=s.accept()
    p=Process(target=Tcp,args=(sock,addr))
    p.start()
