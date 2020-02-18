# -*- coding: utf-8 -*-
# Author      : surfer
# time        : 2019/12/29 10:49
# name        : file.py
# projec_tname: python
# IDE         : PyCharm

import functools


# 一、普通装饰器,被装饰函数不含参数
# def dec1(func):
#     print('========2===========')
#
#     def inner():
#         print('========3===========')
#         func()
#
#     return inner
#
#
#
# @dec1  # 只要Python解释器解释到这一行时，就会自动执行装饰，而不是等到要执行f1()函数才开始装饰 func1=dec1(func1)
# def func1():
#     print('========1===========')
#
#
# func1()
# 输出如下：
# ========2===========
# ========3===========
# ========1===========

# 二、普通装饰器,被装饰函数含参数
# 由于被装饰后的函数返回的是装饰器的内函数，因此，只需要往装饰器的内函数加上可变参数*args和关键字参数**kwargs，
# def dec2(func):
#     print('========2===========')
#
#     def inner(*args, **kwargs):
#         print('========3===========')
#         func(*args, **kwargs)
#
#     return inner
#
#
# @dec2   # @dec2等同于func2 = dec2(func2)('hello','world')
# def func2(a, b):
#     print('========1===========')
#     print(a, b)
#
#
# func2('hello', 'world')
# 输出如下：
# ========2===========
# ========3===========
# ========1===========
# ('hello', 'world')

# 三、带参数的装饰器，注意是装饰器带参数
# 外层嵌套一层函数传参，返回一个装饰器，这时就可以通过外层的函数传进参数
# def outer(arg):
#     print arg
#
#     def dec3(func):
#         print('========2===========')
#
#         def inner(*args, **kwargs):
#             print('========3===========')
#             func(*args, **kwargs)
#
#         return inner
#
#     return dec3
#
#
# @outer('带参数装饰器')  # 等同于func3 = outer('带参数装饰器')(func3)('hello','world')
# def func3(a, b):
#     print('========1===========')
#     print(a, b)
#
#
# func3('hello', 'world')
# 输出如下：
# 带参数装饰器
# ========2===========
# ========3===========
# ========1===========
# ('hello', 'world')


# 四、使用@functools.wraps的目的
# 我们常常看见装饰器函数有用到@functools.wraps，其作用就是将目标函数的属性例如__name__等原封不动转移给包装好的函数，
# 旨在消除装饰器对原函数造成的影响，即对原函数的相关属性进行拷贝，已达到装饰器不修改原函数的目的

# def dec4_nowraps(func):
#     print('========2===========')
#
#     def inner():
#         print('========3===========')
#         func()
#
#     return inner
#
#
# def dec5_withwraps(func):
#     print('========2===========')
#
#     @functools.wraps(func)
#     def inner():
#         print('========3===========')
#         func()
#
#     return inner
#
#
# @dec4_nowraps
# def func4():
#     print('========1===========')
#     print ('函数名为{0}'.format(func4.__name__))
#
#
# @dec5_withwraps
# def func5():
#     print('========1===========')
#     print ('函数名为{0}'.format(func5.__name__))
#
# func4()
# 输出如下，函数名为装饰器的内函数名：
# ========2===========
# ========3===========
# ========1===========
# 函数名为inner


# func5()
# 输出如下，函数名为被装饰的函数名：
# ========2===========
# ========3===========
# ========1===========
# 函数名为func5

# 五、类装饰器不带参数，被装饰函数也不带参数
# class Decorator1(object):
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print '这是不接受参数的类装饰器'
#         self.func()
#
#
# @Decorator1
# def func6():
#     print('========1===========')
#
#
# func6()  # 相当于执行类中的__call__方法
# 输出如下：
# 这是不接受参数的类装饰器
# ========1===========

# # 六、类装饰器不带参数，被装饰函数带参数
# class Decorator2(object):
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print '这是接受参数的类装饰器'
#         self.func(*args, **kwargs)
#
#
# @Decorator2
# def func7(a, b):
#     print('========1===========')
#     print(a, b)
#
#
# func7('hello', 'world')
# 输出如下：
# 这是接受参数的类装饰器
# ========1===========
# ('hello', 'world')


# 七、类装饰器不带参数，被装饰函数带参数
class Decorator3(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, func, *args, **kwargs):
        print '这是接受参数的类装饰器，而且装饰器也带参数'
        print(self.x, self.y)

        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

        return wrapper


@Decorator3('d1', 'd2')
def func8(a, b):
    print('========1===========')
    print(a, b)


func8('hello', 'world')
# 输出如下：
# 这是接受参数的类装饰器，而且装饰器也带参数
# ('d1', 'd2')
# ========1===========
# ('hello', 'world')
