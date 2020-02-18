# -*- coding: utf-8 -*-
# Author      : surfer
# time        : 2019/6/18 18:15
# name        : os_path.py
# projec_tname: python
# IDE         : PyCharm
import os
import sys

print(os.path.abspath(__file__))  # D:\python\os_path.py
print(os.path.dirname(__file__))  # D:/python
print os.path.split(os.path.abspath(__file__))  # ('D:\\python', 'os_path.py')
print(sys.executable)  # C:\Python27\python.exe
print os.path.split(__file__)  # ('D:/python', 'os_path.py')
