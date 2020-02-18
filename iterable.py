# -*- coding: utf-8 -*-
from collections import Iterable,Iterator
# 迭代器iterator、可迭代对象
# 迭代器：可以被next()函数调用，并不断返回下一个值的对象称为迭代器
# 可迭代对象：集合数据类型、生成器generator
# 1、判断一个对象是否是可迭代对象isinstance
print(isinstance([],Iterable))

# 2、判断一个对象是否是迭代器isinstance
print(isinstance((i*2 for i in range(3)),Iterator))

# 3、将可迭代对象转化为迭代器iter()函数
a = [1,2,3]
b = iter(a)
print(isinstance(a,Iterator))
print(isinstance(b,Iterator))

