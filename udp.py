# -*- coding: utf-8 -*-
# Author      : surfer
# time        : 2020/2/17 16:49
# name        : udp.py
# projec_tname: python
# IDE         : PyCharm
from socket import *

udp = socket(AF_INET, SOCK_DGRAM)
addr = ('192.168.100.153', 8080)
udp.sendto('hello',addr)
udp.close()
#test