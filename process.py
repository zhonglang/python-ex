# -*- coding: utf-8 -*-
# Author      : surfer
# time        : 2019/4/14 12:09
# name        : process.py
# projec_tname: python
# IDE         : PyCharm

from mutilprocess import Process
from mutilprocess import Pool
import time
import os

g_num = 100
def test(sec):
    while True:
        print('---1------')
        time.sleep(sec)


def woker(name):
    global  g_num
    g_num +=1
    for i in range(4):
        print('-----pid=%d--num=%d' % (os.getpid(), name))
    print g_num


if __name__ == '__main__':

    pool = Pool(2)
    for i in range(6):
        pool.apply_async(woker, (i,))
        time.sleep(1)

    pool.close()  # 关闭进程池，不能够再向进程池添加任务
    pool.join()

