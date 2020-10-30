# -*- coding: utf-8 -*-
# Author      : surfer
# time        : 2020/3/13 20:49
# name        : tcp_client.py
# projec_tname: python
# IDE         : PyCharm


class A(object):
    def __init__(self, value):
        self.value = value
        print 'A---' + str(self.value)


class B(A):
    def __init__(self, value):
        # 第一种覆盖父类的方式
        # A.__init__(self, value)
        # 第二种覆盖父类的方式
        super(B, self).__init__(value)
        # self.value = value
        print 'B---' + str(self.value)


# B(100)
# =======================================================
class OldClass:
    # __new__方法将永远不会执行，因为它不是老式类的目标函数。
    def __new__(cls):
        print "__new__ is called"  # -> this is never called

    def __init__(self):
        print '老式类，继承于type'


# OldClass()

# 新式类，显示继承object
class Sample(object):
    def __str__(self):
        return "SAMPLE"
    __repr__ = __str__


class NewClass(object):
    def __new__(cls):
        print cls  # cls代表当前类
        print "NewClass.__new__ called"
        # return Sample()
        return object.__new__(Sample)
        # return super(NewClass, cls).__new__(Sample)
        # return 30

    def __init__(self):
        print "NewClass.__init__ called"


print NewClass()


# 单例模式
class Singleton(object):
    __instance = None

    def __new__(cls, age, name):
        if not cls.__instance:
            # cls.__instance = object.__new__(cls)
            cls.__instance = super(Singleton, cls)
        return cls.__instance

    def __init__(self, age, name):
        self.age = age
        self.name = name


#
# a = Singleton(18, 'zzl')
# b = Singleton(10, 'zdzl')


# print id(a)
# print id(b)
# print a.name
# print b.name


# 类方法四种定义方式
# object 公用方法
# __object__ 内建方法，表示Python自己调用，你不该调用，例如：len()和__len__()
# _object 保护变量半保护，该类内部和子类可以调用,类实例不能调用（实际实例也能调用，只是表示你不该去调用该方法和属性）

# __object 私有成员，全私有，全保护，只有该类内部可以调用,子类和实例都不可以调用，在类内部函数名会被‘矫直’，如:A类中的__private方法，被矫直为_A__private,
# Python设计此的真正目的仅仅是为了避免子类覆盖父类的方法

# 使用单下划线(_)开头的函数_func或者变量_var不能被模块外部以: from module import *形式导入；但可以用：from module import _func,_var形式单独导入


class Foo():
    def __init__(self):
        print 'init'

    def public_method(self):
        print 'This is public method'

    def __fullprivate_method(self):
        print 'This is fullprivate_method'

    def _halfprivate_method(self):
        print 'This is halfprivate_method'


# f = Foo()
# f.public_method()  # OK
# f.__fullprivate_method()  # Error occur
# f._halfprivate_method()  # OK
# f._Foo__fullprivate_method()  # OK
class A(object):
    __name = 'zzl'

    def __init__(self):
        # self._A__private()
        self.__private()
        self.public()

    def __private(self):
        print 'A.__private()'

    def public(self):
        print 'A.public()'


class B(A):
    def __private(self):
        print 'B.__private()'

    def public(self):
        print 'B.public()'

# b = B()
