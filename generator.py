# -*- coding: utf-8 -*-

# 生成器(保存了生成数据的算法，并没有生成数据)
# 第一种创建列表生成器的方式
b = (x*2 for x in range(10))
# print b
# print next(b)
# print b.__next()__
# 第二种创建列表生成器的方式
# 1 斐波那契数列
def createNum():
    a,b = 0,1
    for i in range(10):
        print(b)
        a,b = b,a+b

# createNum()

#将print 改为关键字yield，函数变为了生成器，调用createNum()并不是执行函数，而是创建了一个生成器
def createNum():
    print('----start----')
    a,b = 0,1
    for i in range(10):
        print('----1-----')
        yield b
        print('----2-----')
        a,b = b,a+b
        print('----3-----')
    print('----stop-----')

# print next(createNum()) #执行到yield关键字那里，代码会停止执行 ，并返回yield后面的值
# ----start----
# ----1-----
# 1

# 生成器send()用法
def test():
    i = 0
    while i<5:
        temp = yield i
        print(temp)
        i += 1
# a = test()
# print next(a)
# print a.send('hh')
# print a.send('abc')


# 利用yield实现多任务（协程）
def test1():
    while True:
        print '---------1--------'
        yield None


def test2():
    while True:
        print '---------2--------'
        yield None

def mutil_task():
    t1 = test1()
    t2 = test2()
    while True:
        next(t1)
        next(t2)
        print('----3--------')


# mutil_task()