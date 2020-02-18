# -*- coding:utf-8 -*-
import os
import time
from multiprocessing import Process
from threading import Thread,Lock
import threading
from threading import local

# 第一种创建线程的方式，其中主线程等子线程执行结束后才会结束
# def test():
#     print('hello world')
# for i in range(5):
#     t = Thread(target=test)
#     t.start()
# print('finish')

# 第二种创建线程的方式，继承Thread类，并复写run方法,其中主线程等子线程执行结束后才会结束
# class MyThread(Thread):
#     def run(self):
#         for i in range(3):
#             print 'the thread is'+self.name
#             time.sleep(1)
#
#
# mt = MyThread()
# mt.start()


# 多线程共用全局变量的问题
# g_num = 0
#
# def woker1():
#     global g_num
#
#     for i in range(100000):
#         lock.acquire()
#         g_num+=1
#         lock.release()
#
#
#     print 'worker1---g_num=%d' %g_num
#
# def woker2():
#     global g_num
#
#     for i in range(100000):
#         lock.acquire()
#         g_num+=1
#         lock.release()
#
#
#     print 'worker2---g_num=%d' %g_num
#
# lock  = Lock()
# t1 = Thread(target=woker1)
# t2 = Thread(target=woker2)
# t1.start()
# t2.start()
# print('the main g_num=%d' %g_num)
#


#  两个线程执行同一个方法中的变量的情况,这时方法中的变量不是共享的，每个线程的变量独立
# def test():
#     g_num = 100
#     name = threading.current_thread().name
#     if name=='Thread-1':
#         g_num +=1
#     else:
#         time.sleep(1)
#     print 'the thread is %s,g_num=%d' %(name,g_num)
#
# t1 = Thread(target=test)
# t1.start()
#
# t2 = Thread(target=test)
# t2.start()


# 函数之间调用需要传参的情况，用threading中的local()对象
# local = local()
# def get_student():
#     std = local.student
#     print 'hello %s ,the thread id is %s' %(std, threading.current_thread().name)
#
# def set_student(name):
#     local.student = name
#     get_student()
#
# thread_1 = Thread(target=set_student,args=('zzl',))
# thread_2 = Thread(target=set_student,args=('wwk',))
# thread_1.start()
# thread_2.start()



d = 1
def get_val():
    global d
    d+=1
    print(d)

get_val()