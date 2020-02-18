# _*_ coding:utf-8 _*_
# 装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象；
# 在Python中一般callable对象都是函数，但也有例外。只要某个对象重载了__call__()方法，那么这个对象就是callable的。
# def w1(func):
#     def inner():
#         print('------验证代码区--------')
#         func()
#
#     return inner
#
#
# def f1():
#     print('-------f1--------')
#
#
# def f2():
#     print('-------f2--------')


# infun = w1(f1)
# infun()

# f1 = w1(f1)
# f1()


# 类型一、不含参数的普通装饰器

def w1(func):
    print('----不含参数的普通装饰器------')

    def inner():
        func()

    return inner


@w1  # 只要Python解释器解释到这一行时，就会自动执行装饰，而不是等到要执行f1()函数才开始装饰 f1=w1(f1)
def f1():
    print('-------f1--------')


# 类型一、含参数的普通装饰器
def w2(func):
    print('----含参数的普通装饰器------')

    def inner(*args, **kwargs):
        func(*args, **kwargs)

    return inner


@w2
def say(msg):
    print "say {}!".format(msg)


say('world')


# 带参数装饰器
def logging(msg):
    def wrapper(func):
        print('----含参数的装饰器------')

        def inner_wrapper(*args, **kwargs):
            print msg
            return func(*args, **kwargs)

        return inner_wrapper

    return wrapper


@logging('hello')
def say(msg):
    print "say {}!".format(msg)


# say('world')

# 如果没有使用@，等同于 say = logging(level='INFO')(say)

# 基于类实现的装饰器
class DecoratorNoArg(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print '这是不接受参数的类装饰器'
        return self.func(*args, **kwargs)


@DecoratorNoArg
def say(msg):
    print "say {0}".format(msg)


# say('world')

# 带参数的类装饰器
class DecoratorWithArg(object):
    def __init__(self, level):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print '这是接受参数的类装饰器'
            func(*args, **kwargs)

        return wrapper


@DecoratorWithArg('witharg')
def say(msg):
    print "say {0}".format(msg)

# say('world')
