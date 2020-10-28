# -*- coding:utf-8 -*-
import os
import time
from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue
from multiprocessing import Manager


# 进程之间数据不共享
# ret = os.fork() #创建一个子进程，父进程的ret=子进程的pid，创建出来的子进程ret=0，os.getpid() os.getppid()
# g_num = 100
# if ret==0:
#     g_num+=1
#     print g_num  #101
# else:
#     time.sleep(3)
#     print g_num   #100 ,因为不同进程数据不能共享，所以这里的值还是100

# def test():
#     i=0
#     while i<3:
#
#         print('-----test------')
#         time.sleep(1)
#         i+=1
#
# if __name__=='__main__':
#     p = Process(target=test)
#     p.start()
#     p.join()
#     i=0
#     while i<3:
#         print('-----main-------------')
#         time.sleep(1)
#         i+=1

# 1、第一种创建子进程的方式，直接创建Process对象，其中主进程执行完毕后，会等待子进程先结束
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join() #等待子进程执行完毕后主进程后面的内容才执行
#     print('Child process end.')


# 2、第二种创建子进程的方式，创建一个类，继承Process类，然后创建子类对象，
# 子类一定需要重写run()方法,其中主进程执行完毕后，会等待子进程先结束
# class SubProcess(Process):
#
#     def run(self):
#         for i in range(10):
#             print('----sub--------')
#             time.sleep(1)
#
# if __name__ =='__main__':
#     p = SubProcess()
#     p.start()  #
#     # p.join()
#     for i in range(3):
#         print('--------main----------')
#         time.sleep(1)


# 第三种创建进程的方法线程池，其中主进程执行完毕后，会直接结束，不会等待子进程执行完毕
# def woker(name):
#     for i in range(4):
#         print('-----pid=%d--num=%d' %(os.getpid(),name))
#
# if __name__=='__main__':
#
#     pool = Pool(3)
#     for i in range(5):
#         pool.apply_async(woker,(i,))
#
#         time.sleep(1)
#
#     pool.close() #关闭进程池，不能够再向进程池添加任务
#     pool.join()  #等待进程池中的进程执行完毕后主进程才结束，默认情况主进程执行完毕后直接结束（会导致子进程没有执行完毕，整个程序就退出了），
# 不会等待子进程执行完毕


# 进程间通信-Queue，先进先出,适用于process创建出来的进程通讯
# q = Queue(3)
# q.put('hh-1') #往队列添加数据
# q.put('hh-2')
# q.put('hh-3')
# q.put_nowait() #队列满的情况，会报异常，而不会等待
# print q.qsize()  #队列中数据的数量
# print q.empty()
# print q.get()
# q.put('hh-4')
# print q.full()

# 线程池中用到的队列创建方式
# q = Manager().Queue()


# 由Process创建的进程通信
# def write(q):
#     for i in ['a','A','c']:
#         print 'put %s to queue....' %i
#         q.put(i)
#         time.sleep(1)
#
#
# def read(q):
#     while True:
#         if not q.empty():
#             value = q.get()
#             print 'get %s from queue....' %value
#             time.sleep(1)
#
# if __name__=='__main__':
#     q = Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read,args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     # print q.qsize()
#     # pr.join()
#     print '执行完成'


# 多进程拷贝文件
# python2.x input():输入数字则直接输入，如果要输入字符串需要加入双引号；raw_input():直接输入，无论数字还是字符串都反正字符串类型
# python3.x 只有input()函数，用法和raw_input()一样
# def copy_file(file_name,oldFolderName,newFolderName,):
#     fr = open(oldFolderName+'\\'+file_name,'rb')
#     fw = open(newFolderName+'\\'+file_name,'wb')
#     fw.write(fr.read())
#     fr.close()
#     fw.close()
#
#
# def main():
#
#     oldFolderName = raw_input('请输入文件夹的名字：')
#     t1 = time.time()
#     # print oldFolderName
#     newFolderName = oldFolderName + '-copy'
#     # print(newFolderName)
#     os.mkdir(newFolderName)
#     file_names = os.listdir(oldFolderName)
#     print '文件拷贝开始'
#     # 多进程5.4
#     pool = Pool(2)
#     for file_name in file_names:
#         pool.apply_async(copy_file,(file_name,oldFolderName,newFolderName,))
#     pool.close()
#     pool.join()
#
#     # 单线程7.1
#     # for file_name in file_names:
#     #     fr = open(oldFolderName + '\\' + file_name, 'rb')
#     #     fw = open(newFolderName + '\\' + file_name, 'wb')
#     #     fw.write(fr.read())
#     #     fr.close()
#     #     fw.close()
#     print '文件拷贝完成'
#     t2 = time.time()
#     t_total = t2-t1
#     print t_total
#
# if __name__=='__main__':
#     main()

import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()