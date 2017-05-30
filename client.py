#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('10.3.45.144',1027))

print(s.recv(1024).decode('utf-8'))
while True:
    data=input()
    s.send(data.encode())
    if data=='exit':
        break
s.close()
exit()
