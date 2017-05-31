#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import socket
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('10.3.45.144',1027))
s.listen(10)


usend=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


ADDR=['127.0.0.1']

def Tcp(sock,addr):
    print("connection from %s:%s..."%addr)
    sock.send(b'Please enter your name:')
    sock.send(addr[0].encode())
    usrname=sock.recv(1024)
    while True:
        data=sock.recv(1024)
        if data.decode('utf-8')=='exit':break
        sen=Process(target=udpsend,args=(data.decode('utf-8'),addr[0]))
        sen.start()
    sock.close()
    print("connection end(%s:%s)"%addr)

def udpsend(data,addr):
    for con in ADDR:
        if con=='127.0.0.1':continue
        if con==addr:continue
        usend.sendto(data.encode(),(con,1027))


print("Waiting...")
while True:
    sock,addr=s.accept()
    ADDR.append(addr[0])
    p=Process(target=Tcp,args=(sock,addr))
    p.start()
