# -*- coding:utf-8 -*-
import os
import time
from multiprocessing import Process
from threading import Thread, Lock
import threading
from threading import local

# 第一种创建线程的方式，其中主线程等子线程执行结束后才会结束
# def test(a, b):
#     print('hello world')
#     print a + b
#     time.sleep(4)
#     print('sub thread is finish')
#
#
# t = Thread(target=test, args=(1, 2))
# t.start()
# t.join(2)  # 等待子线程结束后，主线程才结束,如果设置了超时时间，则到了超时时间，主线程会继续往下执行
# print('finish')

# 第二种创建线程的方式，继承Thread类，并复写run方法,其中主线程等子线程执行结束后才会结束
# class MyThread(Thread):
#     def __init__(self, name):
#         Thread.__init__(self)
#         self.name = name
#
#     def run(self):
#         for i in range(3):
#             print 'the thread is ' + self.name
#             time.sleep(1)
#
#
# mt = MyThread('zzl')
# mt.start()

# setDaemon()方法 ，把子线程设置为主进程的守护线程，当主线程执行结束后，
# 不管子线程是否执行完毕都会和主线程一起结束，并且mt.setDaemon(True)必须应用于start()之前
# mt = MyThread('hello world')
# mt.setDaemon(True)
# # mt.start()
# print 'this is main thread'


# 多线程共用全局变量的问题,通过给全局变量上锁
# g_num = 0
#
#
# def woker1(lock):
#     global g_num
#
#     for i in range(100000):
#         lock.acquire()
#         g_num += 1
#         lock.release()
#
#     print 'worker1---g_num=%d' % g_num
#
#
# def woker2(lock):
#     global g_num
#
#     for i in range(100000):
#         lock.acquire()
#         g_num += 1
#         lock.release()
#
#     print 'worker2---g_num=%d' % g_num
#
#
# lock = Lock()
#
# t1 = Thread(target=woker1, args=(lock,))
# t2 = Thread(target=woker2, args=(lock,))
# t1.start()
# t2.start()
# print('the main g_num=%d' % g_num)
#
#  # 两个线程执行同一个方法中的变量的情况,这时方法中的变量不是共享的，每个线程的变量独立
# def test():
#     g_num = 100
#     name = threading.current_thread().name
#     if name == 'Thread-1':
#         g_num += 1
#     else:
#         time.sleep(1)
#     print 'the thread is %s,g_num=%d' % (name, g_num)
#
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
