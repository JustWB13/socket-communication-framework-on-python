#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import socket
import time
import fileinput

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('10.3.45.144',1027))
s.listen(10)
usend=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


def Tcp(sock,addr):
    print("connection from %s:%s..."%addr)
    sock.send(b'Please enter your name:')
    sock.send(addr[0].encode())
    usrname=sock.recv(1024)
    while True:
        data=sock.recv(1024)
        if data.decode('utf-8')=='exit':break
        if data.decode('utf-8')=='ask':out()
        sen=Process(target=udpsend,args=(data.decode('utf-8'),addr[0]))
        sen.start()
    sock.close()
    print("connection end(%s:%s)"%addr)

def udpsend(data,address):
    for con in fileinput.input('/sor/usr.list'):
        adr=str(con)
        if adr==address:continue
        usend.sendto(data.encode(),(adr,1027))
    return

def out():
    for con in fileinput.input('/sor/usr.list'):print(con)



print("Waiting...")
sor=open('/sor/usr.list','w')
sor.close()
while True:
    sock,addr=s.accept()
    sor=open('/sor/usr.list','a')
    sor.write("%s\n"%addr[0])
    sor.close()
    p=Process(target=Tcp,args=(sock,addr))
    p.start()
