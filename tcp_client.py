# -*- coding: utf-8 -*-
# Author      : surfer
# time        : 2020/3/13 20:49
# name        : tcp_client.py
# projec_tname: python
# IDE         : PyCharm
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print s.recv(1024)
data = ['zzl','jsc','cl']
for i in data:
    s.send(i)
    print s.recv(1024)
s.send('exit')
s.close()
