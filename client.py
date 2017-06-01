#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import socket
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('10.3.45.144',1027))
temp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)



def udpget():
    temp.bind((myaddr,1027))
    while True:
        data,addr=temp.recvfrom(1024)
        print(data.decode('utf-8'))



print('if you want to exit,please enter exit and Ctrl-c')
myname=input(s.recv(1024).decode('utf-8'))
myaddr=s.recv(1024).decode('utf-8')
rec=Process(target=udpget,args=())
rec.start()
s.send(myname.encode())
while True:
    data=input()
    s.send(data.encode())
    if data=='exit':
        break
s.close()
exit()
